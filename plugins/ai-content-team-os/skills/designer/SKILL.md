---
name: designer
description: Render on-brand visuals as ready-to-post PNGs - Instagram carousels, LinkedIn cards and document pages, X images, Reel covers, article headers and thumbnails. Use when the user says design the carousel, make the slides, render the deck, make me a thumbnail, design this post, I need the visuals, make a LinkedIn carousel, or after the script-writer has written slide copy.
---

## Before you build an Instagram carousel

This plugin ships a second, stricter renderer at `carousel` — a measured
1080x1350 editorial system with fixed geometry. If the
job is a typographic, black-and-white editorial carousel, use that skill, not this one. Its layout is
deterministic and its validator rejects overflow, which is what keeps a deck on-brand
without anyone eyeballing it.

Use this skill for everything else: LinkedIn document pages, X images, Reel covers,
article headers, thumbnails.

# The Designer

Render the copy into images. Layout is deterministic — a Python renderer owns every
measurement — so the work here is choosing the right slide types, writing copy that
fits, and checking the output with your own eyes before it ships.

Read `${CLAUDE_PLUGIN_ROOT}/references/design-system.md` — the full deck grammar,
presets and non-negotiables — and `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md`.
Read `brand/brand-config.md` for the `## Design tokens` block.

## Workflow

**1. Get the copy.** Read `content/<slug>.md` → `## Script`. If the slide copy is
not written yet, run `script-writer` first — do not invent slide copy here.

**2. Build the deck JSON.** Copy `scripts/example-deck.json` and edit it. Fill the
`brand` block from the brand config's design tokens:

```json
"brand": { "name": "<tokens.name>", "tagline": "<tokens.tagline>",
           "accent": "<tokens.accent>", "version": "<tokens.version>",
           "footer": "<tokens.footer>" }
```

Choose the preset from the platform: `ig-portrait` for IG carousels, Reel covers
and LinkedIn document pages; `li-landscape` for LinkedIn single images;
`x-landscape` for X; `article-header` for Pulse covers; `yt-thumb` for thumbnails.

Then map each slide to a type. Vary them — nine `cards` slides in a row is a wall.
A carousel wants a `stats` or `process` slide in the middle and a `quote` before
the close.

**3. Render at scale 1 first.**

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/designer/scripts/render.py deck.json -o out --scale 1
```

Exit code 2 with a `PROBLEMS:` list means the copy does not fit. **Fix the copy,
never the type size** — shorten a headline, add a `|` break, move a card to the
next slide, or add a `delivers` band to an underfilled slide. Re-run until clean.

**4. Look at the output.** Read the rendered PNGs back with the Read tool and
actually look at them. Check:

- no clipped, orphaned or hyphenated words
- headline breaks land on sense units, not mid-phrase
- the accent word is the pivot the sentence turns on, and sits on one line
- the swipe hint is on every slide except the last
- the slide counter runs in order and the denominator is right
- slides read as a sequence, not as six unrelated cards

A renderer that exits 0 can still produce an ugly slide. This step is not optional.

**5. Re-render at scale 2** for delivery, then `SendUserFile` every slide in order.

**6. Record it.** Append to `content/<slug>.md` → `## Assets`: the preset, the
slide count, the date, and the deck JSON inline so the deck can be re-rendered or
edited later without rebuilding it. Update `library/idea-bank.md` to `designed`.

## Judgement calls that are yours

- **Slide count.** Fewer, denser slides beat more, thinner ones. If two adjacent
  slides make the same point, merge them and tell the script-writer.
- **Type mix.** `stats` only when the operator supplied real numbers. Never
  fabricate a metric to fill a tile — if there is no data, use `cards`.
- **Where the accent falls.** One word per headline, and it must be the noun or
  verb the argument turns on. Never an article, preposition or adjective.
- **When to say no.** If the copy needs eleven slides to make one point, send it
  back rather than rendering eleven slides.

## Failure modes

- **Shrinking type to fit.** The scale is fixed by design. Rewrite shorter.
- **Shipping without looking.** The most common way a broken slide reaches a feed.
- **Inventing numbers for a `stats` slide.** Real data or no tile.
- **Two accent words, or none in a headline that needs one.** The renderer rejects
  two; one is the default.
- **Auto-wrapping headlines.** Place every break with `|`.
- **Forgetting the deck JSON in the piece file.** Then the next edit rebuilds from
  scratch.
- **Using a preset that does not match the platform.** A 4:5 slide posted as a
  LinkedIn single image gets cropped.
