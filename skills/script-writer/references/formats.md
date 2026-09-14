# Formats — the beats for each surface

Read only the format you need. Each is a beat structure, not a template to fill
mechanically: the beats decide what goes where, the operator's voice decides how
it sounds.

---

## Instagram Reel script (20–45s)

### Language — Gujarati, not optional

**Every Instagram Reel script is written in Gujarati.** English code-switching is
expected and normal — that is how he actually speaks — but the script is not an English
script and it is never an English script translated afterwards. Write it in Gujarati
from the spine.

| rule | why |
|---|---|
| **Recurring English loanwords go in the brand glossary; one-offs are written in Gujarati script.** | The Gujarati voice mispronounces Latin-script English. A mangled brand name in his own synthesised voice is not a typo. A glossary fixes the spoken audio and leaves captions spelled normally; transliterating changes both. |
| **Count syllables, not words.** 4.0–5.0 syllables per second at Speed 0.9. Budget at 4.0 against a hard cap: 30s = **120 syllables**. | Word counts do not transfer from the English formats below. |
| **One paragraph per beat. No pause tags.** | Pause tags do not work in HeyGen, and a connector render has no scenes — pacing comes from punctuation and sentence length. The paragraph break is a writing habit that keeps beats legible. |
| **The caption is Gujarati too**, with the same code-switching. | Same audience, same voice. A Gujarati Reel under an English caption reads as two people. |
| **Figures go on screen as digits.** | Readable, and it keeps spoken numbers out of the mouth where they are easiest to get wrong. |

The brand line stays in English where the operator has settled it that way — check
`brand/brand-config.md` → `## Language` before changing any fixed wording.

⚠ **There is no Gujarati corpus yet.** `brand/voice-profile.md` is measured from English
LinkedIn and X posts only, so it cannot tell you how he sounds in Gujarati. The banned
phrases in `voice-rules.md` are English and do not transfer. Until Gujarati Reels or
transcripts land in `sources/corpus/`, treat Gujarati voice as **unmeasured** and say so
when handing a script over.

| beat | seconds | job |
|---|---|---|
| Hook | 0–3 | the chosen hook, said out loud, no preamble |
| Context | 3–8 | the minimum setup needed for the payoff to land |
| Turn | 8–20 | the specific thing that happened or changed |
| Proof | 20–32 | the number, screenshot, or artefact that makes it credible |
| Ask | 32–45 | one action, earned |

Write it as spoken lines, one per line, in the operator's speaking rhythm — not as
prose to be read aloud. Mark on-screen text separately:

```
[0:00] SAY: અમદાવાદમાં આજે સાડત્રીસ ટકા ઇન્વેન્ટરી ખાલી પડી છે.
       TEXT: 37%
[0:04] SAY: આ ડિમાન્ડનો પ્રોબ્લેમ નથી. આ કેપિટલનો પ્રોબ્લેમ છે.
       TEXT: ડિમાન્ડ નહીં — કેપિટલ
```

Read what that example is doing, because it is the whole rule in four lines:

- **The spine is Gujarati.** Not an English sentence with Gujarati words dropped in.
- **The English loanwords are in Gujarati script** — ઇન્વેન્ટરી, ડિમાન્ડ, કેપિટલ, પ્રોબ્લેમ.
  That is the code-switching he actually speaks, written so the voice says it correctly.
  Latin-script `inventory` in the same slot comes out mangled.
- **The figure is spoken in words** (સાડત્રીસ ટકા) and shown on screen as `37%`. Reels are
  watched muted, and a spoken number is the easiest thing to get wrong.
- **The on-screen text is Gujarati too.** An English card over a Gujarati read is two
  people talking.

Add a `B-ROLL:` note only where a specific shot is needed. No "hey guys", no
logo intro, no "make sure to follow" mid-script.

### Three script variants, each with its own caption

Instagram ships **three complete Reel scripts** — A data-led, B correction, C
observation — per `variants.md`. Each one carries:

1. **The spoken script**, timed to beats. This is what the HeyGen avatar says verbatim,
   so it obeys the pacing rules: ~20–23 words per 10 seconds, numbers spoken in words,
   no stage directions inside the spoken lines.
2. **The on-screen text plan**, one cue per beat. Put every **figure** here rather than
   only in the mouth — a number is safer read than heard, and Reels are watched muted.
