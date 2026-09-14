# HeyGen — tools, limits, routing

HeyGen is the only video engine in this team. Its job here is **the operator on screen,
speaking**, from a locked avatar, a locked voice, and a script.

The connector exposes far more than that. Everything below is about the narrow slice
this team uses and the deliberate reasons the rest stays unused.

## The tools

Tool names below are the **official HeyGen connector**. They are deferred — load them in
one call. The server prefix depends on how the connector was installed, so read it off
your own tool list rather than assuming; the base names are stable.

| Tool | Does |
|---|---|
| `get_current_user` | Profile, **remaining credits**, billing. Call before a run. |
| `list_avatar_groups` | Avatar groups on the account. Pass `ownership: "private"` for the operator's own. |
| `list_avatar_looks` | Looks inside a group. **The look `id` is the `avatarId` you pass when generating.** Filter with `groupId`, `avatarType: "digital_twin"`, `ownership: "private"`. |
| `list_voices` | Voices. Pass **`type: "private"`** for cloned voices, `limit` up to 100, and page with `token`. |
| `create_video_from_avatar` | avatar + script + voice → a render job. Returns `video_id`. |
| `get_video` | Status and details for one `videoId`. Poll this in an unattended chain. |
| `show_video` | Inline self-updating player for one `videoId`. Use in an interactive session instead of polling. |

**If you are reading an older version of this file that named `generate_avatar_video`,
`get_avatar_video_status`, `get_avatar_groups`, `get_avatars_in_avatar_group`,
`get_voices` or `get_remaining_credits` — those belong to the legacy community MCP server
and none of them exist on this connector.** The table above is the current set.

### Tools this team does not call, and why

The connector also exposes voice cloning (`clone_voice`, `design_voice`), avatar creation
(`create_photo_avatar`, `create_prompt_avatar`, `create_digital_twin`), consent
(`create_avatar_consent`), translation, lipsync, templates, clipping and a Video Agent.

**The absence of a cloning tool used to be the gate. It is not absent any more, so the
gate is now a rule.** No skill in this team creates an avatar, creates a voice, or
records a consent statement through a tool call. Those happen inside HeyGen's own
product, by the operator, on camera. A tool that *can* clone a voice does not make it
this team's job to clone one — see `skills/avatar/SKILL.md` Gate 1.

Two of the unused ones are worth knowing exist, because a job may genuinely call for them
and the answer is *ask him*, not *route around it*:

| Tool | When it comes up | Answer |
|---|---|---|
| `create_video_translation` | An English Reel wanted in Gujarati | A real capability — it clones his voice into the target language. **Never run unattended**: it produces him saying words nobody approved, in a language nobody in the chain read back. Gate 2 applies to the translated script. Raise it with him. |
| `create_brand_glossary` | A brand name mispronounced in the Gujarati read | Genuinely the right fix — see *Pronunciation* below. Safe; no likeness implications. |

Everything else stays off. That is scope, not a capability ceiling.

## The ids are locked, not chosen

`brand/avatar-motion.md` records `avatar_id`, `group_id`, `voice_id`, speed and the
motion block — everything the call needs, in one file. **Read them from there every run.
Never pick from a list.**

The connector's own tool description says the same thing: never invent, infer, replace or
silently substitute an avatar ID. Discovery tools are for the first setup and for
verifying an id still resolves — not for choosing. An account can hold several versions
of the same person, and picking a different one because it sorted first is how a founder's
account starts looking and sounding like two slightly different people. If a recorded id
no longer resolves, stop and say so; do not substitute the nearest match.

**His cloned voice is findable.** `list_voices` with `type: "private"` returns cloned
voices, and `token` pages past any single page. The old "first 100 only, go read it off
the dashboard" advice was a limit of the legacy server and no longer applies.

## Cost

`get_current_user` before a run — it carries the remaining credit balance. HeyGen bills by
**output duration in seconds**, so the lever is script length, not model choice. A
40-second Reel costs roughly twice a 20-second one.

The saving is made in the **script**, before anything is generated: cut the read to the
shortest version that still lands the argument, then generate once. Regenerating a
45-second take three times to fix a line is the expensive mistake.

## The call

```
create_video_from_avatar(
  avatarId:      <locked, from brand/avatar-motion.md>
  voiceId:       <locked, from brand/avatar-motion.md>
  script:        <the approved text, verbatim>
  aspectRatio:   "9:16"                      # Reels. The default is 16:9.
  engine:        { type: "avatar_v" }        # required for motionPrompt on a digital twin
  motionPrompt:  <the verbatim block from brand/avatar-motion.md>
  voiceSettings: { speed: <locked> }         # speed is clamped 0.5-1.5
  brandGlossaryId: <if one exists>
  title:         "<slug> - <variant>"
  caption:       { file_format: "srt" }      # optional; returns subtitle_url
)
```

Four things in there are the ones actually got wrong in practice:

1. **`aspectRatio: "9:16"`.** The default is 16:9. **This is now settled — set the field
   and no cropping is needed.** A Reel that comes back landscape means the field was
   omitted. `4:5`, `1:1`, `5:4` and `auto` are also available if a slot needs them.
2. **`engine: { type: "avatar_v" }` is required to use `motionPrompt` on a digital twin.**
   On the default Avatar IV engine, `motionPrompt` is **rejected** for video avatars, so
   the motion block never applies. If the operator's look is a `photo_avatar` instead,
   `motionPrompt` works on either engine. Check `supported_api_engines` on the look
   before assuming `avatar_v` is available.
