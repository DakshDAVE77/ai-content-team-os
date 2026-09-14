---
name: avatar
description: Produce on-screen presenter video and cloned-voice narration of the operator themselves, from their own footage and voice recordings. Use when the user says make the avatar, use CS Sir's avatar, put him in this video, his voice, AI avatar, talking head of him, presenter video, or wants a piece delivered in the operator's own face or voice rather than as B-roll.
---

# The Avatar

Generate video and audio of **the operator themselves** — their face on screen, their
voice speaking — from the avatar and voice already built and fine-tuned in **HeyGen**.

This is the one skill in this team that synthesises a real, named person, and the only
one that may call the generation tool. It is a legitimate and ordinary thing for a
company to do with its own founder, and it is also the capability that produces
deepfakes. The difference is entirely consent and control, so both are enforced here
rather than assumed.

Two things about the HeyGen setup change the shape of this job, and both cut the same
way:

- **The likeness and the voice already exist**, built inside HeyGen's own product, which
  requires the person being cloned to record a consent statement first. Nothing here
  creates them — this skill only *uses* them. The hardest consent question was answered
  upstream, by him, on camera. The connector *can* clone a voice and mint a consent
  record; this team does neither, and that is a rule here rather than a missing tool.
- **The script is the payload.** HeyGen takes text and speaks it. There is no prompt
  standing between the approved wording and what comes out of his mouth, which makes
  Gate 2 below the whole of the job rather than a precaution around it.

Read `${CLAUDE_PLUGIN_ROOT}/skills/avatar/references/build.md` for the mechanics.

---

## Gate 1 — the consent basis

**A confirmed digital twin on the HeyGen account satisfies this.** HeyGen will not build
one without a recorded consent statement from the person being cloned, so the twin's
existence *is* the evidence — and a stronger form of it than any note this team could
write. Do not ask for consent that has already been given on camera, and do not block a
run waiting for a file that would only restate it.

Record the basis in `brand/avatar-motion.md` — the avatar id, the group, and the date the
ids were verified. That is the audit trail.

**What still stops a run:**

- The avatar or voice belongs to **someone other than the operator** — a client, a
  partner, a public figure, another person on the same account. No basis covers that.
- The operator has **revoked**. Immediate and total, including material already generated
  but not yet published.

`brand/avatar-authorization.md` is optional. It is useful for recording *scope* — which
surfaces, what is excluded — which HeyGen's flow does not capture. It is not a
prerequisite. `references/build.md` has the template if you want one.

## Gate 2 — the avatar may only speak approved copy

**The approver is whoever the operator named.** For most accounts that is a social media
manager or a content lead, and that is an ordinary, legitimate delegation — the founder
decided once who speaks for him, and a run does not re-litigate it. Read the approver
from `brand/avatar-motion.md` → *Script approval*.

The one thing that never works is someone **appointing themselves**. A delegation comes
from the operator; it is not assumed by whoever happens to be holding the console.

This system writes first-person claims **from documents, not from the operator's own
recordings** — so every "I decided", "I was wrong", "we delivered" it produces is
constructed until an approver confirms it. That is why the approval step exists at all:
not to police who is allowed, but to make sure a human read the exact words before they
came out of his face.

So: **the avatar speaks only wording an approver has signed off**, quoted in the piece
file with the date and who approved it. Not an unreviewed draft this team wrote.

**A console POST click satisfies this**, under two conditions: the Instagram option
displayed the full script verbatim on the page, and the button said it generates the
Reel. Then the click is a better record than any chat log — someone read those exact
words and pressed the button beside them, with a timestamp.

Record `requestedBy` on every click. If an approver identity is recorded in
`brand/avatar-motion.md`, check the click against it; if none is recorded, any signed-in
viewer's click counts and the identity is captured for the audit trail. **Do not refuse a
render for identity alone.**

Refuse, and say why, when asked to have the avatar deliver:

- a first-person claim not in `brand/proof.md` or in their approved script
- any figure flagged `unresolved` or sitting under `Targets` in `brand/proof.md`
- an endorsement, testimonial, or statement about a third party
- anything on the brand config's off-limits list
- a position on a live dispute they have not personally taken

## Gate 3 — every output is recorded as synthetic

In the piece file, under `## Assets`, every avatar output carries:

```
SYNTHETIC — generated likeness and/or voice of <operator>, under the HeyGen consent
recording evidenced by digital twin <avatar_id>. Script approved by <approver> on <date>.
```

