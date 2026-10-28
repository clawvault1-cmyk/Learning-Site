"""Low-ink drawing helpers for Proud Little Learners worksheets.

US Letter, black strokes on white, no gray fills. Text that would leave the
safe area raises OverflowError so the build fails instead of clipping.
"""

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas

pdfmetrics.registerFont(TTFont("Inter", "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bold", "/usr/share/fonts/truetype/macos/Inter-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Med", "/usr/share/fonts/truetype/macos/Inter-Medium.ttf"))

W, H = 612.0, 792.0
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)

# Content must stay inside this box. The footer is the only exception.
SAFE_L, SAFE_R = 36.0, W - 36.0
SAFE_TOP, SAFE_BOTTOM = H - 30.0, 46.0
FOOTER_BOTTOM = 26.0


class OverflowError(Exception):
    pass


def sw(text, font, size):
    return pdfmetrics.stringWidth(text, font, size)


def wrap_lines(text, font, size, max_w):
    words = text.split()
    if not words:
        return []
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if sw(trial, font, size) <= max_w:
            cur = trial
            continue
        if not cur:
            raise OverflowError(f"Word does not fit: {word!r} at {size}pt")
        lines.append(cur)
        cur = word
    if cur:
        lines.append(cur)
    return lines


class Doc:
    def __init__(self, path, title):
        self.path = path
        self.c = pdfcanvas.Canvas(path, pagesize=(W, H))
        self.c.setTitle(title)
        self.c.setAuthor("Proud Little Learners")
        self.pages = []

    def new_page(self, pack_name, role, meta=None):
        page = Page(self, pack_name, role, meta or {})
        self.pages.append(page)
        return page

    def save(self):
        self.c.save()


