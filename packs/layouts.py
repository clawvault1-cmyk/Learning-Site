"""Page layouts for Proud Little Learners packs. Black strokes, large type, no gray fills."""

import math

from pdfkit import (
    H,
    W,
    SHAPE_FACTS,
    answer_box,
    answer_phrase,
    draw_group,
    draw_shape,
    sw,
    ten_frame,
)

BOTTOM = 62
GAP = 7


def star(page, cx, cy, r, lw=1.3):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.4
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    page.polygon(pts, lw=lw)


def sheet_header(page, spec, show_answer, index, total):
    page.brand(42, 746)
    label = f"Answer key   {index} of {total}" if show_answer else f"Practice page   {index} of {total}"
    page.text(570, 746, label, "Inter", 9.5, align="right")
    if show_answer:
        page.text(42, 716, "For grown-ups. Match the practice page number.", "Inter", 11)
        title_y = 684
    else:
        page.name_date(714)
        title_y = 676
    title = spec["title"]
    size = 22 if sw(title, "Inter-Bold", 22) <= 520 else 18
    page.text(42, title_y, title, "Inter-Bold", size)
    instr_top = title_y - 16
    bottom = page.wrap(spec["instruction"], 42, instr_top, 526, size=12, leading=15.5, max_lines=2)
    return bottom - 8


def vslots(n, top, bottom=BOTTOM, gap=GAP):
    h = (top - bottom - gap * (n - 1)) / n
    if h < 72:
        raise RuntimeError(f"Only {h:.1f}pt per row for {n} problems (top {top:.0f})")
    slots, y_top = [], top
    for _ in range(n):
        y_bot = y_top - h
        slots.append((42, y_bot, 528, h))
        y_top = y_bot - gap
    return slots


def gslots(n, top, cols, bottom=BOTTOM, gap_x=16, gap_y=8):
    rows = (n + cols - 1) // cols
    h = (top - bottom - gap_y * (rows - 1)) / rows
    w = (528 - gap_x * (cols - 1)) / cols
    if h < 78:
        raise RuntimeError(f"Grid row {h:.1f}pt is short")
    slots = []
    for i in range(n):
        r, c = divmod(i, cols)
        x = 42 + c * (w + gap_x)
        y_top = top - r * (h + gap_y)
        slots.append((x, y_top - h, w, h))
    return slots


def _mark(page, slot, i):
    """Number circle. Returns a content cy that clears the I do / We do label."""
    x, y, w, h = slot
    if i == 1:
        page.text(x + 30, y + h - 13, "I do", "Inter-Med", 9)
    elif i == 2:
        page.text(x + 30, y + h - 13, "We do", "Inter-Med", 9)
    label = 16 if i <= 2 else 4
    cy = y + (h - label) / 2 + 1
    page.circle(x + 13, cy, 11, fill=False, lw=1.35)
    page.center_in(x + 2, cy - 11, 22, 22, str(i), "Inter-Bold", 11)
    return cy


def _caption(page, slot, prob, show):
    """Reserve a bottom band for the key phrase. Returns the rect above it."""
    x, y, w, h = slot
    if not show:
        return slot
    page.phrase(x + 32, y + 5, answer_phrase(prob), size=13)
    return (x, y + 22, w, h - 22)


def _box(page, x, cy, value, show, bw=50, bh=50):
    answer_box(page, x, cy - bh / 2, bw, bh, value if show else None)
    return bw


def paint_count(page, slot, prob, show, i):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    draw_group(page, x + 34, cy, prob["n"], prob.get("shape", "circle"))
    _box(page, x + w - 58, cy, prob["n"], show)


def paint_two(page, slot, prob, show, i):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    wa, _ = draw_group(page, x + 34, cy, prob["a"], "circle")
    page.text(x + 44 + wa, cy - 7, "+", "Inter-Bold", 18)
    draw_group(page, x + 68 + wa, cy, prob["b"], "square")
    # Two writing boxes, labeled by position only (the instruction says first group, then second).
    _box(page, x + w - 124, cy, prob["a"], show, 46, 46)
    _box(page, x + w - 58, cy, prob["b"], show, 46, 46)


def paint_picture_total(page, slot, prob, show, i):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    wa, _ = draw_group(page, x + 34, cy, prob["a"], "circle")
    page.text(x + 42 + wa, cy - 8, "+", "Inter-Bold", 20)
    wb, _ = draw_group(page, x + 66 + wa, cy, prob["b"], "square")
    eqx = x + 76 + wa + wb
    page.text(eqx, cy - 8, "=", "Inter-Bold", 20)
    _box(page, eqx + 22, cy, prob["a"] + prob["b"], show)


