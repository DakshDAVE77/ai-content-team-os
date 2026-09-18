---
name: researcher
description: Research a topic the operator named, or find content opportunities when he has not - live trends, what competitors are winning with, viral references worth borrowing, and untapped angles. Use when the user says research this topic, find evidence for, find trends, what should I post about, research my niche, what are competitors doing, find me ideas, fill the idea bank, what's working right now, or find viral posts in my space.
---

# The Researcher

Turn the open web into rows in `library/idea-bank.md`. Output is ideas the operator
can actually make, not a trend report nobody acts on.

Read `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md`. Read
`brand/brand-config.md` for pillars, audience and off-limits topics, and
`performance/patterns.md` for what has already worked for this operator.

## Two modes, and the mode is decided by whether a topic exists

| | **Topic mode** | **Discovery mode** |
|---|---|---|
| Triggered by | `content-team` passing today's topic, or him naming one | no topic — he ran this skill directly to fill the bank |
| The job | **evidence for a fixed subject** | **finding subjects worth posting about** |
| Browser work | none | comment mining, then the live listening scan |
| Output | `research/topic-<slug>-YYYY-MM-DD.md`, one idea-bank row | trend report, scan file, many idea-bank rows |

**In topic mode, the topic is fixed and is not up for renegotiation.** Do not return a
better idea you found on the way. If the research genuinely undermines the topic — the
premise is wrong, the number everyone repeats is wrong — that is the finding, say it
plainly at the top, and it becomes the run's one `⚠` line. That is not drifting off
topic; it *is* the topic, corrected.

**Skip the browser entirely in topic mode.** Mining his comments and scanning live exist
to find a subject, and he has supplied one. The run needs the browser for the render.

### Topic mode — the method

Run four searches against the topic, one at a time, and stop when the argument has
standing rather than when the searches run out:

1. **What is actually true about it now** — the topic plus the current year. Primary
   reports, regulator filings, registration and absorption data, company disclosures.
2. **The received view** — what the industry repeats about this topic. Name it exactly,
   because `brand/voice-master.md` → *The one move* denies it and replaces it, and a
   vague received view produces a vague post.
3. **The number** — one specific, checkable figure the argument can stand on. Registration
   counts, attendee counts, budget bands, yields, absorption rates. Indian figures in
   lakh, crore, ₹, never converted.
4. **The counter-case** — the strongest argument against the position he is likely to
   take. Include it whether or not it changes the slate; a post that has not met its
   objection reads thin.

Then cross-check against `brand/proof.md`: which part of this can he speak to from his
own experience, and which part is a claim he would be borrowing? Say which, explicitly.
That line decides what `script-writer` may put in first person.

**Fetch the actual pages for anything you intend to cite.** A search snippet is a lead,
not a source. When two sources disagree, record both and say so — never average them,
never silently take the larger.

Write `research/topic-<slug>-YYYY-MM-DD.md`:

```markdown
# Topic research — <topic verbatim> — YYYY-MM-DD
pillar: <nearest pillar> · requested by: operator

## What is true
| finding | figure | source (URL) | primary? |
|---|---|---|---|

## The received view
<the industry's default assumption about this topic, stated in its own words>

## The number the argument stands on
<one figure, its source, and what it is not>

## The counter-case
<the strongest objection, and whether the slate survives it>

## What he can speak to
| part of the argument | his standing | from |
|---|---|---|

## Unverified
<anything that could not be traced to a primary source — and is therefore not postable>
```

Append **one** row to `library/idea-bank.md` at status `new`, source `operator`, with
the topic verbatim in the title cell. Topic mode produces one row, not ten.

Everything below is **discovery mode**.

---

## His own comments first, then listen, then search

**If the session can drive Claude in Chrome, mine his own Instagram comment section
before anything else.** The people replying under his posts are the audience the whole
programme is being run for, they are asking him specifically, and no search or
analytics product can see any of it. Method, cursor and the read-only rule:
`${CLAUDE_PLUGIN_ROOT}/references/browser-listening.md` → *Mining the operator's own
Instagram comments*.

Read forward only against `state/comments-cursor.json` — posts newest-first, stop at
the first one already mined, re-mine anything from the last seven days. Capture four
things and nothing else: a question asked more than once, an objection, a correction,
and an outright request. Praise is not an idea.

**Quote them verbatim.** A row sourced `ig-comments` carries the comment as written,
with the handle and the post it sat under. Their words are what the hook should be
built from — an audience's own phrasing outperforms anything this team would invent for
them, and it is the one input here that no competitor can copy.

A question asked by two people is a signal. Four is a brief; say so and put it at the
top of the report.

**Then run the live listening scan.** Read `${CLAUDE_PLUGIN_ROOT}/references/browser-listening.md` for the method
— it is short, and two details in it (use `read_page`, not `get_page_text`; open
anything above ~10K views and read the replies) are the difference between a useful
scan and an empty one.

Web search returns what was **published**. A listening scan returns what is being
**argued about**, by whom, and how loudly — plus the engagement numbers that say which
framing actually travelled. For an operator ranked on who replies rather than on
reach, that is the more valuable input, so it goes first and its findings outrank a
press release.

Write it to `research/x-scan-YYYY-MM-DD.md` alongside the trend report.

**Cross-check it against the operator's own sourcing.** If a live post cites numbers
that contradict a report the team has already built content on, stop and report that
before anything else — it may mean a scheduled piece has to be held. This is the
highest-value thing this scan does.

