---
name: avatar
description: Produce on-screen presenter video and cloned-voice narration of the operator themselves, from their own footage and voice recordings. Use when the user says make the avatar, use CS Sir's avatar, put him in this video, his voice, AI avatar, talking head of him, presenter video, or wants a piece delivered in the operator's own face or voice rather than as B-roll.
---

# The Avatar

Generate video and audio of **the operator themselves** — their face on screen, their
voice speaking — from the avatar and voice already built and fine-tuned in **HeyGen**.

This is the one skill in this team that produces a real, named person's likeness and
voice. It is a legitimate and ordinary thing for a company to do with its own founder,
and it is also the capability that produces deepfakes. The difference is entirely consent
and control, so both are enforced here rather than assumed.

**It renders — by driving HeyGen Studio in Chrome, through Generate.** Not through the
API. The API cannot synthesise his Cartesia voice, so the render happens in the app, with
Claude at the keyboard following
`${CLAUDE_PLUGIN_ROOT}/skills/post-runner/references/heygen-studio.md` step by step.
That reference is owned by this skill; `post-runner` reuses it when a console click
commissions a Reel later.

The render spec is still written, every time, into the piece file and the console. It is
not a leftover from when a human rendered: it is the checklist Claude follows at the
keyboard and the record of what the run was supposed to produce.

Two things about the HeyGen setup change the shape of this job, and both cut the same
way:

- **The likeness and the voice already exist**, built inside HeyGen's own product, which
  requires the person being cloned to record a consent statement first. Nothing here
  creates them — this skill only *uses* them. The hardest consent question was answered
  upstream, by him, on camera. The connector *can* clone a voice and mint a consent
  record; this team does neither, and that is a rule here rather than a missing tool.
- **The script is the payload.** HeyGen takes text and speaks it. There is no prompt
  standing between the approved wording and what comes out of his mouth, which makes
  Gate 2 below the whole of the job rather than a precaution around it. It also means the
  script is this skill's actual deliverable — get it right and the render is mechanical.

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
displayed the full script verbatim on the page, and the button said it approves the
script. Then the click is a better record than any chat log — someone read those exact
words and pressed the button beside them, with a timestamp.

Record `requestedBy` on every click. If an approver identity is recorded in
`brand/avatar-motion.md`, check the click against it; if none is recorded, any signed-in
viewer's click counts and the identity is captured for the audit trail. **Do not refuse on
identity alone.**

### 🔴 Gate 2 sits after the render, not before it — set 16 September 2026

The operator's own instruction, verbatim:

> *"when I click post for the instagram reel script for the AI avatar video it should
> directly generate the video and do not stop at anything else and then show the video
> here in chat and then if the user says that post the video it should be posted to the
> respected instagram channels."*

So: **a POST click, or picking the avatar route at the top of a run, is the go-ahead.
Render immediately. Do not pause to paste the script and wait for a second yes.**

**The gate did not disappear; it moved to the far side of the render.** Nothing reaches a
live account until he has watched the finished clip and said to post it. A render is
billed and it is his face — but it is private, it is reversible, and it can be re-run. A
post is none of those. The human read therefore happens on the clip, which is a better
artefact to judge than a script: lip sync, hands, mouth and pace are not visible in text
at all.

The sequence is:

```
route chosen, or POST clicked  →  render  →  SendUserFile the clip into chat  →  stop
                                                                                  ↓
                                        he says "post the video"  →  upload  →  URL
```

What still binds **before** Generate, every time, is the **refusal list** below. Those
are about what the words say, not about who has read them, and no click waives them. A
script that trips one of them does not get rendered and he is told which.

Quote the script in the piece file with the date, the render id and who clicked. If he
says the clip is wrong, re-drive Studio once against the cause he names.

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
| **Presenter Reel** — him on screen delivering the argument | An approved script and a render spec, then Studio driven in Chrome through Generate. The default format. |
| **Presenter segment** — a talking-head beat inside a longer piece | Same, cut to the beat's length. Length is set by rewriting the script, never by stretching. |
| **Voice-forward piece** — his voice carrying stills or type | Same; the face is dropped in the edit afterwards. |

**It renders in the app, never through the API.** The API's text-to-speech is
Starfish-only and produces the right voice *identity* in the wrong engine — close enough
to pass a duration check, not close enough to be him. Studio is the only place his
Cartesia voice exists, which is why the render is a browser job rather than a tool call.
See `${CLAUDE_PLUGIN_ROOT}/skills/videographer/references/heygen.md` → *Why the API does
not render*. That is settled; do not re-litigate it with another test render.

**No `~~browser` connector → no render.** Say so in one line, leave the piece
`awaiting_render` with the spec visible, and do not substitute an API call to produce
something. A clip in the wrong voice is worse than no clip.

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

