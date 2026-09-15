# Higgsfield — cutting his own clips in the browser

The second video route. **He films it, Higgsfield joins it.** Clips he shot today,
pasted into chat as paths, cut together with transitions and delivered as a 9:16 Reel.

Higgsfield is driven **in Chrome**, the same way this team drives HeyGen Studio,
Instagram and LinkedIn. There is no API here and none is wanted — he has a subscription
and the work is in the app.

Needs a **`~~browser`** connector. No connector, no cut: say so in one line, write the
**cut plan** into the piece file, and leave the clips where they are. A cut plan is a
real deliverable — he can execute it himself in two minutes.

---

## The one hard line

**Higgsfield generates video. This team only ever lets it edit.**

Text-to-video, image-to-video and generative fill are all one click away in that
product, and every one of them is a door around the `avatar` gates. So:

- **Never generate a likeness of him here.** His face comes from HeyGen, through
  `avatar`, past two gates. A Higgsfield generation of him is an ungated deepfake with
  a friendlier UI.
- **Never generate a likeness of anyone else** — client, partner, official, competitor.
  Unchanged from everywhere else in this team.
- **Never generate footage of a building and let it stand as his project.** Generic
  architecture presented as his work is a false claim about a deliverable, which is the
  same failure as an invented number. If a beat has no footage, it stays a shot list.
- **Uploaded frames only.** Every pixel in the output traces back to a file he handed
  over. If you find yourself typing a prompt describing a scene, stop — that is the
  generator, not the editor.

Label it anyway. Transitions are synthesised frames, so the output is part-synthetic and
gets recorded as such in the piece file. See *Recording it* below.

## Measured limits — read these before promising a length

From the Transitions app, confirmed against the product:

| Limit | Value | What it costs you |
|---|---|---|
| Inputs per render | **2** — video or photo | N clips need **N-1** renders |
| Max length per input | **5 seconds** | A 12s clip is trimmed, not accepted whole |
| Max output per render | **15 seconds** | The transition itself adds ~5s |
| Aspect ratio | **Locked to clip 1** | **Clip 1 must already be 9:16** or the Reel is wrong |
| Render time | 30s - 2 min | Not instant, not slow enough to walk away |
| Cost | Plan credits | Every click spends. Never click Generate twice |

**So a 30-second Reel is not one render.** Say that out loud before he pastes eight
clips expecting a finished edit back. Three clips is one joint if the middles are
trimmed, two joints if not. Plan the cut to the tool, not to a wish.

⚠ **The aspect rule is the silent one.** Output takes clip 1's ratio. A landscape first
clip yields a landscape Reel that looks fine in the Higgsfield preview and wrong in the
Reels tab. Check clip 1 before uploading anything.

## First run — discover his plan, then stop guessing

His subscription may expose apps beyond Transitions — a shorts studio that takes a
longer upload, a captions pass, an upscaler. **This file does not guess which.** On the
first run, read the app list and record the answers in `brand/reel-style.md`:

- Which apps are available on this plan — Transitions, shorts/short-video, video
  editing, upscale, captions?
- Does any of them accept **more than two clips** in one job? That changes the whole
  route from pairwise chaining to one upload.
- Max upload length and max export resolution.
- Does it export 9:16 MP4 directly, and at what resolution?
- Does it publish to Instagram, or is it download-then-composer?

Record it once. Every later run reads the file instead of exploring the product again.

## The sequence

**1. Take the clips.** He pastes paths in chat. Before anything else, read each file:
duration, dimensions, and which one is clip 1. `ffprobe` if it is there; otherwise open
the first clip in the browser and read the player. **Confirm clip 1 is 9:16.** If none
of them are, say so and stop — that is his call, not a thing to fix by cropping.

**2. Write the cut plan first, in the piece file.** Order of clips, where each joint
falls, which transition preset carries it, total running time against the budget. One
line per joint. This is what you check the output against, and it is what he gets if the
browser is unavailable.

The order serves the argument in `content/<slug>.md` — claim, proof, turn. A cut that
looks good and says nothing is decoration.

**3. Open Higgsfield.** `navigate` to `https://higgsfield.ai`. Confirm the signed-in
account is his and that credits remain. Read the page; do not trust a coordinate.

