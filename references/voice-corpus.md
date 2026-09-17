# The voice corpus — deriving how the operator actually writes

`brand-setup` asks the operator to paste two or three things they have already written.
Two or three is enough to start and nowhere near enough to be accurate. **A corpus of
their real posts is the strongest voice signal this system can have**, and it is the
only one that cannot be faked, borrowed, or drifted away from.

This file is the method. It is run by `brand-setup` at install, and again by any run
that finds new files in the corpus folder.

## Where it lives

| folder | holds | feeds |
|---|---|---|
| `sources/corpus/` | **the operator's own writing** — their posts, and any voice or doctrine documents they wrote or commissioned | `brand/voice-profile.md`, `brand/proof.md` candidates, the avatar's approved-wording bank |
| `sources/cs-scrape/` | **anyone's posts** — competitors, references, scraped exports | `library/swipe-file.md`, `performance/patterns.md` → `## From the scrape` |

The split is the whole point. A competitor's post belongs in the swipe file, where it
teaches structure. The same post in the voice corpus would teach the operator to sound
like their competitor, which is the exact failure this system exists to prevent.

**Verify before ingesting.** Where a file carries an `author` field, check it against
the operator's name in `brand/brand-config.md`. A mismatch is not ingested into the
voice profile — say which file, and move it to `cs-scrape/` instead. Where there is no
author field, the folder is the claim and the operator owns it.

Ingest is tracked in `state/ingested.json`, keyed by path relative to `sources/`, so a
file is read exactly once and the folder it sits in is part of its identity.

## Measure per language, and say which languages are unmeasured

**A voice profile is only valid for the language it was measured in.** An operator who
posts in English and speaks in Gujarati has two voices, and a corpus of one says nothing
about the other. Do not let the count hide that: 168 English posts is a strong English
profile and a *zero* Gujarati profile, not a strong profile overall.

Record in `brand/voice-profile.md`, per language: the number of samples, the surfaces
they came from, and the date. A language with no samples is written as
**unmeasured — do not infer from another language**, and every skill that writes in it
says so when handing the draft over.

**Never derive one language's voice from another's.** Translating an English-measured
profile into another language produces writing that is technically correct and sounds
like nobody. That is the specific failure this whole file exists to prevent, and it is
easier to commit across languages than across people, because the byline still matches.

What counts as corpus material in a spoken language: Reel or video transcripts, voice
notes he recorded, talks, interviews, anything he said or wrote himself. Ten pieces move
a language from unmeasured to measured. Ask for them by name rather than waiting — an
operator will not think to hand over WhatsApp voice notes unless told they are useful.

## Demonstrated voice beats stated voice

A corpus usually holds two kinds of thing, and they are not equal:

- **Posts they published** — *demonstrated* voice. What they actually do.
- **Voice guidelines, doctrine and vision documents** — *stated* voice. What they, or
  someone they hired, said they do.

**Where the two disagree, the posts win, and the disagreement gets recorded.** A voice
guideline saying "warm and conversational" against a corpus averaging six words a
sentence with no exclamation marks in a hundred and sixty posts is not a contradiction
to resolve by splitting the difference. It means the guideline describes an aspiration
and the posts describe the writer. Write from the posts. Note the gap in the profile so
nobody re-litigates it every quarter.

## What to measure

Adjectives are not a voice profile. Measure these, **per platform**, because the same
person writes differently on each and the difference is usually large:

| | what to record |
|---|---|
| **Sentence length** | median, mean and p90 words per sentence. The median is the one writers should hit. |
| **Post shape** | median lines per post; whether paragraphs are single lines or blocks |
| **Person** | what share of posts use first-person `I`. Split by platform — this is where the biggest platform gap usually sits. |
| **Openings** | the most common opening words and shapes, counted, not guessed |
| **Closings** | what share end on a question, a statement, or an ask |
| **Punctuation** | exact counts of em-dashes, exclamation marks, ellipses, parentheses, colons. Report the count, not an impression. |
| **Structural signatures** | separators, arrows, numbered ladders, repeated scaffolds — anything they do that a generic writer would not |
| **Lexicon** | their recurring nouns and verbs, with frequencies, quoted from the corpus |
| **Hashtags** | whether they use them, how many, and which recur |

