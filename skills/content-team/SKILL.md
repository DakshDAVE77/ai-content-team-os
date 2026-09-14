---
name: content-team
description: Run the AI content engine - one command that researches the day, then publishes one artifact holding three Instagram options (each with the Reel script as text), three LinkedIn options and three X options, each with a POST button. Use when the user says run the content engine, run the content team, run the engine, what should I post, give me today's posts, content status, or asks for content without naming an employee.
---

# The Content Engine

One command in. Nine post options out, in one artifact, with nothing else in it.

**Run on demand only.** This engine is never put on a schedule and never creates a
scheduled task for itself or for a slot. If asked to schedule it, say once that it is
built to run interactively — the live scan and the posting both need an open browser —
and do not create a trigger.

**Do not narrate the pipeline.** No "now running the researcher", no phase headings, no
progress commentary. Run it, publish the artifact, return the three-line receipt at the
bottom of this file.

Read `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` first and resolve `<root>`.

## Pre-flight — quiet, one pass

1. Resolve `<root>` per the memory map. No connected folder → one line, then run
   stateless.
2. Read `brand/brand-config.md`. **Missing → stop**, one sentence, run `brand-setup`.
3. Read `brand/proof.md`, `brand/brand-config.md` → `## Targets`,
   `library/idea-bank.md`, `performance/patterns.md`.
   Empty scaffolds are normal. Never invent a pattern from an empty file.
4. Read `brand/voice-profile.md`. It is measured from his own posts and it outranks
   `references/voice-rules.md` wherever the two disagree — the overrides are listed in
   the profile itself. Missing profile is not a blocker; say nothing and write from the
   brand config.
5. Ingest anything new in `sources/corpus/` and `sources/cs-scrape/` per
   `state/ingested.json`. Files already ingested are skipped, not re-read. New files in
   `sources/corpus/` mean the voice profile is refreshed before anything is written —
   his own writing is the strongest signal here and it is stale the moment he adds to
   it. Never ingest a corpus file whose author is not him.
6. Confirm what is actually connected — browser automation, video generation. Never
   claim a capability not verified.

## The run

### 1. Mine his own comments, then listen
Both need Claude in Chrome. Skip cleanly if absent — never imply you did either.

**His own Instagram comment section comes first.** Read forward only against
`state/comments-cursor.json`; capture repeated questions, objections, corrections and
requests, quoted verbatim with the handle. Method:
`${CLAUDE_PLUGIN_ROOT}/references/browser-listening.md` → *Mining the operator's own
Instagram comments*. Read-only — nothing is liked, hearted or replied to. New rows go
into the idea bank at `new`, sourced `ig-comments`, and the cursor is written after
they land.

A question two or more people asked outranks anything the public scan returns. It is
stated demand from the audience the targets are about.

**Then the public scan.**

Build queries from the operator's own pillars, city and category terms in
`brand/brand-config.md`, never a hardcoded list. Include one deliberately adversarial
query. Method and the `read_page`-not-`get_page_text` gotcha:
`${CLAUDE_PLUGIN_ROOT}/references/browser-listening.md`.

Capture the claim, the numbers, the engagement, and **what nobody in the thread has
the standing to say that the operator does.** Write `research/x-scan-YYYY-MM-DD.md`.

If a live claim contradicts a source the team has built content on, that outranks the
slate — it is the one `⚠` line in the receipt.

### 2. Read the numbers — forward only
Read `performance/log.md`, `performance/patterns.md` and `state/analytics-cursor.json`.

**Never rescan analytics from the start.** Read the platform only for posts newer than
the cursor, stop at the first post already logged, append the new rows, then recompute
patterns from the local log. Full cursor rules are in the memory map. Write the cursor
only after the log rows land.

Empty log → one line, "no performance data yet, N posts published", move on. Under six
posts on a surface is noise, not a pattern.

### 3. Research
Run `researcher` for web sources. Primary reports over aggregators; fetch before
citing; never cite from memory. When two sources disagree, say so in the piece file.

### 4. Pick three
One idea per surface, from the idea bank or today's scan:

- Honour holds and blocks in the idea bank's **Notes on specific rows**.
- Prefer an idea his own comment section asked for, where one qualifies.
- Weight toward what has produced follows for him — the targets are follower targets.
  Weight; do not override. An idea he cannot speak to does not qualify because it
  might grow the account.
