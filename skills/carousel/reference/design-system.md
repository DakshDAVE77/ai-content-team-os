# Editorial Carousel Design System

Reverse-engineered from `CS posting.pdf` — 10 slides, 1080 × 1350 px, produced in **Figma**.
All values below are **measured**, not estimated, unless marked ⚠.

---

## 1. Canvas

| Property | Value |
|---|---|
| Size | 1080 × 1350 px (4:5) |
| Export | 2× recommended → 2160 × 2700 PNG |
| Background | `#FFFFFF` |
| Texture | Faint graph-paper JPEG, 1100 × 1100 source, drawn `cover` at x −102 → 1248, y 0 → 1350 |
| Texture strength | Max darkness delta ≈ 5/255 (~2% black) |
| Grid pitch | ≈ 45.3 px on canvas |

The texture is a raster asset with organic vignette/noise, not a CSS grid. Extracted to
`assets/paper-grid.jpg` (20 KB) — embed it rather than re-simulating.

---

## 2. Grid & margins

| Token | Value |
|---|---|
| `--margin-x` | **87 px** (left and right — symmetric) |
| `--content-width` | **906 px** (1080 − 87 − 87) |
| Text alignment | Left, ragged right, always |

Every text element on all 10 slides starts at exactly `x = 87`. Longest measured line ends at
`x = 994.9`, confirming the 906 px column.

---

## 3. Type scale

Three roles. No fourth. No bold anywhere.

| Role | Size | Line-height | Weight | Tracking | Colour | Transform |
|---|---|---|---|---|---|---|
| Eyebrow | 25 px | — (single line) | 400–500 | **+0.16 em** (+4 px) | `#848484` | `uppercase` |
| Headline | 95 px | 105 px (1.105) | **300 (Light)** | ≈ −0.04 em | `#000000` | `capitalize` |
| Subhead | 40 px | 54 px (1.35) | 400 (Regular) | ~0 | `#848484` | none |
| Swipe label | 32 px | — | 400 | ~0 | `#666666` | none |

Measured stem widths confirm the weights: headline 6 px @ 95 px = Light 300; subhead 4 px @ 40 px
= Regular 400; eyebrow 2 px @ 25 px.

⚠ **Typeface unconfirmed.** Figma converts text to Type3 outlines on PDF export, so the family
name is stripped. Evidence: round period and round i-dots (rules out Helvetica / Arial, which have
square dots), double-storey `a`, single-storey `g` with a shallow open tail, large x-height,
tight display tracking. Best match available for testing was **Inter** — which is also Figma's
default typeface. Needs confirmation from the source file.

Note the transforms are *CSS-style*: the underlying copy in the PDF is sentence case
("A home is never truly Finished.") and `capitalize` renders it as
"A Home Is Never Truly Finished." — including small words like "Is". Same for the eyebrow.

---

## 4. Vertical rhythm

Positions are **fixed**, not vertically centred. A two-line subhead overflows downward rather
than re-centring the block.

### Cover slide (slide 1)

| Element | Top y | Baseline y |
|---|---|---|
| Eyebrow | 197 | 222 |
| Headline line 1 | 246 | 341 |
| Headline line 2 | 351 | 446 |
| Subhead | 503 | 543 |
| Hero image | 748 → 1350 (full bleed, bottom-anchored) |
| Swipe icon | x 976–1033, y 644–707 (icon only, ~57 × 63, vertically centred) |

### Body & closer slides (slides 2–10)

| Element | Top y | Baseline y |
|---|---|---|
| Eyebrow | 489 | 514 |
| Headline line 1 | 556 | 651 |
| Headline line 2 | 661 | 756 |
| Subhead line 1 | 813 | 853 |
| Subhead line 2 | 867 | 907 |
| Swipe (icon + label) | block ≈ x 892–1020, y 1264–1297 |

Derived gaps: eyebrow baseline → headline baseline = 137 px; headline last baseline → subhead
baseline = 97 px.

---

## 5. Slide archetypes

Only three exist in the reference deck.

**A — Cover (slide 1).** Text block raised to the upper third. Full-bleed grayscale hero image
occupying the bottom 602 px. Large swipe icon, no label, right edge ~47 px, vertically centred.
No text sits over the image.

**B — Body (slides 2–9).** Text block at y 489. Small swipe icon + "Swipe" label bottom-right.
No image.