**Every line in the profile carries its number.** "Never uses em-dashes" is a claim;
"0 em-dashes across 168 posts" is a measurement, and only the second one survives an
argument with a writer who wants to use an em-dash.

## Where the corpus overrides `voice-rules.md`

This is the most valuable section of the profile and the easiest to skip.

`references/voice-rules.md` is a floor built from what generic AI social copy gets
wrong. It says so itself: the brand's actual voice beats anything in it. A real corpus
will contradict it in specific, nameable ways — and unless those are written down,
every writing employee will "fix" the operator's real voice back into the generic one,
every run, forever.

So the profile carries an explicit override list:

```markdown
## Where this overrides voice-rules.md
- voice-rules bans the stacked one-line paragraph. He writes in them: median 15 lines
  per LinkedIn post, most of them one sentence. The stack is his form. Keep it.
- voice-rules says vary sentence length deliberately. His median is 6 words on both
  platforms, p90 13. Short and even is the voice. Do not add long clauses for variety.
```

Everything in `voice-rules.md` that the corpus does **not** contradict still binds —
the banned phrases, the invented-number rule, the specificity test. An override is
per-line and needs its measurement. "His voice is different" is not an override.

## The precedence chain

Five things describe the voice. When they disagree, higher wins, and every writing
employee reads them in this order:

1. **`brand/brand-config.md` → `## Voice corrections`** — what the operator personally
   rejected and rewrote. Nothing outranks a correction they made by hand.
2. **`brand/voice-master.md`** — the voice document the operator supplied, distilled to
   the rules a writer applies. **The writing spec**: register, post architecture, hook
   formulas, story shapes, CTA formulas, vocabulary, do-not list.
3. **`brand/voice-profile.md`** — measured from their real corpus. It outranks the
   voice master **on counted numbers only**; on shape and register the voice master wins.
4. **`brand/brand-config.md` → `## Voice profile` / `## Their words`** — what they said
   about themselves at onboarding.
5. **`references/voice-rules.md`** — the floor.

**A supplied voice document is not a "stated voice" guideline.** The rule below — posts
beat guidelines — is about a doctrine document written *about* an aspiration. A voice
master distilled from a count of his real posts is demonstrated voice in compressed
form, and it sits above the profile on everything except the counts themselves.

## Writing the profile

Write `brand/voice-profile.md`. Replace it in full on each refresh — a stale
measurement is worse than none — but never touch `## Voice corrections`, which lives in
the brand config and is appended, never regenerated.

```markdown
# Voice profile — measured
updated: YYYY-MM-DD · derived from <n> posts in sources/corpus/ · <date range>

## Provenance
<counts per platform, and the documents read as stated voice>

## Per platform
### LinkedIn (<n> posts)
<the measurements above, each with its number>
### X (<n> posts)
<same>

## The platform split
<the one or two differences large enough that a writer must not treat the platforms
as one voice>

## Lexicon
<recurring words with counts, and the words he does not use>

## Structural signatures
<the scaffolds that are his>

## Where this overrides voice-rules.md
<the per-line override list, each with its measurement>

## Stated vs demonstrated
<where the voice documents and the posts disagree, and which was taken>

## Proof candidates — unverified
<figures and claims asserted in his own published posts, with the post and date.
These are candidates for brand/proof.md, not entries in it. Conflicting values for
the same figure are listed together and marked unresolved — never merged, never
averaged, never silently resolved to the larger one.>
```

## What the corpus is not

- **Not performance data.** Corpus posts usually carry reactions and comments but no
  reach and no follows. They can seed pattern claims about *shape* — which openings and
  formats travelled — and they must be excluded from anything ranked on follow rate,
  including the `angle_factor` in the confidence formula
  (`skills/script-writer/references/variants.md` → `## Confidence`). A factor computed
  from posts with no follow data is a number pretending to be evidence.
- **Not proof.** A figure in a published post is a strong candidate for
  `brand/proof.md` because he already put his name on it. It still goes in as a
  candidate for him to confirm, and conflicting values stay flagged.
- **Not a template bank.** Never reuse a corpus post's argument as new content. It
  teaches how he writes, not what is left to say.