3. **Its own caption.** Not shared, not copied across the three. The caption's first line
   sharpens *that variant's* hook, because that is the only line most people read.

The three scripts run to the same length band and carry the same number. If variant C
needs eight seconds more to land, the argument is not the same argument.

**The first three seconds cannot be founder-centred** — that is in the brand config and
it applies to all three openings. A data-led open states the finding, not who found it.

---

## Instagram carousel (6–9 slides)

| slide | type | job |
|---|---|---|
| 1 | cover | the hook, and the promise of what the swipe buys |
| 2 | cards | pay the promise off immediately — the least patient slide |
| 3–7 | cards / stats / process | one idea per slide, in argument order |
| 8 | quote or process | the synthesis: what it all adds up to |
| 9 | cta | one ask |

Nine slides is the ceiling for a first-person story; six is often better. Slide 2
is where carousels die — if it restates slide 1, the swipe rate collapses.

Write in deck grammar (see `design-system.md`): one `**accent**` word per
headline, manual `|` line breaks, card labels under ~34 characters, card
descriptions one sentence.

---

## LinkedIn feed post (700–1,400 characters)

```
<line 1: the hook — a complete thought under 140 chars>
<line 2: the consequence or stake>

<the story: 3–5 one-line paragraphs, chronological, specific>

<the turn: what you understood>

<the transferable point: one sentence, plainly stated>

<the ask: a question, or nothing>
```

Real line breaks between every paragraph. No hashtag wall — three at most, at the
end. No "Agree?" No "Thoughts?" as a lone closer. If the post carries a link, put
it in the post unless `performance/patterns.md` shows first-comment does better
for this operator specifically.

**Three variants**, per `variants.md`. The first two lines are all most readers see, so
the three genuinely diverge there and converge by the third paragraph. Write each to the
full 700–1,400 range; a variant that is visibly shorter reads as the afterthought it is.

---

## X thread (5–12 posts)

- **Post 1** is a complete argument. It must work if nobody reads post 2.
- Each subsequent post carries one move and stands alone if quoted.
- No "🧵", no "a thread:", no numbering unless order genuinely matters.
- The last post restates the claim; it does not thank anyone for reading.
- If the thread would be better as one post, make it one post.

Single X post: one claim, one specific, under 280 characters. Cut the setup.

**Three variants**, per `variants.md`. At 280 characters the angle *is* the post — there
is no room for the way in and the argument to differ, so the opening carries everything.
If two variants read nearly the same, one of them was not written, it was nudged. Rewrite
it from its own hook.

---

## Threads post (under 500 characters)

Warmer than X, and built for replies rather than saves. One observation, one
specific, and a genuine question at the end — not a rhetorical one. Threads
rewards conversation, so write something the operator will actually reply to
people about.

---

## Pulse article (900–1,600 words)

```
Title            under 80 chars, no colon-subtitle
Standfirst       2 sentences: the claim and who should read it
The moment       the specific event that prompted the piece
What I believed  the prior, honestly stated
What happened    the sequence, with real detail
What I do now    the method, concretely — steps, not principles
What I still     the open question or caveat, honestly
  don't know
Monday           what the reader should change tomorrow
```

Four to six sections with plain sub-headings. A lived example in every section.
No summary bullets at the top. No "conclusion" heading. An article is where a post
that already earned attention gets its full version — check `performance/log.md`
before drafting a new argument from scratch.

---

## Caption (Instagram)

```
<line 1: repeat or sharpen the visual hook — the only line most people read>
<one line of white space>
<2–4 short paragraphs: the story the visuals could not carry>
<the ask, one line>
<3–8 hashtags, specific to the niche, not volume tags>
```

The caption is not a transcript of the carousel or the Reel. It adds the part the
visuals could not carry.

**One caption per variant.** Three scripts means three captions, each opening off its
own hook. A single caption bolted onto whichever variant he picks is the tell that the
variants were cosmetic.

Captions ship **final** — the exact text to paste, hashtags included, no options and no
brackets. The posting console copies this string to the clipboard verbatim, so anything
left unresolved in it goes out unresolved.

---

## Universal cuts

Before handing anything off, delete:

- the first sentence, if the second one is stronger — it usually is
- every adverb doing the work a verb should do
- "I think", "I believe", "in my opinion" — the byline covers it
- any sentence that only restates the previous one in different words
- the closing platitude
