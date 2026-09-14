# AI Content Team OS

Twelve skills that run one person's content pipeline end to end. One command in, nine
ready-to-post options out — three per platform — in a single artifact that holds the
content, a confidence number on each option, and nothing else.

Built for **Instagram, LinkedIn and X**, with Threads and Pulse (LinkedIn long-form)
available from the same pieces.

---

## The one command

Say **"run the content engine"**. It researches the day, then publishes one artifact:

```
INSTAGRAM   A / B / C   ·74 emerging   caption + the Reel script as text   [POST]
LINKEDIN    A / B / C   ·66 weak       full post                           [POST]
X           A / B / C   ·58 weak       full post                           [POST]
```

Nothing else is on that page — no rationale, no sources, no metrics, no labels. The
chat gets three lines:

```
SLATE 2026-09-12

⚠ the one thing that outranks the slate, if there is one

NEEDS YOU · the specific thing only you can answer
```

**It never runs on a schedule.** It runs when you run it.

## Posting

Click **POST** on the option you want — that records the pick. Then say **"post"** in
chat, and Claude opens Chrome, fills the composer with your chosen copy and submits it.

All three platforms go at once. LinkedIn and X land in seconds; Instagram takes minutes
because the Reel is rendered first. **They never wait for each other**, and one failing
never stops the other two.

The button records; the chat sends. A published web page has no route into a Claude
session, so a button that claimed to post directly from the page would be a button that
did nothing.

Nothing goes out that you did not pick, the copy is never edited on the way to the
composer, the signed-in account is checked before anything is typed, Post is clicked
once, and nothing is recorded as published without a live URL read from the page.

## The Instagram button is different, on purpose

Every Instagram option shows the full Reel script, so picking one means approving the
words. That button therefore says **POST — generates the Reel**, and clicking it:

1. sends that variant's script to HeyGen, with your locked voice, speed and motion block
2. renders at 9:16 and downloads the file
3. shows you the clip in the console
4. posts it as a Reel with **that variant's** caption when you tap once

Two things are deliberate. **The console records who pressed the button** — you decide
once who may approve wording for your avatar, commonly your social media manager, and
every click is logged against that. And **the clip is shown before it posts**, because
lip sync, teeth, hands and a render at the wrong speed are invisible in a script and the
face is yours. One tap, not another approval round.

Want it fully unattended, with no look at the clip? Say so and it can be, but that is the
one checkpoint worth its seconds.

## Setup — ten minutes, once

1. Install the plugin.
2. **Connect a folder** in the Claude desktop app. That folder is the memory — the
   plugin is just the skills, and neither works alone. A `ContentEngine` folder is
   created inside it holding your brand profile, idea bank, performance log, patterns
   and the three cursors.
3. Say **"set up my brand"**. It interviews you in three rounds and — this is the part
   that matters — asks you to paste two or three things **you have already written**.
   That is what makes the output sound like you rather than like an AI. It also takes
   your follower targets per platform. It then scaffolds the whole memory.
4. **Drop your own posts into `ContentEngine/sources/corpus/`.** This is the single
   highest-value thing you can do for output quality — it is what the team learns your
   voice from, and more of it is strictly better than any instruction you could write.
   Other people's posts go into `ContentEngine/sources/cs-scrape/` instead. Each file
   in either folder is read exactly once, ever.
5. Say **"content status"** to verify, then **"run the content engine"**.

## Ideas come from your own comment section

Before it searches anything, a run opens the comments under your own recent Instagram
posts and reads them. It keeps four things: a question asked more than once, an
objection, a correction, and an outright request — quoted in the commenter's own words,
because their phrasing is what the hook should be built from.

Everything else — praise, emoji, bots — is discarded. A question two people asked is a
signal. Four is a brief.

It is strictly read-only. Nothing is liked, hearted, replied to or deleted from your
account, and a comment is treated as a lead to verify, never as a fact.

## It learns your voice from your own posts

Drop your posts into `sources/corpus/` and the team measures them instead of guessing.
Not adjectives — numbers, per platform: median sentence length, how often you write in
first person, your exact em-dash and exclamation-mark counts, what you open on, what
you close on, the scaffolds you actually use, and your recurring vocabulary. Every line
in the profile carries the number it came from.

