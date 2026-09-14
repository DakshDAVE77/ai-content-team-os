# Copy System

The layout is deterministic. The copy is the whole job. Write it first, get it
approved, then render.

---

## The unit

Every slide is the same two-part unit. No eyebrow, no exceptions, no alternative layouts.

```
Headline.    the claim — max 2 lines, ends in "." or "?", exactly one **bold** word
Subhead      the support — 1 sentence, max 2 lines
```

Written in the deck JSON in **sentence case**. CSS applies the Title Case transform.

---

## The spine

The deck used to print a small uppercase eyebrow on each slide, and those eyebrows —
read alone — formed the argument. They are no longer rendered, but **the argument still
has to be there.** The logic now lives in the headlines, which means the headlines must
carry more: each one has to advance the case, not just restate the theme.

Record the beat in the deck JSON's `beat` field. It never appears on the slide; it
exists so you can read the arc down the column and catch a deck that has stopped
arguing and started repeating.

The reference deck's spine, generalised:

**Truth → Context → Tension → Contradiction → Question → Pivot → Model → Rationale → System → Purpose**

| Beat | Original eyebrow | What the slide does |
|---|---|---|
| Truth | A SIMPLE TRUTH | States something the reader already believes |
| Context | AFTER POSSESSION | Locates where the story actually happens |
| Tension | YET | Introduces the gap |
| Contradiction | BUT LIFE DOESN'T | Sharpens the gap into a conflict |
| Question | SO WE ASKED | Reframes as an open question |
| Pivot | THAT CHANGED EVERYTHING | The decision that followed |
| Model | ONE JOURNEY | What was built instead |
| Rationale | BECAUSE | Why it matters to the reader |
| System | ONE ECOSYSTEM | How the parts fit |
| Purpose | OUR PURPOSE | The resolution, stated plainly |

### Adapting to slide count

Compress from the middle. Truth, Tension, Question and Purpose are load-bearing —
never drop them.

| Slides | Beats |
|---|---|
| 6 | Truth → Tension → Question → Pivot → Model → Purpose |
| 7 | + Contradiction |
| 8 | + Context |
| 9 | + Rationale |
| 10 | Full spine (reference) |
| 11–12 | Split Model into two or three concrete chapters, each a distinct beat |

### Alternative arcs

Use when the manifesto arc doesn't fit the brief.

**Myth-buster (7–9):** Common Belief → Actually → The Cost → What's True Instead →
Why It Happens → What To Do → The Takeaway

**Project story (8–10):** The Site → The Constraint → The Idea → The Choice →
What Changed → How It Lives → For Whom → Still Standing

**Explainer (6–8):** The Question → The Short Answer → What Most People Miss →
Step One → Step Two → What It Adds Up To → The Point

**Milestone (6–7):** The Number → What It Represents → Where It Started →
What Held → Who Made It → What's Next

---

## Headline rules

- **Two lines maximum.** Always place the break yourself with `|`.
- **Exactly one word wrapped in `**asterisks**`,** rendered Semibold 600 against the
  Light 300 line. Required on every slide; the renderer rejects zero or two.
- 2–4 words per line, 20–40 characters total.
- A complete declarative sentence. Always terminal-punctuated: `.` or `?`.
- Verb-led and concrete. "We Stopped Building Projects." — not "Redefining Living
  Experiences". If it could appear in any developer's deck, rewrite it.
- Only the final beat may name a commitment. Earlier headlines describe the world,
  not the company.
- Question marks are for the Question beat only. One per deck.

Good, from the reference:

> A home is never truly **finished**.
> Most developers leave **here**.
> We **stopped** building projects.
> Build for everything that comes **after**.

---

## Choosing the emphasised word

The bold word is the hinge the sentence turns on. Read the headline with the word
removed — if the argument survives, you picked the wrong word.

- **Emphasise** the noun or verb carrying the claim: `finished`, `stopped`, `home`,
  `Sunday`, `forgets`.
- **Never emphasise** an article, preposition, adjective, or the brand's own name.
- **Never** let the emphasis straddle the line break — keep it on one line.
- Prefer a word in the **second** line. It lands last and holds the eye.
- Across the deck, vary which word carries it. Ten headlines all bolding the final
  word reads as a tic rather than a decision.
- One span, one word. `**lived in**` is two words wearing one asterisk pair — write
  `feel **lived** in?` instead.

---

## Subhead rules

- One sentence. Occasionally two very short ones. Never three lines.
- ≤ ~50 characters per line.
- Never restates the headline. It adds the "so what".
- Three recurring shapes:
  - **Parallel triad** — "Families grow. Children grow. Dreams grow."
  - **Staccato list** — "Complete the home. Simplify life. Build belonging."
  - **Sequence with arrows** — "Residence → Living → Community → Care"
- Use the arrow shape at most once per deck, on the Model beat.

---

## Voice

Plain, declarative, present tense, short. The brand talks about the reader's life,
not about itself. "We" appears only after the pivot beat.

**Banned:** superlatives; "state-of-the-art", "world-class", "unparalleled",
"luxurious", "iconic", "bespoke", "curated", "elevate", "redefine", "seamless",
"journey" as a marketing noun; adjective stacking; exclamation marks; rhetorical "Imagine…"; emoji;
hashtags; any second-person imperative CTA.

**Compliance:** no prices, no returns or appreciation claims, no possession dates,
no RERA numbers on slides. Those belong in the caption, if anywhere, and only when
the user supplies the exact wording.

---

## Caption (separate deliverable)

Slides carry no hashtags or handles. If the user wants a caption, write it as plain
text alongside the images:

- 2–4 short paragraphs, same voice as the slides, no emoji.
- Opens with a line that is *not* a repeat of slide 1's headline.
- Ends with one soft line — an invitation to think, not a CTA to click.
- Hashtags, if requested, go on their own final line, 5–10 maximum, lowercase.