- No two of the three from the same pillar, and never two on the same source table.
- Nothing repeating an argument or proof story used in the last seven days.
- The Reel idea should be implementable as a presenter piece via the operator's avatar.
  If `brand/avatar-motion.md` has no confirmed `avatar_id`, or there is no video
  connector, the Reel idea must work without him on camera at all — decide that before
  writing, not after.

### 5. Build
`hook-writer` → `script-writer`, then `videographer` for the Reel beat plan and
`avatar` only where authorization and approved wording both exist. `videographer`
never generates his likeness itself.

Twelve hooks written and scored, **three chosen — one per angle** (data-led,
correction, observation). Those become variants A, B and C. Never one. Never one
marked recommended.

Each variant carries a **confidence number and its evidence label**, computed once by
the script-writer per
`${CLAUDE_PLUGIN_ROOT}/skills/script-writer/references/variants.md` → `## Confidence`
and copied — never recomputed — into the console. The number is a property, like the
exposure note. Naming a pick on top of it is still pre-choosing and is still out.

Write each piece to `content/<slug>.md`, advance idea-bank rows to `scripted`, then
hand to `publisher`, which builds the artifact and sets the rows to `staged`.

---

## The output — one artifact, content only

`publisher` republishes the console to the **same URL** every run, following
`${CLAUDE_PLUGIN_ROOT}/skills/publisher/references/console.md`.

**The artifact contains the content, one confidence chip per option, and nothing
else.** Nine options — three Instagram, three LinkedIn, three X — each as full final
copy. Each Instagram option carries **the Reel script as plain readable text**,
shot-by-shot, in the option itself. No rationale, no "why this works", no sources, no
metrics, no pillar labels, no strategy notes, no explanation of what the engine did,
and nothing on the page explaining the chip. A platform name, A/B/C, the confidence
chip, the copy, a POST button. That is the whole page.

The chip is the number **and** its label (`74 emerging`), never a bare number, never a
bar or a colour ramp, and the three options stay in A/B/C order whatever their
numbers.

Then return **this, and nothing more**:

````
SLATE <date>

⚠ <the one thing that outranks the slate. Omit the line entirely if there isn't one.>

NEEDS YOU · <the specific thing, or "nothing">
````

Plus the artifact card, which the app renders on its own.

**Hard limits on the chat response:**

- **No post copy, scripts, captions, hooks or sources in chat.** All of it is in the
  artifact and in `content/<slug>.md`. The confidence numbers are on the console; do
  not repeat them in the receipt.
- **No commentary on the machinery** — not what was researched, not what was skipped,
  not what was held back. Those belong in the piece files and the run log.
- **One `⚠` line at most.**
- **Never apologise for the response being short.** It is short on purpose.

The one exception: if he asks to see a piece in chat, paste that piece.

## Posting

Posting is a separate step and a separate skill. He clicks POST on an option in the
artifact; that records the pick. On an **Instagram** option the button also commissions
the Reel — his click on a visible script is `avatar` Gate 2, so the console records who
clicked, and only his click starts a render. When he then says **"post"** in chat, `post-runner`
reads the pick and drives Claude in Chrome to publish it. Do not attempt to post
during this run, and never treat a click as evidence that something went live — only a
URL is evidence.

Append a one-line note to `runs/YYYY-MM-DD.md`: date, three slugs, cursor state,
anything held.

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

## Never

- Put this engine, or a posting slot, on a schedule.
- Put anything in the artifact that is not the content itself or a confidence chip.
- Recompute a confidence number, invent a second scale for it, or order the options
  by it.
- Report progress toward a follower target, or let one reach a post in any form. They
  are goals; the analyst reports pace, and nothing publishes them.
- Build anything for YouTube. It is recorded as a target and is not a surface here.
- Write the copy yourself because it seems faster. The employees carry the voice rules.
- Let a draft drift back toward generic copy because `voice-rules.md` says so. The
  measured profile wins, and the overrides in it are there precisely to stop that.
- Rescan analytics from the beginning, or write a cursor ahead of the log.
- Advance a status you did not earn, or invent a metric to justify a plan.
- Claim you scanned live social when the browser was unavailable.
- Generate a synthetic version of the operator outside the `avatar` skill, whose
  consent gates are the point.
- Narrate the machinery. Return the receipt.
