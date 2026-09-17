---
name: content-team
description: Run the AI content engine on a topic you name - one command that takes today's topic and asks how the Reel gets made (cut the clips he filmed, or an AI avatar video rendered in HeyGen Studio), researches that topic, and publishes one artifact holding three Instagram options, three LinkedIn options and three X options, each with a POST button. Use when the user says run the content engine, run the content team, run the engine, post about <topic>, today's topic is, give me today's posts, content status, or asks for content without naming an employee.
---

# The Content Engine

One topic in. Nine post options out, in one artifact, with nothing else in it.

**The topic is the brief.** He names what today is about; the engine researches that,
builds one argument from it, and writes that argument nine ways. It does not go looking
for a different idea it likes better, and it does not spread the slate across three
unrelated topics.

**Run on demand only.** This engine is never put on a schedule and never creates a
scheduled task for itself or for a slot. If asked to schedule it, say once that it is
built to run interactively — the render and the posting both need an open browser —
and do not create a trigger.

**Do not narrate the pipeline.** No "now running the researcher", no phase headings, no
progress commentary. Run it, publish the artifact, return the three-line receipt at the
bottom of this file.

**One place the run speaks: Step 0.** The topic and the video route change what gets
built, so they are not narration. Nothing else earns a line.

**The avatar route no longer stops for a script approval.** Set by the operator on
16 September 2026 — picking the route is the go-ahead, the Reel renders during the run,
and the finished clip is delivered into the chat alongside the console. He watches it
there and says "post the video" when he wants it live. See `avatar` → *Gate 2 sits after
the render*.

Read `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` first and resolve `<root>`.

## Pre-flight — quiet, one pass

1. Resolve `<root>` per the memory map. No connected folder → one line, then run
   stateless.
2. Read `brand/brand-config.md`. **Missing → stop**, one sentence, run `brand-setup`.
3. Read `brand/voice-master.md` — **the writing spec**, and the first voice file every
   run reads. It carries the register split, the post architecture, the hook formulas,
   the story shapes, the CTA formulas and the do-not list. Missing → say so in one line
   and fall back to the profile; do not write around its absence silently.
4. Read `brand/voice-profile.md`. It keeps authority over **counted numbers** — sentence
   medians, punctuation counts, per-platform first-person share, post length — and the
   voice master wins on shape and register. Full order:
   `${CLAUDE_PLUGIN_ROOT}/references/voice-corpus.md` → *The precedence chain*.
5. Read `brand/proof.md`, `brand/brand-config.md` → `## Targets`, and
   `performance/patterns.md`. Empty scaffolds are normal. Never invent a pattern from
   an empty file.
6. Ingest anything new in `sources/corpus/` per `state/ingested.json`. Files already
   ingested are skipped, not re-read. New files in `sources/corpus/` mean the voice
   profile is refreshed before anything is written. Never ingest a corpus file whose
   author is not him.
7. Confirm what is actually connected — browser automation, video generation. Never
   claim a capability not verified.

## The run

### 0. Take the topic and the route — first, before anything else

**One exchange, and it is the only thing the engine asks.**

**The topic.** If he gave one with the command — "run the content engine, topic:
handover is not the finish line" — take it and do not ask again. If he did not, ask for
it in one line and wait. **Do not pick a topic for him.** An engine that invents today's
subject is back to guessing, which is the thing this redesign removed.

A topic can be broad ("leasing"), narrow ("why Fund II closed at the size it did"), or a
thing that happened this morning. Width is his call. Where a topic is broad enough to
carry four different arguments, the narrowing happens in Step 3 against the research —
not by asking him a second question.

**The route.** One `AskUserQuestion` call, three options:

| Option | What it commits to |
|---|---|
| **Cut today's clips** | He filmed something today. He pastes the clip paths in chat; `videographer` joins them in Higgsfield with transitions and delivers 9:16. |
| **AI avatar video** | `avatar` drives HeyGen Studio in Chrome and renders him on screen, locked avatar, **Cartesia / Sonic 3.6**, through Generate. |
| **No video today** | Text slate. The three Instagram options ship as caption plus cover, and no Reel is planned or promised. |

