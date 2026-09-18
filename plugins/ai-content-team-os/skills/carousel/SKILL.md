---
name: carousel
description: Create on-brand editorial Instagram carousels as 1080x1350 PNG slides. Writes the slide copy from a topic or brief using the brand's headline/subhead narrative system, lays it out on the exact measured design system, and renders ready-to-post images. Use when the user asks for an Instagram carousel, a carousel post, IG slides, a swipe post, social slides, a post about a topic for Instagram, or wants to turn a message, announcement, or idea into carousel form.
---

# Editorial Instagram Carousel

Turns a topic into a finished 4:5 Instagram carousel that matches the brand's
reference deck exactly. Every geometry value in this skill was measured from the
source Figma export — treat them as fixed, not as suggestions.

## Read the brand first

read `brand/brand-config.md` → `## Design tokens`. This deck system is
**typographic**: emphasis is weight, not colour, so it works for any operator whose
tokens do not fight it. Two things come from their config:

- **`name` / `tagline` / `footer`** — the chrome, if their tokens define it.
- **Their accent colour is deliberately NOT used on slides.** If the operator wants
  a coloured deck, this is the wrong skill — use `designer`, which is palette-driven.
  Say so once rather than bending this system.

Everything below is the measured geometry. It is fixed, and it is what makes the
output look designed rather than generated. Do not treat the numbers as suggestions.

## Workflow

1. **Get the brief.** If the user gave only a topic, ask (once, compactly) for: the
   angle or point they want to land, the slide count if they have a preference, and
   whether they have a cover image. Don't ask more than that — the copy system does
   the rest.
2. **Write the copy first, before touching the renderer.** Draft the full deck as
   headline / subhead pairs following `${CLAUDE_PLUGIN_ROOT}/skills/carousel/reference/copy-system.md`. Show
   the copy to the user as plain text and get a nod before rendering. Copy is where
   these decks live or die; layout is deterministic.
3. **Build the deck JSON.** See `${CLAUDE_PLUGIN_ROOT}/skills/carousel/scripts/example-deck.json` for the exact shape.
4. **Render.**
   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/carousel/scripts/render.py deck.json -o out --scale 2
   ```
   Exits non-zero and lists every fit problem if any headline or subhead overflows.
   Fix the copy — never the type size.
5. **Verify before delivering.** Read the rendered PNGs back with the Read tool and
   look at them. Check: no clipped or orphaned words, headline breaks land on sense
   units, the cover image reads high-key, the swipe affordance is present on body
   slides and absent on the closer.
6. **Deliver** every slide with SendUserFile, in order.

## Deck JSON

```json
{
  "slides": [
    { "type": "cover",  "beat": "Truth",   "headline": "A skyline arrives|before a **city** does.", "subhead": "...", "image": "hero.jpg" },
    { "type": "body",   "beat": "Tension", "headline": "Most of it goes|**home** at seven.",        "subhead": "..." },
    { "type": "closer", "beat": "Purpose", "headline": "Build for the city|that comes **after**.",  "subhead": "..." }
  ]
}
```

- `type` — `cover` (first), `body` (middle), `closer` (last). Omitted types are inferred by position.
- `beat` — the narrative beat this slide carries. Not rendered; it exists so the arc
  stays visible while writing. See `${CLAUDE_PLUGIN_ROOT}/skills/carousel/reference/copy-system.md`.
- Write copy in **sentence case**. The headline is rendered Title Case by CSS
  transform — do not pre-capitalise or the output looks wrong.
- **Exactly one word per headline is wrapped in `**asterisks**`** and renders in
  Semibold 600 against the Light 300 line. Not optional — the renderer rejects a deck
  with a headline that has none, or more than one. Emphasis is headline-only; asterisks
  in a subhead are an error.
- Use `|` inside a headline or subhead to force a line break. **Use it on every
  headline.** Automatic wrapping produces breaks that split sense units; the reference
  deck breaks every headline manually.
- `image` is cover-only, relative to the deck file. Supply ≥ 2160px wide. The renderer
  converts it to grayscale and bottom-anchors it full-bleed.

## The non-negotiables

Reproduced from `${CLAUDE_PLUGIN_ROOT}/skills/carousel/reference/design-system.md`, which has the full measurements.

| | |
|---|---|
| Canvas | 1080 × 1350, white, faint paper-grid texture |
| Margins | 87 px left and right, 906 px text column, always left-aligned |
| Headline | 95 px / 105 px, Inter **Light 300**, `#000000`, max 2 lines |
| Emphasis | one word per headline, Inter **Semibold 600**, same size and colour |
| Subhead | 40 px / 54 px, Inter Regular, `#848484`, max 2 lines |
| Palette | black, `#848484`, `#676363`, white. Nothing else. |

There is **no eyebrow**. The headline sits at its original position and the space
above it stays empty — that white is deliberate, do not close it up.

**Never add:** a logo, wordmark, handle, website, phone number, CTA button, price,
offer, accent colour, italics, icon (other than the swipe glyph), slide number,
progress dot, divider, card, box, emoji, exclamation mark, or hashtag. The only
heavier weight permitted anywhere is the single emphasised headline word.
The restraint *is* the brand. If asked to add any of these, flag the conflict once,
then do what the user decides.

## Files

| Path (under `${CLAUDE_PLUGIN_ROOT}/skills/carousel/`) | Purpose |
|---|---|
| `reference/design-system.md` | Every measured value, with provenance |
| `reference/copy-system.md` | Narrative arcs for 6–12 slides, headline/subhead/emphasis rules, voice |
| `scripts/render.py` | Deck JSON → PNG slides, with fit validation |
| `scripts/example-deck.json` | The reference deck, reproduced |
| `assets/` | Paper-grid texture, swipe glyph, Inter Light/Regular/Medium |

## Failure modes to avoid

- **Shrinking type to fit.** The scale is fixed. Rewrite shorter instead.
- **Three-line headlines.** Two is the hard ceiling; the renderer will reject them.
- **Marketing voice.** No superlatives, no "state-of-the-art", no "unparalleled".
  Short declarative sentences about the reader's life, not about the company.
- **Rendering before the copy is approved.** Wasted cycles.
- **Auto-wrapping headlines.** Always place the break with `|`.
- **Emphasising a weak word.** The bold word must be the pivot the sentence turns on —
  a noun or verb that carries the argument. Never an article, preposition or adjective.
- **Emphasising a word that spans the line break.** Keep it on one line.
