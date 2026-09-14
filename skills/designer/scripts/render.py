#!/usr/bin/env python3
"""
Render a deck JSON into ready-to-post PNGs for the AI Content Team OS.

Usage:
    python3 render.py deck.json -o out [--scale 2] [--html-only] [--allow-overflow]

The deck is brand-driven: colours, name and handle come from the `brand` block,
so the same renderer produces on-brand assets for any creator. Geometry is
derived from a single canvas preset so every platform size stays consistent.

Exits non-zero and lists every fit problem if any text overflows its box.
Fix the copy, never the type size.
"""
import argparse, base64, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(os.path.dirname(HERE), "assets", "fonts")

# ----------------------------------------------------------------- presets ---
# name -> (width, height). Base width 1080 defines the type scale; other widths
# scale proportionally so a LinkedIn card and an IG slide read as one system.
PRESETS = {
    "ig-portrait":    (1080, 1350),   # Instagram carousel / feed, 4:5
    "ig-square":      (1080, 1080),   # Instagram square
    "ig-story":       (1080, 1920),   # Stories / Reels cover, 9:16
    "li-landscape":   (1200, 627),    # LinkedIn link card
    "li-portrait":    (1080, 1350),   # LinkedIn document carousel page
    "x-landscape":    (1600, 900),    # X / Twitter in-stream image
    "article-header": (1920, 1080),   # LinkedIn Pulse / newsletter cover
    "yt-thumb":       (1280, 720),    # YouTube thumbnail
}

DEFAULT_BRAND = {
    "name": "YOUR BRAND",
    "tagline": "CONTENT OS",
    "handle": "@yourhandle",
    "accent": "#FF6B35",
    "ink": "#111111",
    "bg": "#F7F5F2",
    "muted": "#6B6660",
    "line": "#DDD8D2",
    "ok": "#1F9D55",
    "version": "v1.0",
    "footer": "BUILDING IN PUBLIC_",
    "theme": "signal",
}

# Theme defaults, applied under whatever the brand block sets explicitly.
THEMES = {
    # condensed caps display, one accent-coloured word, warm paper, tech chrome
    "signal": {},
    # stark editorial: black on white, sentence case, emphasis by WEIGHT not colour
    "editorial": {
        "bg": "#FFFFFF",
        "ink": "#111111",
        "muted": "#6E6E6E",
        "line": "#D9D9D9",
        "accent": "#111111",
    },
}

FONT_FILES = {
    "Display": "Anton-Regular.ttf",
    "Body": "Inter-var.ttf",
    "Mono": "JetBrainsMono-var.ttf",
    "Alt": "Archivo-var.ttf",
}

SLIDE_TYPES = {"cover", "cards", "stats", "process", "quote", "cta"}


# -------------------------------------------------------------- font embed ---
def font_css() -> str:
    out = []
    for family, fname in FONT_FILES.items():
        path = os.path.join(FONT_DIR, fname)
        if not os.path.exists(path):
            continue
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        rng = "100 900" if family != "Display" else "400"
        out.append(
            f"@font-face{{font-family:'{family}';"
            f"src:url(data:font/ttf;base64,{b64}) format('truetype');"
            f"font-weight:{rng};font-style:normal;font-display:block}}"
        )
    return "".join(out)


# ------------------------------------------------------------------- markup ---
def esc(s: str) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def rich(s: str) -> str:
    """`**word**` -> accent span. `|` -> hard line break."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<span class="ac">\1</span>', s)
    return s.replace("|", "<br>")


def plain(s: str) -> str:
    return esc(str(s).replace("|", " ").replace("**", ""))


def chrome_top(slide, idx, total, brand, theme) -> str:
    counter = "" if slide.get("counter") is False else f"{idx:02d}/{total:02d}"

    if theme == "editorial":
        # No glyph, no status light — a masthead and a folio, nothing else.
        return f"""<header class="bar top">
  <div class="mark">
    <div class="marktext">
      <div class="brandname">{plain(brand['name'])}</div>
      <div class="brandtag">{plain(brand['tagline'])}</div>
    </div>
  </div>
  <div class="statuswrap"><div class="counter">{counter}</div></div>
