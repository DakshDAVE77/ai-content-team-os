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

## Handing the clip over — HeyGen never publishes

**Studio renders. `post-runner` publishes. There is no second route**, and any social
publishing action Studio offers for the finished video stays unused.

That is a deliberate narrowing. A clip published from HeyGen skips the gates, the
variant's own caption, and the log writes that `post-runner` does on the way out — and
it leaves two ways a Reel can reach the account, which is exactly the ambiguity this
system removed.

So, every time:

1. **Download the finished file.** Confirm 9:16 from the file, not from the preview.
2. Hand the local path to `post-runner`, which delivers it into the chat for him to
   watch and, on his word, uploads that exact file through the Browser plugin.

**A HeyGen URL cannot be posted.** The composer takes a local file, not a remote link,
so the render is always downloaded first and the saved path is what the console carries.

Record the HeyGen video id in the piece file so a clip traces back to the script it was
approved against.

## Failure modes

- **Clicking Generate before checking the engine dropdown.** The single most expensive
  mistake available here, and the least visible.
- **Clicking Generate twice** because the first looked slow. Read the page.
- **Letting an editor normalise the script.** The Latin/Gujarati mix is deliberate.
- **Leaving a scene at default speed** because the previous one was set correctly.
- **Publishing from HeyGen.** Studio renders; `post-runner` posts. Download and hand over.
- **Handing over a landscape render.** A video reaches the Reels tab only if the file
  itself is 9:16. Confirm it from the file, never from the preview.

Publishing override: use `skills/post-runner/SKILL.md` and the connected Browser plugin.
Console POST authorizes the exact selected existing content; no repeated approval. No CLI
publishing route remains.
