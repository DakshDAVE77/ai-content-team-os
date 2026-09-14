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

### How he actually writes it — measured from his own production scripts

**English stays in Latin script. Numbers stay as digits. Gujarati carries the grammar.**

This is not a style preference, it is what his working HeyGen scripts do:

> છ મહિનામાં **Ahmedabad** ની આસપાસ **1.8 million square feet warehouse space lease** થઈ —
> **Cushman and Wakefield** નો આંકડો છે. ગયા વર્ષ કરતાં **54%** વધારે. એમાંથી **45%** એકલા
> **Kheda** એ લીધું. **Changodar 20%**. **Sanand 17%**.

| rule | why |
|---|---|
| **English words are written in Latin script, not transliterated.** `warehouse space lease`, `Asset class`, `Tenants`, `market average` — as he types them. Never વેરહાઉસ, never એસેટ ક્લાસ. | This is his demonstrated pattern across production scripts. Transliterating makes it read as someone imitating him. |
| **Place names, company names and brands stay Latin.** `Ahmedabad`, `Kheda`, `Sanand`, `Swiggy`, `Amazon`, `Voltas Beko`, `Cushman and Wakefield`. | Same reason. He does not transliterate proper nouns. |
| **Numbers are digits in the script, not words.** `1.8 million`, `54%`, `190,000`, `8 September`. | He writes them as digits and the voice reads them. Do not spell figures out. |
| **Gujarati carries the grammar** — verbs, connectives, case endings, everything structural: ની આસપાસ, નો આંકડો છે, ગયા વર્ષ કરતાં, એમાંથી, એ લીધું. | Gujarati is the matrix language. English is embedded in it, not the other way round. |
| **Count syllables, not words.** 4.0–5.0 syllables per second. Budget at 4.0 against a hard cap: 30s = **120 syllables**. Count the English words as spoken syllables too. | Word counts do not transfer from the English formats below. |
| **One paragraph per beat. No pause tags.** | Pause tags do not work in HeyGen. The paragraph break keeps beats legible. |
| **The caption is Gujarati too**, with the same code-switching. | Same audience, same voice. A Gujarati Reel under an English caption reads as two people. |
| **Figures also go on screen as type.** | Reels are watched muted. |

⚠ **Do not "fix" the mixed script.** A draft that looks inconsistent — Latin and Gujarati
in the same sentence — is correct. Normalising it in either direction is the most common
way to make a script stop sounding like him.

**Pronunciation is handled in Studio, not in the spelling.** If a specific English term
comes out wrong in the render, fix it with a HeyGen **Brand Glossary** entry — which
changes the spoken audio and leaves the script and captions spelled normally. Do not
transliterate a word into Gujarati script to force a pronunciation; that changes what the
viewer reads as well as what they hear.

The brand line stays in English where the operator has settled it that way — check
`brand/brand-config.md` → `## Language` before changing any fixed wording.

⚠ **The Gujarati corpus is thin.** `brand/voice-profile.md` is measured from English
LinkedIn and X posts, so it cannot tell you how he sounds in Gujarati. The banned phrases
in `voice-rules.md` are English and do not transfer.

What *is* available: his **production HeyGen scripts**, which are real Gujarati written by
him. The code-switching rules above are measured from those, and they are the strongest
Gujarati signal in the system. Pull more of them into `sources/corpus/` as they are
written — each one narrows the gap.

Until that corpus is real, say when handing a script over that the Gujarati **phrasing**
is inferred, even though the code-switching pattern is measured.

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
[0:00] SAY: છ મહિનામાં Ahmedabad ની આસપાસ 1.8 million square feet warehouse space
            lease થઈ — Cushman and Wakefield નો આંકડો છે.
       TEXT: 1.8M sq ft
[0:07] SAY: ગયા વર્ષ કરતાં 54% વધારે. એમાંથી 45% એકલા Kheda એ લીધું.
       TEXT: Kheda 45%
```

That is lifted from his own production script. Read what it is doing:

- **Gujarati is the matrix language.** છ મહિનામાં, ની આસપાસ, થઈ, નો આંકડો છે, ગયા વર્ષ કરતાં,
  એમાંથી, એકલા, એ લીધું — all the structure is Gujarati.
- **English sits inside it, in Latin script.** `warehouse space lease`, `Cushman and
  Wakefield`, `Kheda`. Not transliterated. This is the single most important rule and the
  easiest to get wrong.
- **Numbers are digits.** `1.8 million`, `54%`, `45%`. Written as digits, read aloud by
  the voice.
- **On-screen text is short and can be English.** It is a card, not a sentence.

Add a `B-ROLL:` note only where a specific shot is needed. No "hey guys", no
logo intro, no "make sure to follow" mid-script.

### Three script variants, each with its own caption

Instagram ships **three complete Reel scripts** — A data-led, B correction, C
observation — per `variants.md`. Each one carries:

1. **The spoken script**, timed to beats. This is what the HeyGen avatar says verbatim,
   so it obeys the rules above: Gujarati grammar, English in Latin script, numbers as
   digits, no stage directions inside the spoken lines.
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