</header>"""

    status = slide.get("status", "ALL SYSTEMS RUNNING")
    return f"""<header class="bar top">
  <div class="mark">
    <svg viewBox="0 0 24 24" class="glyph" aria-hidden="true">
      <g stroke="{brand['accent']}" stroke-width="2.4" stroke-linecap="round">
        <path d="M12 2.5v19M2.5 12h19M5.2 5.2l13.6 13.6M18.8 5.2L5.2 18.8"/>
      </g>
    </svg>
    <div class="marktext">
      <div class="brandname">{plain(brand['name'])}</div>
      <div class="brandtag">{plain(brand['tagline'])}</div>
    </div>
  </div>
  <div class="statuswrap">
    <div class="counter">{counter}</div>
    <div class="statuslabel">STATUS:</div>
    <div class="status"><span class="dot"></span>{plain(status)}</div>
  </div>
</header>"""


def chrome_bottom(slide, brand, is_last, theme) -> str:
    hint = slide.get("swipe")
    if hint is None:
        hint = "" if is_last else "SWIPE →"
    lead = "" if theme == "editorial" else "&gt;&nbsp; "
    sep = "·&nbsp;" if theme == "editorial" else ""
    return f"""<footer class="bar bottom">
  <div class="verpill">{lead}{plain(brand['version'])}<span class="vsub">{sep}{plain(brand['footer'])}</span></div>
  <div class="swipe">{plain(hint)}</div>
</footer>"""


def cards_html(items, numbered=False) -> str:
    rows = []
    for i, it in enumerate(items, 1):
        if isinstance(it, str):
            label, desc = it, ""
        else:
            label, desc = it.get("label", ""), it.get("desc", "")
        badge = f'<div class="cardnum">{i:02d}</div>' if numbered else '<div class="cardtick"></div>'
        d = f'<div class="carddesc">{rich(desc)}</div>' if desc else ""
        rows.append(f'<div class="card">{badge}<div class="cardbody">'
                    f'<div class="cardlabel">{rich(label)}</div>{d}</div></div>')
    return f'<div class="cards">{"".join(rows)}</div>'


def stats_html(items) -> str:
    tiles = []
    for it in items:
        delta = it.get("delta", "")
        dcls = "up" if str(delta).strip().startswith("+") else ("down" if str(delta).strip().startswith("-") else "flat")
        d = f'<div class="delta {dcls}">{plain(delta)}</div>' if delta else ""
        sub = f'<div class="statsub">{plain(it.get("sub",""))}</div>' if it.get("sub") else ""
        tiles.append(f'<div class="tile"><div class="statlabel">{plain(it.get("label",""))}</div>'
                     f'<div class="statvalue">{plain(it.get("value",""))}</div>{d}{sub}</div>')
    n = min(max(len(tiles), 1), 3)
    return f'<div class="tiles cols{n}">{"".join(tiles)}</div>'


def process_html(steps) -> str:
    out = []
    for i, s in enumerate(steps):
        if i:
            out.append('<div class="arrow">→</div>')
        if isinstance(s, str):
            name, desc = s, ""
        else:
            name, desc = s.get("label", ""), s.get("desc", "")
        d = f'<div class="stepdesc">{plain(desc)}</div>' if desc else ""
        out.append(f'<div class="step"><div class="stepdot">{i+1}</div>'
                   f'<div class="stepname">{plain(name)}</div>{d}</div>')
    return f'<div class="process">{"".join(out)}</div>'


def deliver_html(items, title="WHAT IT DELIVERS") -> str:
    chips = "".join(f'<div class="chip">{plain(x)}</div>' for x in items)
    return f'<div class="band"><div class="bandtitle">{plain(title)}</div><div class="chips">{chips}</div></div>'


def body_html(slide) -> str:
    t = slide.get("type", "cards")
    parts = []
    if slide.get("kicker"):
        parts.append(f'<div class="kicker">{plain(slide["kicker"])}</div>')
    if slide.get("headline"):
        cls = "headline big" if t in ("cover", "quote", "cta") else "headline"
        parts.append(f'<h1 class="{cls}">{rich(slide["headline"])}</h1>')
    if slide.get("subline"):
        parts.append(f'<p class="subline">{rich(slide["subline"])}</p>')

    if t == "stats" and slide.get("stats"):
        parts.append(stats_html(slide["stats"]))
    if slide.get("cards"):
        parts.append(cards_html(slide["cards"], numbered=slide.get("numbered", t == "cta")))
    if slide.get("quote"):
        parts.append(f'<blockquote class="quote">{rich(slide["quote"])}</blockquote>')
        if slide.get("attrib"):
            parts.append(f'<div class="attrib">— {plain(slide["attrib"])}</div>')
    foot = []
    if slide.get("delivers"):
        foot.append(deliver_html(slide["delivers"], slide.get("deliversTitle", "WHAT IT DELIVERS")))
    if slide.get("process"):
        foot.append(process_html(slide["process"]))
    if foot:
        parts.append(f'<div class="footgroup">{"".join(foot)}</div>')
    if slide.get("action"):
        parts.append(f'<div class="action">{rich(slide["action"])}</div>')
    if slide.get("note"):
        parts.append(f'<div class="note">{rich(slide["note"])}</div>')
    return f'<div class="content" data-content>{"".join(parts)}</div>'


def editorial_css(k: float) -> str:
    """Stark black-and-white editorial theme.

    Sentence-case Archivo headlines, emphasis carried by WEIGHT not colour, hairline
    rules instead of cards and pills, no status light, no accent bar, no paper grid.
    """
    r = lambda v: round(v * k)
    return f"""