class Page:
    def __init__(self, doc, pack_name, role, meta):
        self.doc = doc
        self.c = doc.c
        self.pack_name = pack_name
        self.role = role
        self.meta = meta
        self.texts = []
        self.boxes = []  # text bboxes
        self.phrases = []
        self._footer_done = False
        self.c.setFillColorRGB(*WHITE)
        self.c.rect(0, 0, W, H, stroke=0, fill=1)
        self.c.setFillColorRGB(*BLACK)
        self.c.setStrokeColorRGB(*BLACK)

    def _ink(self, lw):
        self.c.setStrokeColorRGB(*BLACK)
        self.c.setFillColorRGB(*BLACK)
        self.c.setLineWidth(lw)
        self.c.setLineCap(0)
        self.c.setLineJoin(0)

    def _check(self, box, what, footer=False):
        x0, y0, x1, y1 = box
        bottom = FOOTER_BOTTOM if footer else SAFE_BOTTOM
        if x0 < SAFE_L - 0.5 or x1 > SAFE_R + 0.5 or y0 < bottom - 0.5 or y1 > SAFE_TOP + 0.5:
            raise OverflowError(
                f"{self.role} {self.meta.get('title', '')}: {what!r} overflows {tuple(round(v, 1) for v in box)}"
            )

    def text(self, x, y, s, font="Inter", size=12, align="left", footer=False):
        if s is None or s == "":
            return 0
        width = sw(s, font, size)
        if align == "center":
            x = x - width / 2
        elif align == "right":
            x = x - width
        asc = size * 0.80
        desc = size * 0.22
        box = (x, y - desc, x + width, y + asc)
        self._check(box, s, footer=footer)
        self._ink(1)
        self.c.setFont(font, size)
        self.c.drawString(x, y, s)
        self.texts.append(s)
        self.boxes.append(box)
        return width

    def wrap(self, text, x, top, max_w, font="Inter", size=12, leading=None, max_lines=None, align="left"):
        """Draw wrapped text. `top` is the top of the first line's em box. Returns the y under the block."""
        leading = leading or round(size * 1.38, 2)
        lines = wrap_lines(text, font, size, max_w)
        if max_lines is not None and len(lines) > max_lines:
            raise OverflowError(
                f"{self.role} {self.meta.get('title', '')}: {len(lines)} lines > {max_lines}: {text[:80]!r}"
            )
        block_w = max(sw(line, font, size) for line in lines) if lines else 0
        y_top = top
        for i, line in enumerate(lines):
            baseline = y_top - size * 0.80 - i * leading
            lx = x
            if align == "center":
                lx = x + (max_w - sw(line, font, size)) / 2
                self.text(lx, baseline, line, font, size, align="left")
            else:
                self.text(lx, baseline, line, font, size, align=align)
        if not lines:
            return top
        return y_top - len(lines) * leading

    def measure(self, text, max_w, font="Inter", size=12, leading=None):
        leading = leading or round(size * 1.38, 2)
        lines = wrap_lines(text, font, size, max_w)
        return lines, len(lines) * leading

    def center_in(self, x, y, w, h, s, font="Inter-Bold", size=22):
        width = sw(s, font, size)
        baseline = y + (h - size) / 2 + size * 0.18
        self.text(x + (w - width) / 2, baseline, s, font, size)

    def line(self, x0, y0, x1, y1, lw=1.25):
        pad = lw / 2
        self._check((min(x0, x1) - pad, min(y0, y1) - pad, max(x0, x1) + pad, max(y0, y1) + pad), "line")
        self._ink(lw)
        self.c.line(x0, y0, x1, y1)

    def rect(self, x, y, w, h, lw=1.5):
        self._check((x - lw, y - lw, x + w + lw, y + h + lw), "rect")
        self._ink(lw)
        self.c.rect(x, y, w, h, stroke=1, fill=0)

    def roundrect(self, x, y, w, h, r=6, lw=1.5):
        self._check((x - lw, y - lw, x + w + lw, y + h + lw), "roundrect")
        self._ink(lw)
        self.c.roundRect(x, y, w, h, r, stroke=1, fill=0)

    def circle(self, cx, cy, r, fill=False, lw=1.5):
        self._check((cx - r - lw, cy - r - lw, cx + r + lw, cy + r + lw), "circle")
        self._ink(lw)
        self.c.circle(cx, cy, r, stroke=1, fill=1 if fill else 0)

    def polygon(self, pts, lw=1.5):
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        self._check((min(xs) - lw, min(ys) - lw, max(xs) + lw, max(ys) + lw), "polygon")
        self._ink(lw)
        p = self.c.beginPath()
        p.moveTo(pts[0][0], pts[0][1])
        for x, y in pts[1:]:
            p.lineTo(x, y)
        p.close()
        self.c.drawPath(p, stroke=1, fill=0)

    def curve(self, x0, y0, x1, y1, lift, lw=1.35):
        self._check((min(x0, x1) - 2, min(y0, y1) - 2, max(x0, x1) + 2, max(y0, y1) + lift + 2), "curve")
        self._ink(lw)
        p = self.c.beginPath()
        p.moveTo(x0, y0)
        p.curveTo(x0, y0 + lift, x1, y1 + lift, x1, y1)
        self.c.drawPath(p, stroke=1, fill=0)

    def phrase(self, x, y, s, size=16):
        """Draw a canonical answer phrase. Keys only."""
        self.text(x, y, s, "Inter-Bold", size)
        self.phrases.append(s)

    def footer(self):
        label = f"Proud Little Learners · {self.pack_name}"
        self.line(40, 48, W - 40, 48, lw=0.8)
        self.text(42, 32, label, "Inter", 9, footer=True)
        self._footer_done = True

    def finish(self):
        if not self._footer_done:
            self.footer()
        self._check_overlaps()
        self.c.showPage()

    def _check_overlaps(self):
        boxes = self.boxes
        for i in range(len(boxes)):
            a = boxes[i]
            for j in range(i + 1, len(boxes)):
                b = boxes[j]
                dx = min(a[2], b[2]) - max(a[0], b[0])
                dy = min(a[3], b[3]) - max(a[1], b[1])
                if dx > 1.5 and dy > 1.5:
                    raise OverflowError(
                        f"Overlapping text on {self.role} {self.meta.get('title', '')}: "
                        f"{self.texts[i]!r} and {self.texts[j]!r}"
                    )

    def brand(self, x, y):
        self.roundrect(x, y - 3, 15, 15, 3, lw=1.15)
        self.center_in(x, y - 3, 15, 15, "P", "Inter-Bold", 9)
        self.text(x + 20, y, "Proud Little Learners", "Inter-Med", 9.5)

    def name_date(self, y=716):
        self.text(42, y, "Name", "Inter", 13)
        self.line(88, y - 1, 330, y - 1, lw=1.1)
        self.text(348, y, "Date", "Inter", 13)
        self.line(390, y - 1, 560, y - 1, lw=1.1)

    def bowl(self, x, cy):
        """Empty-group mark. A bowl, not a dot, so it is not counted as one object."""
        self._ink(1.35)
        p = self.c.beginPath()
        p.moveTo(x, cy + 8)
        p.lineTo(x + 2, cy - 2)
        p.curveTo(x + 4, cy - 16, x + 32, cy - 16, x + 34, cy - 2)
        p.lineTo(x + 36, cy + 8)
        self._check((x - 1, cy - 18, x + 38, cy + 10), "bowl")
        self.c.drawPath(p, stroke=1, fill=0)
        return 36, 28


