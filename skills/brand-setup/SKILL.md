---
name: brand-setup
description: Set up or update the operator's brand profile that the whole AI content team writes from - voice, niche, content pillars, proof, palette and offers. Use when the user says set up my brand, onboard the content team, configure my content system, update my brand voice, change my accent colour, add a content pillar, my drafts do not sound like me, or when any other content-team skill reports that brand/brand-config.md is missing.
---

# Brand setup

Produce `brand/brand-config.md` — the file every other employee reads before it
writes a word. Without it the team writes generic content, so this runs first and
gets updated whenever the operator corrects a draft.

Read `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` for where things live.

## Check state first

read `brand/brand-config.md`.

- **Missing** → run the full interview below.
- **Exists and the user asked to change something** → read it, change only what
  they named, write the whole file back. Do not re-interview.
- **Exists and the user asked to "set up"** → show them the current profile in a
  short summary and ask what to change.

## The interview

Ask with **AskUserQuestion**, in three rounds. Never more than four questions per
round. Offer real options rather than open boxes wherever a choice is bounded —
the operator answers faster and the answers are more usable.

**Round 1 — position.**
Who they are and what they post about; who the content is for; what outcome they
want from the account (audience, leads, hiring, credibility); how often they can
realistically publish.

Also capture their **follower targets** per platform, and the date they want to hit
them by. Ask for the date — a target with no horizon cannot be paced against, and
pacing is the only thing that makes a target useful rather than decorative. If they
have no date, record `no date set` rather than inventing one.

**Round 2 — substance.**
Their three to five content pillars. What they have actually done that gives them
standing to talk about this — projects, numbers, jobs, failures. What they will
not talk about. Whether there is an offer, and what it is.

**Round 3 — voice and look.**
Three accounts whose writing they like and what specifically they like about it.
Words and phrases they would never say. Their accent colour, if they have one, and
whether they want the default warm-paper look or something else.

Then ask them to paste **two or three things they have already written** — a post,
a Slack message, an email, anything in their own hand. This matters more than every
answer above. If they have nothing, say so in the file rather than guessing.

**Then ask the question that matters more than all of it: do they have an export of
their existing posts?** A folder of their real posts beats three pasted samples by so
much that it is worth asking twice. If they do, have them drop it into
`sources/corpus/` and derive the profile from it — see the next section. Pasted
samples become the fallback, not the source.

## Derive the voice profile

**If `sources/corpus/` has files, derive from those, not from the pasted samples.**
Read `${CLAUDE_PLUGIN_ROOT}/references/voice-corpus.md` and follow it: measure per
platform, record every claim with its number, write `brand/voice-profile.md`, and fill
the `## Where this overrides voice-rules.md` section — that section is what stops every
later draft sanding their real voice back into generic copy.

Record ingested files in `state/ingested.json` under their `corpus/...` path so they
are never re-read. Pull `## Proof candidates` out of the corpus at the same time —
figures they have already published under their own name — and hand them to the
operator to confirm before any of it reaches `brand/proof.md`.

From the pasted samples — or as a cross-check against the corpus — extract and record
concretely, not as adjectives:

- median sentence length, and whether they use fragments
- do they use first person singular, plural, or avoid it
- how they open (question / claim / anecdote / number)
- how they close (ask / statement / question)
- punctuation habits: em-dashes, ellipses, parentheses, exclamation marks
- their actual recurring words and phrases, quoted
- register: do they swear, joke, hedge, address the reader directly

"Conversational and authentic" is not a voice profile. "Averages 11 words a
sentence, opens on a number, never uses exclamation marks, says 'ship' not
'launch'" is.

## Write the file

write to `brand/brand-config.md`:

```markdown
# Brand config
updated: YYYY-MM-DD

## Identity
operator: <name> · handle: <@handle> · timezone: <tz>
one-liner: <what they do, in their words>
audience: <who, specifically>
goal: <what the account is for>
cadence: <posts per week, per platform>

## Platforms
in scope: Instagram, LinkedIn, X/Threads, Pulse
notes: <anything platform-specific they said>

## Language
| surface | language |
|---|---|
| Instagram — Reel script and caption | **Gujarati, with English code-switching.** Not optional, and never an English script translated afterwards. Recurring English terms go in a HeyGen brand glossary; one-offs are written in Gujarati script. One voice carries both languages, so an untreated English word is mispronounced in his own voice. |
| LinkedIn | English |
| X | English |
| Pulse | English |

fixed wording that stays English regardless: <the brand line, product names — list them>

Ask which surfaces are in which language, and which phrases stay English whatever the
surrounding language. Record both. A script that translates a locked brand line is a
script that changed a name.

## Targets
| platform | follower target | by | tracked |
|---|---|---|---|
| Instagram | 10,000,000 | <date or "no date set"> | yes |
| X | 1,000,000 | <date or "no date set"> | yes |
| LinkedIn | 100,000 | <date or "no date set"> | yes |
| YouTube | 1,000,000 | <date or "no date set"> | **no — not a surface in this system** |

These are **goals, not results.** The same rule that governs `brand/proof.md` →
Targets governs them: a target published as though it were achieved is the worst
failure this system can produce. Never write a target into a post, a caption, a hook
or a script, in any form, including "on our way to" framings that imply the number.

The analyst reports pace against them; nothing else reads them as a fact.

YouTube is recorded because the operator stated it, and marked untracked because
nothing in this system publishes to or measures YouTube. Do not build toward it, do
not write YouTube scripts, and do not report progress on it.

## Content pillars
| pillar | what it covers | share of output |
|---|---|---|

## Proof
<projects, numbers, roles, failures they can speak from — the raw material every
writer draws on. Specific and dated.>

## Off limits
<topics, claims, and clients not to mention>

## Voice profile
<the derived, concrete list above>

## Their words
<quoted phrases from the samples, to reuse verbatim>

## Never say
<their banned list, plus anything from voice-rules.md they agreed with>

## Design tokens
accent: #RRGGBB
name: <what goes in the slide chrome, usually the handle or a short brand mark>
tagline: <the mono line under it>
version: <the footer pill text>
footer: <the accent footer text>

## Voice corrections
<appended over time — date, what the team wrote, what the operator changed it to>
```