Where the topic was supplied with the command, this question is the whole of Step 0 —
ask it alone, take the answer, and get on with the run.

**If he picks the clips route**, ask for the paths in the same breath and wait for them.
Do not guess a folder, do not go looking in Downloads, and do not start the run around a
Reel whose footage has not arrived. Clips are files he hands over; nothing else is a clip.

**If he picks the avatar route**, say nothing further about it now. Picking it is the
go-ahead: the Reel renders inside this run, without a second question, and the finished
clip arrives in chat with the console. What it must not carry is set by `avatar`'s
refusal list, which is about the words rather than about who approved them.

**Check the browser before promising either.** Both routes are browser jobs. No
`~~browser` connector means no render on either path: say so in one line, take the answer
anyway, and let the Reel ship as a cut plan or a script plus spec. Do not quietly demote
him to the text slate.

Record the topic and the chosen route in `runs/YYYY-MM-DD.md` with the rest of the run
line.

### 1. Read the numbers — locally, no browser

Read `performance/log.md` and `performance/patterns.md`. **Do not open a platform.**
The log is the store of record and the confidence factors are computed from it; a
topic-driven run has no reason to spend browser time on an analytics scan.

Empty log → one line, "no performance data yet, N posts published", move on. Under six
posts on a surface is noise, not a pattern, and both confidence factors stay at 1.00.

**The discovery layer is not in this run.** Mining his Instagram comments and the live X
listening scan exist to *find* a topic; he just gave one. They are still there and still
work — he runs `researcher` directly when he wants the idea bank filled, and the cursors
in `state/` keep working forward-only when he does. Never imply this run did either.

### 2. Research the topic

Run `researcher` in **topic mode**: the topic is fixed, and the job is evidence for it
rather than a hunt for ideas. Primary reports over aggregators; fetch before citing;
never cite from memory. When two sources disagree, say so in the piece file.

If the research contradicts something the team has already built content on, or
contradicts the topic itself, that outranks the slate — it is the one `⚠` line in the
receipt.

**If the topic cannot be supported** — nothing verifiable, or everything found sits
outside what he can speak to — say so in one line and stop. Do not substitute a
different topic and do not pad the slate with a claim he has no standing for.

### 3. Frame the one argument

The topic is the subject. The **argument** is what the slate says about it, and there
is exactly one, written once:

```
claim:    the one thing this slate argues about the topic
proof:    the specific experience or figure that supports it, from brand/proof.md
turn:     the moment the reader's view should change
ask:      what the slate has earned the right to request
```

Test it before writing a word:

- **He can speak to it.** Cross-check `brand/proof.md`. No standing → find the adjacent
  claim he does have standing for, inside the same topic.
- **It fits a pillar.** Name which. A topic that fits no pillar is still postable if he
  asked for it — say which pillar it is nearest and note the gap in the run log.
- **It is an argument, not a category.** "Leasing" is a topic. "Leasing is the only part
  of the lifecycle that pays before possession" is an argument.
- **It is the one move.** `brand/voice-master.md` → *The one move*: state the received
  view, deny it, replace it. A slate that does not argue with a default assumption is
  not in his voice whatever else it gets right.
- **Nothing repeating an argument or proof story used in the last seven days.** Check
  `content/` and the idea bank. Same topic, different argument, is fine; same argument
  twice is not.

**Pick the register here**, per `brand/voice-master.md` → *Step 0*. Register B is the
house style and the default. Register A only where the brief is a challenge to industry
orthodoxy, a product bet, or an internal-logic reveal. **Write the register into the
piece file**, and never mix the two inside one post.

**The Reel has to fit the route he chose in Step 0.** Decide that now, not after writing.