**4. Open the app named in `brand/reel-style.md`.** Transitions by default.

**5. Upload clip 1, then clip 2.** In the order the cut plan says. Do not let the
uploader reorder them.

**6. Choose the transition from the approved list in `brand/reel-style.md`** — not from
whatever the gallery is featuring today. This is the same rule as the locked avatar id
and it is there for the same reason: a feed that speaks a different visual language
every week does not look like one person. A preset that is not on the list gets added by
him, not by a run that liked the look of it.

**7. Confirm the aspect reads 9:16, then Generate. Once.** Renders take minutes. Read
the page for completion rather than clicking again — a second click is a second charge.

**8. Chain the next joint** if the cut plan has one, using the previous output as clip 1.
Watch the running time: each pass re-encodes, so the fewest joints that tell the story
wins. **Three chained renders is the practical ceiling** before quality visibly drops —
past that, hand him the cut plan and let him assemble it in a real editor.

**9. Download the file.** 9:16 MP4, highest resolution the plan gives.

**10. Watch it end to end before it goes anywhere.** Every joint, at full speed and
once more slowly:

- Does the morph mangle a face or a sign mid-transition? That is the common defect.
- Does it cut cleanly at the length the script needs, or does it dribble?
- Is it 9:16 all the way through, including the last frame?
- Does any transition invent a detail that reads as a claim about a building?

A mangled joint is fixed by re-cutting, not by shipping and hoping the feed is small.

## His style — where it comes from

"Beautiful" is not a setting. Three files decide what this cut looks like, and none of
them is taste:

| Decision | Read it from |
|---|---|
| Which transitions are on-brand | `brand/reel-style.md` → *Approved transitions* |
| Pace, energy, how long a beat holds | `brand/voice-profile.md` — measured from his own posts |
| What the cut is arguing | `content/<slug>.md` — claim, proof, turn |

If `brand/reel-style.md` does not exist yet, do not invent a house style. Use the most
conservative transition available, say in one line that the style file is not set up,
and let him name his presets once.

**On-screen text stays with `designer`.** If Higgsfield offers burned-in captions, they
may carry only the approved script wording, verbatim. Titles, covers and any typographic
frame are laid out from measured geometry by `designer` and composited after — asking a
video model to hold a type system produces mangled words.

## The style file

`brand/reel-style.md`, owned by the operator, drafted for him to confirm:

```markdown
# Reel style

## Higgsfield account
plan:            <tier>
apps available:  <Transitions, shorts studio, upscale, captions - as read on first run>
multi-clip app:  <name, or "none - pairwise only">
max upload:      <seconds>
export:          <resolution> 9:16 MP4
IG publishing:   <yes / no - no means download then composer>
verified:        <date the above was read from the app>

## Approved transitions
- <preset name> - <when it is right>
- <preset name> - <when it is right>

## Never use
- <preset> - <why: too flashy, wrong register, mangles faces>

## Pace
beat length:     <seconds a clip holds before the cut>
joints per reel: <number, typically 2-3>
captions:        <burned in / none / designer only>
```

## Recording it

Append to the piece file under `## Assets`:

```
CLIP EDIT - <n> clips filmed by <operator>, joined in Higgsfield.
Transitions: <preset per joint>. Transition frames are synthetic; all other
footage is his own. Cut plan above. <duration>s, 9:16.
```

That line answers the only question anyone asks six months later: which frames were
real. Every frame except the joints, and the joints are named.

## Failure modes

- **A landscape clip 1.** Silent, and it ruins the ratio of everything downstream.
- **Clicking Generate twice** because the first looked slow. Read the page.
- **Promising a 45-second edit** from a tool that caps a render at 15 seconds.
- **Prompting instead of uploading.** The moment a text box describes a scene, this
  stopped being an edit and became an ungated generation.
- **Chaining six joints** and shipping something that has been re-encoded six times.
- **Picking a transition because it looked good in the gallery** rather than reading the
  approved list.
- **Shipping a joint nobody watched at full speed.** A morph that mangles a face is
  obvious on the second viewing and invisible on the first.
