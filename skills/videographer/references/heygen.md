# HeyGen — how this team renders, and why

HeyGen is the only video engine here. It produces **the operator on screen, speaking**,
from a locked avatar and a locked voice.

**Renders happen in HeyGen Studio, by a human. Not through the API.** That is a
deliberate decision, it is the single most important thing in this file, and the reason
is below. Do not "fix" it.

## Why the API does not render

The operator's voice is a **Cartesia** voice (model Sonic 3.6). It was built in HeyGen's
app and it is the only voice permitted for his avatar — see `brand/avatar-motion.md`.

**The HeyGen API cannot synthesise a Cartesia voice.**

| Evidence | Detail |
|---|---|
| HeyGen's public docs | Text-to-Speech is documented as *"synthesize catalog voices… on the **Starfish** engine"* |
| `create_speech` | States outright: the voice must support the Starfish engine |
| `voiceSettings.engine_settings` | Accepts `elevenlabs`, `fish`, `starfish`. **No `cartesia` value exists** — on `create_video_from_avatar`, `create_video_from_studio`, or anywhere else |
| Measured | Seven API renders across both of his voice ids. Same script, same speed: consistently the wrong timbre against the app render. Duration matched to ~4%; **timbre did not.** |

Passing `voiceId` gets you the right voice *identity* synthesised by the *wrong engine*.
It is close enough to pass a duration check and not close enough to be his voice. That is
the worst kind of wrong, because it looks correct in every log.

**Duration is not a proxy for timbre.** That mistake cost seven renders. Two engines can
pace within a few per cent of each other and sound like different people.

So: the team writes the script, a human renders it in Studio where Cartesia lives.

## What the API is still used for

| Tool | Use |
|---|---|
| `get_current_user` | Remaining credits, before a batch |
| `list_avatar_groups` | Verify the group still resolves (`ownership: "private"`) |
| `list_avatar_looks` | Verify `avatar_id` still resolves. The look `id` **is** the avatar id |
| `list_voices` | Verify `voice_id` still resolves (`type: "private"`, page with `token`) |
| `get_video` | Read back a finished render's URL and duration, if someone wants it recorded |

**Never call** `create_video_from_avatar`, `create_video_from_studio`, `create_speech`,
`create_video_agent`, `generate_from_template`, or any other generation tool. They all
route through Starfish TTS. A render that came out of one of them is not his voice, and
publishing it is worse than publishing nothing.

Also never: `clone_voice`, `design_voice`, `create_photo_avatar`, `create_digital_twin`,
`create_avatar_consent`. Avatars and voices are made by him, in HeyGen, on camera.

## The render spec

This is what `avatar` hands over. It goes in the piece file and into the console, and it
is what the person at the keyboard follows.

```
RENDER IN HEYGEN STUDIO
avatar:        <look name from brand/avatar-motion.md>
voice:         <voice label>
Voice Engine:  <e.g. Cartesia>      ← CHECK THE DROPDOWN BEFORE GENERATE
Model:         <e.g. Sonic 3.6>     ← CHECK THE DROPDOWN BEFORE GENERATE
Speed:         <locked value>        ← RE-SET ON EVERY SCENE
motion:        paste the custom-motion block verbatim, EVERY scene
aspect:        9:16
script:        <the approved script, verbatim - do not edit in Studio>
```

The two dropdown lines are not decoration. See below.

### Before clicking Generate — check the voice engine

**Open the Edit Voice panel and read the two dropdowns.** They must say exactly what
`brand/avatar-motion.md` records — for this account, **Voice Engine: Cartesia** and
**Model: Sonic 3.6**.

This is the single most common way a render comes out wrong. Studio will happily assign a
different engine — ElevenLabs is a frequent default — to the *same* voice. The voice name
in the panel still reads correctly, the avatar is right, the script is right, and the
output is a different person's delivery. Nothing in the render log flags it.

If the dropdowns are wrong: set them, then click **Update default settings** so the voice
keeps that engine for future scenes.

Two more Studio behaviours that bite, all app-side, none of them API:

- **Speed resets on every scene.** Re-set it on each one and confirm on the preview. A
  scene left at default is a different man talking in the middle of his own video.
- **The motion block is pasted per scene**, verbatim, not shortened for a short scene.

## Pacing — the script is the deliverable

The script is what this team actually produces, so it does the whole job.

- **English: roughly 20–23 words per 10 seconds.** A 30-second Reel is about 65–70 words.
- **Gujarati: count syllables.** 4.0–5.0 syllables per second. Budget at **4.0** against a
  hard cap — a 30-second Reel is **120 syllables**, 45 seconds is 180. Do not convert a
  word count between the languages.
- Write to the number rather than trimming afterwards.
- **Length is fixed by rewriting, never by speed.** Speed is a locked character setting.
- **Every full stop costs about 0.7s.** Short sentences read slower than they look.
- **Write for the ear.** Parentheses and colons do not survive a read — restructure
  instead. Numbers stay as digits in the script; the voice reads them.
- **No stage directions in the script.** Everything in the script field gets spoken.
  Camera notes and on-screen text cues live in the piece file.
- **No pause tags.** Pacing comes from punctuation and the scene break.
- **Open on the claim.** The first three seconds carry the hook.

⚠ The syllable rates above were measured in Studio. They are the right numbers *because*
Studio is where rendering happens. Do not re-derive them from an API render.

## Pronunciation

He code-switches — English inside a Gujarati read — and **one Gujarati voice carries
both**. Every English word is said by that voice.

**His scripts keep English in Latin script.** Place names, company names and business
terms are typed as English — `Ahmedabad`, `Kheda`, `Cushman and Wakefield`, `warehouse
space lease`, `Asset class` — with Gujarati carrying the grammar around them. Numbers are
digits. That is measured from his production scripts, not inferred.

**So pronunciation is fixed in Studio, never in the spelling.** If a term comes out wrong
in a render, add it to HeyGen's **Brand Glossary**: that changes the spoken audio and
leaves the script and captions spelled normally. Start with Shivalik, the project names,
RERA, EMI, and any place name the voice trips on.

**Do not transliterate a word into Gujarati script to force a pronunciation.** It changes
what the viewer reads as well as what they hear, and it makes the script stop looking like
something he wrote. See `skills/script-writer/references/formats.md` → *How he actually
writes it*.

## What HeyGen is not used for

| Job | Where it goes |
|---|---|
| **Reel cover** | `designer`, preset `ig-portrait` |
| **Thumbnail / video cover** | `designer`, preset `yt-thumb` |
| **Article header** | `designer`, preset `article-header` |
| **Quote card / ambient still** | `designer` |
| **On-screen text** | `designer`. Type is laid out from measured geometry, never asked of a model |
| **Atmospheric B-roll** | Filmed, not generated. Produce a shot list — one prompt-shaped line per beat with the timing it covers |

## If someone wants API rendering back

The only thing that would change this is HeyGen exposing Cartesia through the API. If
that happens the fix is small — `create_video_from_avatar` with `avatarId`, `voiceId`,
`aspectRatio: "9:16"`, the locked speed, and whatever engine parameter they add.

Until then, confirm it with HeyGen support rather than re-testing it here. The question
to ask is precise: *can a Cartesia-engine voice be synthesised through the v3 video API,
and if so with which parameter?* Seven renders already answered "not with anything
currently documented".