If they have an offer, write `brand/offers.md` too: what it is, who it is
for, price, the proof that supports it, and the exact CTA wording they want used.

## Scaffold the memory — do not skip this

A fresh install has no memory, and every other employee reads before it writes.
**Resolve `<root>` first** per `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` — a
`ContentEngine` folder inside one of the operator's connected folders. No connected
folder means no memory: ask for one before going further, because everything below
has nowhere to live otherwise.

Then **create every file** listed in
`${CLAUDE_PLUGIN_ROOT}/references/first-run.md`, not just the brand config. Scaffolds
are written **empty but structured** — headers, table columns, and one line saying the
file is empty. A missing file breaks a read; an empty one with the right shape does not.

write each of these if it does not already exist. Never overwrite one that does.

| Path | Seed with |
|---|---|
| `brand/voice-profile.md` | Measured from `sources/corpus/` per `voice-corpus.md`, if there is a corpus. If there is not, a heading, the pasted-sample profile, and one line saying the profile is derived from N samples and will be replaced when a corpus arrives. Record which languages the corpus actually covers — a profile measured from English posts says nothing about how they sound in another language. |
| `brand/avatar-motion.md` | Only if they use an avatar. Use the template in `skills/avatar/references/build.md` → *The motion file*: locked `voice_id`, engine, speed, pitch, brand glossary id, and the verbatim motion block passed as `motionPrompt`. Draft it for them to confirm; never invent motion direction. |
| `brand/proof.md` | The proof material from Round 2, as a dated list, under a heading that says these are the only numbers publishable about the operator. Add the corpus proof candidates as a separate **unconfirmed** section for the operator to tick through. Flag any figure given twice with different values as **unresolved — do not publish**, whether the conflict came from the interview or from two of their own posts. |
| `brand/offers.md` | Only if they have an offer. |
| `library/idea-bank.md` | The status ladder and the empty table from `memory-map.md`. |
| `library/hooks.md` | Heading, the scoring rubric, and "no hooks written yet". |
| `library/swipe-file.md` | Heading and "empty — add references worth stealing the structure of". |
| `content/calendar.md` | The slot-hypothesis table from `platform-specs.md`, marked as hypotheses to be replaced by real data. |
| `performance/log.md` | The column headers from `skills/analyst/SKILL.md` — including `angle` and `confidence` — plus what the operator should paste and when, and a `follower count` line per platform so pace against the targets can be computed from the first week. |
| `performance/patterns.md` | Heading, plus the rule: no pattern from fewer than six posts on a surface. |
| `state/analytics-cursor.json` | `{"updated": "<today>", "linkedin": {}, "instagram": {}, "x": {}, "log_rows": 0, "patterns_computed_from_rows": 0}` — this is what stops every run rescanning analytics from the beginning. |
| `state/comments-cursor.json` | `{"updated": "<today>", "instagram": {"last_scan": null, "posts": {}}, "ideas_from_comments": 0}` — stops every run re-reading every comment on every post. |
| `state/ingested.json` | `{"files": {}}` |
| `sources/corpus/` | An empty directory, plus a `README.md` inside it saying: drop **your own** posts and voice documents here. This is what the team learns your voice from, and more of it is strictly better. Each file is read once, ever. **Include every language you publish in** — a corpus in one language measures only that language, and a spoken language needs transcripts, voice notes, talks or interviews. Name the gap in the README if a configured surface has no corpus in its language. |
| `sources/cs-scrape/` | An empty directory, plus a `README.md` inside it saying: drop **other people's** scraped post exports here — JSON, CSV or markdown — and the next run ingests each file once and never re-reads it. Your own posts go in `sources/corpus/` instead; mixing them teaches the team to sound like your competitors. |

## Check what is connected

Before finishing, say plainly which optional capabilities are available — browser
automation, video generation, analytics. See the table in
`references/first-run.md`. The team works without all of them; the operator should
know what they are and are not getting rather than discovering it mid-run.

Say one more thing, once: the engine runs only when they run it — it is never put on a
schedule — and posting happens when they click POST in the console and then say
"post".

Do not ask them to connect anything. Name what is on, name what a missing one costs,
and move on.

## Finish

1. Show the operator the derived voice profile as plain text and ask if it sounds
   like them. Fix it now if not — every later output inherits this.
   Where it came from a corpus, show the **measurements** — median sentence length,
   punctuation counts, the platform split — and the `## Where this overrides
   voice-rules.md` list. Those are the lines they are most likely to correct, and a
   correction there is worth more than anything else in this interview.
   Show the targets table back too, and say once that targets are never published as
   results and that YouTube is recorded but not tracked.
2. Confirm every file in `${CLAUDE_PLUGIN_ROOT}/references/first-run.md` exists. Count
   the table, do not count from memory — the list grows.
3. Tell them the one command that matters: **"run the content engine"**. Mention they
   can also call a single employee by name.

## Keeping it alive

Whenever the operator rewrites something the team drafted, append the correction to
`## Voice corrections` with the date, their version, and the team's version. This
is the only mechanism that makes the output sound more like them over time — do it
every time, unprompted.