/* ---------------- theme: editorial ---------------- */
.slide{{background-image:none;padding:{r(84)}px {r(80)}px {r(64)}px}}
.slide::before{{display:none}}
.slide::after{{display:none}}
.glyph{{display:none}}
.bar.top{{align-items:flex-start;border-bottom:1px solid var(--line);padding-bottom:{r(16)}px}}
.brandname{{font-family:'Alt';font-weight:700;font-size:{r(24)}px;letter-spacing:{r(-0.2)}px;
  text-transform:none}}
.brandtag{{font-family:'Body';font-weight:400;font-size:{r(13)}px;color:var(--muted);
  letter-spacing:{r(1.9)}px;text-transform:uppercase;margin-top:{r(5)}px}}
.counter{{font-family:'Body';font-weight:400;font-size:{r(13)}px;color:var(--muted);
  letter-spacing:{r(1.6)}px}}
.bar.bottom{{border-top:1px solid var(--line);padding-top:{r(18)}px}}
.verpill{{border:0;padding:0;font-family:'Body';font-weight:400;font-size:{r(13)}px;
  color:var(--muted);letter-spacing:{r(1.9)}px;text-transform:uppercase;gap:{r(8)}px}}
.vsub{{color:var(--muted)}}
.swipe{{font-family:'Body';font-weight:400;font-size:{r(13)}px;letter-spacing:{r(1.9)}px;
  color:var(--muted)}}

.content{{gap:{r(24)}px;padding:{r(44)}px 0}}
.kicker{{font-family:'Body';font-weight:500;font-size:{r(14)}px;color:var(--muted);
  letter-spacing:{r(2.2)}px}}
.headline{{font-family:'Alt';font-weight:400;text-transform:none;
  font-size:{r(64)}px;line-height:1.06;letter-spacing:{r(-1.6)}px}}
.headline.big{{font-size:{r(78)}px}}
.ac{{color:inherit;font-weight:800}}
.subline{{font-family:'Body';font-size:{r(28)}px;line-height:1.42;max-width:{r(800)}px}}
.subline .ac{{font-weight:700}}

.cards{{gap:0;border-top:1px solid var(--line)}}
.card{{background:transparent;border:0;border-bottom:1px solid var(--line);border-radius:0;
  padding:{r(20)}px 0;gap:{r(22)}px}}
.cardnum{{font-family:'Alt';font-weight:400;font-size:{r(30)}px;color:var(--muted);
  padding-top:0;min-width:{r(52)}px}}
.cardtick{{display:none}}
.cardlabel{{font-family:'Alt';font-weight:700;font-size:{r(25)}px;text-transform:none;
  letter-spacing:{r(-0.3)}px}}
.carddesc{{font-size:{r(21)}px;margin-top:{r(6)}px}}

.tile{{border:0;border-top:2px solid var(--ink);border-radius:0;background:transparent;
  padding:{r(16)}px 0 0}}
.statlabel{{font-family:'Body';font-weight:500;font-size:{r(13)}px;color:var(--muted);
  letter-spacing:{r(1.8)}px}}
.statvalue{{font-family:'Alt';font-weight:700;font-size:{r(56)}px;letter-spacing:{r(-1.6)}px;
  margin-top:{r(10)}px}}