- **Clips route** — the argument must be carryable by the footage actually in hand. Read
  what the clips show, and remember the shape Higgsfield renders: 2 inputs per pass, 5s
  each, 15s out. If the topic needs eight beats, the Reel carries one beat of it and the
  caption carries the rest.
- **Avatar route** — the argument must be a judgement, correction or position worth him
  saying to camera. If `brand/avatar-motion.md` has no confirmed `avatar_id`, or the
  browser is unreachable, it ships as script plus spec.
- **No video** — the Instagram options land as caption and cover alone.

Open the piece file at `content/<slug>.md`, slug derived from the argument rather than
from the topic, and add a row to `library/idea-bank.md` at `new`, sourced `operator`,
carrying the topic verbatim.

### 4. Build — one argument, three surfaces, three angles each

`hook-writer` → `script-writer`, then `videographer`, which takes the Step 0 route.

**Twelve hooks written and scored against the one argument, three chosen — one per
angle** (data-led, correction, observation). Those three angles become variants A, B and
C, and each is then adapted to each surface per `hook-writer` → *Adapt per platform*.
The angle is shared across surfaces; the string is not.

**The spine is written once and is identical in all nine options.** Same claim, same
proof, same number, same ask. What varies is the angle (A/B/C) and the surface
adaptation — LinkedIn carries the thesis in full, X is the observer's compression,
Instagram is the Gujarati spoken version with its own caption. Adapting is re-cutting
for the surface, never pasting one text with different line breaks.

If you find yourself writing a second claim, you have started a second slate. Stop and
use the first.

Then `videographer` builds or hands over:

- **Clips route** — `videographer` writes the cut plan, then drives Higgsfield itself.
  Editing his own footage needs no gate beyond the ones already on the copy.
- **Avatar route** — `videographer` writes the beat plan and hands the script to
  `avatar`, which checks the refusal list, reads the locked ids and drives Studio through
  Generate. **`videographer` never renders his likeness itself**, in either product.

**The avatar route does not pause the run.** It renders, and the finished clip is sent
into the chat with `SendUserFile` next to the console. He watches it there; nothing is
published until he says to post it. If the browser is unreachable or a script trips the
refusal list, the Reel is left `awaiting_render` with the spec visible and the slate
still ships.

Each variant carries a **confidence number and its evidence label**, computed once by
the script-writer per
`${CLAUDE_PLUGIN_ROOT}/skills/script-writer/references/variants.md` → `## Confidence`
and copied — never recomputed — into the console. The number is a property, like the
exposure note. Naming a pick on top of it is still pre-choosing and is still out.

Write everything to `content/<slug>.md`, advance the idea-bank row to `scripted`, then
hand to `publisher`, which builds the artifact and sets it to `staged`.

---

## The output — one artifact, content only

`publisher` republishes the console to the **same URL** every run, following
`${CLAUDE_PLUGIN_ROOT}/skills/publisher/references/console.md`.

**The artifact contains the content, one confidence chip per option, and nothing
else.** Nine options — three Instagram, three LinkedIn, three X — each as full final
copy. Each Instagram option carries **the Reel script as plain readable text**,
shot-by-shot, in the option itself. No rationale, no "why this works", no sources, no
metrics, no pillar labels, no strategy notes, no topic header, no explanation of what
the engine did, and nothing on the page explaining the chip. A platform name, A/B/C,
the confidence chip, the copy, a POST button. That is the whole page.

The chip is the number **and** its label (`74 emerging`), never a bare number, never a
bar or a colour ramp, and the three options stay in A/B/C order whatever their
numbers.

Then return **this, and nothing more**:

````
SLATE <date> · <topic>

⚠ <the one thing that outranks the slate. Omit the line entirely if there isn't one.>

NEEDS YOU · <the specific thing, or "nothing">
````

Plus the artifact card, which the app renders on its own.

**Hard limits on the chat response:**