def paint_picture_sentence(page, slot, prob, show, i):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    wa, _ = draw_group(page, x + 32, cy, prob["a"], "circle", gap=22, r=8)
    page.text(x + 40 + wa, cy - 8, "+", "Inter-Bold", 18)
    wb, _ = draw_group(page, x + 60 + wa, cy, prob["b"], "square", gap=22, r=8)
    eqx = x + 72 + wa + wb
    a, b = prob["a"], prob["b"]
    if show:
        page.text(eqx, cy - 8, f"{a} + {b} =", "Inter-Bold", 16)
        _box(page, eqx + sw(f"{a} + {b} =", "Inter-Bold", 16) + 6, cy, a + b, show, 46, 46)
    else:
        page.text(eqx, cy - 8, f"{a} + {b} =", "Inter-Bold", 16)
        _box(page, eqx + sw(f"{a} + {b} =", "Inter-Bold", 16) + 6, cy, None, show, 46, 46)


def paint_count_on(page, slot, prob, show, i):
    """Filled dots for the first addend, empty circles for the second."""
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    wa, _ = draw_group(page, x + 32, cy, prob["a"], "circle", gap=20, r=8)
    page.text(x + 40 + wa, cy - 7, "+", "Inter-Bold", 16)
    # Empty circles the child can fill while counting on. Zero stays a bowl.
    if prob["b"] == 0:
        wb, _ = draw_group(page, x + 58 + wa, cy, 0, "circle")
    else:
        wb, _ = draw_group(page, x + 58 + wa, cy, prob["b"], "open", gap=20, r=8)
    eqx = x + 70 + wa + max(wb, 10)
    a, b = prob["a"], prob["b"]
    page.text(eqx, cy - 7, f"{a} + {b} =", "Inter-Bold", 16)
    _box(page, eqx + sw(f"{a} + {b} =", "Inter-Bold", 16) + 6, cy, a + b if show else None, show, 46, 46)


