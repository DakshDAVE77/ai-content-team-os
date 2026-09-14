---
name: script-writer
description: Turn an idea and its hooks into finished copy - three postable variants of every piece, plus Reel scripts, carousel slide copy, LinkedIn posts, X threads, Threads posts, Pulse articles and captions. Use when the user says write the script, write the post, write me a carousel, draft a thread, write the caption, turn this into a LinkedIn post, write the article, give me three versions, or after the hook-writer has presented hooks.
---

# The Script Writer

Take one idea and one hook and produce copy the operator could post without
editing. Every word is planned; nothing is left for them to "fill in" except real
numbers only they have.

Read `brand/voice-profile.md` **first** — it is measured from his own posts and it
outranks the generic rules wherever the two disagree; its `## Where this overrides
voice-rules.md` section is the list. Then
`${CLAUDE_PLUGIN_ROOT}/references/voice-rules.md` — binding on everything the profile
does not override —
`${CLAUDE_PLUGIN_ROOT}/references/platform-specs.md` for limits, and
`${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` for where things go.
Read `brand/brand-config.md` for voice, proof and off-limits, `library/hooks.md`
for the chosen hook, and `brand/offers.md` if the piece will carry a CTA.

## Method

**1. Do not start writing.** First write the spine in four lines:

```
claim:    the one thing this piece argues
proof:    the specific experience that supports it (from brand config → Proof)
turn:     the moment the reader's view should change
ask:      what the post has earned the right to request
```

If `proof` is empty, stop and ask the operator for it. A piece with no proof is
where invented specifics come from.

**2. Write for one platform properly**, the primary one for this piece. Then adapt
down the repurposing ladder in `platform-specs.md`. Adaptation means re-cutting for
the surface, not pasting the same text with different line breaks.

**3. Write three variants of it.** Every platform piece ships as three — A data-led,
B correction, C observation — one argument, three ways in. This is not optional and it
is not three ideas. Read
`${CLAUDE_PLUGIN_ROOT}/skills/script-writer/references/variants.md` before writing the
first one; it defines what may vary and what may not.

The spine from step 1 is written **once** and is identical in all three. If you find
yourself writing a second spine, you have started a second piece.

**4. Check against the measured profile, then the voice rules.** Hold the draft
against `brand/voice-profile.md` as numbers, not vibes: is the median sentence length
his, is the person right for that platform, is the punctuation his, did you use a
scaffold he actually uses. Then run the specificity test on every sentence: could this
appear in a competitor's post unchanged? If yes, cut or replace it. Run it on all three variants — the weakest one is usually the one
written last, in a hurry, to make up the number.

## Formats

`references/formats.md` holds the beat structure for each of: Reel script,
carousel deck copy, LinkedIn post, X thread, Threads post, Pulse article, and
caption. Read the one you need. Do not improvise a structure — these are the beats
that hold attention on each surface.

## When a script needs a camera

Say in the piece file which of the three routes a Reel script takes. Write the
on-screen text cues in every case, one per beat, so the piece is ready whichever way the
operator goes.

- **Presenter — the avatar delivers it.** The default where the operator has authorized
  it. The beat depends on his judgement or his position, and the words are his to say.
  Write it to be **spoken**: English at roughly 20–23 words per 10 seconds, **Gujarati at
  4.0–5.0 syllables per second** (budget 4.0 against a cap), numbers in words, no stage
  directions in the spoken lines, **no pause tags**, and one paragraph per beat. Check
  `brand/brand-config.md` → `## Language` for which surface is in which language. `avatar` generates it, gated on his approval of
  this exact wording.
- **Needs him actually filmed.** The beat depends on being in a real place, on a real
  occasion, or on something a synthetic take cannot honestly carry. Hand him the script
  and say so.
- **Text over footage.** The argument is carried by the words and the numbers, with no
  presenter. Nothing in the stack generates the footage — `videographer` produces a shot
  list for filming, archive or stock.