3. **`voiceSettings.speed` is a request field**, clamped 0.5–1.5. Pass the locked value on
   every call. See *Scenes* below for why this used to be harder.
4. **`voiceId` is optional but never omitted here.** Left out, it falls back to the
   avatar's default voice — which is not necessarily his cloned one.

## Scenes — an app problem, not an API one

The HeyGen **web app** breaks a video into scenes, and there the speed resets on every
scene and the motion block has to be pasted into each one. That is where the avatar was
built and it is a real trap when the operator works there.

**Through this connector there are no scenes.** One call takes one script, one speed and
one motion prompt, and they apply to the whole render. Do not split a script into scenes
to control pacing — pacing comes from punctuation and sentence length, as below.

The old rule "one paragraph per scene" survives only as a writing habit: paragraph breaks
read as beats. It is not a mechanism any more.

## Limits worth knowing

- **Script cap:** 5,000 characters per avatar video.
- **Max output:** 30 minutes. Irrelevant here — see pacing below.
- **Concurrency:** 10 jobs in flight.
- **Rate limits** apply to every endpoint; a 429 means wait, not fail.
- **Resolution:** Avatar IV and Avatar V render the avatar at up to 1080p. Fine for Reels.
  `resolution: "4k"` composites onto a 4K canvas rather than rendering natively — not
  worth the seconds here.

## Pacing — the script is the prompt

There is no prompt recipe here. The text **is** the input, so the script does the work
that a prompt used to.

- **English: roughly 20–23 words per 10 seconds.** A 30-second Reel is about 65–70 words.
- **Gujarati: count syllables.** Measured at Speed 0.9: 188 syllables ran 38–47 seconds,
  so **4.0–5.0 syllables per second**. Budget at **4.0** when there is a hard cap — a
  30-second Reel is **120 syllables**, 45 seconds is 180. Do not convert a word count
  between the languages; they do not map.
- Write to the number rather than trimming afterwards.
- **Length is fixed by rewriting, never by speed.** `voiceSettings.speed` is a locked
  character setting, not a length dial. Moving it to fit a script changes who he sounds
  like.
- **Every full stop costs about 0.7s.** Short punchy sentences are slower than they look
  on the page. Budget them.
- **Write for the ear.** Numbers spoken aloud need their unit ("thirty-seven per cent
  empty", not "37%"). Parentheses, em-dashes and colons do not survive a read — restructure
  the sentence instead.
- **No stage directions in `script`.** Everything in that field gets said aloud. Camera
  notes, on-screen text cues and B-roll notes live in the piece file. Motion direction
  goes in `motionPrompt`, which is a separate field and is not spoken.
- **No pause tags.** Pacing comes from punctuation.
- **Open on the claim.** The first three seconds carry the hook, and a synthetic presenter
  has less grace than a real one — a slow open loses the viewer before the face earns any
  trust.

## Pronunciation — the glossary is the code-switching mechanism

Where the operator code-switches — English words inside a Gujarati read, which is how most
Indian-language business content actually sounds — **one voice carries both languages.**
There is no second English voice, no language switch mid-render, and if the voice reports
`support_locale: false` there is no accent hint either. Every English word is said by the
Gujarati voice reading whatever sits in `script`.

So the mispronunciation is not an edge case to patch later. It is every recurring brand
name, project name and business term, in every single Reel, until the glossary exists. A
mangled brand name in his own voice is not a typo.

Two fixes, and the first is better:

1. **`create_brand_glossary`** once, with every brand name, place name and English
   loanword that recurs, each mapped to a respelling. Pass the returned id as
   `brandGlossaryId` on every `create_video_from_avatar` call. **Pronunciation affects the
   generated audio only** — captions and subtitles keep the original spelling, which is
   exactly what you want. Record the glossary id in `brand/avatar-motion.md` next to the
   voice id.
2. **Transliterate into Gujarati script inside the script text.** The fallback when no
   glossary exists. It works, but it also changes what the SRT says.

## Sequence

```
get_current_user                      -> check credits
create_video_from_avatar              -> video_id
  interactive:  show_video(video_id)  -> self-updating player, do not also poll
  unattended:   get_video(video_id)   -> poll until complete, read the URL
download -> watch it end to end
```

Renders take a few minutes. In an interactive session `show_video` mounts a player that
polls on its own — calling `get_video` in a loop alongside it is wasted work. In the
`post-runner` chain there is nobody looking at a player, so poll `get_video`.

**Watch it end to end before delivering.** This is the operator's face; lip-sync drift, a
wrong emphasis, or a mangled number costs more than a bad crop ever did.

## What this team does not use HeyGen for — and where those jobs go

| Job | Where it goes |
|---|---|
| **Reel cover** | `designer`, preset `ig-portrait`. Deterministic type on a measured grid. |
| **Thumbnail / video cover** | `designer`, preset `yt-thumb`. |
| **Article header** | `designer`, preset `article-header`. |
| **Quote card / ambient still** | `designer`. |
| **Burned-in on-screen text** | `designer`. HeyGen's `caption.style` burn-in is generic subtitle styling, not the brand type system. Take the **sidecar SRT** (`caption: {file_format: "srt"}` → `subtitle_url`) and let `designer` own anything typographic. |
| **Atmospheric B-roll** | Filmed, not generated. Produce a shot list — one prompt-shaped line per beat, with the timing it covers — for the operator to film, pull from the archive, or buy as stock. |

Covers, thumbnails and headers are typographic jobs, and `designer` lays type out from
measured geometry instead of asking a model to spell. B-roll is a shot list — say so
plainly when a piece needs it, rather than substituting a still and hoping.