def paint_sentence(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h / 2
    page.circle(x + 14, cy, 11, fill=False, lw=1.3)
    page.center_in(x + 3, cy - 11, 22, 22, str(i), "Inter-Bold", 11)
    if i == 1:
        page.text(x + 32, y + h - 14, "I do", "Inter-Med", 8.5)
    elif i == 2:
        page.text(x + 32, y + h - 14, "We do", "Inter-Med", 8.5)
    a, b = prob["a"], prob["b"]
    if show:
        page.phrase(x + 36, cy - 8, answer_phrase(prob), size=20)
    else:
        prompt = f"{a} + {b} ="
        page.text(x + 36, cy - 8, prompt, "Inter-Bold", 22)
        _box(page, x + 42 + sw(prompt, "Inter-Bold", 22), cy, None, False, 48, 48)


def paint_build(page, slot, prob, show, i):
    """Pictures only. Child writes both addends and the total."""
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    wa, _ = draw_group(page, x + 32, cy, prob["a"], "circle", gap=20, r=8)
    wb, _ = draw_group(page, x + 56 + wa, cy, prob["b"], "square", gap=20, r=8)
    eqx = x + 84 + wa + wb
    a, b = prob["a"], prob["b"]
    _box(page, eqx, cy, a if show else None, show, 42, 44)
    page.text(eqx + 46, cy - 7, "+", "Inter-Bold", 16)
    _box(page, eqx + 64, cy, b if show else None, show, 42, 44)
    page.text(eqx + 110, cy - 7, "=", "Inter-Bold", 16)
    _box(page, eqx + 128, cy, a + b if show else None, show, 42, 44)


def paint_story(page, slot, prob, show, i, sentence):
    x, y, w, h = slot
    if i == 1:
        page.text(x, y + h - 12, "I do", "Inter-Med", 9)
    elif i == 2:
        page.text(x, y + h - 12, "We do", "Inter-Med", 9)
    page.circle(x + 12, y + h - 28, 10, fill=False, lw=1.25)
    page.center_in(x + 2, y + h - 38, 20, 20, str(i), "Inter-Bold", 10)
    page.text(x + 28, y + h - 32, "Grown-up reads", "Inter-Med", 9)
    text_bottom = page.wrap(prob["text"], x + 28, y + h - 38, w - 28, size=12, leading=15.5, max_lines=3)
    a, b = prob["a"], prob["b"]
    phrase_h = 22 if show else 0
    if show:
        page.phrase(x + 28, y + 5, answer_phrase(prob), size=13)
    box_bottom = y + 8 + phrase_h
    box_top = text_bottom - 8
    box_h = box_top - box_bottom
    if box_h < 42:
        raise RuntimeError(f"Story block too tight ({box_h:.0f}pt): {prob['text']}")
    page.roundrect(x, box_bottom, 124, box_h, 5, lw=1.3)
    page.text(x + 8, box_top - 14, "Draw here", "Inter", 9)
    eqx = x + 140
    eqy = box_bottom + box_h / 2
    if sentence:
        _box(page, eqx, eqy, a if show else None, show, 40, 42)
        page.text(eqx + 46, eqy - 6, "+", "Inter-Bold", 16)
        _box(page, eqx + 66, eqy, b if show else None, show, 40, 42)
        page.text(eqx + 112, eqy - 6, "=", "Inter-Bold", 16)
        _box(page, eqx + 132, eqy, (a + b) if show else None, show, 40, 42)
    else:
        page.text(eqx, eqy + 8, "How many in all?", "Inter", 12)
        _box(page, eqx + 140, eqy, (a + b) if show else None, show, 46, 46)


def paint_ten_count(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h / 2 + (6 if show else 0)
    page.circle(x + 12, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 2, cy - 10, 20, 20, str(i), "Inter-Bold", 10)
    if i == 1:
        page.text(x + 28, y + h - 12, "I do", "Inter-Med", 8)
    elif i == 2:
        page.text(x + 28, y + h - 12, "We do", "Inter-Med", 8)
    ten_frame(page, x + 30, cy - 26, prob["n"], 0, cell=24)
    _box(page, x + w - 54, cy, prob["n"], show, 46, 46)
    if show:
        page.phrase(x + 30, y + 4, answer_phrase(prob), size=12)


def paint_ten_add(page, slot, prob, show, i):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    ten_frame(page, x + 32, cy - 26, prob["a"], prob["b"], cell=24)
    a, b = prob["a"], prob["b"]
    page.text(x + 176, cy - 6, f"{a} + {b} =", "Inter-Bold", 16)
    _box(page, x + 182 + sw(f"{a} + {b} =", "Inter-Bold", 16), cy, a + b if show else None, show, 46, 46)


def paint_nline(page, slot, prob, show, i):
    x, y, w, h = slot
    if i == 1:
        page.text(x, y + h - 12, "I do", "Inter-Med", 8.5)
    elif i == 2:
        page.text(x, y + h - 12, "We do", "Inter-Med", 8.5)
    page.circle(x + 11, y + h - 30, 10, fill=False, lw=1.2)
    page.center_in(x + 1, y + h - 40, 20, 20, str(i), "Inter-Bold", 10)
    a, b = prob["a"], prob["b"]
    line_y = y + (46 if show else 36)
    x0 = x + 36
    width = 360
    gap = width / 10
    page.line(x0, line_y, x0 + width, line_y, lw=1.45)
    for n in range(11):
        tx = x0 + n * gap
        page.line(tx, line_y - 4, tx, line_y + 4, lw=1.15)
        page.text(tx, line_y - 16, str(n), "Inter", 8, align="center")
    if b > 0:
        xa = x0 + a * gap
        xb = x0 + (a + b) * gap
        lift = min(22, 8 + b * 2.2)
        page.curve(xa, line_y + 6, xb, line_y + 6, lift, lw=1.3)
        page.line(xb, line_y + 6, xb - 5, line_y + 11, lw=1.25)
        page.line(xb, line_y + 6, xb - 6, line_y + 3, lw=1.25)
    prompt = f"{a} + {b} ="
    page.text(x0 + width + 14, line_y - 4, prompt, "Inter-Bold", 12)
    _box(page, x + w - 48, line_y - 16, a + b if show else None, show, 42, 42)
    if show:
        page.phrase(x + 36, y + 4, answer_phrase(prob), size=12)


def paint_partners(page, slot, prob, show, i):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    total, a, b = prob["total"], prob["a"], prob["b"]
    label = f"{total}  ="
    page.text(x + 30, cy - 7, label, "Inter-Bold", 18)
    cursor = x + 38 + sw(label, "Inter-Bold", 18)
    wa, _ = draw_group(page, cursor, cy, a, "circle", gap=16, r=6.5)
    cursor += wa + 10
    _box(page, cursor, cy, a if show else None, show, 38, 40)
    cursor += 46
    page.text(cursor, cy - 6, "+", "Inter-Bold", 16)
    cursor += 20
    wb, _ = draw_group(page, cursor, cy, b, "square", gap=16, r=6.5)
    cursor += wb + 10
    _box(page, cursor, cy, b if show else None, show, 38, 40)
    if cursor + 40 > x + w:
        raise RuntimeError(f"partners row runs off the page ({cursor:.0f})")


def paint_missing(page, slot, prob, show, i, with_picture):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    total, known = prob["total"], prob["known"]
    miss = total - known
    page.text(x + 32, cy - 7, f"{total}  =  {known}  +", "Inter-Bold", 18)
    eqw = sw(f"{total}  =  {known}  +", "Inter-Bold", 18)
    _box(page, x + 40 + eqw, cy, miss if show else None, show, 46, 46)
    if with_picture:
        # Pictures sit to the right of the answer box. A zero part is a bowl,
        # so the next group starts after that bowl instead of on top of it.
        gx = x + 100 + eqw
        wa, _ = draw_group(page, gx, cy, known, "circle", gap=16, r=6.5)
        kind = "open" if miss else "circle"
        draw_group(page, gx + wa + 14, cy, miss, kind, gap=16, r=6.5)


def paint_make10(page, slot, prob, show, i, frame=True):
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    a = prob["a"]
    miss = 10 - a
    if frame:
        ten_frame(page, x + 32, cy - 24, a, 0, cell=22)
        ex = x + 160
    else:
        page.roundrect(x + 32, cy - 22, 70, 44, 4, lw=1.2)
        page.text(x + 40, cy + 8, "Draw", "Inter", 9)
        if show and miss:
            draw_group(page, x + 40, cy - 6, min(miss, 5), "open", gap=12, r=4)
        ex = x + 114
    page.text(ex, cy - 6, f"{a} +", "Inter-Bold", 16)
    _box(page, ex + sw(f"{a} +", "Inter-Bold", 16) + 6, cy, miss if show else None, show, 44, 44)
    page.text(ex + sw(f"{a} +", "Inter-Bold", 16) + 56, cy - 6, "=  10", "Inter-Bold", 16)


def paint_explain(page, slot, prob, show, i):
    x, y, w, h = slot
    if i == 1:
        page.text(x + 28, y + h - 12, "I do", "Inter-Med", 9)
    elif i == 2:
        page.text(x + 28, y + h - 12, "We do", "Inter-Med", 9)
    page.circle(x + 12, y + h - 28, 10, fill=False, lw=1.2)
    page.center_in(x + 2, y + h - 38, 20, 20, str(i), "Inter-Bold", 10)
    a, b = prob["a"], prob["b"]
    page.text(x + 30, y + h - 32, f"{a}  +  {b}  =", "Inter-Bold", 18)
    _box(page, x + 30 + sw(f"{a}  +  {b}  =", "Inter-Bold", 18) + 8, y + h - 48, a + b if show else None, show, 44, 44)
    page.roundrect(x, y + (24 if show else 8), w, h - 70, 6, lw=1.3)
    page.text(x + 8, y + h - 68, "Draw the groups here.", "Inter", 10)
    if show:
        draw_group(page, x + 16, y + 48, a, "circle", gap=16, r=6)
        draw_group(page, x + 30 + max(a, 1) * 16, y + 48, b, "square", gap=16, r=6)
        page.phrase(x + 8, y + 6, answer_phrase(prob), size=13)


def paint_sub(page, slot, prob, show, i, mode):
    """mode: shown (X already there), cross (child crosses), sentence."""
    slot = _caption(page, slot, prob, show)
    x, y, w, h = slot
    cy = _mark(page, slot, i)
    a, b = prob["a"], prob["b"]
    left = a - b
    # On the practice 'cross' page the child makes the X. The key shows it.
    styles = []
    for n in range(a):
        if n < left:
            styles.append("fill")
        else:
            if mode == "cross" and not show:
                styles.append("fill")
            else:
                styles.append("cross")
    _tokens(page, x + 34, cy, styles)
    if mode == "cross":
        page.text(x + 40 + a * 22, cy + 10, f"Cross out {b}", "Inter", 11)
    prompt_x = x + w - 168
    if mode == "sentence" or show:
        page.text(prompt_x, cy - 6, f"{a} - {b} =", "Inter-Bold", 14)
        _box(page, prompt_x + sw(f"{a} - {b} =", "Inter-Bold", 14) + 6, cy, left if show else None, show, 44, 44)
    else:
        page.text(prompt_x, cy - 4, "How many?", "Inter", 12)
        _box(page, prompt_x + 78, cy, left if show else None, show, 46, 46)


def _tokens(page, x, cy, styles, gap=22, r=8):
    for i, st in enumerate(styles):
        cx = x + r + i * gap
        if st == "fill":
            page.circle(cx, cy, r, fill=True, lw=1.15)
        elif st == "cross":
            page.circle(cx, cy, r, fill=False, lw=1.35)
            page.line(cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2, lw=1.3)
            page.line(cx - r + 2, cy + r - 2, cx + r - 2, cy - r + 2, lw=1.3)
        else:
            page.circle(cx, cy, r, fill=False, lw=1.3)
    return len(styles) * gap


def paint_compare(page, slot, prob, show, i):
    x, y, w, h = slot
    cy_mid = y + h / 2
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 11, cy_mid, 10, fill=False, lw=1.2)
    page.center_in(x + 1, cy_mid - 10, 20, 20, str(i), "Inter-Bold", 10)
    pw, ph = (w - 50) / 2, h - 28
    py = y + 4
    left_x = x + 28
    right_x = left_x + pw + 8
    heavy = None
    kind = prob["kind"]
    if kind == "more":
        heavy = "L" if prob["a"] > prob["b"] else "R"
    elif kind == "fewer":
        heavy = "L" if prob["a"] < prob["b"] else "R"
    lw_l = 2.6 if show and heavy == "L" else 1.25
    lw_r = 2.6 if show and heavy == "R" else 1.25
    page.roundrect(left_x, py, pw - 8, ph, 7, lw=lw_l)
    page.roundrect(right_x, py, pw - 8, ph, 7, lw=lw_r)
    draw_group(page, left_x + 10, py + ph / 2, prob["a"], "circle", gap=16, r=6)
    draw_group(page, right_x + 10, py + ph / 2, prob["b"], "square", gap=16, r=6)
    if show:
        page.phrase(x + w - 130, y + h - 14, answer_phrase(prob), size=11)


def paint_same(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h * 0.58
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 11, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 1, cy - 10, 20, 20, str(i), "Inter-Bold", 10)
    draw_group(page, x + 30, cy, prob["a"], "circle", gap=16, r=6.5)
    draw_group(page, x + 160, cy, prob["b"], "square", gap=16, r=6.5)
    same = prob["a"] == prob["b"]
    for label, chosen, ox in (("same", same, 330), ("not the same", not same, 410)):
        lw = 2.5 if show and chosen else 1.2
        page.circle(x + ox, cy, 8, fill=False, lw=lw)
        page.text(x + ox + 12, cy - 4, label, "Inter", 11)
    if show:
        page.phrase(x + 30, y + 5, answer_phrase(prob), size=12)


def paint_numerals(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h / 2 + 4
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 12, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 2, cy - 10, 20, 20, str(i), "Inter-Bold", 11)
    a, b = prob["a"], prob["b"]
    la = 2.7 if show and a >= b else 1.4
    lb = 2.7 if show and b >= a else 1.4
    page.roundrect(x + 40, cy - 24, 70, 52, 6, lw=la)
    page.center_in(x + 40, cy - 24, 70, 52, str(a), "Inter-Bold", 26)
    page.roundrect(x + 140, cy - 24, 70, 52, 6, lw=lb)
    page.center_in(x + 140, cy - 24, 70, 52, str(b), "Inter-Bold", 26)
    if show:
        page.phrase(x + 230, cy - 6, answer_phrase(prob), size=14)


def paint_sequence(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h / 2 + (4 if show else 0)
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 12, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 2, cy - 10, 20, 20, str(i), "Inter-Bold", 10)
    seq, blank = prob["seq"], prob["blank"]
    for n, value in enumerate(seq):
        bx = x + 32 + n * 58
        if n == blank and not show:
            answer_box(page, bx, cy - 22, 48, 46, None)
        elif n == blank and show:
            answer_box(page, bx, cy - 22, 48, 46, value)
        else:
            page.roundrect(bx, cy - 22, 48, 46, 5, lw=1.2)
            page.center_in(bx, cy - 22, 48, 46, str(value), "Inter-Bold", 20)
    if show:
        page.phrase(x + 32, y + 4, answer_phrase(prob), size=12)


def paint_draw_dots(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h / 2
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 12, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 2, cy - 10, 20, 20, str(i), "Inter-Bold", 10)
    page.roundrect(x + 32, cy - 26, 64, 54, 6, lw=1.5)
    page.center_in(x + 32, cy - 26, 64, 54, str(prob["n"]), "Inter-Bold", 28)
    page.roundrect(x + 112, cy - 28, 250, 58, 6, lw=1.3)
    if show:
        draw_group(page, x + 124, cy, prob["n"], "circle", gap=20, r=7)
        page.phrase(x + 380, cy - 6, answer_phrase(prob), size=14)
    else:
        page.text(x + 124, cy - 4, "Draw the dots", "Inter", 12)


def paint_shape_attr(page, slot, prob, show, i, attr):
    x, y, w, h = slot
    cy = y + h / 2
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 12, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 2, cy - 10, 20, 20, str(i), "Inter-Bold", 10)
    draw_shape(page, prob["shape"], x + 90, cy, 46)
    idx = 1 if attr == "corners" else 0
    value = SHAPE_FACTS[prob["shape"]][idx]
    _box(page, x + w - 64, cy, value if show else None, show, 50, 50)
    if show:
        page.phrase(x + 140, cy - 6, answer_phrase(prob), size=16)


