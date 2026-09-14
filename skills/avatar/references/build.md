# Avatar — build reference

Engine: **HeyGen**. Tool names, limits and pacing are in
`${CLAUDE_PLUGIN_ROOT}/skills/videographer/references/heygen.md` — read it once before
the first generation. This file covers only what is specific to synthesising the
operator.

## The authorization file — optional

**Not a prerequisite.** Gate 1 is satisfied by the digital twin existing on the account;
HeyGen required an on-camera consent recording to build it. This file is for recording
*scope* — which surfaces, what is excluded — which HeyGen's flow does not capture. Write
it when scope matters, skip it when it does not.

The ids do **not** live here; they live in `brand/avatar-motion.md`. Draft this for the
operator to confirm; do not write it as though they already agreed.

```markdown
# Avatar authorization
granted by: <operator full name, the person being synthesised>
granted on: <date>
recorded by: <who wrote this file down>
basis: <how consent is evidenced — HeyGen's on-camera consent recording, a signed note, an email>

## Covers
- [ ] Likeness / on-screen presenter
- [ ] Voice
- surfaces: <which platforms>
- purpose: <what it is for>

## Excludes
<anything they do not want it used for>

## Script approval
Only <operator> approves wording the avatar speaks. Named delegates, if any: <none>

## Ids, voice, motion and delivery
All in `brand/avatar-motion.md`. Read it every run; never improvise these.

## Revocation
<operator> may revoke at any time, in writing or verbally. On revocation: stop
generating immediately, and treat unpublished avatar material as withdrawn.
```

**On consent evidence.** Where the avatar and voice were built in HeyGen, the consent
recording HeyGen required is stronger evidence than a written note: a third party made
the person state it on camera before producing anything. Record that as the basis. It
does not, however, settle *scope* — which surfaces, and what is excluded — and it does
not settle script approval. Those stay open until he answers them, and they are marked
`[CONFIRM]` in the file until he does.

**The connector can create consent records, avatars and voices. This team never does.**
`create_avatar_consent`, `clone_voice`, `design_voice`, `create_photo_avatar` and
`create_digital_twin` all exist on the connector and all stay unused. Consent is
something he gives on camera in HeyGen's own flow, not something a tool call asserts on
his behalf. If a job appears to need a new voice or a new avatar, it needs him.

## The motion file

write to `brand/avatar-motion.md`. This file did not exist before the first avatar run;
draft it from what he actually chose in HeyGen and have him confirm it. **Never invent
motion direction** — the block below is a shape to fill, not defaults to adopt.

```markdown
# Avatar motion and delivery — locked
confirmed by: <operator>
confirmed on: <date>

## Ids
group_id: <id from list_avatar_groups, ownership: "private">
avatar_id: <the LOOK id from list_avatar_looks - this is what avatarId takes>
look type: <digital_twin | photo_avatar> · engine: <avatar_v | avatar_iv>
verified on: <date the ids were last confirmed to resolve>

## Script approval
approver: <who the operator named - commonly a social media manager>
sign-in identity: <email or handle, or: none recorded - clicks are logged, not checked>

## Voice
voice_id: <id from list_voices, type: "private">
voice label: <the name shown in HeyGen>
engine: <starfish | elevenlabs | fish>
model: <only if the engine takes one, e.g. eleven_multilingual_v2>
speed: <n>            # passed as voiceSettings.speed, clamped 0.5-1.5
pitch: <n>            # passed as voiceSettings.pitch, default 0
locale: <e.g. en-IN>  # only if the voice is multi-lingual
brand_glossary_id: <id, or: none yet>

## Motion
Passed verbatim as `motionPrompt`. Requires engine { type: "avatar_v" } on a
digital twin — on the default Avatar IV engine this field is rejected.

More expressive motion: OFF
Expression tags in use: Calm · Confident · Sincere · Warm
Never: Enthusiastic

<the verbatim custom-motion block, exactly as he approved it, including its
final line DO NOT SHOW TEETH>

## Out of character — check every render against this list
- teeth showing
- hands raised above the lap
- blink cadence reading as fast or mechanical
- <anything else he has named>
```

Everything in this file is **read at generation time, never decided at generation time**,
and none of it is regenerated to suit a particular script.

## Locking the ids — once

Do this at setup, and again only when an id stops resolving.

1. `list_avatar_groups` with `ownership: "private"` → find the group holding his avatars.
2. `list_avatar_looks` with that `groupId`, `ownership: "private"` and
   `avatarType: "digital_twin"` → identify his fine-tuned look. **The look `id` is the
   `avatarId` you pass when generating** — there is no separate avatar id. If several
   versions exist, **ask him which one is current.** Do not infer it from the name or the
   date. Note `supported_api_engines` on the look while you are there; it decides whether
   `avatar_v` is available, and `avatar_v` is what makes the motion block apply.
3. `list_voices` with `type: "private"` → find his cloned voice. Page with `token` if it
   is not on the first page. **There is no 100-voice ceiling on this connector** — if his
   voice genuinely does not appear under `type: "private"`, it was not cloned on this
   account, and that is a question for him rather than a reason to substitute a library
   voice.
4. **Write everything into `brand/avatar-motion.md` immediately**, with the date
   verified: `avatar_id`, `group_id`, look type, supported engine, `voice_id`, speed and
   the motion block. One file, so there is one place to read and one place to correct.
   Every later job reads them from there. Never pass an id from memory.

## The motion and voice lock — read, never decide

`brand/avatar-motion.md` holds the operator's locked voice, engine, speed, and the
verbatim motion block. **Read it every run.**