.delta{{font-family:'Body';font-weight:600;font-size:{r(18)}px;color:var(--ink)}}
.delta.up,.delta.down,.delta.flat{{color:var(--ink)}}
.statsub{{font-size:{r(18)}px}}

.band{{border-bottom:0;padding:{r(18)}px 0 0}}
.bandtitle{{font-family:'Body';font-weight:500;font-size:{r(13)}px;color:var(--muted);
  letter-spacing:{r(2.2)}px;text-align:left}}
.chips{{justify-content:flex-start;gap:{r(10)}px;margin-top:{r(14)}px}}
.chip{{font-family:'Body';font-weight:500;font-size:{r(18)}px;text-transform:none;
  letter-spacing:0;border:1px solid var(--line);border-radius:0;background:transparent;
  padding:{r(9)}px {r(14)}px}}

.stepdot{{border:0;width:auto;height:auto;font-family:'Alt';font-weight:400;
  font-size:{r(24)}px;color:var(--muted);margin:0 auto {r(6)}px}}
.stepname{{font-family:'Alt';font-weight:700;font-size:{r(17)}px;text-transform:none;
  letter-spacing:{r(-0.2)}px}}
.arrow{{color:var(--muted);font-size:{r(20)}px}}
.process{{border-top:1px solid var(--line);padding-top:{r(18)}px}}

.quote{{font-family:'Alt';font-weight:400;font-size:{r(44)}px;line-height:1.16;
  letter-spacing:{r(-1)}px}}
.quote .ac{{font-weight:800}}
.attrib{{font-family:'Body';font-weight:400;font-size:{r(18)}px;letter-spacing:{r(0.4)}px}}
.action{{font-family:'Alt';font-weight:700;text-transform:none;font-size:{r(38)}px;
  letter-spacing:{r(-0.8)}px;border-left:0;border-top:2px solid var(--ink);
  padding:{r(16)}px 0 0}}
