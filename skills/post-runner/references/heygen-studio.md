# Driving HeyGen Studio in the browser

**Owned by `avatar`.** It lives under `post-runner` for historical reasons and is read by
both: `avatar` follows it during a run when the operator picks the avatar route, and
`post-runner` follows it when a console POST click commissions a Reel that was left
`awaiting_render`. Same sequence either way. Only one of them runs it for a given piece —
check the doc's status before starting, because a second render of the same piece is
billed twice.

The API cannot select the voice engine. The Studio UI can. So the Reel is produced by
**driving Studio in Chrome** — the same way this team drives Instagram, LinkedIn and X.

Needs a `~~browser` connector. No connector, no render: say so and leave the doc
`awaiting_render` with the spec visible for a human.

**Everything here is UI automation against someone else's product.** Read the page before
each click rather than trusting a coordinate, and stop rather than guess if a control has
moved. A wrong click here spends credits and puts the operator's face on the wrong words.

### When the editor will not screenshot

Studio's editor sometimes returns a blank frame to `computer {action: "screenshot"}` while
its DOM loads normally — `read_page` shows the title field, the Portrait/Landscape toggle,
the script box, Advanced Settings and Generate, and the pixels come back flat dark.

**Do not abandon the render for this.** Work from the accessibility tree: `read_page
{filter: "interactive"}` and `find` locate every control this sequence needs, and the
values to set are all read from `brand/avatar-motion.md` rather than off the screen.
Set them by ref, then Generate.

**Say in the line that carries the finished clip which checks you could not make** —
typically the Voice Engine and Model dropdowns and the scene-chip duration. That is the
honest version, and it costs him one look at a clip he was going to watch anyway. Stopping
before Generate because a screenshot was blank is not caution; it is handing back nothing
when one render would have answered the question.

Only stop if a control genuinely cannot be located in the tree.

## Before you start

Read from `brand/avatar-motion.md`: look name, voice label, **Voice Engine**, **Model**,
Speed, the motion block. Read the approved script from the piece file. Do not proceed
without all of them.

## The sequence

**1. Open Studio.** `navigate` to `https://app.heygen.com`. Confirm the signed-in account
matches the one in `brand/avatar-motion.md`. A different workspace has different avatars.

**2. Open the working project or template.** Whichever `brand/avatar-motion.md` names. If
it names none, create a new avatar video and select the locked look by name.

**3. Confirm the avatar.** The look name in the Avatar panel must match exactly — for this
account there are six looks in one group and they are not interchangeable.

**4. Paste the script.** Clear the Script pane and paste the approved text verbatim. Do
not retype it, do not let an editor autocorrect the Gujarati, and do not "tidy" the mixed
Latin/Gujarati script — that mix is correct.

One scene per beat. Use **+ Add scene** for each beat rather than one long scene.

**5. ⚠ Set the voice engine. This is the step that keeps going wrong.**

Open **Edit Voice** and set all four controls:

| Control | Set to |
|---|---|
| Voice (name at the top) | the locked voice label from `brand/avatar-motion.md` |
| **Voice Engine** dropdown | **Cartesia** — always, no exceptions |
| **Model** dropdown | **Sonic 3.6** |
| Speed slider | the locked value from `brand/avatar-motion.md` |

**Voice Engine is Cartesia. It is not a variable and it is not read from anywhere.** If
the dropdown shows ElevenLabs, Fish, Starfish or anything else, change it to Cartesia
before doing anything else.

Studio can assign a different engine to the same voice. When it does, the voice name still
reads correctly and the output is a different delivery, with nothing to flag it. **Read the
dropdowns; do not assume.**

Click **Update default settings** once they are right, so the voice keeps them.

**6. Re-set Speed and paste the motion block on EVERY scene.** Speed resets per scene.
Motion goes in Scene → Set Motion Style → Apply custom motion, verbatim, every time.

**7. Set the aspect ratio to 9:16.**

**8. Preview each scene** before generating. This is where a reset speed, a wrong engine
and a mispronounced term get caught — before they cost output seconds.

**9. Click Generate.** Then wait. Renders take minutes; read the page for completion
rather than re-clicking. **Never click Generate twice for the same piece** — each click
bills output seconds.

**10. Watch the finished clip end to end.** Against the out-of-character list in
`brand/avatar-motion.md`: teeth, hands above the lap, blink cadence, a scene at the wrong
speed, a mangled term. This is the operator's face; a defect here is worse than a late post.

## Publishing to Instagram from HeyGen

If Studio exposes a social publishing action for the finished video, use it: it avoids a
download, a re-upload, and a re-encode.

**On the first run, establish and record the answer in `brand/avatar-motion.md`:**

- Does this account's plan expose Instagram publishing from a finished video?
- Is the Instagram account connected, and is it the right one?
- Does it post a **Reel** (9:16, to the Reels tab) or a feed video? A feed video in a Reel
  slot is the wrong deliverable.
- Can the caption be set at publish time?

**If all four are yes:** publish from HeyGen with that variant's caption, then read back
the live Instagram URL. Nothing is recorded as published without a URL read from
Instagram itself — a HeyGen "published" state is that product's claim, not proof.

**If any is no — and it commonly is:** fall back to the route in `composers.md`. Download
the file, then drive the Instagram composer. That path is already proven and it is not a
lesser outcome; it is one extra step.

Record which route was used in the piece file. Someone will ask in six months why two
Reels went up by different paths.

## Failure modes

- **Clicking Generate before checking the engine dropdown.** The single most expensive
  mistake available here, and the least visible.
- **Clicking Generate twice** because the first looked slow. Read the page.
- **Letting an editor normalise the script.** The Latin/Gujarati mix is deliberate.
- **Leaving a scene at default speed** because the previous one was set correctly.
- **Trusting HeyGen's "posted" state** instead of reading the Instagram URL.
- **Posting a feed video into a Reel slot** because the publish dialog defaulted there.