1. **Check both gates.** Consent basis, then approved script. Neither is a formality.
2. **Read the locked values, do not choose any of them.** Avatar, voice, engine, speed
   and the verbatim motion block all come from `brand/avatar-motion.md`. Every run. The
   discovery tools exist to verify an id still resolves, not to pick one. An account can
   hold several versions of the same person; choosing whichever sorted first is how his
   account starts looking and sounding like two slightly different men. If a recorded id
   stops resolving, stop and say so — never substitute the nearest match.
3. **Write the script to be spoken.** Everything in the script field gets said aloud, so
   no stage directions, and numbers in words. English at 20–23 words per 10 seconds,
   Gujarati at 4.0 syllables per second against a hard cap. Cut to length *before* it
   reaches Studio — rendering is billed by output seconds and re-rendering to fix a line
   is the expensive mistake.
4. **Emit the render spec**, exactly as laid out in
   `${CLAUDE_PLUGIN_ROOT}/skills/videographer/references/heygen.md` → *The render spec*:
   avatar, voice, engine, model, speed, motion block, 9:16, and the script verbatim. Put
   it in the piece file and in the console **before** opening the browser. It is the
   checklist you are about to follow, and the record of what this run intended.
5. **Drive Studio in Chrome**, following
   `${CLAUDE_PLUGIN_ROOT}/skills/post-runner/references/heygen-studio.md` step by step.
   Read the page before each click; stop rather than guess if a control has moved. The
   three steps that decide whether it comes back as him:

   - **Voice Engine: Cartesia, Model: Sonic 3.6.** Set both dropdowns, every render.
     Studio will happily assign ElevenLabs to the same voice — the name still reads
     correctly and the output is a different man, with nothing in the log to flag it.
   - **Speed resets on every scene.** Re-set it on each one and confirm on the preview.
   - **The motion block is pasted verbatim on every scene**, never shortened for a short
     one.

   Then 9:16, preview each scene, **mute any browser-tab audio** — and **click Generate
   once.** Renders take minutes — read the page for completion rather than re-clicking.
   Every click bills output seconds.
6. **Send it to him and let him watch it.** Download the finished file and deliver it
   with `SendUserFile`, captioned with the piece id, the variant and the duration. Confirm
   9:16 from the file. Then stop — the clip is the deliverable of this skill, and the
   decision to publish is a separate word from him.

   **Look at it yourself first, and say what you saw in one line — do not hold it back.**
   Lip sync drift, a wrong emphasis, a number said incorrectly, blink cadence, hands above
   the lap, a scene at the wrong speed, and above all the mouth: the target is closed lip,
   lips together at rest, a soft closed-mouth smile on a warm line, and a faint tooth line
   for about a second mid-scene is fine. A tooth row held across a phrase, a grin, or teeth
   on an opening or closing frame is worth naming with roughly the second it happens.

   **Name it; he decides.** Withholding a finished clip he asked for, to protect him from
   a defect he can see in three seconds of watching, is the failure mode this step was
   rewritten to remove. If he wants it re-rendered, fix the named cause — a motion block
   that lost its mouth lines, an expression tag that reverted, `More expressive motion`
   left on, a script with an exclamation mark in it — and drive Studio once more.
7. **Record it** per Gate 3, with the HeyGen video id, so any clip traces back to the
   script it was approved against. `get_video` will give you the id, URL and duration.

## Never

- Generate an avatar or voice that is not the operator's own.
- Choose a voice, engine or speed instead of reading `brand/avatar-motion.md`.
- **Click Generate twice for the same piece** because the first looked slow. Read the
  page. Each click bills output seconds.
- **Publish on an assumed yes.** A render is not a post. Nothing reaches a live account
  until he has watched the clip and said to post it. Silence after a clip is sent is not
  that word.
- **Stop an approved render to ask a question.** A POST click, or the avatar route chosen
  at the top of a run, is the go-ahead. Render, send, then raise anything you noticed in
  the line that carries the file.
- **Click Generate before reading the Voice Engine dropdown.** The least visible and most
  expensive mistake available here.
- **Render through the API.** `create_video_from_avatar`, `create_video_from_studio`,
  `create_speech`, `generate_from_template`, `create_video_agent` — all of them synthesise
  through Starfish, not his Cartesia voice. A clip from any of them is not him.
- **Substitute a different voice because the right one is inconvenient.** The voice named
  in `brand/avatar-motion.md` is compulsory. If it cannot be used, the answer is that the
  Reel is not rendered yet — not that it is rendered differently.
- Shorten, summarise or reword the motion block because the script is short.
- **Turn `More expressive motion` on, or reach for an Enthusiastic, Excited, Happy,
  Joyful, Laughing, Playful or Energetic expression tag** because the script is upbeat.
  The script gets calmer; the face does not get more expressive.
- **Upload a clip with teeth held across a phrase, a grin, or teeth on an opening or
  closing frame without saying so** — including "just this once because the post is time
  sensitive". Send it, name the defect and the second it lands on, and let him choose
  between posting it and a re-render.
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