Two folders, and the difference matters more than it looks:

| folder | whose writing | what it teaches |
|---|---|---|
| `sources/corpus/` | **yours** | how you sound — `brand/voice-profile.md` |
| `sources/cs-scrape/` | **anyone's** | structures worth stealing — the swipe file |

A competitor's post in the corpus folder would teach the team to write like your
competitor. That is why they are separate.

**The part that actually changes the output.** The generic writing rules in
`references/voice-rules.md` are a floor built from what AI social copy gets wrong. Your
real corpus will contradict them, and the profile records every contradiction with its
measurement — so no later draft quietly "corrects" your voice back into the generic
one. Measured profile beats generic rule; only a correction you made by hand beats the
profile.

It also reads the voice and doctrine documents you put there. Where those disagree with
your actual posts, **the posts win** and the gap is written down, because a guideline
describes an aspiration and the posts describe the writer.

Two things it will not do with the corpus: treat it as performance data (your exports
carry reactions, not reach, so nothing there touches a follow rate, a median or a
confidence number), and reuse an old argument as new content.

It does feed one more thing. Your published posts become the **approved-wording bank**
for the avatar — a script assembled from lines you already put your name on clears the
consent gate in a way a draft written this morning never does.

## Targets

Set once during brand setup, reported on every readout, and **never published**:

| platform | target | tracked |
|---|---|---|
| Instagram | 10,000,000 | yes |
| X | 1,000,000 | yes |
| LinkedIn | 100,000 | yes |
| YouTube | 1,000,000 | no — nothing here posts to or measures YouTube |

They change two things. The analyst ranks every post on **follows per 1,000 reached**
rather than reach, and the researcher weights toward angles that have actually won you
followers — weights, not overrides, because an idea you cannot speak to does not become
postable just because it might grow the account.

The readout states pace as arithmetic and says plainly when the current rate does not
reach the number. A target never appears in a post, a caption or a hook, in any form,
including "on our way to" framings — a goal published as a result is the failure this
system guards hardest against.

## The confidence number

Every option on the console carries one, with an evidence label: `74 emerging`.

It is **not** a prediction of reach and it is not a recommendation. It is how much of
what the system already knows supports that particular way in — the hook's own
five-axis score, adjusted by how that angle and that pillar have actually performed for
you. Under six posts on a surface the adjustments are switched off entirely and the
number is the hook score alone; the label (`weak` / `emerging` / `established`) tells
you which you are looking at.

The three options usually land within a few points of each other. That is correct —
they share one claim, one proof and one number, so the angle is the only thing
separating them.

Once ten scored posts exist, the analyst checks whether higher confidence actually
produced a higher follow rate. If it did not, it says so and the number ships tagged
`uncalibrated` until it earns its keep. A confidence score nobody has checked against
an outcome is decoration, and decoration next to a POST button is worse than none.

Nothing is marked recommended. You still pick by reading the copy.

## Nothing is ever rescanned

Three small files under `ContentEngine/state/` are what keep a daily run cheap.

`analytics-cursor.json` holds the newest post already logged on each platform. A run
reads the platform newest-first and **stops at the first post it already has** — two or
three posts on a normal day, never the whole history. Every median, ranking and pattern
is then recomputed from the local log, which costs nothing. Posts logged in the last
seven days are re-read once more because their numbers are still moving; anything older
is settled and left alone.

`comments-cursor.json` holds, per post, the newest comment already mined. A run opens
your posts newest-first and stops at the first one it has already read — two or three
posts on a normal day. Posts from the last week are re-read once more, because comment
threads keep growing.

`ingested.json` holds a hash per file in `sources/cs-scrape/`. A file already ingested
is skipped without being opened.

Going back past a cursor happens for exactly two reasons — you ask for a full re-read,
or the log and the cursor disagree, which means a run died mid-write. Either way it
says so.

## The team