.note{{font-family:'Body';font-weight:400;font-size:{r(19)}px;letter-spacing:0}}
"""


def build_html(deck) -> str:
    incoming = deck.get("brand", {})
    theme = incoming.get("theme", DEFAULT_BRAND["theme"])
    if theme not in THEMES:
        raise SystemExit(f"unknown theme '{theme}'. choose from: {', '.join(sorted(THEMES))}")
    brand = dict(DEFAULT_BRAND)
    brand.update(THEMES[theme])          # theme palette
    brand.update(incoming)               # explicit brand values still win
    preset = deck.get("preset", "ig-portrait")
    if preset not in PRESETS:
        raise SystemExit(f"unknown preset '{preset}'. choose from: {', '.join(sorted(PRESETS))}")
    W, H = PRESETS[preset]
    k = W / 1080.0                                    # single type-scale factor
    slides = deck["slides"]
    total = deck.get("total", len(slides))

    frames = []
    for i, s in enumerate(slides, 1):
        t = s.get("type", "cards")
        if t not in SLIDE_TYPES:
            raise SystemExit(f"slide {i}: unknown type '{t}'. choose from: {', '.join(sorted(SLIDE_TYPES))}")
        frames.append(
            f'<section class="slide t-{t}" id="s{i}">'
            f'{chrome_top(s, i, total, brand, theme)}{body_html(s)}'
            f'{chrome_bottom(s, brand, i == len(slides), theme)}</section>'
        )

    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{font_css()}
:root{{
  --w:{W}px; --h:{H}px; --k:{k};
  --ink:{brand['ink']}; --bg:{brand['bg']}; --ac:{brand['accent']};
  --muted:{brand['muted']}; --line:{brand['line']}; --ok:{brand['ok']};
  --pad:{round(72*k)}px;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:#3a3a3a}}
body{{display:flex;flex-direction:column;align-items:flex-start;gap:24px}}
.slide{{
  position:relative;width:var(--w);height:var(--h);background:var(--bg);color:var(--ink);
  font-family:'Body',system-ui,sans-serif;overflow:hidden;
  display:flex;flex-direction:column;padding:var(--pad);
  background-image:radial-gradient(circle at 1px 1px, rgba(17,17,17,.055) 1px, transparent 0);
  background-size:{round(26*k)}px {round(26*k)}px;
}}
.slide::before{{content:"";position:absolute;inset:{round(30*k)}px;border:1px solid var(--line);
  border-radius:{round(10*k)}px;pointer-events:none}}
.slide::after{{content:"";position:absolute;left:0;top:0;width:{round(9*k)}px;height:100%;background:var(--ac)}}

/* ---- chrome ---- */
.bar{{display:flex;align-items:flex-end;justify-content:space-between;flex:0 0 auto;position:relative;z-index:2}}
.bar.bottom{{align-items:center;margin-top:auto;padding-top:{round(22*k)}px}}
.mark{{display:flex;align-items:center;gap:{round(14*k)}px}}
.glyph{{width:{round(40*k)}px;height:{round(40*k)}px;flex:0 0 auto}}
.brandname{{font-family:'Display';font-size:{round(27*k)}px;line-height:1;letter-spacing:{round(0.6*k)}px}}
.brandtag{{font-family:'Mono';font-weight:500;font-size:{round(15*k)}px;color:var(--ac);
  letter-spacing:{round(1.4*k)}px;margin-top:{round(4*k)}px}}
.statuswrap{{text-align:right;font-family:'Mono';font-weight:500}}
.counter{{font-size:{round(17*k)}px;color:var(--ac);letter-spacing:{round(1*k)}px}}
.statuslabel{{font-size:{round(12*k)}px;color:var(--muted);letter-spacing:{round(1.6*k)}px;margin-top:{round(6*k)}px}}
.status{{font-size:{round(13*k)}px;color:var(--muted);letter-spacing:{round(1.2*k)}px;
  display:flex;align-items:center;gap:{round(7*k)}px;justify-content:flex-end;margin-top:{round(3*k)}px}}
.dot{{width:{round(9*k)}px;height:{round(9*k)}px;border-radius:50%;background:var(--ok);
  box-shadow:0 0 0 {round(3*k)}px rgba(31,157,85,.18)}}
.verpill{{font-family:'Mono';font-weight:500;font-size:{round(14*k)}px;letter-spacing:{round(1.2*k)}px;
  border:1px solid var(--line);border-radius:{round(7*k)}px;
  padding:{round(11*k)}px {round(16*k)}px;display:flex;gap:{round(10*k)}px;align-items:baseline}}
.vsub{{color:var(--ac)}}
.swipe{{font-family:'Mono';font-weight:600;font-size:{round(15*k)}px;letter-spacing:{round(2*k)}px;color:var(--muted)}}

/* ---- content ---- */
.content{{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;
  gap:{round(20*k)}px;padding:{round(30*k)}px 0;min-height:0;position:relative;z-index:2}}
.kicker{{font-family:'Mono';font-weight:600;font-size:{round(17*k)}px;letter-spacing:{round(2.6*k)}px;
  color:var(--ac);text-transform:uppercase}}
.headline{{font-family:'Display';font-weight:400;text-transform:uppercase;
  font-size:{round(76*k)}px;line-height:.94;letter-spacing:{round(-0.5*k)}px}}
.headline.big{{font-size:{round(96*k)}px}}
.ac{{color:var(--ac)}}
.subline{{font-size:{round(30*k)}px;line-height:1.36;color:var(--muted);font-weight:400;
  max-width:{round(760*k)}px}}
.subline .ac{{font-weight:600}}

.cards{{display:flex;flex-direction:column;gap:{round(13*k)}px;margin-top:{round(4*k)}px}}
.card{{display:flex;gap:{round(16*k)}px;align-items:flex-start;background:#fff;
  border:1px solid var(--line);border-radius:{round(12*k)}px;
  padding:{round(17*k)}px {round(20*k)}px}}
.cardnum{{font-family:'Mono';font-weight:700;font-size:{round(17*k)}px;color:var(--ac);
  padding-top:{round(3*k)}px;flex:0 0 auto}}
.cardtick{{flex:0 0 auto;width:{round(11*k)}px;height:{round(11*k)}px;border-radius:2px;
  background:var(--ac);margin-top:{round(9*k)}px;transform:rotate(45deg)}}
.cardlabel{{font-family:'Alt';font-weight:700;font-size:{round(26*k)}px;line-height:1.16;
  text-transform:uppercase;letter-spacing:{round(0.3*k)}px}}
.carddesc{{font-size:{round(22*k)}px;line-height:1.36;color:var(--muted);margin-top:{round(5*k)}px}}

.tiles{{display:grid;gap:{round(14*k)}px}}
.tiles.cols1{{grid-template-columns:1fr}}
.tiles.cols2{{grid-template-columns:1fr 1fr}}
.tiles.cols3{{grid-template-columns:1fr 1fr 1fr}}
.tile{{background:#fff;border:1px solid var(--line);border-radius:{round(12*k)}px;
  padding:{round(20*k)}px}}
.statlabel{{font-family:'Mono';font-weight:600;font-size:{round(14*k)}px;letter-spacing:{round(1.4*k)}px;
  color:var(--muted);text-transform:uppercase}}
.statvalue{{font-family:'Display';font-size:{round(52*k)}px;line-height:1.02;margin-top:{round(8*k)}px}}
.delta{{font-family:'Mono';font-weight:700;font-size:{round(19*k)}px;margin-top:{round(4*k)}px}}
.delta.up{{color:var(--ok)}}
.delta.down{{color:#C0392B}}
.delta.flat{{color:var(--muted)}}
.statsub{{font-size:{round(19*k)}px;color:var(--muted);margin-top:{round(4*k)}px}}

.band{{border-top:1px solid var(--line);border-bottom:1px solid var(--line);
  padding:{round(16*k)}px 0;margin-top:{round(4*k)}px}}
.bandtitle{{font-family:'Mono';font-weight:600;font-size:{round(14*k)}px;letter-spacing:{round(2.2*k)}px;
  color:var(--ac);text-align:center;text-transform:uppercase}}
.chips{{display:flex;flex-wrap:wrap;gap:{round(10*k)}px;justify-content:center;margin-top:{round(12*k)}px}}
.chip{{font-family:'Alt';font-weight:600;font-size:{round(19*k)}px;text-transform:uppercase;
  letter-spacing:{round(0.6*k)}px;border:1px solid var(--line);border-radius:999px;
  padding:{round(8*k)}px {round(15*k)}px;background:#fff}}

.process{{display:flex;align-items:flex-start;gap:{round(8*k)}px;flex-wrap:nowrap;margin-top:{round(6*k)}px}}
.step{{flex:1 1 0;min-width:0;text-align:center}}
.stepdot{{width:{round(34*k)}px;height:{round(34*k)}px;border-radius:50%;border:1.5px solid var(--ac);
  color:var(--ac);font-family:'Mono';font-weight:700;font-size:{round(16*k)}px;
  display:flex;align-items:center;justify-content:center;margin:0 auto {round(9*k)}px}}
.stepname{{font-family:'Alt';font-weight:700;font-size:{round(18*k)}px;text-transform:uppercase;
  line-height:1.14;letter-spacing:{round(0.2*k)}px}}
.stepdesc{{font-size:{round(16*k)}px;color:var(--muted);line-height:1.26;margin-top:{round(4*k)}px}}
.arrow{{color:var(--ac);font-size:{round(24*k)}px;line-height:1;padding-top:{round(5*k)}px;flex:0 0 auto}}

.quote{{font-family:'Alt';font-weight:600;font-size:{round(46*k)}px;line-height:1.2}}
.attrib{{font-family:'Mono';font-weight:500;font-size:{round(19*k)}px;color:var(--muted);
  letter-spacing:{round(1*k)}px}}
.action{{font-family:'Display';text-transform:uppercase;font-size:{round(44*k)}px;line-height:1.02;
  border-left:{round(6*k)}px solid var(--ac);padding-left:{round(20*k)}px}}
.note{{font-family:'Mono';font-weight:500;font-size:{round(20*k)}px;color:var(--muted);
  letter-spacing:{round(0.6*k)}px}}
.footgroup{{margin-top:auto;display:flex;flex-direction:column;gap:{round(18*k)}px}}
.footgroup .band{{margin-top:0}}
{editorial_css(k) if theme == "editorial" else ""}
</style></head><body>
{"".join(frames)}
</body></html>"""