def paint_shape_count(page, slot, prob, show, i):
    x, y, w, h = slot
    cy = y + h / 2 + (2 if show else 0)
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 12, cy, 10, fill=False, lw=1.2)
    page.center_in(x + 2, cy - 10, 20, 20, str(i), "Inter-Bold", 10)
    page.roundrect(x + 30, y + 18, w - 100, h - 36, 6, lw=1.2)
    for n, shape in enumerate(prob["shapes"]):
        draw_shape(page, shape, x + 58 + n * 52, cy, 32)
    n = sum(1 for s in prob["shapes"] if s == prob["target"])
    _box(page, x + w - 58, cy, n if show else None, show, 46, 46)
    if show:
        page.phrase(x + 36, y + 4, answer_phrase(prob), size=12)


def paint_pattern(page, slot, prob, show, i):
    x, y, w, h = slot
    if i <= 2:
        page.text(x, y + h - 12, "I do" if i == 1 else "We do", "Inter-Med", 8.5)
    page.circle(x + 12, y + h - 32, 10, fill=False, lw=1.2)
    page.center_in(x + 2, y + h - 42, 20, 20, str(i), "Inter-Bold", 10)
    rule = prob["rule"]
    shown = prob["repeats"] * len(rule)
    ask = prob["ask"]
    total = shown + ask
    cell = 40
    yb = y + (28 if show else 18)
    for n in range(total):
        bx = x + 30 + n * (cell + 4)
        page.rect(bx, yb, cell, cell, lw=1.5 if n >= shown else 1.2)
        shape = rule[n % len(rule)]
        if n < shown or show:
            draw_shape(page, shape, bx + cell / 2, yb + cell / 2, 24)
    if show:
        page.phrase(x + 30, y + 6, answer_phrase(prob), size=12)


