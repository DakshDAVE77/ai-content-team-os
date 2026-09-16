# The console — one artifact, content only

A published Artifact holding today's nine options: three Instagram, three LinkedIn,
three X. Same URL every run. It is the only deliverable the operator reads.

## The rule that governs the whole page

**Nothing on the page that is not the content — plus one number.** No rationale, no
"why this works", no sources, no metrics, no pillar or format labels, no strategy
notes, no run summary, no instructions, no counts, no dates beyond the one in the
header, no footer text beyond what a locked variant must say. The page is:

```
<date>

INSTAGRAM
  A   ·74 emerging   <caption>      SCRIPT: <the Reel script as text>   [POST]
  B   ·71 emerging   …
  C   ·69 emerging   …

LINKEDIN
  A   ·66 weak       <full post text>                                   [POST]
  B   …  C   …

X
  A   ·58 weak       <full post text>                                   [POST]
  B   …  C   …
```

That is the entire page. If a thing you want to add is not post copy, a Reel script,
a POST button, or the confidence chip below, it does not go on the page.

## The confidence chip — the one exception, and its limits

The operator asked for a confidence level on every option, so each variant carries one:
**the number and its evidence label, nothing else.** The formula, what it means and
what it does not mean are defined once in
`${CLAUDE_PLUGIN_ROOT}/skills/script-writer/references/variants.md` → `## Confidence`.
Read it there; never recompute it here and never invent a second scale.

This is a deliberate override of the rule above, so keep the override narrow:

- **The number and the label travel together, always.** `74 emerging`, never `74`.
  A bare number reads as a measurement, and under ten posts it is not one.
- **No bars, no meters, no colour ramps, no sorting by it.** A chip of small mono type
  set quietly beside the option. Green-to-red would make the choice for him, which is
  the thing this whole system is built not to do.
- **The three stay in A / B / C order** whatever their numbers. Ordering by confidence
  is ranking with extra steps.
- **Nothing is marked recommended**, and no copy on the page explains the number.
  If he asks what it means, that answer goes in chat.
- **A locked variant shows no chip.** It is not on offer, so it has no confidence.

A tight spread across the three is the expected result and is not to be corrected —
see `variants.md` → `### A tight spread is correct`.

- **Full text, always visible.** No accordions, no truncation, no "read more". He
  picks by reading.
- **No variant marked recommended.**
- **The Instagram Reel script is plain readable text inside the option** — beat by
  beat, spoken lines and on-screen text, nothing else. Not a download, not a link,
  not a table of production notes.

## The POST button

**The button records the pick. It does not post.** A published page has no route into
a Claude session, so it cannot drive the Chrome extension itself. What it does is
write the pick to `db`; `post-runner` reads that pick in the next chat turn and drives
the browser.

On click, write exactly one doc and flip the button to a plain "queued" state:

```
post_request/<platform>     { pieceId, variant, text, script?, angle,
                              confidence, confidenceLabel, requestedAt, status: "queued" }
```

`angle`, `confidence` and `confidenceLabel` ride along so `post-runner` can write them
straight into `performance/log.md` without reopening the piece file. That is what makes
the calibration check in `variants.md` cheap enough to actually happen.

`platform` is `instagram` | `linkedin` | `x` — one doc per platform, so a re-pick
overwrites cleanly. `text` is the final copy verbatim, so `post-runner` never has to
reconstruct it.

`post-runner` advances `status` and writes the result back. Subscribe with `onSnapshot`
and render it on the option. Once `posted`, lock that platform's three options.

| platform | ladder |
|---|---|
| LinkedIn, X | `queued` → `posting` → `posted` (with `url`) or `failed` |
| Instagram | `queued` → `generating` → `rendered` → `posting` → `posted` or `failed` |

Instagram is longer because approving an Instagram option **commissions a video of the
operator** and then posts it. See below.

**Tell him in one line, once, in chat — never on the page — that clicking POST queues
it and saying "post" sends it.** If he asks what the chip means, answer in chat too;
the page never explains itself.

## Instagram — the button commissions a video

Instagram options carry the Reel script in full, and the operator picks by reading it.
So a POST click on an Instagram option is not only a pick of a caption. It is **his
approval of the exact words his synthesised face and voice will say**, and it starts a
paid render.

That makes the Instagram button a different object from the other two, and the page has
to say so. Label it **`POST — generates the Reel`**, not `POST`. This is the second and
last exception to the content-only rule, and it exists for the same reason as the first:
a gate a human has to notice in a chat log is a gate in the weakest possible place.

**Declare the `user` capability alongside `db`, and record who clicked.** Not to gate
the render — `avatar` Gate 2 accepts the approver the operator named, commonly a social
media manager — but because a button that generates someone's likeness should leave a
record of who pressed it. Write it:

