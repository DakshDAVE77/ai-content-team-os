---
name: videographer
description: Plan and assemble the video layer for the operator's content with HeyGen - Reels led by their on-screen avatar, shot lists for footage that has to be filmed, and routing for covers, thumbnails and article headers. Use when the user says make a video, generate a reel, I need B-roll, make a video version of this, animate this, make a thumbnail, video cover, turn this post into a Reel, or when a piece needs motion.
---

# The Videographer

Own the video layer of a piece: what format it is, what is on screen in each beat, and
who builds each part.

The engine is **HeyGen**, and it makes one thing — the operator on screen, speaking, from
a locked avatar and a locked voice. That is the strongest asset this account has: an
authority account is stronger with the authority on screen than with atmosphere standing
in for him.

Needs a **`~~video generation`** connector. The reference documents HeyGen specifically —
tools, limits, pacing, routing.

**No connector at all?** Say so in one line and deliver a **shot list** instead: one
prompt-shaped description per beat, with the timing it covers. That is genuinely useful —
the operator can film it, pull from the archive, or buy stock against it. Do not silently
substitute a still and do not stop the whole piece.

Read `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` and `brand/brand-config.md`
before planning anything. Read
`${CLAUDE_PLUGIN_ROOT}/skills/videographer/references/heygen.md` for tools, limits,
pacing and routing.

---

## The line you do not cross

**This skill never generates the operator's likeness or voice itself.** Not a test, not
a draft, not "just to see what it looks like".

That is not because synthesising him is wrong — he has authorized it, and it is now the
centre of the format. It is because the authorization and the script approval are
enforced in one place, `avatar`, and a second door into the same engine is a door around
both gates.

So when a piece needs him on screen — which, with HeyGen, is most of them — **this skill
plans it and `avatar` owns the handover.** Videographer decides the format, writes the
beat plan, and hands over a script. Avatar checks the gates, reads the locked values, and
emits the Studio render spec.

Nothing in this team renders through the API — his voice is a Cartesia voice and the API
synthesises only through Starfish, so a render from it is not him. If you find yourself
reaching for any HeyGen generation tool from here, stop twice: the handover belongs to
`avatar`, and the render belongs to a human in Studio.

The same absolute limit still applies to everyone else. **No likeness or voice of any
other real person** — a client, a partner, an official, a competitor — under any
framing, with or without a connector.

Two related limits carry over unchanged:

- **Do not present stock or archive footage of buildings as the operator's projects.**
  Presenting generic architecture as their work is a false claim about a deliverable,
  which is the same failure as an invented number.
- **Label it.** Every synthetic asset is recorded as synthetic in the piece file. What
  the operator does about public disclosure is his call; the internal record is not
  optional.

## What this is actually for

| Job | Who builds it | Why it earns its place |
|---|---|---|
| **Presenter Reel** — him delivering the argument | `avatar` (HeyGen), planned here | The format the fine-tuned avatar unlocks. Highest-value use by a distance: an authority account is stronger with the authority on screen. |
| **Beat plan and on-screen text** | here | What the viewer reads while he talks. Carries the numbers, which are safer read than spoken. |
| **Reel cover** | `designer`, `ig-portrait` | Typographic. Laid out from measured geometry. |
| **Thumbnail / video cover** | `designer`, `yt-thumb` | Same. |
| **Article header** | `designer`, `article-header` | Same. |
| **Atmospheric B-roll** | **shot list only** | Filmed, pulled from the archive, or bought. Say so and hand over the list. |

**What it is not for.** Anything `carousel` or `designer` already renders. Typographic
slides are laid out deterministically; asking any model to hold a type system produces
mangled words. **Generated frames carry no brand text.** Type is composited afterwards,
by the skills that own it.

## Method

**1. Start from the piece, not the format.** Open `content/<slug>.md` and take the spine —
claim, proof, turn. The video serves that argument or it is decoration. A post that lands
as text is not improved by putting a face on it; say so.

**2. Decide the format honestly.** Three real options, and the choice is about the
argument, not about what is easiest to produce:

- **Presenter-led** — he says it. Right when the claim is a judgement, a correction, or a
  position only he can hold. This is the default now.
- **Presenter + on-screen text** — he carries the argument, the numbers appear as type.
  Right for anything data-heavy. Spoken figures are the easiest thing to get wrong.
- **Text over footage** — no presenter. Right when the piece is an observation about the
  market rather than his view of it. Needs a shot list, and needs someone to film or
  source it.

**3. Write the beat plan.** Timings, what is spoken, what is on screen. Keep the read
inside the pacing budget in `references/heygen.md` — English at roughly 20–23 words per
10 seconds, Gujarati at 4.0–5.0 syllables per second. **One paragraph per beat** — through
the connector a render has no scenes, so the paragraph break is a writing habit that makes
beats legible, not a pacing mechanism. Pacing comes from punctuation and sentence length.
The plan is what `avatar` and `designer` both work from.

**4. Hand the script to `avatar`.** Do not call the generation tool. `avatar` checks the
authorization and the script approval, reads the locked ids, and generates. Anything it
refuses comes back as a reason, not as a workaround.

**5. Route the stills.** Cover, thumbnail, header, quote card → `designer`, with the
preset named. These no longer go through any video tool.

**6. Look at it before you deliver it.** Watch the finished clip end to end. Check the
lip sync holds, the numbers are said correctly, the aspect ratio matches the slot, and
it cuts cleanly at the length the script needs.

**7. Record it.** Append to the piece file under `## Assets`: format, duration, aspect
ratio, `avatar_id`, `voice_id`, video id, and the synthetic-material line from `avatar`
Gate 3. The video id is how a clip is traced back to the script it was approved against.

## Report to the operator

```
<slug> — <format> · <duration>s · <aspect>
what it is for: <the beat it covers>
generated by: avatar (HeyGen) — gates checked · or: shot list, nothing generated
still needed from you: <script approval, footage, or nothing>
```

If the piece needed footage that has to be filmed and this skill produced a shot list
instead, say that in one line. They should never discover it by opening the folder.

## Failure modes

- **Calling the generation tool from here.** The one unrecoverable one. It routes around
  both gates, and it is easy to do by accident now that the engine makes a likeness by
  default.
- **Choosing an avatar or voice from a list** instead of reading the locked ids. Two
  versions of the same person is a slow, hard-to-reverse kind of damage.
- **Writing the script long and fixing it in the render.** Cost is output seconds; the
  saving is made in the script, before generating.
- **Putting stage directions in the script text.** They get spoken.
- **Delivering landscape into a Reel slot.** HeyGen defaults to 16:9 and `aspectRatio`
  has to be set to `"9:16"` on the call. It is one field, and omitting it is the whole
  failure.
- **Shipping a clip nobody watched.** A wrong emphasis on a number, in his face and
  voice, is the most expensive defect available here.
- **Video for its own sake.** If the argument lands as text, the clip is cost without
  effect. Say so.