def paint_sub_story(page, slot, prob, show, i):
    paint_story(page, slot, prob, show, i, sentence=True)


def draw_uniform(page, spec, show, top, paint, cols=1):
    probs = spec["problems"]
    slots = gslots(len(probs), top, cols) if cols == 2 else vslots(len(probs), top)
    for i, (prob, slot) in enumerate(zip(probs, slots), start=1):
        paint(page, slot, prob, show, i)


def render_sheet(page, spec, show, index, total):
    top = sheet_header(page, spec, show, index, total)
    layout = spec["layout"]
    if layout == "count":
        draw_uniform(page, spec, show, top, paint_count)
    elif layout == "two":
        draw_uniform(page, spec, show, top, paint_two)
    elif layout == "picture_total":
        draw_uniform(page, spec, show, top, paint_picture_total)
    elif layout == "picture_sentence":
        draw_uniform(page, spec, show, top, paint_picture_sentence)
    elif layout == "count_on":
        draw_uniform(page, spec, show, top, paint_count_on)
    elif layout == "sentence":
        draw_uniform(page, spec, show, top, paint_sentence, cols=2 if len(spec["problems"]) > 4 else 1)
    elif layout == "build":
        draw_uniform(page, spec, show, top, paint_build)
    elif layout == "story_total":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_story(p, s, pr, sh, i, False))
    elif layout == "story_sentence":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_story(p, s, pr, sh, i, True))
    elif layout == "ten_count":
        draw_uniform(page, spec, show, top, paint_ten_count, cols=2)
    elif layout == "ten_add":
        draw_uniform(page, spec, show, top, paint_ten_add)
    elif layout == "nline":
        draw_uniform(page, spec, show, top, paint_nline)
    elif layout == "partners":
        draw_uniform(page, spec, show, top, paint_partners)
    elif layout == "missing_pic":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_missing(p, s, pr, sh, i, True))
    elif layout == "missing_draw":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_missing(p, s, pr, sh, i, False))
    elif layout == "make10_frame":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_make10(p, s, pr, sh, i, True))
    elif layout == "make10_draw":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_make10(p, s, pr, sh, i, False))
    elif layout == "explain":
        draw_uniform(page, spec, show, top, paint_explain)
    elif layout == "sub_shown":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_sub(p, s, pr, sh, i, "shown"))
    elif layout == "sub_cross":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_sub(p, s, pr, sh, i, "cross"))
    elif layout == "sub_sentence":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_sub(p, s, pr, sh, i, "sentence"))
    elif layout == "sub_story":
        draw_uniform(page, spec, show, top, paint_sub_story)
    elif layout == "more":
        draw_uniform(page, spec, show, top, paint_compare)
    elif layout == "fewer":
        draw_uniform(page, spec, show, top, paint_compare)
    elif layout == "same":
        draw_uniform(page, spec, show, top, paint_same)
    elif layout == "numerals":
        draw_uniform(page, spec, show, top, paint_numerals)
    elif layout == "sequence":
        draw_uniform(page, spec, show, top, paint_sequence)
    elif layout == "draw_dots":
        draw_uniform(page, spec, show, top, paint_draw_dots)
    elif layout == "corners":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_shape_attr(p, s, pr, sh, i, "corners"))
    elif layout == "sides":
        draw_uniform(page, spec, show, top, lambda p, s, pr, sh, i: paint_shape_attr(p, s, pr, sh, i, "sides"))
    elif layout == "shape_count":
        draw_uniform(page, spec, show, top, paint_shape_count)
    elif layout == "pattern":
        draw_uniform(page, spec, show, top, paint_pattern)
    elif layout == "inter_mixed":
        _mixed(page, spec, show, top)
    elif layout == "adv_mixed":
        _mixed(page, spec, show, top)
    else:
        raise KeyError(layout)
    if show and len(page.phrases) != len(spec["problems"]):
        raise RuntimeError(
            f"{spec['title']}: {len(page.phrases)} key phrases for {len(spec['problems'])} problems"
        )
    if not show and page.phrases:
        raise RuntimeError(f"Practice page leaked an answer phrase: {page.phrases[0]}")