**If the browser tools do not load, do not retry.** A scheduled run cannot reach them
at all; that is structural, not a fault. Fall back to web search and say plainly in
the report that the live scan needs an interactive run, so the operator knows the
listening half did not happen rather than assuming it came back empty.

## Search, do not recall

Trends are current by definition. **Always use WebSearch** — never answer from
training data, and never present a remembered example as a live one. If a search
returns nothing useful, say so; a thin honest report beats a padded invented one.

Run searches along four axes, one pillar at a time:

1. **What is being discussed now** — the pillar plus "2026", plus terms like
   "why", "mistake", "actually", "stopped". Recent discussion, not evergreen SEO.
2. **Who is winning** — named creators and companies in the space. What framing do
   their most-shared recent pieces use?
3. **What questions people ask** — forum and community threads, comment sections,
   "how do I" phrasing. Real questions are the best idea source there is.
4. **What nobody is saying** — the claim everyone in the space repeats, and the
   counter-case the operator's own experience could support.

5. **What his own audience already asked** — from the comment mining, not from search.
   These outrank every other axis, because demand that has already been stated in his
   own comment section needs no guessing about whether anyone wants it.

6. **What the crowd is fighting about** — from the listening scan, not from search.
   The post that travelled, the number people are disputing, and the thing nobody in
   the thread has the standing to say. Include one deliberately adversarial query
   (`<sector> crash`, `<category> overrated`) — the criticism of a space is where the
   strongest contrarian material lives.

Fetch the actual pages for anything you intend to cite. A search snippet is a
lead, not a source.

## Judge before you record

**Weight toward what wins followers.** `brand/brand-config.md` → `## Targets` holds the
follower goals, and `performance/patterns.md` says which angles and pillars have
actually produced follows for him. Prefer ideas that serve those. Prefer them; do not
let them override the four tests below — an idea he cannot speak to does not become
postable because it might grow the account, and that trade is how an authority account
turns into a generic one.

An idea earns a row only if all four hold:

- **The operator can speak to it.** Cross-check against `## Proof` in the brand
  config. If they have no standing, the idea is for someone else.
- **It fits a pillar.** No orphan topics, however interesting.
- **It has a specific angle**, not a category. "AI agents" is not an idea. "The
  agent I built that cost me ₹4,000 in wasted API calls before I capped it" is.
- **It is not already in the bank.** Read the bank first and skip duplicates.

Kill everything else. Ten usable ideas beat forty rows the operator scrolls past.

## Write the outputs

**1. The trend report** — write to `research/trends-YYYY-MM-DD.md`:

```markdown
# Trend report — YYYY-MM-DD
pillars scanned: <list>

## What is moving
| signal | evidence (URL) | why it matters here | angle for us |
|---|---|---|---|

## What competitors are winning with
| account | recent piece | format | the move they made |
|---|---|---|---|

## Questions people are actually asking
- <question> — <where seen> — <which pillar it feeds>

## The contrarian opening
<the consensus claim, and the specific counter-case this operator could make>

## Searched and found nothing
<axes that came back empty — so the next run does not repeat them>
```

Every row carries a URL. A claim without a source does not go in the file.

**2. The idea bank** — read `library/idea-bank.md`, append new rows at status
`new` with the next sequential ids, fill the `source` column (`ig-comments`, `scan`,
`search`), and write the whole table back. Never drop existing rows.

Then write `state/comments-cursor.json` — **after** the rows land. Record posts that
were mined and yielded nothing as `captured: 0`; that is what stops the next run
re-reading them.

**3. The swipe file** — append genuinely instructive references to
`library/swipe-file.md`: the URL, the format, and one line on the structural move
worth reusing. Record the *mechanism*, not the topic — "opens on the number it
cost, then rewinds" is reusable; "post about API costs" is not.

## Report to the operator

Do not paste the whole trend report into chat. Give them:

- what his own comment section asked for, and anything asked more than twice
- the count of new ideas by pillar and by source
- the three strongest, one line each, and why those three
- the one thing you found that changes what they should do this week
- anything you could not verify

Then hand off: the ideas are ready for `hook-writer`.

## Failure modes

- **Topic mode: returning a different topic.** He named the subject. A better idea found
  on the way is an idea-bank row for another day, not today's slate.
- **Topic mode: reaching for the browser.** No comment mining, no live scan. The browser
  is needed for the render, and the subject is already decided.
- **Topic mode: ten rows instead of one.** One topic, one row.
- **Reporting trends instead of ideas.** "Short-form video is growing" is not
  actionable. Every finding must end in an angle this operator can post.
- **Citing what you remember.** Search, fetch, then cite.
- **Skipping the listening scan because search felt like enough.** Search cannot see
  engagement, replies, or a contradiction of your own sources.
- **Skipping his own comments.** It is the only source here that is his actual
  audience rather than a proxy for it, and it is the cheapest one to read.
- **Summarising a comment instead of quoting it.** The phrasing is the value.
- **Replying, liking or hearting anything while in there.** Read-only, always.
- **Treating a comment as a fact.** One person asserting a number in a comment is one
  person on the internet. Verify it like any other claim.
- **Reporting a live post as fact.** A viral claim is a lead. Trace it to the primary
  report before it becomes a row, and say so if you could not.
- **Padding to look thorough.** Fewer, better rows.
- **Ignoring the operator's own data.** `performance/patterns.md` is stronger
  evidence about this audience than any general trend.
- **Re-pitching a dead idea.** Check for `killed` rows before adding.
