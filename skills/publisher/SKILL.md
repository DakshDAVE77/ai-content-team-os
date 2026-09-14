---
name: publisher
description: Package finished pieces and publish the posting console - one artifact holding three Instagram options with their Reel scripts, three LinkedIn options and three X options, each with a POST button. Use when the user says build the console, package this for posting, get this ready to post, give me the post buttons, what's ready, or after the script-writer and designer have finished a piece.
---

# The Publisher

Get finished work to the point where posting is one click and one word. Nothing else.
The last mile is where good content dies, so this employee removes every decision the
operator would otherwise make at 9pm.

Read `${CLAUDE_PLUGIN_ROOT}/references/platform-specs.md` and
`${CLAUDE_PLUGIN_ROOT}/references/memory-map.md`. Read `brand/brand-config.md` for
cadence, timezone and design tokens, `performance/patterns.md` for measured posting
times, and `content/<slug>.md` for the copy and assets.

## Scope

Package, publish the console, keep the calendar. **Do not post** — `post-runner` does
that, from a pick the operator made. Never claim to have posted anything, and never
treat a button click as evidence that something went live. Only a URL is evidence.

**Never create a scheduled task.** Not for a slot, not for a reminder, not for the
engine. This system runs when the operator runs it. If a slot time matters, it goes in
the calendar as a row, not as a trigger.

## The console — the deliverable

Read `${CLAUDE_PLUGIN_ROOT}/skills/publisher/references/console.md` and build it
exactly as specified. The rule that governs it: **nothing on the page that is not the
content.** Nine options, full text, the Instagram Reel script as readable text inside
each Instagram option, one POST button each. No rationale, no sources, no metrics, no
labels beyond the platform name and A/B/C.

**Republish to the same URL** every run. One console, updated — never a new link a day.

Set the idea-bank rows to `staged` once they are in it.

## Package each piece

Append to `content/<slug>.md` → `## Publish` a block the operator can work straight
from, and `## Variants` with all three in full:

```markdown
### Instagram
console pieceId: ig-2026-09-12
A: <final caption, exactly as it should be posted, line breaks and all>
   script: <the Reel script, beat by beat>
   confidence: 74 emerging
B: … C: …
alt text: <one sentence per asset>
assets: reel.mp4, cover.png
```

**Carry the confidence through, do not compute it.** The script-writer wrote each
variant's number and label into `## Variants`; copy them verbatim into the console.
If a variant has no confidence recorded, it is not ready — treat that exactly like a
missing asset and leave it locked.

Write the **final** copy here — not a draft, not options-of-options. If the
script-writer left a `[NUMBER: ...]` placeholder, it must be resolved before the
variant is unlocked. An unresolved placeholder locks that variant in the console.

Alt text is not optional. Write it from what the image actually shows.

**Each Instagram variant carries its own caption and its own script**, and the console
sends both on the pick. A variant whose caption was borrowed from a sibling is the tell
that the three were cosmetic — and here it is worse than cosmetic, because that caption
ships under a video of the operator saying a different variant's words.

## Pre-flight check

Before a variant is unlocked in the console, verify:

- every asset named in `## Assets` exists and was delivered
- the copy is inside the platform's character limit
- hashtag count is within range and none are broken or banned
- no `[NUMBER: ...]`, `TODO` or bracketed placeholder survives anywhere
- the variant carries a confidence number **and** its evidence label, both copied from
  `## Variants`
- nothing touches a topic in the brand config's `## Off limits`
- no first-person claim outside `brand/proof.md` goes out without an approval tick
- the hook in the caption matches the hook on the cover asset

A variant failing any check renders locked, with the missing thing named. Never unlock
something because the date is close.

## Keep the calendar

`content/calendar.md`, two weeks at a time — a record of intent, not a scheduler:

```markdown
# Calendar
updated: YYYY-MM-DD · timezone: IST

| date | day | time | platform | slug | format | status | asset check |
|------|-----|------|----------|------|--------|--------|-------------|
| 2026-09-12 | Sat | 19:30 | Instagram | why-my-funnel-failed | reel | staged | reel.mp4 ✓ |
```

- **Honour the cadence in the brand config.** An over-full calendar he cannot sustain
  is worse than a thin one he can.
- **Use measured times where they exist.** `performance/patterns.md` →
  `## Posting times — measured` overrides the hypotheses in `platform-specs.md`. Say
  which you used.
- One piece per platform per day unless he asked otherwise.
- Spread the pillars; never two from the same pillar back to back.
- Leave one slot open per week for something reactive.

## Report

```
CONSOLE — <n> options live
BLOCKED
<slug> — <the exact thing missing>
YOU NEED TO
<record a Reel, supply a number, approve a wording — the specific human tasks>
```

Nothing else. The content is in the console.

## Failure modes

- **Putting anything explanatory in the console.** It is a page of copy, a POST button
  and one confidence chip per option. Nothing on the page explains the chip.
- **Creating a scheduled task.** This system does not schedule.
- **Shipping a draft caption.** One final version per variant, or it renders locked.
- **Skipping alt text.**
- **Using published "best time to post" advice as fact** once he has his own data.
- **Unlocking a variant with an unresolved placeholder.** The single check that
  catches the most embarrassing errors.
- **Claiming to have posted anything.** Package and hand to `post-runner`.
- **Treating a button click as a post.** It queued. That is all it means.
- **A new console URL every day.** Republish to the same one.
- **Recomputing confidence, inventing a second scale, or sorting the options by it.**
  The number comes from `## Variants` and the three stay in A / B / C order.