def _mixed(page, spec, show, top):
    paints = {
        "ten_add": paint_ten_add,
        "nline": paint_nline,
        "picture_sentence": paint_picture_sentence,
        "sentence": paint_sentence,
        "missing_draw": lambda p, s, pr, sh, i: paint_missing(p, s, pr, sh, i, False),
        "make10_draw": lambda p, s, pr, sh, i: paint_make10(p, s, pr, sh, i, False),
        "story_sentence": lambda p, s, pr, sh, i: paint_story(p, s, pr, sh, i, True),
    }
    probs = spec["problems"]
    weights = spec.get("weights") or [1] * len(probs)
    total_w = sum(weights)
    span = top - BOTTOM - GAP * (len(probs) - 1)
    slots = []
    y_top = top
    for wt in weights:
        h = span * wt / total_w
        y_bot = y_top - h
        slots.append((42, y_bot, 528, h))
        y_top = y_bot - GAP
    for i, (prob, slot) in enumerate(zip(probs, slots), start=1):
        paints[prob["paint"]](page, slot, prob, show, i)


def draw_blocks(doc, pack_name, role, title, blocks, max_pages, meta):
    """Flow parent-facing text. Raises if it needs more than max_pages."""
    made = []

    def start(continued):
        page = doc.new_page(pack_name, role, meta)
        page.brand(42, 746)
        if continued:
            page.text(42, 708, title, "Inter-Bold", 22)
            y = 684
        else:
            page.text(42, 706, title, "Inter-Bold", 26)
            y = 678
        made.append(page)
        return page, y

    page, y = start(False)
    size, leading = 12, 16.2
    for index, (kind, text) in enumerate(blocks):
        if kind == "break":
            page.finish()
            page, y = start(True)
            continue
        if kind == "h":
            follow = 0
            if index + 1 < len(blocks) and blocks[index + 1][0] in ("p", "license"):
                _lines, follow = page.measure(
                    blocks[index + 1][1],
                    500 if blocks[index + 1][0] == "license" else 526,
                    size=size,
                    leading=leading,
                )
                follow += 36
            if y - 28 - follow < 68:
                page.finish()
                page, y = start(True)
            page.text(42, y - 4, text, "Inter-Bold", 14)
            page.line(42, y - 10, 42 + min(220, sw(text, "Inter-Bold", 14)), y - 10, lw=1.15)
            y -= 28
        elif kind in ("p", "license"):
            lines, h = page.measure(text, 500 if kind == "license" else 526, size=size, leading=leading)
            need = h + (18 if kind == "license" else 10)
            if y - need < 68:
                page.finish()
                page, y = start(True)
            if kind == "license":
                page.roundrect(42, y - h - 14, 528, h + 14, 6, lw=1.45)
                y = page.wrap(text, 52, y - 6, 500, size=size, leading=leading)
                y -= 16
            else:
                y = page.wrap(text, 42, y, 526, size=size, leading=leading)
                y -= 9
        else:
            raise KeyError(kind)
    page.finish()
    if len(made) > max_pages:
        raise RuntimeError(f"{title} used {len(made)} pages; max is {max_pages}")
    if len(made) < 1:
        raise RuntimeError("empty flow")
    return made


