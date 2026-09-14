#!/usr/bin/env python3
"""
Render an editorial Instagram carousel deck to 1080x1350 PNG slides.

Usage:
    python3 render.py deck.json [-o OUTDIR] [--scale 2] [--html-only]

All geometry constants below are MEASURED from the reference deck (CS posting.pdf).
Do not "tidy" them. See reference/design-system.md.
"""
import argparse, base64, json, mimetypes, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

# ---------------------------------------------------------------- tokens ----
CANVAS_W, CANVAS_H = 1080, 1350
MARGIN_X = 87
CONTENT_W = CANVAS_W - 2 * MARGIN_X          # 906

COLOR_INK = "#000000"
COLOR_MUTED = "#848484"
COLOR_SWIPE = "#676363"
COLOR_BG = "#FFFFFF"

# Inter metrics (unitsPerEm 2048, ascender 1984, descender -494)
ASC, DESC, UPM = 1984, 494, 2048
CONTENT_AREA = (ASC + DESC) / UPM            # 1.2100 em
BASELINE_FACTOR = ASC / UPM - CONTENT_AREA / 2   # 0.36375 em

EMPHASIS_WEIGHT = 600            # the one bold word per headline

TYPE = {
    "headline": dict(size=95,    lh=105, weight=300, ls=-0.0518, color=COLOR_INK,   transform="capitalize"),
    "subhead":  dict(size=40,    lh=54,  weight=400, ls=-0.0353, color=COLOR_MUTED, transform="none"),
    "swipe":    dict(size=32,    lh=32,  weight=400, ls=0.0,     color=COLOR_SWIPE, transform="none"),
}

# Measured first-baseline positions, in canvas px.
# The eyebrow is no longer rendered; headline and subhead keep their measured positions.
BASELINES = {
    "cover": dict(headline=341, subhead=543),
    "body":  dict(headline=651, subhead=853),
}
BASELINES["closer"] = BASELINES["body"]

COVER_IMAGE_TOP = 748                        # full-bleed, bottom-anchored, 602px tall
SWIPE_RIGHT, SWIPE_BOTTOM = 56, 52           # body/closer swipe group
SWIPE_ICON_W, SWIPE_ICON_H = 29.65, 32.98
SWIPE_GAP = 9.35
COVER_ICON_W, COVER_ICON_H, COVER_ICON_RIGHT = 57, 63, 47

MAX_HEADLINE_LINES = 2
MAX_SUBHEAD_LINES = 2


def block_top(role: str, baseline: float) -> float:
    """CSS `top` for an absolutely positioned block whose FIRST baseline must land on `baseline`."""
    t = TYPE[role]
    return baseline - t["lh"] / 2 - BASELINE_FACTOR * t["size"]


def data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as fh:
        return f"data:{mime};base64," + base64.b64encode(fh.read()).decode()


def font_face(name: str, weight: int, filename: str) -> str:
    return (f"@font-face{{font-family:'{name}';font-style:normal;font-weight:{weight};"
            f"font-display:block;src:url({data_uri(os.path.join(ASSETS,'fonts',filename))}) format('woff2');}}")