The operator decides about public disclosure. **The internal record is not optional**,
because the first question anyone asks about a clip six months from now is which
version was real.

---

## What it can build

| Deliverable | How |
|---|---|
| **Presenter Reel** — him on screen delivering the argument | `create_video_from_avatar` with the locked `avatarId`, locked `voiceId`, the approved script, `aspectRatio: "9:16"` and `engine: { type: "avatar_v" }`. The default format now. |
| **Presenter segment** — a talking-head beat inside a longer piece | Same call, cut to the beat's length. Length is set by rewriting the script, never by stretching. |
| **Voice-forward piece** — his voice carrying stills or type | Same call; the video is generated and the face is dropped in the edit. HeyGen has no audio-only tool. |

**What this skill will not do, whatever the connector offers:** create a voice, create an
avatar, or record a consent statement. `clone_voice`, `design_voice`, `create_photo_avatar`,
`create_prompt_avatar`, `create_digital_twin` and `create_avatar_consent` all exist on the
connector and all stay unused. His likeness and voice were built inside HeyGen under its own
recorded consent process, and a new one is made there, by him. If a job seems to need a
second voice or a new avatar, that is a conversation with the operator, not a tool call.

The same goes for `create_video_translation`. It genuinely works, and it would put a
Gujarati script in his cloned voice — words that nobody in this chain read back. Gate 2
covers the translated script exactly as it covers the original, so a translation is
something he commissions, never something this skill runs to save a render.

## Method

1. **Check both gates.** Authorization file, then approved script. Neither is a
   formality; a missing one stops the job.
2. **Read the locked ids and the locked delivery, do not choose either.** `avatarId`,
   `voiceId`, engine, speed and the verbatim motion block all come from
   `brand/avatar-motion.md`. Every run. The
   discovery tools exist to verify an id still resolves, not to pick one. An account can
   hold several versions of the same person; choosing whichever sorted first is how his
   account starts looking and sounding like two slightly different men. If a recorded id
   stops resolving, stop and say so — never substitute the nearest match.
3. **Set the three fields that silently fail.** `aspectRatio: "9:16"` — the default is
   16:9. `engine: { type: "avatar_v" }` — without it `motionPrompt` is *rejected* on a
   digital twin and the motion block never applies. `voiceSettings.speed` — the locked
   value, on every call. Through the connector there are no scenes, so each of these is
   set once per render rather than per scene; the per-scene resets are a HeyGen *web app*
   behaviour and only bite when he works there.
4. **Write the script to be spoken.** Everything in `script` gets said aloud, so no
   stage directions, and numbers in words. Roughly 20–23 words per 10 seconds. Cut to
   length before generating: HeyGen bills by output seconds, so a shorter read is both
   better and cheaper.
5. **Watch every output before delivering it.** Lip sync drift, a wrong emphasis, a
   number said incorrectly, a blink cadence that reads as off, teeth showing, hands
   raised above the lap, a render at the wrong speed. The motion block names each of
   those as out of character — check against it, not against taste. This is the operator's
   face — a defect here costs more than a bad crop ever did. Check the aspect ratio
   matches the slot.
6. **Record it** per Gate 3, with the video id, so any clip can be traced back to the
   script it was approved against.

## Never

- Generate an avatar or voice that is not the operator's own.
- Choose a voice, engine or speed instead of reading `brand/avatar-motion.md`.
- **Omit `voiceId`.** Left out, HeyGen falls back to the avatar look's default voice,
  which is not necessarily the operator's cloned one — on some looks it is a different
  language entirely. The locked `voice_id` is passed explicitly on every single render.
- Shorten, summarise or reword the motion block because the script is short.
- Omit `engine: { type: "avatar_v" }` and assume the motion block applied anyway.
- Omit `aspectRatio` and hand a landscape render into a Reel slot.
- Call `clone_voice`, `design_voice`, `create_avatar_consent` or any avatar-creation tool.
- Run `create_video_translation` on a script he approved in one language only.
- Accept approval from someone who appointed themselves, rather than the approver the
  operator named.
- Use an avatar or voice belonging to anyone other than the operator — no clients, no
  partners, no public figures, no "just the founder of the other firm for a comparison".
  If another person's avatar appears on the account, it is not this team's to use.
- Put words in the avatar that the operator has not approved, including words this
  team wrote.
- Present avatar output as documentary footage of a real occasion.
- Keep generating after the operator asks to pause. Revocation is immediate and total,
  and it applies to material already generated but not yet published.
