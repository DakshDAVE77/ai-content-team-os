# Platform specs

Four channels are in scope: **Instagram**, **LinkedIn feed**, **X / Threads**, and
**Pulse** — LinkedIn's long-form article and newsletter surface.

Limits move. Treat the numbers below as the working spec and verify anything that
would break a post if it were wrong (a hard character cap, a file size) with a web
search before publishing at scale.

## Instagram

| | |
|---|---|
| Caption | 2,200 characters; only the first ~125 show before "more" |
| Hashtags | 30 maximum; use 3–8, placed in the caption, not a comment |
| Carousel | up to 20 slides, 1080×1350 (4:5) — preset `ig-portrait` |
| Reel | vertical 1080×1920; write for 20–45s unless the story needs more |
| Reel cover | 1080×1350 so it sits correctly in the grid — preset `ig-portrait` |

**Language:** Instagram is **Gujarati**, with English code-switching — Reel script and
caption both. This is a brand rule, not a preference; see `brand/brand-config.md` →
`## Language` and the Gujarati block in `script-writer/references/formats.md`. Reel
scripts are budgeted in **syllables**, not words.

**Structure that works here:** the first slide is the whole pitch; slides 2–3 must
pay off the promise before anyone swipes further; the last slide carries one ask.
Reels: hook in the first sentence, no logo intro, no "hey guys".

## LinkedIn feed

| | |
|---|---|
| Text post | 3,000 characters; ~140–210 show before "see more" on mobile |
| Document carousel | PDF, 1080×1350 pages render best; keep to 8–12 pages |
| Single image | 1200×627 — preset `li-landscape` |

**Structure that works here:** first two lines carry the entire hook, because that
is all most readers see. Then short paragraphs, one line each, with real line
breaks. No hashtag walls — three at most, at the end. Links in the first comment
only if the operator has evidence it matters for them; otherwise in the post.

## X / Threads

| | |
|---|---|
| X post | 280 characters on a free account; long-form only if the operator has Premium |
| X thread | 5–12 posts; each must stand alone if quoted |
| X image | 1600×900 — preset `x-landscape` |
| Threads post | 500 characters, up to 10 images |

**Structure that works here:** the first post is a complete thought, not a teaser.
No "🧵" emoji, no "a thread:". Numbered posts only if order genuinely matters.
Threads (Meta) rewards conversational replies — write posts that invite a reply,
not a save.

## Pulse — LinkedIn articles and newsletters

| | |
|---|---|
| Article body | very long ceiling (~110,000 characters); target 900–1,600 words |
| Title | under 80 characters, no colon-subtitle construction |
| Cover image | 1920×1080 — preset `article-header` |
| Cadence | weekly or fortnightly; a newsletter that slips loses subscribers |

**Structure that works here:** one argument, four to six sections with plain
sub-headings, a concrete example the operator lived through in every section, and
a closing paragraph that states what the reader should do differently on Monday.
An article is where a well-performing feed post gets its full version — check
`performance/log.md` for what already earned attention before drafting a new one.

## Repurposing ladder

One idea, five outputs, cheapest first:

1. **X post** — the argument in one paragraph. Test the idea here.
2. **Threads post** — the same argument, warmer, ending in a question.
3. **Instagram carousel** — the argument broken into 6–9 slides.
4. **LinkedIn post** — the argument plus the operator's specific story.
5. **Pulse article** — the argument, the story, the method, and the caveats.

Only climb the ladder for ideas that earned attention on the rung below. The
analyst decides which; the researcher does not re-pitch a dead idea.

## Timing

Do not treat any published "best time to post" as fact. Start with these as
**hypotheses to test**, in the operator's timezone (IST):

- Instagram: 08:00–09:30 and 19:00–21:00
- LinkedIn feed and Pulse: Tue–Thu, 08:00–10:00
- X / Threads: 09:00, 13:00, 21:00

After four weeks, `performance/patterns.md` replaces these entirely. The analyst
owns that call — the publisher follows it.
