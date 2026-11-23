"""Generate Figure 1 (workflow x entry-surface map) from threat_catalog.yaml.

Outputs figures/fig1_map.svg and figures/fig1_map.png (7 in wide at 300 dpi = 2100 px,
i.e., a full-width magazine figure). Each catalog row is a chip showing its ASI number;
chip style encodes the operator (whose agent it is). Clinical documentation is shaded
as the contrast row. Standard library + Pillow only.
"""
import importlib.util, os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("cc", os.path.join(ROOT, "check_catalog.py"))
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
items, errs = cc.parse(os.path.join(ROOT, "threat_catalog.yaml"))
if errs:
    sys.exit("catalog parse errors: " + "; ".join(errs))

ROWS = [("prior_authorization", "Prior\nauthorization"), ("claims", "Claims and\npayment integrity"),
        ("eligibility", "Eligibility"), ("member_service", "Member\nservice"),
        ("clinical_documentation", "Clinical\ndocumentation\n(contrast)")]
COLS = [("x12", "X12"), ("hl7v2", "HL7 v2"), ("ccda", "C-CDA"), ("fhir", "FHIR"), ("fax_ocr", "Fax/\nOCR"),
        ("chat", "Chat"), ("voice", "Voice"), ("messaging", "Messag-\ning"),
        ("events", "Events"), ("knowledge", "Know-\nledge"), ("memory", "Memory"), ("tool_metadata", "Tool\nmeta-\ndata"),
        ("agent_to_agent", "Agent-\nto-\nagent"), ("internal", "Internal")]
GROUPS = [("Healthcare data standards", 0, 5), ("Human channels", 5, 8), ("Agent internals and links", 8, 13), ("None", 13, 14)]
OPS = ["payer", "provider", "intermediary", "consumer"]

W = 2100
LEFT = 300
CW = (W - LEFT - 20) // len(COLS)          # column width
GH, HH = 60, 150                           # group header, column header heights
RH = 150                                   # row height
TOP = 20
GRID_T = TOP + GH + HH
H = GRID_T + RH * len(ROWS) + 150
CHIP_W, CHIP_H, GAP = 50, 34, 6
FS_LABEL, FS_HEAD, FS_CHIP, FS_LEG = 30, 26, 22, 26

cells = {}
for e in items:
    cells.setdefault((e["workflow"], e["entry_surface"]), []).append(e)
for k in cells:
    cells[k].sort(key=lambda e: (e["owasp_asi"], e["id"]))

# ---------- primitive list (rendered to both SVG and PNG)
prims = []
def rect(x, y, w, h, fill="none", stroke="none", sw=0, dash=False, r=0): prims.append(("rect", x, y, w, h, fill, stroke, sw, dash, r))
def text(x, y, s, size, anchor="middle", bold=False, fill="#000"): prims.append(("text", x, y, s, size, anchor, bold, fill))
def line(x1, y1, x2, y2, stroke="#000", sw=1): prims.append(("line", x1, y1, x2, y2, stroke, sw))