| Skill | Say this | What it does |
|---|---|---|
| **content-team** | "run the content engine" | The front door. Runs everything, returns the three parts. |
| **brand-setup** | "set up my brand" | Interviews you once, derives your real voice from your own writing, scaffolds the memory. |
| **researcher** | "find trends" | Mines your own IG comments for stated demand, then live social listening plus web research, into usable angles — not trend reports. |
| **hook-writer** | "write hooks" | Twelve openings, scored on five axes, cut to three. Never presents one. |
| **script-writer** | "write the post" | Reels, carousels, LinkedIn, X, Pulse, captions. |
| **carousel** | "make a carousel" | Typographic 1080×1350 slides on measured geometry, with a validator that rejects overflow. |
| **designer** | "design this" | Everything else visual — LinkedIn pages, X images, covers, headers. |
| **videographer** | "make the reel" | Plans the video layer and the beat plan. Routes generation to `avatar`, stills to `designer`, footage to a shot list. |
| **avatar** | "use my avatar" | The only skill that synthesises you. HeyGen, your fine-tuned avatar and voice, gated on your own authorization and your approval of the exact wording. |
| **analyst** | "did it work" | Logs numbers, names patterns with sample-size labels, refuses to rank a sample too small. |
| **publisher** | "build the console" | Calendar, captions, pre-flight, and the console — nine options, content only, a POST button each. |
| **post-runner** | "post" | Takes the option you picked and posts it, by driving Chrome. Verifies the account, submits once, and records nothing as published without a live URL. |

## What it will not do

These are deliberate, and they are what keep the account credible:

- **Never invents a number.** Anything about you comes from `brand/proof.md` or is
  written as `[NUMBER: what is needed]` and flagged.
- **Never synthesises you outside one gated skill.** Your avatar and voice are used by
  `avatar` alone, and only where you have granted it in writing and approved the exact
  wording, by you or by the approver you named.
  Every clip is recorded as synthetic, with the script it was approved against.
- **Never synthesises anyone else.** No client, partner, official or competitor, under
  any framing.
- **Never presents one hook, and never one version.** Three variants of every post - data-led, correction, observation - same claim underneath. Each carries a confidence number and its evidence label. Nothing is marked "recommended"; you choose.
- **Never publishes a target as a result.** The follower goals are goals. They are reported as pace and never reach a post.
- **Never acts inside your comment section.** It reads; it does not like, reply or delete.
- **Never posts anything you did not pick.** It posts the option you clicked, with the copy exactly as written, once — and only after you say "post".
- **Never calls a post a winner before six posts on that surface.** Three is noise.
- **Never posts on its own initiative, and never on a schedule.** You pick; you say go.
- **Never claims it scanned live social when it could not.**

## Optional connectors

All optional. The team works without every one of them, it just does less. See
`CONNECTORS.md`.

| Category | Unlocks |
|---|---|
| Browser automation | Live listening, and reading your own analytics pages |
| Video generation (HeyGen) | Presenter Reels — you on screen, in your own voice |
| Browser automation | Posting your picked option to the live account |
| Analytics | Automatic performance logging |

**Live listening works in interactive sessions only.** A scheduled run has no browser
at all — that is structural, not a setting.

## Memory

A `ContentEngine` folder inside a folder you connect, created by `brand-setup`, read by
every skill — yours to open, edit and back up:

```
brand/       brand-config · voice-profile · proof · offers · avatar-motion
library/     idea-bank · hooks · swipe-file
content/     calendar · <slug>.md per piece
performance/ log · patterns
research/    trends-YYYY-MM-DD · x-scan-YYYY-MM-DD
state/       analytics-cursor.json · comments-cursor.json · ingested.json
sources/     corpus/     ← drop YOUR posts here (voice)
             cs-scrape/  ← drop OTHER people's exports here (swipe file)
runs/        YYYY-MM-DD.md
```

`references/first-run.md` is the contract. `references/memory-map.md` is the detail.
`references/voice-corpus.md` is how your posts become a voice profile.

## Making it sound more like you

Two loops, and they compound.

**Feed the corpus.** Every post you add to `sources/corpus/` sharpens the measured
profile. It is the cheapest quality lever in the system and the only one that works
without you writing a single instruction.

**Correct the drafts.** Whenever you rewrite something the team drafted, say so. The
correction gets appended to `## Voice corrections` in your brand config, and it
outranks everything — including the measured profile. Every later draft reads it.

Voice corrections beat the measured profile, which beats what you said about yourself
at onboarding, which beats the generic rules.