def answer_phrase(prob):
    """Canonical key phrase. The checker parses this; it does not call this helper."""
    k = prob["kind"]
    if k == "count":
        return f"Count: {prob['n']}"
    if k == "two":
        return f"Counts: {prob['a']} and {prob['b']}"
    if k in ("add", "make10"):
        return f"{prob['a']} + {prob['b']} = {prob['a'] + prob['b']}"
    if k == "sub":
        return f"{prob['a']} - {prob['b']} = {prob['a'] - prob['b']}"
    if k == "partners":
        return f"{prob['total']} = {prob['a']} + {prob['b']}"
    if k == "missing":
        miss = prob["total"] - prob["known"]
        return f"{prob['total']} = {prob['known']} + {miss}"
    if k == "more":
        side = "Left" if prob["a"] > prob["b"] else "Right"
        return f"{side} has more"
    if k == "fewer":
        side = "Left" if prob["a"] < prob["b"] else "Right"
        return f"{side} has fewer"
    if k == "same":
        return "Same" if prob["a"] == prob["b"] else "Not the same"
    if k == "numerals":
        if prob["a"] == prob["b"]:
            return "Both the same"
        return "Left is more" if prob["a"] > prob["b"] else "Right is more"
    if k == "missing_num":
        return f"Missing: {prob['seq'][prob['blank']]}"
    if k == "dots":
        return f"Dots: {prob['n']}"
    if k == "corners":
        return f"Corners: {SHAPE_FACTS[prob['shape']][1]}"
    if k == "sides":
        return f"Sides: {SHAPE_FACTS[prob['shape']][0]}"
    if k == "shape_count":
        n = sum(1 for s in prob["shapes"] if s == prob["target"])
        return f"{prob['target'].capitalize()}: {n}"
    if k == "pattern":
        rule = prob["rule"]
        start = len(rule) * prob["repeats"]
        nxt = [rule[i % len(rule)] for i in range(start, start + prob["ask"])]
        return "Next: " + ", ".join(nxt)
    raise KeyError(k)


# Renderer copy of shape facts. The checker has its own copy on purpose.
SHAPE_FACTS = {
    "triangle": (3, 3),  # sides, corners
    "square": (4, 4),
    "rectangle": (4, 4),
    "circle": (0, 0),
}


def draw_group(page, x, cy, n, kind="circle", gap=24, r=9, per_row=5):
    """Draw n objects centered on cy. Returns width, height."""
    if n == 0:
        page.bowl(x, cy)
        return 36, 28
    rows = (n + per_row - 1) // per_row
    cols = min(n, per_row)
    for i in range(n):
        col = i % per_row
        row = i // per_row
        cx = x + r + col * gap
        yy = cy + (rows - 1) * gap / 2 - row * gap
        if kind == "circle":
            page.circle(cx, yy, r, fill=True, lw=1.2)
        elif kind == "open":
            page.circle(cx, yy, r, fill=False, lw=1.5)
        elif kind == "square":
            s = r * 2 - 1
            page.rect(cx - s / 2, yy - s / 2, s, s, lw=1.45)
        else:
            raise KeyError(kind)
    w = (cols - 1) * gap + 2 * r
    h = (rows - 1) * gap + 2 * r
    return w, h


def draw_shape(page, kind, cx, cy, size):
    if kind == "circle":
        page.circle(cx, cy, size / 2, fill=False, lw=1.6)
    elif kind == "square":
        page.rect(cx - size / 2, cy - size / 2, size, size, lw=1.6)
    elif kind == "rectangle":
        page.rect(cx - size / 2, cy - size * 0.32, size, size * 0.64, lw=1.6)
    elif kind == "triangle":
        page.polygon(
            [(cx, cy + size * 0.52), (cx - size * 0.55, cy - size * 0.42), (cx + size * 0.55, cy - size * 0.42)],
            lw=1.6,
        )
    else:
        raise KeyError(kind)


def ten_frame(page, x, y, filled, open_n=0, cell=26):
    """y is the bottom of the frame. Top row fills first, left to right."""
    cols = 5
    w, h = cols * cell, 2 * cell
    page.rect(x, y, w, h, lw=1.6)
    for c in range(1, cols):
        page.line(x + c * cell, y, x + c * cell, y + h, lw=1.1)
    page.line(x, y + cell, x + w, y + cell, lw=1.1)
    rdot = cell * 0.28

    def center(i):
        top = i < 5
        col = i if top else i - 5
        cy = y + (cell + cell / 2 if top else cell / 2)
        cx = x + col * cell + cell / 2
        return cx, cy

    for i in range(filled):
        page.circle(*center(i), rdot, fill=True, lw=1.0)
    for j in range(open_n):
        page.circle(*center(filled + j), rdot, fill=False, lw=1.35)
    return w, h


def answer_box(page, x, y, w, h, value):
    page.roundrect(x, y, w, h, 5, lw=1.9)
    if value is not None:
        page.center_in(x, y, w, h, str(value), "Inter-Bold", 24 if len(str(value)) == 1 else 20)