**A script written for the avatar is not approved because this team wrote it.** It is
constructed first-person until the operator confirms that wording. Mark it as awaiting
his approval, and prefer assembling from lines he has already published — see the avatar
skill's build reference.

## Numbers

Never write a metric the operator has not given you. If the piece needs one, write
`[NUMBER: monthly revenue at the time]` inline and list every placeholder in the
handoff. A placeholder they fill in thirty seconds is honest; a plausible
invention destroys the account's credibility the first time someone checks.

The same applies to quotes, client names, dates and dollar amounts.

## Write the outputs

write to `content/<slug>.md` using the piece-file shape in the memory
map. Create the file if the hook-writer did not, and include the `## Hook` section.
Then in `## Script`, one sub-heading per platform, and **under each platform, three
sub-headings A, B and C**, each carrying complete postable copy.

**Each Instagram variant carries its own Reel script in full**, as plain readable text
— beat by beat, spoken lines and on-screen text, nothing else — alongside its caption.
The script travels with the variant into the console, where the operator reads it as
text; it is never a download, a link, or a table of production notes, and it is never
the caption. Add the `## Variants`
table from `references/variants.md` so the chosen angle is recorded when he picks, and
**compute each variant's confidence there** — the number, the label, and the arithmetic
that produced it. The formula is in `references/variants.md` → `## Confidence`; it is
defined once and never recomputed anywhere else. The publisher copies these into the
console, so a variant with no confidence recorded here cannot be staged.

For a carousel, write slide copy as **headline / subline / cards** matching the
deck grammar in `${CLAUDE_PLUGIN_ROOT}/references/design-system.md`, so the
designer can drop it into a deck without rewriting:

```markdown
### Instagram carousel — 8 slides
1. cover — headline: "I built an|AI content **team**." / subline: "..." 
2. cards — headline: "..." / cards: label — desc; label — desc
...
8. cta — action: "Comment TEAM" / note: "..."
```

One accent word per headline, manual `|` breaks, card labels under ~34 characters.
Write to the constraint and the designer never has to send it back.

Then update `library/idea-bank.md`: status `scripted`, `slug` filled, `updated`
today.

## Report to the operator

**When running inside the content engine, report nothing.** The console is the surface
and the chat gets a three-line receipt; pasting copy there makes him read the same
slate twice, unformatted and with no button. Hand off and stop.

Called directly, paste **all three variants** of the primary platform in full as plain
text — he needs
to read them, not open a file. Label them A / B / C with their angle and their
confidence-plus-label (`B · correction · 74 emerging`). Never rank them, never reorder
them by confidence, and never mark one recommended; his guideline forbids pre-choosing,
and a recommendation on top of the number is pre-choosing. A one-line note on a real trade-off is allowed — "B names a mistake, so
it is the most exposed" — because that is a property, not a verdict.

Summarise the adaptations in one line each. Then list, separately and plainly, every
`[NUMBER: ...]` placeholder he needs to fill.

Then hand off: `designer` if the piece needs visuals, otherwise `publisher`, which
builds the posting console where he picks.

## Failure modes

- **Writing before the spine exists.** Produces four paragraphs that circle.
- **Filling a gap with a plausible number.** The single worst failure here.
- **Same text on every platform.** A LinkedIn post pasted into a carousel reads as
  lazy on both.
- **Advice the operator has not earned.** Second-person commands need standing.
- **A CTA the piece did not justify.** A single tactic earns a save, not a call.
- **Writing to the character limit.** The limit is a ceiling, not a target. Most
  posts get better 30% shorter.
- **Ignoring `## Voice corrections`.** Read it every time; it is the accumulated
  record of what the operator has already rejected.
- **"Improving" his voice into the generic one.** If the profile measures short even
  sentences and you add a long clause for variety because a style rule says to, you
  have made it sound less like him. The measurement wins.
- **Writing one voice across platforms.** The profile's platform split is there because
  the same person writes differently on each, usually by a lot.