- **No post copy, scripts, captions, hooks or sources in chat.** All of it is in the
  artifact and in `content/<slug>.md`. The confidence numbers are on the console; do
  not repeat them in the receipt.

  **One exception: the finished Reel itself.** On the avatar route the rendered clip is
  delivered into the chat with `SendUserFile`, with one line naming the piece, the variant,
  the duration and anything worth looking at. That is a file, not post copy, and it is the
  surface Gate 2 now sits on — he watches it before anything is published.
- **No commentary on the machinery** — not what was researched, not what was skipped,
  not what was held back. Those belong in the piece file and the run log.
- **One `⚠` line at most.**
- **Never apologise for the response being short.** It is short on purpose.

The one exception: if he asks to see a piece in chat, paste that piece.

## Posting

Posting is a separate step and a separate skill. He clicks POST on an option in the
artifact; that records the pick. When he then says **"post"** in chat, `post-runner` reads
the pick and drives Claude in Chrome to publish it. Do not attempt to post during this
run, and never treat a click as evidence that something went live — only a URL is
evidence.

**On an Instagram option, whether the button commissions a Reel depends on Step 0.**

- **A route ran and produced a file** — the video already exists. The console carries it,
  the POST click is a pick and nothing more, and `post-runner` uploads what is there.
  **It does not render again.** A second render of a piece that already has one is billed
  twice and can come back subtly different from the clip that was approved.
- **The avatar route was chosen but the browser was unreachable, or a script tripped the
  refusal list** — the option stays `awaiting_render` with the script visible, and the
  click is Gate 2 exactly as before: his click on a visible script approves it, the
  console records who clicked, and only that click starts a render.
- **No video route** — the Instagram options are caption plus cover. The button posts;
  nothing is commissioned.

Record which of the three applies on the `post_request` doc, so `post-runner` reads it
rather than inferring it.

Append a one-line note to `runs/YYYY-MM-DD.md`: date, **the topic verbatim**, the slug,
the register written, the route, anything held.

## Authority — who may decide what

The operator or a content manager may both run this. **Four things a manager may never
decide alone**, because each produces a claim only the operator can stand behind:

1. **A first-person claim he has not made** — any "I decided", "I was wrong", "we
   tried" not already quoted in `brand/proof.md`.
2. **A number about him or his company** not in `brand/proof.md`, or sitting there
   under **Targets**. A target published as a result is the worst failure available.
3. **Anything on the off-limits list** in the brand config.
4. **A public position on a live dispute in his sector.**

Route these to NEEDS YOU, batched. Do not block the run — build everything else, and
lock only the blocked variant in the artifact.

**A topic is not authority.** He naming a subject is not him approving a claim made
about it. The four above still gate, even when the topic came from him.

## Never

- **Choose the topic.** Ask for it, or read it from the command. Never supply one.
- **Drift off the topic** because the research turned up something better. Say so in the
  `⚠` line and build what he asked for.
- **Build a slate carrying three different arguments.** One argument, three surfaces,
  three angles. Nine options, one spine.
- **Mix Register A and Register B inside one post.** The single fastest way to write
  something that reads false.
- Put this engine, or a posting slot, on a schedule.
- Put anything in the artifact that is not the content itself or a confidence chip.
- Recompute a confidence number, invent a second scale for it, or order the options
  by it.
- Report progress toward a follower target, or let one reach a post in any form. They
  are goals; the analyst reports pace, and nothing publishes them.
- Build anything for YouTube. It is recorded as a target and is not a surface here.
- Write the copy yourself because it seems faster. The employees carry the voice rules.
- Let a draft drift back toward generic copy because `voice-rules.md` says so.
  `brand/voice-master.md` is the spec and the measured profile holds the counts; the
  floor loses to both.
- Claim a comment mine or a live scan this run did not do.
- Advance a status you did not earn, or invent a metric to justify a plan.
- Generate a synthetic version of the operator outside the `avatar` skill, whose
  consent gates are the point.
- Narrate the machinery. Return the receipt.
