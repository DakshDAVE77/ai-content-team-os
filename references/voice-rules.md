# Voice rules — shared by every writing employee

These override generic "good writing" instincts. They exist because AI-written
social copy has a recognisable smell, and that smell costs reach and credibility.

## Read the brand first — this file is the floor, not the ceiling

Five things describe the voice, and when they disagree **higher wins**:

1. `brand/brand-config.md` → `## Voice corrections` — what the operator personally
   rejected and rewrote by hand.
2. `brand/voice-master.md` — the voice document the operator supplied, distilled into
   the rules a writer applies: register, post architecture, hook formulas, story shapes,
   CTA formulas, vocabulary and the do-not list. **This is the writing spec.**
3. `brand/voice-profile.md` — measured from their real posts in `sources/corpus/`.
   See `${CLAUDE_PLUGIN_ROOT}/references/voice-corpus.md`. It outranks the voice master
   **on counted numbers only** — sentence-length medians, punctuation counts, per-platform
   first-person share, post length. On shape and register, the voice master wins.
4. `brand/brand-config.md` → `## Voice profile` / `## Their words` — what they said
   about themselves at onboarding.
5. **This file.**

Everything below is built from what generic AI social copy gets wrong. It is a good
floor and it is not a description of any particular person. A real corpus **will**
contradict parts of it, in specific and measured ways, and `brand/voice-profile.md`
carries those contradictions under `## Where this overrides voice-rules.md`.

**Read `brand/voice-master.md` first, then that section.** The voice master is the
operator's own supplied document and it is the spec; a measured override beats this
file every time. What the corpus does not contradict still binds — the banned phrases,
the numbers discipline, and the specificity test especially.

Correcting a writer's real voice back into a generic one, every run, forever, is the
single most expensive thing this file can cause. Do not do it.

## Banned outright

**Phrases.** "In today's fast-paced world", "game-changer", "unlock", "unleash",
"supercharge", "dive in", "delve", "elevate", "harness the power of", "at the end
of the day", "the secret sauce", "it's not X, it's Y" as a formula, "let that sink
in", "here's the kicker", "spoiler alert", "plot twist", "the truth is".

**Shapes.** The three-word staccato paragraph stack ("Focus. Execute. Repeat.").
The em-dash-heavy aphorism. The rhetorical question opener that answers itself.
The numbered list where every item is the same length. Ending on a one-line
"platitude drop". Starting a LinkedIn post with a single word and a full stop.

**Moves.** Fake vulnerability ("I'll be honest with you"). Invented statistics.
Rounded numbers presented as measured ("grew 300%"). Second-person commands the
operator has not earned ("Stop doing X"). Claiming a result the operator did not
get. Speaking for an audience's feelings ("You're probably thinking...").

## Required

- **Concrete over abstract.** A number, a name, a date, a dollar amount, or a
  specific object in every paragraph that makes a claim.
- **First person, past tense, real events.** Write what happened, not what one
  should do. If the operator has no experience of the claim, either find their
  real adjacent experience in `brand/brand-config.md` or drop the claim.
- **Vary sentence length deliberately.** A long clause, then a short one. Never
  three same-length sentences in a row.
- **One idea per piece.** If a draft carries two arguments, it is two posts.
- **Earned CTA.** Ask for the thing the post actually justifies. A post that
  taught one tactic can ask for a save. It cannot ask for a sales call.

## The specificity test

Before handing anything off, check every sentence against: *could this sentence
appear in a competitor's post with no edits?* If yes, it is filler. Replace it
with something only this operator could write, or cut it.

## Numbers discipline

Never write a metric the operator has not supplied. If a number is needed and
absent, write `[NUMBER: what you need]` and flag it in the handoff. A placeholder
the operator fills is honest. A plausible invention is not, and it is the fastest
way to lose an audience.

## When the operator edits you

Log what changed. Append the correction to `brand/brand-config.md` under
`## Voice corrections` with the date, the phrase that was wrong, and the phrase
they replaced it with. That file is the only thing that makes the team sound more
like them over time.