**C — Closer (slide 10).** Identical to B, swipe affordance removed.

---

## 6. Imagery

- Exactly **one** image in ten slides, on the cover only.
- Grayscale (`DeviceGray` in the PDF), high-key, near-white. An architectural 3D massing model.
- Full width, aspect preserved, anchored to the bottom edge, no crop-in, no overlay, no gradient.
- Source resolution 4096 × 2286 → downscaled, so images should be supplied at ≥ 2× the placement box.

---

## 7. Things the system deliberately does NOT have

Worth stating, because these are the usual defaults a generator would add:

- No logo, no wordmark, no brand name on any slide
- No Instagram handle, no website, no phone number
- No CTA button, no "DM us", no price, no offer
- No accent colour — the entire palette is black, one grey, one darker grey, white
- No bold weight, no italics
- No icons other than the swipe glyph
- No slide numbers, no progress dots
- No dividers, rules, cards, or boxes
- No emoji, no exclamation marks, no hashtags on the slides

---

## 8. Copy system

The strongest part of the system. Each slide is a **three-part unit**:

```
EYEBROW      connective tissue — 1–3 words, uppercase
Headline.    the claim — max 2 lines, ends in "." or "?"
Subhead      the support — 1 sentence, max 2 lines
```

### The narrative spine

The eyebrows alone read as a coherent argument. From the reference deck:

| # | Eyebrow | Function |
|---|---|---|
| 1 | A SIMPLE TRUTH | premise |
| 2 | AFTER POSSESSION | context |
| 3 | YET | tension |
| 4 | BUT LIFE DOESN'T | contradiction |
| 5 | SO WE ASKED | the question |
| 6 | THAT CHANGED EVERYTHING | the pivot |
| 7 | ONE JOURNEY | the model |
| 8 | BECAUSE | the rationale |
| 9 | ONE ECOSYSTEM | the system |
| 10 | OUR PURPOSE | the resolution |

Abstracted: **Truth → Context → Tension → Contradiction → Question → Pivot → Model → Rationale →
System → Purpose.** This is the reusable template.

### Headline rules

- 2 lines maximum, 2–4 words per line
- 20–40 characters total, must fit 906 px at 95 px Light
- A complete declarative sentence, always terminal-punctuated (`.` or `?`)
- Written sentence case in source, rendered Title Case by transform
- Verb-led and concrete: "We Stopped Building Projects." not "Redefining Living Experiences"

### Subhead rules

- One sentence, occasionally two short ones. 1–2 lines, ≤ ~50 characters per line
- Frequently a **parallel triad**: "Families grow. Children grow. Dreams grow." /
  "Complete the home. Simplify life. Build belonging."
- Or a **sequence** with arrows: "Residence → Living → Community → Care"
- Never restates the headline; always adds the "so what"

### Voice

Plain, declarative, short. Present tense. No adjective stacking, no superlatives, no
industry jargon ("state-of-the-art", "unparalleled", "world-class" are all absent). The brand
speaks about the customer's life, not about itself — the company is only named implicitly via
"we" and only from slide 6 onward.

---

## 9. Extracted assets

| File | Description |
|---|---|
| `assets/paper-grid.jpg` | 1100 × 1100 graph-paper texture, exact from source |
| `assets/cover-hero-reference.jpg` | 4096 × 2286 grayscale cover image, for style reference |

---

## 10. Amendments to the reference deck

Everything above documents `CS posting.pdf` as measured. The following changes were
made deliberately afterwards and are what the renderer now produces.

### Eyebrow removed

The 25px uppercase eyebrow is no longer rendered. **Headline and subhead keep their
original positions** — the headline still starts at baseline y=651 (y=341 on the
cover), so the space the eyebrow occupied is now empty white. This was chosen over
shifting the block up, to preserve the reference deck's proportions.

The narrative beat each slide carries is still recorded, in the deck JSON's `beat`
field, but never drawn.

### One emphasised word per headline

| | |
|---|---|
| Weight | Inter **Semibold 600** |
| Size / colour / tracking | unchanged — 95px, `#000000`, −0.0518em |
| Count | exactly one span per headline, enforced by the renderer |
| Scope | headline only; emphasis in a subhead is rejected |
| Syntax | `**word**` in the deck JSON |

This is the only place a weight above 300 appears on a slide. `assets/fonts/`
gained `Inter-SemiBold.woff2` to support it.