def draw_cover(page, spec):
    page.rect(38, 58, 536, 688, lw=1.6)
    page.rect(44, 64, 524, 676, lw=0.8)
    page.roundrect(276, 676, 60, 42, 8, lw=1.5)
    page.center_in(276, 676, 60, 42, "P", "Inter-Bold", 22)
    page.text(306, 648, "PROUD LITTLE LEARNERS", "Inter-Med", 11, align="center")
    page.text(306, 626, "Kindergarten math", "Inter", 12, align="center")
    # Title may be two lines.
    title = spec["name"]
    if sw(title, "Inter-Bold", 34) <= 460:
        page.text(306, 560, title, "Inter-Bold", 34, align="center")
        sub_y = 524
    else:
        # Split on the last space before it fits, else wrap.
        page.wrap(title, 76, 590, 460, font="Inter-Bold", size=32, leading=38, max_lines=2, align="center")
        sub_y = 500
    page.text(306, sub_y, spec.get("level_line", ""), "Inter", 14, align="center")
    page.wrap(spec["blurb"], 86, sub_y - 16, 440, size=13, leading=18, max_lines=4, align="center")
    # Prerequisite box
    pre = spec["prereq_cover"]
    page.roundrect(78, 300, 456, 78, 8, lw=1.35)
    page.text(96, 354, "Before you start", "Inter-Bold", 12)
    page.wrap(pre, 96, 346, 424, size=12, leading=16, max_lines=2)
    page.text(96, 268, "Inside this pack", "Inter-Bold", 13)
    y = 246
    for line in spec["inside"]:
        page.circle(104, y + 3, 2.4, fill=True, lw=0.4)
        page.text(116, y, line, "Inter", 12)
        y -= 20
    page.text(306, 96, "US Letter  ·  print in black and white  ·  about 10 minutes a day", "Inter", 10, align="center")


