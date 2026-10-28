#!/usr/bin/env python3
"""Build the Proud Little Learners kindergarten packs and weekly packets.

    python3 packs/build_packs.py

Writes PDFs, preview PNGs and WebPs, contact sheets, and packs/packs.json.
Exits nonzero if any answer, limit, or overflow check fails.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pdfkit
from pdfkit import Doc, sw
from catalog import NUMW, all_products
from layouts import draw_blocks, draw_certificate, draw_cover, draw_tracker, draw_weekly_cover, render_sheet

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
QA = Path("/tmp/pll-qa")
ART = Path("/opt/cursor/artifacts")

# Checker copy of shape facts. The renderer has its own.
SHAPE_FACTS = {
    "triangle": (3, 3),
    "square": (4, 4),
    "rectangle": (4, 4),
    "circle": (0, 0),
}

BANNED = (
    "free sample",
    "common core",
    "endorsed",
    "guaranteed",
    "certified",
    "research-based",
    "aligned to",
)


def norm_space(text):
    return re.sub(r"\s+", " ", text or "").strip()


def has_word(text, word):
    return re.search(rf"\b{re.escape(word)}\b", text.lower()) is not None


def check_phrase(phrase, prob, limit):
    """Parse a drawn answer phrase and check it against the operands."""
    kind = prob["kind"]
    if kind in ("add", "make10"):
        match = re.fullmatch(r"(\d+) \+ (\d+) = (\d+)", phrase)
        if not match:
            raise AssertionError(f"bad add phrase {phrase!r}")
        a, b, total = (int(match.group(i)) for i in (1, 2, 3))
        if a != prob["a"] or b != prob["b"] or total != a + b:
            raise AssertionError(f"{phrase} does not match {prob}")
        if total > limit or a < 0 or b < 0:
            raise AssertionError(f"{phrase} outside 0..{limit}")
        if kind == "make10" and (total != 10 or b != 10 - a):
            raise AssertionError(f"make 10 broken: {phrase}")
        return total
    if kind == "sub":
        match = re.fullmatch(r"(\d+) - (\d+) = (\d+)", phrase)
        if not match:
            raise AssertionError(f"bad sub phrase {phrase!r}")
        a, b, left = (int(match.group(i)) for i in (1, 2, 3))
        if a != prob["a"] or b != prob["b"] or left != a - b:
            raise AssertionError(f"{phrase} does not match {prob}")
        if b < 0 or b > a or a > 5 or left < 0:
            raise AssertionError(f"subtraction out of range: {phrase}")
        return left
    if kind == "count":
        match = re.fullmatch(r"Count: (\d+)", phrase)
        if not match or int(match.group(1)) != prob["n"] or prob["n"] > limit:
            raise AssertionError(f"{phrase} vs {prob}")
        return prob["n"]
    if kind == "two":
        match = re.fullmatch(r"Counts: (\d+) and (\d+)", phrase)
        if not match:
            raise AssertionError(phrase)
        a, b = int(match.group(1)), int(match.group(2))
        if a != prob["a"] or b != prob["b"] or a > limit or b > limit:
            raise AssertionError(f"{phrase} vs {prob}")
        return max(a, b)
    if kind == "partners":
        match = re.fullmatch(r"(\d+) = (\d+) \+ (\d+)", phrase)
        if not match:
            raise AssertionError(phrase)
        total, a, b = (int(match.group(i)) for i in (1, 2, 3))
        if (total, a, b) != (prob["total"], prob["a"], prob["b"]) or a + b != total or total > limit:
            raise AssertionError(f"{phrase} vs {prob}")
        return total
    if kind == "missing":
        match = re.fullmatch(r"(\d+) = (\d+) \+ (\d+)", phrase)
        if not match:
            raise AssertionError(phrase)
        total, known, miss = (int(match.group(i)) for i in (1, 2, 3))
        if total != prob["total"] or known != prob["known"] or known + miss != total or total > limit:
            raise AssertionError(f"{phrase} vs {prob}")
        return total
    if kind == "more":
        match = re.fullmatch(r"(Left|Right) has more", phrase)
        side = match.group(1) if match else ""
        ok = (side == "Left" and prob["a"] > prob["b"]) or (side == "Right" and prob["b"] > prob["a"])
        if not ok or prob["a"] == prob["b"] or max(prob["a"], prob["b"]) > limit:
            raise AssertionError(f"{phrase} vs {prob}")
        return max(prob["a"], prob["b"])
    if kind == "fewer":
        match = re.fullmatch(r"(Left|Right) has fewer", phrase)
        side = match.group(1) if match else ""
        ok = (side == "Left" and prob["a"] < prob["b"]) or (side == "Right" and prob["b"] < prob["a"])
        if not ok or max(prob["a"], prob["b"]) > limit:
            raise AssertionError(f"{phrase} vs {prob}")
        return max(prob["a"], prob["b"])
    if kind == "same":
        same = prob["a"] == prob["b"]
        if phrase != ("Same" if same else "Not the same"):
            raise AssertionError(f"{phrase} vs {prob}")
        if max(prob["a"], prob["b"]) > limit:
            raise AssertionError(prob)
        return max(prob["a"], prob["b"])
    if kind == "numerals":
        if prob["a"] == prob["b"]:
            if phrase != "Both the same":
                raise AssertionError(phrase)
        elif prob["a"] > prob["b"]:
            if phrase != "Left is more":
                raise AssertionError(phrase)
        elif phrase != "Right is more":
            raise AssertionError(phrase)
        if max(prob["a"], prob["b"]) > limit:
            raise AssertionError(prob)
        return max(prob["a"], prob["b"])
    if kind == "missing_num":
        match = re.fullmatch(r"Missing: (\d+)", phrase)
        seq, blank = prob["seq"], prob["blank"]
        if not match or int(match.group(1)) != seq[blank]:
            raise AssertionError(f"{phrase} vs {seq}")
        for i in range(1, len(seq)):
            if seq[i] != seq[i - 1] + 1:
                raise AssertionError(f"sequence jump {seq}")
        if max(seq) > limit or min(seq) < 0:
            raise AssertionError(seq)
        return seq[blank]
    if kind == "dots":
        match = re.fullmatch(r"Dots: (\d+)", phrase)
        if not match or int(match.group(1)) != prob["n"] or prob["n"] > limit:
            raise AssertionError(phrase)
        return prob["n"]
    if kind in ("corners", "sides"):
        label = "Corners" if kind == "corners" else "Sides"
        match = re.fullmatch(rf"{label}: (\d+)", phrase)
        sides, corners = SHAPE_FACTS[prob["shape"]]
        expect = corners if kind == "corners" else sides
        if not match or int(match.group(1)) != expect:
            raise AssertionError(f"{phrase} for {prob['shape']}")
        return expect
    if kind == "shape_count":
        match = re.fullmatch(r"([A-Z][a-z]+): (\d+)", phrase)
        count = sum(1 for shape in prob["shapes"] if shape == prob["target"])
        if not match or match.group(1).lower() != prob["target"] or int(match.group(2)) != count:
            raise AssertionError(f"{phrase} vs {prob}")
        if any(shape not in SHAPE_FACTS for shape in prob["shapes"]):
            raise AssertionError(prob["shapes"])
        return count
    if kind == "pattern":
        match = re.fullmatch(r"Next: ([a-z, ]+)", phrase)
        rule = prob["rule"]
        start = len(rule) * prob["repeats"]
        expect = [rule[i % len(rule)] for i in range(start, start + prob["ask"])]
        got = [part.strip() for part in match.group(1).split(",")] if match else []
        if got != expect or prob["repeats"] < 2 or prob["ask"] < 1:
            raise AssertionError(f"{phrase} vs {expect}")
        if any(shape not in SHAPE_FACTS for shape in rule):
            raise AssertionError(rule)
        return 0
    raise AssertionError(f"unknown kind {kind}")


def check_story_words(prob):
    text = prob.get("text")
    if not text:
        return
    if prob["kind"] == "add":
        a, b = prob["a"], prob["b"]
        if a > 0 and not has_word(text, NUMW[a]):
            raise AssertionError(f"story missing {NUMW[a]}: {text}")
        if b > 0 and not has_word(text, NUMW[b]):
            raise AssertionError(f"story missing {NUMW[b]}: {text}")
        if a == 0 and not text.lower().startswith("no "):
            raise AssertionError(text)
        if b == 0 and "no more" not in text.lower():
            raise AssertionError(text)
        total = a + b
        if total not in (a, b) and has_word(text, NUMW[total]):
            raise AssertionError(f"story gives away {NUMW[total]}: {text}")
    elif prob["kind"] == "sub":
        a, b = prob["a"], prob["b"]
        if not has_word(text, NUMW[a]) or not has_word(text, NUMW[b]):
            raise AssertionError(text)
        if has_word(text, NUMW[a - b]):
            raise AssertionError(f"take-away story gives away the answer: {text}")


def climb(records, entry, step, label):
    """records: list of (page_number, max_value, step_back)."""
    base = None
    for number, value, step_back in records:
        if base is None:
            if value > entry:
                raise AssertionError(f"{label} page {number} starts at {value}, entry allows {entry}")
            base = value
        elif step_back:
            if value > base:
                raise AssertionError(f"{label} page {number} step-back rose to {value} from {base}")
            base = value
        else:
            if value > base + step:
                raise AssertionError(f"{label} page {number} jumps to {value} from {base}")
            base = max(base, value)


def page_max(spec, pred):
    vals = []
    for prob in spec["problems"]:
        got = pred(prob)
        if got is not None:
            vals.append(got)
    return max(vals) if vals else None


def check_progression(pack):
    ident = pack["id"]
    pages = pack["practice"]

    def rows(pred):
        found = []
        for i, spec in enumerate(pages, start=1):
            value = page_max(spec, pred)
            if value is not None:
                found.append((i, value, spec.get("step_back", False)))
        return found

    add_rows = rows(lambda p: p["a"] + p["b"] if p["kind"] == "add" and "text" not in p else None)
    story_rows = rows(lambda p: p["a"] + p["b"] if p["kind"] == "add" and "text" in p else None)
    count_rows = rows(lambda p: p["n"] if p["kind"] == "count" else None)
    partner_rows = rows(lambda p: p.get("total") if p["kind"] in ("partners", "missing") else None)
    sub_rows = rows(lambda p: p["a"] if p["kind"] == "sub" else None)

    if ident == "k-add-beginner":
        climb(add_rows, 3, 1, ident + " add")
        climb(story_rows, 3, 1, ident + " story")
    elif ident == "k-add-intermediate":
        climb(add_rows, 5, 1, ident + " add")
    elif ident == "k-add-advanced":
        climb(story_rows, 5, 2, ident + " story")
        climb(partner_rows, 5, 1, ident + " partners")
    elif ident == "week-02":
        climb(count_rows, 6, 1, ident + " count")
    elif ident == "week-04":
        climb(add_rows, 3, 1, ident + " add")
    elif ident == "week-05":
        climb(add_rows, 5, 1, ident + " add")
        climb(story_rows, 3, 1, ident + " story")
    elif ident == "week-06":
        climb(add_rows, 5, 1, ident + " add")
    elif ident == "week-07":
        climb(sub_rows, 3, 1, ident + " sub")

    # Week 1 never goes past 5. Week 2's climb already caps the steps.
    if ident == "week-01":
        for prob in (p for spec in pages for p in spec["problems"]):
            for key in ("n", "a", "b"):
                if key in prob and prob[key] > 5:
                    raise AssertionError(prob)


def check_guide_pages(pack):
    text = " ".join(block for _kind, block in pack["guide"])
    count = len(pack["practice"])
    patterns = (
        r"[Pp]ractice pages (\d+) to (\d+)",
        r"[Pp]ractice pages (\d+), (\d+), and (\d+)",
        r"[Pp]ractice pages (\d+) and (\d+)",
        r"[Pp]ractice page (\d+)",
    )
    mentioned = []
    for pattern in patterns:
        mentioned.extend(int(n) for match in re.finditer(pattern, text) for n in match.groups())
    for number in mentioned:
        if not 1 <= number <= count:
            raise AssertionError(f"{pack['id']} guide mentions practice page {number}")
    low = text.lower()
    if "10 minutes" not in low and "about 10 minutes" not in low:
        raise AssertionError(f"{pack['id']} guide missing the 10-minute note")
    if "i do" not in low or "we do" not in low:
        raise AssertionError(f"{pack['id']} guide missing gradual release")
    if "do not resell" not in low:
        raise AssertionError(f"{pack['id']} missing license")


def check_pack_model(pack):
    limit = pack["limit"]
    n = len(pack["practice"])
    if pack.get("weekly"):
        if not 6 <= n <= 8:
            raise AssertionError(f"{pack['id']} has {n} practice pages")
    elif not 15 <= n <= 20:
        raise AssertionError(f"{pack['id']} has {n} practice pages")
    for spec in pack["practice"]:
        if not 4 <= len(spec["problems"]) <= 8:
            raise AssertionError(spec["title"])
        for prob in spec["problems"]:
            check_story_words(prob)
            # Every operand that is a quantity stays inside the pack limit.
            for key in ("n", "a", "b", "total", "known"):
                if key in prob and isinstance(prob[key], int) and prob[key] > limit:
                    raise AssertionError(f"{spec['title']} {key}={prob[key]} > {limit}")
            if prob["kind"] in ("add", "make10"):
                if prob["a"] + prob["b"] > limit:
                    raise AssertionError(spec["title"])
    check_progression(pack)
    check_guide_pages(pack)


def check_rendered(pack, pages):
    """Pair each practice page with its key and compare drawn phrases to the math."""
    practice = [p for p in pages if p.role == "practice"]
    answers = [p for p in pages if p.role == "answer"]
    if len(practice) != len(answers) or len(practice) != len(pack["practice"]):
        raise AssertionError(f"{pack['id']} page pairing {len(practice)} vs {len(answers)}")
    phrase_count = 0
    for spec, sheet, key in zip(pack["practice"], practice, answers):
        if "Name" not in sheet.texts or "Date" not in sheet.texts:
            raise AssertionError(f"{spec['title']} missing name/date")
        if key.phrases != [phrase for phrase in key.phrases]:
            raise AssertionError("empty")
        if len(key.phrases) != len(spec["problems"]):
            raise AssertionError(f"{spec['title']} phrase count")
        have = Counter(key.texts)
        practice_blob = "\n".join(sheet.texts)
        for prob, phrase in zip(spec["problems"], key.phrases):
            check_phrase(phrase, prob, pack["limit"])
            if have[phrase] < 1:
                raise AssertionError(f"phrase not drawn: {phrase}")
            have[phrase] -= 1
            if phrase in sheet.texts:
                raise AssertionError(f"answer leaked onto practice page: {phrase}")
            phrase_count += 1
        footer = f"Proud Little Learners · {pack['name']}"
        if footer not in sheet.texts or footer not in key.texts:
            raise AssertionError("footer missing")
    for sheet in pages:
        footer = f"Proud Little Learners · {pack['name']}"
        if footer not in sheet.texts:
            raise AssertionError(f"footer missing on {sheet.role} {sheet.meta.get('title')}")
        blob = " ".join(sheet.texts).lower()
        for banned in BANNED:
            if banned in blob:
                raise AssertionError(f"{pack['id']} contains {banned!r}")
    return phrase_count


def raster_check(pdf_path, qa_dir):
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf_path))
    scale = 110 / 72
    failures = []
    ratios = []
    qa_dir.mkdir(parents=True, exist_ok=True)
    thumbs = []
    for index, page in enumerate(doc):
        image = page.render(scale=scale).to_pil().convert("L")
        image.save(qa_dir / f"page-{index + 1:02d}.png")
        thumbs.append(image.copy())
        w, h = image.size
        px = image.load()
        margin = 24
        bottom_clear = 18

        def dirty(x0, y0, x1, y1):
            for y in range(y0, y1):
                for x in range(x0, x1):
                    if px[x, y] < 250:
                        return True
            return False

        bad = []
        if dirty(0, 0, w, margin):
            bad.append("top")
        if dirty(0, h - bottom_clear, w, h):
            bad.append("bottom")
        if dirty(0, 0, margin, h):
            bad.append("left")
        if dirty(w - margin, 0, w, h):
            bad.append("right")
        dark = 0
        step = 3
        seen = 0
        for y in range(0, h, step):
            for x in range(0, w, step):
                seen += 1
                if px[x, y] < 200:
                    dark += 1
        ratio = dark / seen
        ratios.append(ratio)
        if bad:
            failures.append(f"page {index + 1} margin {bad}")
        if ratio < 0.002 or ratio > 0.2:
            failures.append(f"page {index + 1} ink {ratio:.3f}")
        page.close()
    doc.close()
    return failures, ratios, thumbs


def pdf_contains_phrases(pdf_path, pages):
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    if len(reader.pages) != len(pages):
        raise AssertionError("PDF page count drifted")
    missing = []
    for sheet, pdf_page in zip(pages, reader.pages):
        extracted = norm_space(pdf_page.extract_text() or "")
        for phrase in sheet.phrases:
            if norm_space(phrase) not in extracted:
                missing.append(phrase)
    if missing:
        raise AssertionError("PDF text missing phrases: " + "; ".join(missing[:8]))


def contact_sheet(thumbs, titles, dest):
    cols = 6
    thumb_w = 190
    gap = 12
    label_h = 28
    rows = (len(thumbs) + cols - 1) // cols
    sample = thumbs[0]
    thumb_h = int(thumb_w * sample.size[1] / sample.size[0])
    sheet_w = cols * thumb_w + (cols + 1) * gap
    sheet_h = rows * (thumb_h + label_h) + (rows + 1) * gap + 36
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, (thumb, title) in enumerate(zip(thumbs, titles)):
        r, c = divmod(i, cols)
        x = gap + c * (thumb_w + gap)
        y = 36 + gap + r * (thumb_h + label_h + gap)
        fitted = thumb.convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(fitted, (x, y))
        draw.rectangle((x, y, x + thumb_w - 1, y + thumb_h - 1), outline=(0, 0, 0))
        draw.text((x, y + thumb_h + 4), title[:42], fill=(0, 0, 0), font=font)
    sheet.save(dest, "PNG", optimize=True)
    return dest


def write_previews(pdf_path, selections, out_dir):
    import pypdfium2 as pdfium

    doc = pdfium.PdfDocument(str(pdf_path))
    paths = []
    scale = 1200 / 612
    for index, stem in selections:
        page = doc[index]
        image = page.render(scale=scale).to_pil().convert("RGB")
        page.close()
        if image.size[0] != 1200:
            image = image.resize((1200, round(image.size[1] * 1200 / image.size[0])), Image.Resampling.LANCZOS)
        png = out_dir / f"{stem}.png"
        webp = out_dir / f"{stem}.webp"
        image.save(png, "PNG", optimize=True)
        image.save(webp, "WEBP", quality=82, method=6)
        paths.append(png)
        paths.append(webp)
    doc.close()
    return paths


def render_product(pack):
    slug = pack["name"].lower().replace(" ", "-")
    if pack.get("weekly"):
        out_dir = ROOT / "weekly" / pack["id"]
        pdf_path = out_dir / f"proud-little-learners-{pack['id']}-{slug}.pdf"
    else:
        out_dir = ROOT / pack["id"]
        pdf_path = out_dir / f"proud-little-learners-{slug}.pdf"
    out_dir.mkdir(parents=True, exist_ok=True)
    n = len(pack["practice"])
    inside = [f"{n} practice pages", "An answer key for every practice page"]
    if pack.get("weekly"):
        inside += ["A one-page note for the grown-up", "A small progress tracker"]
    else:
        inside += ["A parent guide", "A progress tracker", "A certificate of completion"]
    pack = dict(pack)
    pack["inside"] = inside

    doc = Doc(str(pdf_path), f"{pack['name']} — Proud Little Learners")
    cover = doc.new_page(pack["name"], "cover", {"title": "Cover"})
    (draw_weekly_cover if pack.get("weekly") else draw_cover)(cover, pack)
    cover.finish()

    guide_pages = draw_blocks(
        doc, pack["name"], "guide", pack["guide_title"], pack["guide"], pack["guide_pages"], {"title": pack["guide_title"]}
    )
    for guide in guide_pages:
        guide.role = "guide"

    for index, spec in enumerate(pack["practice"], start=1):
        sheet = doc.new_page(pack["name"], "practice", {"title": spec["title"], "index": index})
        render_sheet(sheet, spec, False, index, n)
        sheet.finish()

    tracker = doc.new_page(pack["name"], "tracker", {"title": "Progress tracker"})
    intro = "Color a star, or put a sticker on it, when a practice page is finished. About 10 minutes is enough for a day."
    draw_tracker(tracker, pack["name"], [(i, spec["tracker"]) for i, spec in enumerate(pack["practice"], start=1)], intro)
    tracker.finish()

    if pack.get("certificate"):
        cert = doc.new_page(pack["name"], "certificate", {"title": "Certificate"})
        draw_certificate(cert, pack["name"])
        cert.finish()

    for index, spec in enumerate(pack["practice"], start=1):
        sheet = doc.new_page(pack["name"], "answer", {"title": spec["title"], "index": index})
        render_sheet(sheet, spec, True, index, n)
        sheet.finish()

    doc.save()
    return pdf_path, doc.pages, pack


def product_record(pack, pdf_path, preview_paths, page_count):
    n = len(pack["practice"])
    rel_preview = [str(path.relative_to(REPO)) for path in preview_paths]
    if pack.get("weekly"):
        supporting = {"cover": 1, "parentNote": 1, "tracker": 1}
    else:
        supporting = {"cover": 1, "guide": pack["guide_pages"], "tracker": 1, "certificate": 1}
    record = {
        "id": pack["id"],
        "name": pack["name"],
        "totalPages": page_count,
        "practicePages": n,
        "answerPages": n,
        "supportingPages": supporting,
        "skillsPracticed": pack["skills"],
        "prerequisites": pack["prereq"],
        "materialsNeeded": ["printer", "pencil", "optional counters such as cereal or coins"],
        "fileFormat": "PDF",
        "paperSize": "US Letter",
        "pdf": str(pdf_path.relative_to(REPO)),
        "previewImages": rel_preview,
    }
    if pack.get("weekly"):
        record["week"] = pack["week"]
    return record


def select_previews(pack, pages):
    """Cover, parent guide, a few practice pages, and the tracker."""
    cover = next(i for i, page in enumerate(pages) if page.role == "cover")
    wanted = [(cover, "preview-cover")]
    guides = [i for i, page in enumerate(pages) if page.role == "guide"]
    wanted.append((guides[0], "preview-guide"))
    practice_indexes = {page.meta.get("index"): i for i, page in enumerate(pages) if page.role == "practice"}
    for number in pack["preview_practice"]:
        wanted.append((practice_indexes[number], f"preview-practice-{number:02d}"))
    tracker = next(i for i, page in enumerate(pages) if page.role == "tracker")
    wanted.append((tracker, "preview-tracker"))
    # Cover plus 4 to 6 representative pages.
    reps = len(wanted) - 1
    if not 4 <= reps <= 6:
        raise AssertionError(f"{pack['id']} has {reps} representative previews")
    return wanted


def main():
    packs, weeks = all_products()
    products = packs + weeks
    report = {"packs": [], "ok": True}
    records_main = []
    records_weekly = []
    for pack in products:
        print(f"building {pack['id']} …", flush=True)
        check_pack_model(pack)
        pdf_path, pages, pack = render_product(pack)
        phrases = check_rendered(pack, pages)
        pdf_contains_phrases(pdf_path, pages)
        qa_dir = QA / pack["id"]
        failures, ratios, thumbs = raster_check(pdf_path, qa_dir)
        if failures:
            raise SystemExit(f"{pack['id']} raster failures:\n" + "\n".join(failures[:20]))
        titles = []
        for i, page in enumerate(pages, start=1):
            titles.append(f"{i}. {page.role} {page.meta.get('title', '')}"[:48])
        sheet_path = pdf_path.parent / "contact-sheet.png"
        contact_sheet(thumbs, titles, sheet_path)
        previews = write_previews(pdf_path, select_previews(pack, pages), pdf_path.parent)
        record = product_record(pack, pdf_path, previews, len(pages))
        if pack.get("weekly"):
            records_weekly.append(record)
        else:
            records_main.append(record)
        report["packs"].append(
            {
                "id": pack["id"],
                "pages": len(pages),
                "practice": len(pack["practice"]),
                "answers": len(pack["practice"]),
                "phrases_checked": phrases,
                "ink_min": round(min(ratios), 4),
                "ink_max": round(max(ratios), 4),
                "raster": "pass",
                "pdf": str(pdf_path.relative_to(REPO)),
            }
        )
        print(f"  {len(pages)} pages, {phrases} answers checked, ink {min(ratios):.3f}-{max(ratios):.3f}")

    payload = {"packs": records_main, "weekly": records_weekly}
    (ROOT / "packs.json").write_text(json.dumps(payload, indent=2) + "\n")
    (ROOT / "check-report.json").write_text(json.dumps(report, indent=2) + "\n")
    ART.mkdir(parents=True, exist_ok=True)
    # Artifact copies are written by a later step so names stay stable.
    print("OK", len(records_main), "packs,", len(records_weekly), "weeks")


if __name__ == "__main__":
    main()
