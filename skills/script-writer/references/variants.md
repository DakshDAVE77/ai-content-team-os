# Variants — three versions of every post

Every platform piece ships as **three variants of one argument**, labelled A, B and C.
The operator picks one. The other two are discarded, not banked.

This is not three ideas. The claim, the proof and the transferable point are **identical
across all three** — only the way in changes. That is what makes the choice safe: whichever
he picks is already on-strategy, already inside the proof ledger, already the right pillar.
He is choosing a way in, not re-deciding the argument.

## The three angles

They are not invented. `brand/brand-config.md` says he opens on **"an assumption he held,
a person he met, or an observation."** Those are the three.

| | Angle | Opens on | Voice | Reach for it when |
|---|---|---|---|---|
| **A** | **Data-led** | the number, stated flat | Builder | The figure is genuinely surprising and needs no setup. Strongest with the institutional reader. |
| **B** | **Correction** | an assumption he held that broke | Builder | He was wrong about something and found out. His most persuasive shape, and the one competitors cannot copy. |
| **C** | **Observation** | a person, a place, a thing he noticed | Observer | The argument is about the city, buyers, or how people behave. Warmest, widest, best on Instagram. |

**Do not write all three in Observer.** Drafts drift there because it feels safer. A and B
are Builder. If all three read warm and curious, two of them are wrong.

## Rules

1. **One claim, three doors.** If variant B makes a different argument than variant A, it
   is not a variant — it is a second idea, and it does not belong in this slate.
2. **Every variant is complete and postable.** No "and then continue as in A". He must be
   able to pick C, post it, and never read the other two.
3. **Every variant carries the same number**, from `brand/proof.md`, in the same form. A
   figure that only appears in one variant is a figure the piece does not actually need.
4. **Each variant gets its own hook**, from the three the hook-writer presented. Variant A
   takes the data hook, B the assumption-break, C the observation. If the three hooks do
   not split that way, the hook-writer has not done its job — send it back.
5. **Never name a recommendation.** No "recommended", no "strongest", no "I'd go with B".
   Each variant carries a confidence number and its evidence label — see `## Confidence`
   below — and that number is the only comparative thing said about them. It is a
   property, like the exposure note in rule 6. Saying which one to post on top of it is
   still pre-choosing, and it is still forbidden.
6. **Label the trade honestly** if one carries a real cost — "B names a mistake, so it is
   the most exposed" is useful. That is a property, not a ranking.
7. **A variant carrying an unresolved `[NUMBER: ...]` is blocked**, not shipped as a
   choice. All three block together, because they carry the same number.

## What varies, precisely

| element | varies? |
|---|---|
| Opening line / hook | **yes** — this is the whole point |
| Order of the middle beats | yes, where the opening demands it |
| The claim | no |
| The number and its source | no |
| The transferable point | no |
| The ask | no, unless the platform format differs |
| Pillar | no |
| Length | within the platform's range, freely |

## Per platform

- **LinkedIn** — three complete posts, each 700–1,400 characters, each with its own first
  line. The first two lines are all most readers see, so the variants genuinely diverge
  there and converge by the third paragraph.
- **X** — three single posts under 280 characters. At this length the angle *is* the post.
  If two variants read nearly the same, cut one and rewrite it properly.
- **Instagram** — three Reel scripts, each with its own spoken script, its own on-screen
  text plan, and **its own caption**. The caption is not shared across variants: it opens
  by sharpening that variant's hook. See `formats.md` → Instagram Reel script.
- **Pulse** — three titles and three standfirsts, one body. A 1,400-word article is not
  written three times; the way in is what gets chosen, and the body follows the pick.

## Confidence

Every variant ships with a confidence number and an evidence label, on the console
beside its POST button. The operator asked for it. It is the one thing on that page
that is not post copy, and it is the only comparative statement the system makes about
the three.

Be exact about what it is, because the name oversells it. It is **not** a prediction of
reach, and it is not a recommendation. It is *how much of what this system already
knows supports this way in* — the hook's own score, adjusted by how this angle and this
pillar have actually performed for him. A high number on a piece with no history behind
it means the hook scored well and nothing more, and the label is there to say so.

### The number

```
confidence = round( 100 x (hook_total / 25) x angle_factor x pillar_factor )
             clamped to 35-90
```

| term | where it comes from |
|---|---|
| `hook_total` | the hook-writer's five-axis score for that variant's hook, 5-25 |
| `angle_factor` | this angle's median follow rate divided by his overall median for that format, from `performance/log.md`, clamped 0.80-1.25 |
| `pillar_factor` | this pillar's median follow rate divided by the same overall median, same clamp |

**Both factors are exactly 1.00 until there are six posts on that surface.** Under six
is noise, and multiplying by noise produces a confident wrong number, which is worse
than a plain one. Show the work in the piece file: the hook total, each factor, and the
result.

Never 100, never under 35. A number at either rail is a claim this system cannot
support.

### The label

Reuses the strength ladder in `performance/patterns.md`. Do not invent a second one.

| posts on that surface | label | what the number actually is |
|---|---|---|
| under 10 | `weak` | mostly or entirely the hook score |
| 10-24 | `emerging` | hook score with real but thin history behind it |
| 25+ | `established` | hook score adjusted by history worth trusting |

The label ships with the number **everywhere the number ships** — console, chat, piece
file. A bare number is a false precision, and it is the fastest way to make a guess
look like a measurement.

### A tight spread is correct

The three variants share one spine, so their confidences usually land within a few
points of each other. **That is the truth, not a defect.** A four-point spread means
the angle is the only thing separating them, which is exactly what a variant is. Never
widen the numbers to make the choice look easier, and never round one up to break a tie.

If one variant sits 15 or more points clear of the other two, the other two are the
problem — usually a hook padded to make up the number. Send them back to the
hook-writer rather than shipping a slate with two decoys in it.

### Calibration - the part that keeps it honest

`confidence` and `angle` are written into `performance/log.md` on every published post.
Once ten scored posts exist on a surface, the analyst checks whether higher confidence
actually produced a higher follow rate.

**If it did not, the analyst says so in `performance/patterns.md` and the number keeps
shipping tagged `uncalibrated` until it does.** A confidence score nobody has ever
checked against an outcome is decoration, and decoration next to a POST button is worse
than none.

## Recording them

In `content/<slug>.md`:

```markdown
## Variants
| id | angle | hook | confidence | status |
|----|-------|------|-----------|--------|
| A | data-led | <first line> | 71 weak | offered |
| B | correction | <first line> | 74 weak | **chosen 2026-09-11** |
| C | observation | <first line> | 68 weak | discarded |
```

Record the arithmetic under the table, once per piece, so a number can be audited
later:

```
confidence: hook 22/25 x angle 1.00 x pillar 1.00 = 88 -> clamped 88 -> weak (4 posts on IG)
```

Set the chosen row when he picks. The discarded two stay in the file — the analyst reads
which angle he keeps choosing, and that pattern is worth more than any single post's
metrics. After six picks, `performance/patterns.md` should be able to say whether he is a
correction writer or a data writer, and the hook-writer should weight accordingly.