# ---------------------------------------------------------------- measuring ---
MEASURE_JS = r"""() => Array.from(document.querySelectorAll('.slide')).map(sl => {
  const c = sl.querySelector('[data-content]');
  const h = sl.querySelector('.headline');
  const lh = h ? parseFloat(getComputedStyle(h).lineHeight) : 0;
  const proc = sl.querySelector('.process');
  const kids = Array.from(c.children);
  const gap = parseFloat(getComputedStyle(c).rowGap) || 0;
  const used = kids.reduce((a, e) => a + e.getBoundingClientRect().height, 0)
             + gap * Math.max(0, kids.length - 1);
  return {
    id: sl.id,
    fill: c.clientHeight ? used / c.clientHeight : 1,
    overflow: Math.max(0, Math.round(c.scrollHeight - c.clientHeight)),
    headlineLines: h && lh ? Math.round(h.getBoundingClientRect().height / lh) : 0,
    procOverflow: proc ? Math.max(0, Math.round(proc.scrollWidth - proc.clientWidth)) : 0,
    wide: Math.max(0, Math.round(sl.scrollWidth - sl.clientWidth)),
  };
})"""

MAX_HEADLINE_LINES = 4

# Below this share of the frame a slide reads empty. The editorial theme is
# deliberately airy, so it tolerates far more white space than the signal theme.
UNDERFILL = {"signal": 0.62, "editorial": 0.34}
UNDERFILL_EXEMPT = {"quote"}      # the one-line slide is meant to be sparse