def chip(x, y, op, label):
    if op == "payer":
        rect(x, y, CHIP_W, CHIP_H, fill="#222", stroke="#222", sw=2, r=4); text(x + CHIP_W / 2, y + CHIP_H / 2, label, FS_CHIP, bold=True, fill="#fff")
    elif op == "provider":
        rect(x, y, CHIP_W, CHIP_H, fill="#fff", stroke="#222", sw=3, r=4); text(x + CHIP_W / 2, y + CHIP_H / 2, label, FS_CHIP, bold=True)
    elif op == "intermediary":
        rect(x, y, CHIP_W, CHIP_H, fill="#bbb", stroke="#222", sw=2, dash=True, r=4); text(x + CHIP_W / 2, y + CHIP_H / 2, label, FS_CHIP, bold=True)
    else:  # consumer
        rect(x, y, CHIP_W, CHIP_H, fill="#fff", stroke="#222", sw=2, dash=True, r=CHIP_H // 2); text(x + CHIP_W / 2, y + CHIP_H / 2, label, FS_CHIP, bold=True)

# background shading for the contrast row
ci = [r[0] for r in ROWS].index("clinical_documentation")
rect(0, GRID_T + ci * RH, W, RH, fill="#e6e6e6")
# group headers
for name, a, b in GROUPS:
    x0, x1 = LEFT + a * CW, LEFT + b * CW
    text((x0 + x1) / 2, TOP + GH / 2, name, FS_HEAD, bold=True)
    line(x0 + 6, TOP + GH - 6, x1 - 6, TOP + GH - 6, sw=2)
# column headers
for j, (_, lab) in enumerate(COLS):
    lines_ = lab.split("\n"); n = len(lines_)
    for k, ln in enumerate(lines_):
        text(LEFT + j * CW + CW / 2, TOP + GH + HH / 2 + (k - (n - 1) / 2) * (FS_HEAD + 4), ln, FS_HEAD)
# grid lines
for i in range(len(ROWS) + 1):
    line(0, GRID_T + i * RH, W - 20, GRID_T + i * RH, stroke="#888", sw=1)
for j in range(len(COLS) + 1):
    sw = 3 if j in (0, 5, 8, 13, 14) else 1
    line(LEFT + j * CW, GRID_T, LEFT + j * CW, GRID_T + RH * len(ROWS), stroke="#888" if sw == 1 else "#333", sw=sw)
# row labels and chips
for i, (wf, lab) in enumerate(ROWS):
    lines_ = lab.split("\n"); n = len(lines_)
    for k, ln in enumerate(lines_):
        text(12, GRID_T + i * RH + RH / 2 + (k - (n - 1) / 2) * (FS_LABEL + 4), ln, FS_LABEL, anchor="start", bold=(wf != "clinical_documentation"))
    for j, (sf, _) in enumerate(COLS):
        es = cells.get((wf, sf), [])
        if not es:
            continue
        per_row = 2
        nrows = (len(es) + per_row - 1) // per_row
        block_h = nrows * CHIP_H + (nrows - 1) * GAP
        y0 = GRID_T + i * RH + (RH - block_h) / 2
        for k, e in enumerate(es):
            r_, c_ = divmod(k, per_row)
            in_row = min(per_row, len(es) - r_ * per_row)
            row_w = in_row * CHIP_W + (in_row - 1) * GAP
            x0 = LEFT + j * CW + (CW - row_w) / 2
            chip(x0 + c_ * (CHIP_W + GAP), y0 + r_ * (CHIP_H + GAP), e["operator"], e["owasp_asi"][3:])
# legend
ly = GRID_T + RH * len(ROWS) + 40
text(12, ly + CHIP_H / 2, "Chip = one catalog entry; number = OWASP ASI entry (01-10).  Operator (whose agent):", FS_LEG, anchor="start")
lx = 12; ly2 = ly + 60
for op, name in zip(OPS, ["Payer", "Provider", "Intermediary", "Consumer"]):
    chip(lx, ly2, op, "06"); text(lx + CHIP_W + 12, ly2 + CHIP_H / 2, name, FS_LEG, anchor="start"); lx += 300
rect(lx + 20, ly2, 60, CHIP_H, fill="#e6e6e6", stroke="#888", sw=1); text(lx + 92, ly2 + CHIP_H / 2, "Shaded row = clinical contrast", FS_LEG, anchor="start")

# ---------- SVG
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, Helvetica, sans-serif">',
       f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>']
for p in prims:
    if p[0] == "rect":
        _, x, y, w, h, fill, stroke, sw, dash, r = p
        svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"' + (' stroke-dasharray="6,4"' if dash else '') + '/>')
    elif p[0] == "line":
        _, x1, y1, x2, y2, stroke, sw = p
        svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
    else:
        _, x, y, s, size, anchor, bold, fill = p
        svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" dominant-baseline="central" fill="{fill}"' + (' font-weight="bold"' if bold else '') + f'>{esc(s)}</text>')
svg.append("</svg>")
open(os.path.join(HERE, "fig1_map.svg"), "w", encoding="utf-8").write("\n".join(svg))

# ---------- PNG
FONTS = {False: "C:/Windows/Fonts/arial.ttf", True: "C:/Windows/Fonts/arialbd.ttf"}
_fc = {}
def font(size, bold):
    k = (size, bold)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(FONTS[bold], size)
    return _fc[k]
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)
def dashed_rect(x, y, w, h, stroke, sw):
    for (x1, y1, x2, y2) in [(x, y, x + w, y), (x + w, y, x + w, y + h), (x + w, y + h, x, y + h), (x, y + h, x, y)]:
        L = max(abs(x2 - x1), abs(y2 - y1)); n = int(L // 10)
        for t in range(n):
            a, b = t * 10 / L, min((t * 10 + 6) / L, 1)
            d.line([(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)], fill=stroke, width=sw)
for p in prims:
    if p[0] == "rect":
        _, x, y, w, h, fill, stroke, sw, dash, r = p
        d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=None if fill == "none" else fill,
                            outline=None if (stroke == "none" or dash) else stroke, width=sw if not dash else 0)
        if dash and stroke != "none":
            dashed_rect(x, y, w, h, stroke, sw)
    elif p[0] == "line":
        _, x1, y1, x2, y2, stroke, sw = p
        d.line([(x1, y1), (x2, y2)], fill=stroke, width=sw)
    else:
        _, x, y, s, size, anchor, bold, fill = p
        d.text((x, y), s, font=font(size, bold), fill=fill, anchor="mm" if anchor == "middle" else "lm")
img.save(os.path.join(HERE, "fig1_map.png"), dpi=(300, 300))

n_by_op = {op: sum(1 for e in items if e["operator"] == op) for op in OPS}
print(f"Figure 1 written: {W}x{H} px (7.0 in wide at 300 dpi); {len(items)} chips; operators {n_by_op}")
print(f"max chips in one cell: {max(len(v) for v in cells.values())}")