def draw_weekly_cover(page, spec):
    page.rect(38, 58, 536, 688, lw=1.6)
    page.rect(44, 64, 524, 676, lw=0.8)
    page.roundrect(276, 680, 52, 36, 8, lw=1.4)
    page.center_in(276, 680, 52, 36, "P", "Inter-Bold", 18)
    page.text(306, 658, "PROUD LITTLE LEARNERS", "Inter-Med", 11, align="center")
    page.text(306, 634, "Weekly kindergarten math", "Inter", 12, align="center")
    page.text(306, 590, spec["kicker"], "Inter-Med", 13, align="center")
    page.wrap(spec["name"], 70, 570, 472, font="Inter-Bold", size=32, leading=38, max_lines=2, align="center")
    page.wrap(spec["blurb"], 90, 470, 432, size=13, leading=18, max_lines=4, align="center")
    page.roundrect(78, 300, 456, 70, 8, lw=1.3)
    page.text(96, 344, "Before you start", "Inter-Bold", 12)
    pre = spec["prereq_cover"]
    page.wrap(pre, 96, 336, 424, size=12, leading=16, max_lines=2)
    y = 270
    page.text(96, y, "Inside this week", "Inter-Bold", 13)
    y -= 22
    for line in spec["inside"]:
        page.circle(104, y + 3, 2.4, fill=True, lw=0.4)
        page.text(116, y, line, "Inter", 12)
        y -= 20
    page.text(306, 96, "US Letter  ·  print in black and white  ·  about 10 minutes a day", "Inter", 10, align="center")


def draw_tracker(page, pack_name, rows, intro):
    page.brand(42, 746)
    page.text(42, 708, "Progress tracker", "Inter-Bold", 26)
    bottom = page.wrap(intro, 42, 694, 526, size=12, leading=16, max_lines=3)
    y = bottom - 16
    cols = 2 if len(rows) > 8 else 1
    per = (len(rows) + cols - 1) // cols
    col_w = 250 if cols == 2 else 520
    gap_x = 28
    row_h = min(46, (y - 70) / per)
    for i, (num, label) in enumerate(rows):
        c = i // per
        r = i % per
        x = 42 + c * (col_w + gap_x)
        yy = y - (r + 1) * row_h
        page.circle(x + 14, yy + 12, 12, fill=False, lw=1.25)
        page.center_in(x + 2, yy, 24, 24, str(num), "Inter-Bold", 11)
        page.text(x + 34, yy + 6, label, "Inter", 12)
        star(page, x + col_w - 18, yy + 12, 11, lw=1.25)


def draw_certificate(page, pack_name):
    page.rect(48, 78, 516, 650, lw=1.7)
    page.rect(56, 86, 500, 634, lw=0.8)
    star(page, 110, 680, 14, lw=1.3)
    star(page, 306, 690, 18, lw=1.4)
    star(page, 502, 680, 14, lw=1.3)
    page.text(306, 630, "Certificate of completion", "Inter-Bold", 22, align="center")
    page.text(306, 598, "Proud Little Learners", "Inter", 12, align="center")
    page.text(306, 548, pack_name, "Inter-Bold", 26, align="center")
    page.wrap(
        "has finished the practice pages in this pack.",
        90,
        520,
        432,
        size=14,
        leading=19,
        max_lines=2,
        align="center",
    )
    page.text(120, 430, "Child's name", "Inter", 11)
    page.line(120, 418, 492, 418, lw=1.2)
    page.text(120, 360, "Date", "Inter", 11)
    page.line(120, 348, 300, 348, lw=1.2)
    page.text(330, 360, "Grown-up signature", "Inter", 11)
    page.line(330, 348, 492, 348, lw=1.2)
    page.wrap(
        "This page celebrates careful practice. It is not a test score and not a credential.",
        90,
        300,
        432,
        size=11,
        leading=15,
        max_lines=2,
        align="center",
    )
    page.wrap(
        "Personal, homeschool, and single-classroom use. Do not resell or redistribute.",
        90,
        250,
        432,
        size=10,
        leading=14,
        max_lines=2,
        align="center",
    )
    page.text(306, 150, "Answer keys for grown-ups follow this page.", "Inter", 11, align="center")