def validate(reports, slides, theme="signal"):
    problems = []
    floor = UNDERFILL.get(theme, 0.62)
    for r, s in zip(reports, slides):
        n = r["id"][1:]
        if r["overflow"] > 0:
            problems.append(f"slide {n}: content overflows the frame by {r['overflow']}px "
                            f"— cut copy or move a card to the next slide")
        if r["headlineLines"] > MAX_HEADLINE_LINES:
            problems.append(f"slide {n}: headline wraps to {r['headlineLines']} lines "
                            f"(max {MAX_HEADLINE_LINES}) — shorten it or add a '|' break")
        if r["procOverflow"] > 0:
            problems.append(f"slide {n}: the process chain is too wide by {r['procOverflow']}px "
                            f"— use at most 6 steps with short labels")
        if r["wide"] > 0:
            problems.append(f"slide {n}: something is wider than the canvas by {r['wide']}px")
        if (r["overflow"] == 0 and r["fill"] < floor
                and s.get("type", "cards") not in UNDERFILL_EXEMPT):
            problems.append(f"slide {n}: only {round(r['fill']*100)}% of the frame is used — the slide reads "
                            f"empty. Add a card, a stat, a delivers band, or fold it into another slide")
    return problems


def check_copy(deck):
    problems = []
    for i, s in enumerate(deck["slides"], 1):
        for field in ("headline", "quote"):
            txt = s.get(field, "")
            if txt and len(re.findall(r"\*\*(.+?)\*\*", txt)) > 1:
                problems.append(f"slide {i}: more than one **emphasised** word in the {field} — keep exactly one")
        if s.get("type") == "stats" and len(s.get("stats", [])) > 6:
            problems.append(f"slide {i}: more than 6 stat tiles — split across slides")
        for c in s.get("cards", []) or []:
            lab = c.get("label", "") if isinstance(c, dict) else c
            if len(plain(lab)) > 34:
                problems.append(f"slide {i}: card label '{plain(lab)[:28]}…' is too long (max ~34 chars)")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("-o", "--outdir", default="out")
    ap.add_argument("--scale", type=int, default=2)
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--allow-overflow", action="store_true")
    ap.add_argument("--prefix", default="slide")
    args = ap.parse_args()

    with open(args.deck) as fh:
        deck = json.load(fh)
    if not deck.get("slides"):
        raise SystemExit("deck has no slides")

    W, H = PRESETS[deck.get("preset", "ig-portrait")]
    os.makedirs(args.outdir, exist_ok=True)
    html_path = os.path.join(args.outdir, "_deck.html")
    with open(html_path, "w") as fh:
        fh.write(build_html(deck))
    if args.html_only:
        print(html_path)
        return

    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--disable-lcd-text",
                                           "--font-render-hinting=none",
                                           "--force-color-profile=srgb"])
        page = browser.new_page(viewport={"width": W, "height": H},
                                device_scale_factor=args.scale)
        page.goto("file://" + os.path.abspath(html_path))
        page.wait_for_timeout(500)
        reports = page.evaluate(MEASURE_JS)
        theme = deck.get("brand", {}).get("theme", DEFAULT_BRAND["theme"])
        problems = check_copy(deck) + validate(reports, deck["slides"], theme)
        written = []
        for i, r in enumerate(reports, 1):
            out = os.path.join(args.outdir, f"{args.prefix}-{i:02d}.png")
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