Three things are the ones actually got wrong in practice:

1. **`motionPrompt` silently does nothing on the wrong engine.** For a digital twin it is
   *rejected* on the default Avatar IV engine — so `engine: { type: "avatar_v" }` goes on
   every call, and a render that came back with default body language means that field
   was omitted. For a photo avatar it works on either engine.
2. **The motion block is passed verbatim.** Not summarised, not shortened for a short
   script, not reworded to match the line being spoken. It is one fixed block, and its
   final line is `DO NOT SHOW TEETH`.
3. **Speed is a request field now, not a per-scene setting.** The HeyGen *web app* resets
   speed on every scene, which is a real trap when he works there. Through the connector
   there are no scenes: one `voiceSettings.speed` applies to the whole render. Pass the
   locked value on every call and never move it to fit a script to a length.

`More expressive motion` stays **OFF**. Expression tags stay inside the persona — Calm,
Confident, Sincere, Warm. Never Enthusiastic; it contradicts the block.

## Handing over for render

**Nothing here calls a generation tool.** His voice is a Cartesia voice and HeyGen's API
synthesises only through Starfish, so an API render returns the right voice identity in
the wrong engine. `references/heygen.md` → *Why the API does not render* carries the
evidence. Emit this instead:

```
RENDER IN HEYGEN STUDIO
avatar:      <look name>            (avatar_id <id>, verify it still resolves)
voice:       <voice name>           (voice_id <id>)
engine:      Cartesia · model <model>
speed:       <locked>               re-set on EVERY scene
motion:      paste the block verbatim, EVERY scene
aspect:      9:16
script:      <the approved text, verbatim - not edited in Studio>
```

Verify first, with the read-only tools: `get_current_user` for credits,
`list_avatar_looks` and `list_voices` to confirm both ids still resolve. If either has
stopped resolving, stop and say so — do not let someone pick the nearest match in Studio.

**Afterwards.** When the file comes back, watch it end to end, confirm 9:16, then use
`get_video` to capture the HeyGen video id, URL and duration for the record.

**Cost.** Billing is by output duration, so the saving is made in the script — cut the
read before it reaches Studio. Three re-renders to fix one line is the expensive mistake,
and it is more expensive now because a human does each one.

## Writing what he says

The `script` field is spoken verbatim. That makes it the whole of the deliverable.

- **English: roughly 20–23 words per 10 seconds.** A 30-second Reel is about 65–70 words.
- **Gujarati: count syllables, not words.** Measured at Speed 0.9, 188 syllables ran
  38–47 seconds — **4.0 to 5.0 syllables per second.** Budget at **4.0** whenever there
  is a hard cap, so a 30-second Reel is **120 syllables** and a 45-second one is 180.
  Word counts do not transfer between the two languages; do not convert one to the other.
- Write to the count rather than trimming a long draft.
- **Fix length by rewriting.** Never by speed or pitch.
- **Every full stop costs about 0.7s.** Short sentences read slower than they look.
- **Numbers in words**, with the unit: "thirty-seven per cent empty", not "37%". Better
  still, put the figure on screen as type and let him say the claim — spoken numbers are
  the easiest thing to get wrong, and a wrong figure in his voice is not a typo.
- **No stage directions, no camera notes, no on-screen-text cues in `script`.** They get
  spoken. Motion direction has its own field, `motionPrompt`, and that one is not spoken.
- **No parentheses, em-dashes or colons.** They do not survive a read; restructure the
  sentence.
- **Recurring English loanwords belong in a brand glossary**, not only in transliteration.
  `create_brand_glossary` once, then pass `brandGlossaryId` on every call: it fixes the
  spoken pronunciation and leaves captions spelled normally. Transliterating into Gujarati
  script inside `script` still works as the fallback and changes the SRT too.

## Building scripts he has already approved

The strongest mitigation available, and it is worth preferring over a fresh draft.

`sources/corpus/` holds his own published posts — usually far more of them than
`performance/log.md`, which only knows what this system posted. **That corpus is the
approved-wording bank, and it is the best thing that has happened to Gate 2.** A script
assembled from wording he has already published under his own name is approved in the
only sense that matters: he wrote it and put his name on it.

Search the corpus for what he has already said on this claim before drafting anything
new. Quote the source post, its URL and its date in the piece file alongside the
script. A clip built from three lines he published last March is categorically safer
than a clip built from a paragraph this team invented this morning, however good the
paragraph is.

Two limits on that, and neither bends:

- **It must be his.** A corpus file whose author is not him is not approved wording,
  and it never becomes approved wording by sitting in the right folder.
- **Assembly is not licence to recombine freely.** Stitching two true sentences from
  different posts into a claim he never made is a new claim wearing his old words. If
  the assembled script says something no single source post says, it is a draft and
  it goes to him for approval like any other.

A draft this team wrote, however good, is constructed first-person until he confirms it.
In text that is a draft he can disown. In his face and voice it is footage of him saying
it.

## Recording the output

In the piece file under `## Assets`:

```
SYNTHETIC — generated likeness and voice of <operator>, under the HeyGen consent
recording evidenced by digital twin <avatar_id>. Script approved by <approver> on <date>
<or: assembled from his published post "<title>", <date>>.
engine: HeyGen create_video_from_avatar · avatar_v · avatar_id: <id> · voice_id: <id>
video_id: <id> · duration: <s> · aspect: 9:16 (set at request) · glossary: <id or none>
```

The video id matters more here than anywhere else: it is how a specific clip is traced
back to a specific approved script.