def css() -> str:
    faces = "".join([
        font_face("InterCarousel", 300, "Inter-Light.woff2"),
        font_face("InterCarousel", 400, "Inter-Regular.woff2"),
        font_face("InterCarousel", 500, "Inter-Medium.woff2"),
        font_face("InterCarousel", 600, "Inter-SemiBold.woff2"),
    ])
    rules = []
    for role, t in TYPE.items():
        rules.append(
            f".t-{role}{{font-size:{t['size']}px;line-height:{t['lh']}px;font-weight:{t['weight']};"
            f"letter-spacing:{t['ls']:.4f}em;color:{t['color']};text-transform:{t['transform']};}}"
        )
    return faces + """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{background:#555;}
.slide{position:relative;width:%(W)spx;height:%(H)spx;background:%(BG)s;overflow:hidden;
  font-family:'InterCarousel',sans-serif;font-kerning:normal;
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}
.texture{position:absolute;left:-102px;top:0;width:1350px;height:1350px;
  background-image:url(%(TEX)s);background-size:100%% 100%%;}
.block{position:absolute;left:%(MX)spx;width:%(CW)spx;}
.hero{position:absolute;left:0;top:%(HT)spx;width:%(W)spx;height:%(HH)spx;
  object-fit:cover;object-position:center bottom;filter:grayscale(1);}
.swipe{position:absolute;right:%(SR)spx;bottom:%(SB)spx;display:flex;align-items:center;
  gap:%(SG)spx;color:%(SC)s;}
.swipe > svg{width:%(SIW)spx;height:%(SIH)spx;display:block;flex:0 0 auto;}
.swipe > .swipe-label{display:block;white-space:nowrap;}
.t-headline em{font-style:normal;font-weight:%(EM)s;}
.cover-swipe{position:absolute;right:%(CIR)spx;top:50%%;transform:translateY(-50%%);
  width:%(CIW)spx;height:%(CIH)spx;color:%(SC)s;}
.cover-swipe svg{width:100%%;height:100%%;display:block;}
""" % dict(W=CANVAS_W, H=CANVAS_H, BG=COLOR_BG, MX=MARGIN_X, CW=CONTENT_W,
           TEX=data_uri(os.path.join(ASSETS, "paper-grid.jpg")),
           HT=COVER_IMAGE_TOP, HH=CANVAS_H - COVER_IMAGE_TOP,
           SR=SWIPE_RIGHT, SB=SWIPE_BOTTOM, SG=SWIPE_GAP, SC=COLOR_SWIPE,
           SIW=SWIPE_ICON_W, SIH=SWIPE_ICON_H,
           CIR=COVER_ICON_RIGHT, CIW=COVER_ICON_W, CIH=COVER_ICON_H,
           EM=EMPHASIS_WEIGHT) + "".join(rules)


EMPHASIS_RE = re.compile(r"\*\*(.+?)\*\*")


