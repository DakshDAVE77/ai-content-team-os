# Design system

The renderer at `skills/designer/scripts/render.py` is the only way visuals get
made. It reads a deck JSON and writes PNGs. Colours, name and handle come from
`brand/brand-config.md`, so the system is one look per operator, not per post.

## Canvas presets

| preset | pixels | use |
|---|---|---|
| `ig-portrait` | 1080×1350 | IG carousel, IG feed, Reel cover, LinkedIn doc page |
| `ig-square` | 1080×1080 | IG single image |
| `ig-story` | 1080×1920 | Stories, Reel background |
| `li-landscape` | 1200×627 | LinkedIn single image |
| `x-landscape` | 1600×900 | X / Twitter in-stream image |
| `article-header` | 1920×1080 | Pulse article and newsletter cover |
| `yt-thumb` | 1280×720 | YouTube thumbnail |

Type scales from a single factor derived from canvas width, so a LinkedIn card and
an IG slide read as one system.

## Themes

Two looks. Set `brand.theme`; the theme supplies a palette, and anything set
explicitly in the `brand` block still wins. Take the theme from
`brand/brand-config.md` → `## Design tokens` and never switch it per post.

| theme | look | emphasis | chrome |
|---|---|---|---|
| `signal` (default) | warm paper, condensed ALL-CAPS Anton headlines, one accent-coloured word, cards as white boxes, dotted grid | **colour** | brand glyph, status light, accent rule |
| `editorial` | stark black on white, sentence-case Archivo headlines, hairline rules instead of cards, generous white space | **weight** (800 against 400) | masthead and folio only — no glyph, no status light |

`editorial` is the Vision-document look: it is deliberately airy, so its underfill
floor is 34% rather than 62%. `quote` slides are exempt from the underfill check in
both themes.

In `editorial`, `**word**` renders as a heavier weight, not as coloured type — so
setting an accent colour there does nothing to the headline. That is intended.

## Deck JSON

```json
{
  "preset": "ig-portrait",
  "brand": { "theme": "editorial", "name": "...", "tagline": "...",
             "version": "...", "footer": "..." },
  "total": 9,
  "slides": [ { "type": "cover", "...": "..." } ]
}
```

`total` overrides the slide counter denominator — set it when rendering part of a
deck. Omit it and it equals the number of slides.

## Slide types

| type | carries |
|---|---|
| `cover` | kicker, headline, subline, optional cards |
| `cards` | kicker, headline, subline, 2–5 cards, optional delivers + process |
| `stats` | kicker, headline, 1–6 stat tiles, subline, cards |
| `process` | headline, subline, a 3–6 step chain |
| `quote` | headline or quote + attrib — the one-line slide |
| `cta` | headline, action, subline, numbered cards, note |

## Field grammar

| field | rule |
|---|---|
| `headline` | ALL CAPS in `signal`, sentence case in `editorial`. **Exactly one** `**word**` is emphasised. Use `\|` to place every line break by hand. Max 4 lines. |
| `kicker` | mono, accent, uppercase. Slide number and role, or the beat. Keep under 40 chars. |
| `subline` | sentence case, muted. One or two lines. `**word**` renders semibold. |
| `cards` | `{label, desc}`. Label max ~34 chars, uppercase by render. Desc one sentence. |
| `stats` | `{label, value, delta, sub}`. `delta` starting `+` renders green, `-` red. |
| `process` | strings, or `{label, desc}`. Max 6 steps or the chain overflows. |
| `delivers` | chip row under a "WHAT IT DELIVERS" rule. 3–5 short nouns. |
| `action` | the CTA line, display type with an accent bar. `cta` slides only. |
| `swipe` | `""` on the last slide to drop the swipe hint. |
| `counter` | `false` to hide the slide counter on a standalone image. |

## Non-negotiables

- **Never edit type sizes to make copy fit.** The renderer exits non-zero and
  names the slide. Rewrite the copy shorter.
- **One emphasised word per headline (or quote).** Zero is allowed; two is rejected.
- **Every headline break is manual.** Auto-wrapping splits sense units.
- **Never invent a metric for a `stats` slide.** Values come from
  `performance/log.md` or from the operator. No placeholder numbers ship.
- **Fill the frame.** The validator rejects a slide using under 62% of its frame in
  `signal`, or 34% in `editorial`. Add a card, add a delivers band, or fold the slide
  into its neighbour.

## Running it

```bash
python3 skills/designer/scripts/render.py deck.json -o out --scale 2
```

`--scale 2` for delivery, `--scale 1` while iterating (four times faster).
`--html-only` writes the page without launching a browser, for debugging.
`--allow-overflow` renders anyway and still prints the problems — use it only to
look at a broken slide, never to ship one.

Exit code 2 with a `PROBLEMS:` list means fix the copy and run again.