```
post_request/instagram  { pieceId, variant, text, script, angle, confidence,
                          confidenceLabel, requestedAt, requestedBy, status: "queued" }
```

`text` is that variant's caption, `script` is that variant's Reel script — **per
variant, never shared across the three.** `requestedBy` is the signed-in viewer.

`post-runner` carries `requestedBy` into the piece file. If `brand/avatar-motion.md`
records an approver identity and the click does not match it, it says so — it does not
refuse.

**What the Instagram click does depends on whether a video already exists.** The engine
asks for a video route at the top of every run, so by the time the console is built the
Reel has usually already been cut or rendered. Three cases, and the button is labelled
differently in each:

| State of the option | The click | Button |
|---|---|---|
| **A clip exists** — cut in Higgsfield, or rendered in Studio during the run | Records the pick. `post-runner` uploads the file that is already there and **starts nothing**. | **`POST`** |
| **`awaiting_render`** — the run could not render it: no script approval, or no browser | **This is Gate 2.** Show the script in full on the page, plus the render spec — avatar, voice, engine, speed, motion block, 9:16, script verbatim — with a copy action. The click approves those exact words and commissions the render. | **`POST — approves the script`** |
| **No video** — caption and cover only | Records the pick. Nothing is commissioned. | **`POST`** |

Status runs `queued → awaiting_render → rendering → rendered → posted`, and an option
that arrives with a clip simply starts further along it.

`awaiting_render` is a **waiting** state, not a progress state — nothing is running until
he clicks, so do not draw a progress bar against it. `rendering` is the one that may show
a bar, because by then a machine really is doing something.

### The rendered state

When the render lands, `post-runner` writes `status: "rendered"` with `videoUrl`, and
the option shows **the clip, playable, with one confirm control**. He watches it, taps
once, and it posts with that variant's caption.

**The clip is also delivered into the chat** with `SendUserFile` the moment it renders —
set by the operator on 16 September 2026, so the watch step reaches him wherever he is
rather than only on this page. Saying "post the video" in chat does the same thing as the
confirm control here. Both write the same doc; whichever lands first wins.

That tap is not a second approval of the copy — he already approved that. It is the
`watch every output before delivering it` rule from `avatar` and `videographer`, made
into one action instead of a chat round-trip. Lip sync, teeth, hands above the lap, a
scene that rendered at the wrong speed: none of those are visible in a script, and the
clip is his face.

Add the `downloads` capability so he can pull the file down from that state.

## Locked variants

A variant is locked — POST disabled — when:

- it carries an unresolved `[NUMBER: ...]`, `TODO` or bracketed placeholder
- it carries a **constructed first-person claim** the operator has not confirmed

A locked variant renders **without a confidence chip**. It is not an option yet, and a
number beside a disabled button invites him to want the thing he cannot have.

A locked variant shows the flagged sentence and a checkbox recording his approval of
that exact wording. Ticking it writes `approval/<pieceId>__<variant>` with a timestamp
and unlocks POST. This is the script-writer's marker and the avatar skill's Gate 2 made
physical: previously a human had to notice a flag in a chat log, which is the weakest
place to put a gate. This is the only explanatory text the page is allowed to carry,
and it appears only on a locked variant.

## Building it

Declare `capabilities: {db: {}, user: {}}`. `user` is not optional once an Instagram
option can commission a render — it is what keeps `avatar` Gate 2 standing on a page a
content manager can open. Add `downloads` to hand over the rendered Reel or a cover.

Split the two kinds of data:

| | lives in | why |
|---|---|---|
| **The copy** — options, captions, scripts | the page itself, as a JS constant | It renders even when `db` is unavailable, and the publisher republishes every run anyway. A console showing nothing because storage failed is worse than useless. |
| **The state** — picks, approvals, post results | `db` | It must survive a republish and be readable from a later session with `read_db`. |

Keep state docs flat, one fact per doc, so a stale write cannot clobber a good one.
`db` is last-writer-wins with no transactions: never bundle unrelated facts into one
doc and never retry a failed write — the next click writes again.

**Handle `claude.use("db")` returning `null`.** Render the whole page, disable the POST
buttons, and carry on. Never block the first paint on storage.

Follow the design tokens in `brand/brand-config.md`. Editorial, black on white,
emphasis by weight, generous space. He will look at this more than anything else the
team makes, so it should read like a page of type, not like a dashboard.

## Reading it back

From a later session, `read_db` on `post_request/*`, `approval/*` and `posted/*` gives
the whole state of the slate without re-reading the page. That is how `post-runner`
starts and how the analyst learns which angle he keeps choosing — the single most
useful thing this system learns about him.