def esc(s: str) -> str:
    """Escape, then apply **emphasis** and explicit "|" line breaks."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = EMPHASIS_RE.sub(r"<em>\1</em>", s)
    s = s.replace("\r\n", "\n").replace("|", "\n")
    return "<br>".join(part.strip() for part in s.split("\n"))


def slide_html(slide: dict, index: int, total: int) -> str:
    kind = slide.get("type") or ("cover" if index == 0 else "closer" if index == total - 1 else "body")
    if kind not in BASELINES:
        raise ValueError(f"slide {index+1}: unknown type {kind!r} (use cover|body|closer)")
    bl = BASELINES[kind]
    swipe_svg = open(os.path.join(ASSETS, "swipe.svg")).read()

    parts = ['<div class="texture"></div>']
    if kind == "cover" and slide.get("image"):
        parts.append(f'<img class="hero" src="{data_uri(slide["image"])}">')

    for role in ("headline", "subhead"):
        text = (slide.get(role) or "").strip()
        if not text:
            continue
        parts.append(
            f'<div class="block t-{role}" data-role="{role}" '
            f'style="top:{block_top(role, bl[role]):.3f}px">{esc(text)}</div>'
        )

    if kind == "cover":
        parts.append(f'<div class="cover-swipe">{swipe_svg}</div>')
    elif kind == "body":
        parts.append(f'<div class="swipe">{swipe_svg}'
                     f'<span class="swipe-label t-swipe">Swipe</span></div>')

    return f'<div class="slide" id="s{index+1}" data-kind="{kind}">' + "".join(parts) + "</div>"


def build_html(deck: dict) -> str:
    slides = deck["slides"]
    body = "".join(slide_html(s, i, len(slides)) for i, s in enumerate(slides))
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css()}</style></head><body>{body}</body></html>"


MEASURE_JS = """
() => Array.from(document.querySelectorAll('.slide')).map(sl => ({
  id: sl.id,
  kind: sl.dataset.kind,
  blocks: Array.from(sl.querySelectorAll('.block')).map(b => {
    const cs = getComputedStyle(b);
    const lh = parseFloat(cs.lineHeight);
    const r = b.getBoundingClientRect();
    return {
      role: b.dataset.role,
      lines: Math.round(b.scrollHeight / lh),
      widthPx: Math.max(...Array.from(b.getClientRects()).map(x => x.width), 0),
      right: r.left - sl.getBoundingClientRect().left + b.scrollWidth,
      bottom: r.top - sl.getBoundingClientRect().top + b.scrollHeight,
    };
  })
}))
"""


def check_copy(deck: dict):
    """Copy-level rules, checked before anything is rendered."""
    problems = []
    for i, s in enumerate(deck["slides"], 1):
        headline = s.get("headline") or ""
        if not headline.strip():
            problems.append(f"slide {i}: missing headline")
            continue
        n_em = len(EMPHASIS_RE.findall(headline))
        if n_em == 0:
            problems.append(f"slide {i}: headline has no emphasised word — wrap exactly one in **asterisks**")
        elif n_em > 1:
            problems.append(f"slide {i}: headline has {n_em} emphasised words — exactly one is allowed")
        if EMPHASIS_RE.search(s.get("subhead") or ""):
            problems.append(f"slide {i}: emphasis belongs in the headline only, not the subhead")
        if s.get("eyebrow"):
            problems.append(f"slide {i}: 'eyebrow' is no longer rendered — use 'beat' to note the narrative beat")
    return problems


def validate(reports):
    """Layout rules, checked against the rendered page."""
    problems = []
    limits = {"headline": MAX_HEADLINE_LINES, "subhead": MAX_SUBHEAD_LINES}
    for r in reports:
        n = r["id"].replace("s", "")
        for b in r["blocks"]:
            cap = limits[b["role"]]
            if b["lines"] > cap:
                problems.append(f"slide {n}: {b['role']} wraps to {b['lines']} lines (max {cap}) — shorten the copy")
            if b["bottom"] > CANVAS_H - 40:
                problems.append(f"slide {n}: {b['role']} runs past the safe bottom edge")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("-o", "--outdir", default="out")
    ap.add_argument("--scale", type=int, default=2)
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--allow-overflow", action="store_true")
    args = ap.parse_args()

    with open(args.deck) as fh:
        deck = json.load(fh)
    deckdir = os.path.dirname(os.path.abspath(args.deck))
    for s in deck["slides"]:
        if s.get("image") and not os.path.isabs(s["image"]):
            s["image"] = os.path.join(deckdir, s["image"])

    copy_problems = check_copy(deck)

    os.makedirs(args.outdir, exist_ok=True)
    html = build_html(deck)
    html_path = os.path.join(args.outdir, "_deck.html")
    with open(html_path, "w") as fh:
        fh.write(html)
    if args.html_only:
        print(html_path)
        return

    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=[
            "--disable-lcd-text",            # grayscale AA, matches the Figma export
            "--font-render-hinting=none",
            "--force-color-profile=srgb",
        ])
        page = browser.new_page(viewport={"width": CANVAS_W, "height": CANVAS_H},
                                device_scale_factor=args.scale)
        page.goto("file://" + os.path.abspath(html_path))
        page.wait_for_timeout(400)
        reports = page.evaluate(MEASURE_JS)
        problems = copy_problems + validate(reports)
        written = []
        for i, r in enumerate(reports):
            out = os.path.join(args.outdir, f"slide-{i+1:02d}.png")
            page.locator("#" + r["id"]).screenshot(path=out)
            written.append(out)
        browser.close()

    for p in written:
        print(p)
    if problems:
        print("\nPROBLEMS:", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        if not args.allow_overflow:
            sys.exit(2)


if __name__ == "__main__":
    main()
