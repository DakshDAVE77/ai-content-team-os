---
name: post-runner
description: Publish the exact console-selected copy and existing carousel or video through the Browser plugin session. Use for post, publish, or an authorized console request.
---

# Browser publisher

Read CODEX-INTEGRATION.md and ContentEngine/brand/brand-config.md. Use the available cua_repl browser API, following its returned documentation. Default to the user-selected Browser plugin (Codex in-app browser). Use Chrome only when explicitly selected and available. Discover available browser surfaces on the current device; do not assume sessions or credentials carry between devices.

## Authorization
Selecting an option and pressing POST explicitly authorizes publication of that exact option and its existing assets to that platform. After pressing POST in the console, the user says "post", "publish", "post selected", or "continue posting" in this chat to start execution. This chat message is the dispatch trigger, not another approval request. Process every selected, authorized, unpublished platform unless the message narrows the scope. Do not publish all A/B/C alternatives or republish existing posts. Continue through the final platform Publish button without asking again. This does not authorize changing the copy, publishing other variants, generating paid videos, or using a different account.

## Execution
1. Read ContentEngine/state/post_request/*.json. Process publicationAuthorized requests in queued or awaiting_browser state. Preserve each request independently. If none exist, report that no option is selected.
2. For posting, submitted or unknown outcomes, reconcile before another submission. Skip posted records. Legacy external job IDs also require reconciliation; never resubmit them blindly.
3. Connect the Browser plugin using cua_repl, reusing the selected browser and existing social tabs where available. Open the platform's own site: instagram.com, linkedin.com/feed/, or x.com. Verify the visible account matches the configured handle. If the selected browser is unavailable, leave awaiting_browser; login, account mismatch, verification challenge or unsupported media upload are concrete blockers, not reasons to pretend publication succeeded.
4. Open the actual composer using observed controls. Paste the saved text exactly. For a carousel, upload every saved slide in order. For an existing video, upload that exact file and any selected cover the platform supports. Never replace an eight-slide carousel with its first image. Use only supported browser upload capabilities; stop if they are unavailable.
5. Check the composer text, destination, media count/order and processing status. Record status posting, attempt timestamp and target account before clicking the final publish control once.
6. Read the result. Store submitted if accepted but not yet verified, or unknown if the outcome is ambiguous. A matching visible post and permalink earn posted. Save url, postedAt and observed account. Do not click Publish again on a timeout; inspect profile/recent posts first.
7. Update content record, calendar, idea-bank and performance log only for verified publication. Keep unposted siblings intact. Report each platform's URL or exact blocker.

## Video and carousel media — what may be uploaded
The saved asset list is the deliverable. Upload those exact files, in the saved order, and nothing else.

| Saved state | Do this |
|---|---|
| A rendered avatar Reel, or a Higgsfield clip edit, is on the request | **Upload that exact file.** It was already rendered and already watched. Never re-render it: a second render is billed again and can come back subtly different from the clip that was approved. |
| A carousel | Upload every slide, in the saved order. The first image alone is not the post. |
| Caption and cover only | Post the copy with the cover. Do not invent a Reel. |
| No rendered file where one is expected | **Stop that platform** and report it. Do not post a Reel that does not exist, and do not substitute a still for a video. |

**A POST click never commissions a render.** It authorizes publication of content that
already exists. Rendering is a separate, paid, explicitly requested step owned by
`avatar` (HeyGen Studio) and `videographer` (Higgsfield) — see below. This skill uploads;
it does not generate.

Confirm 9:16 from the file before uploading a Reel. A landscape file reaches the feed,
not the Reels tab, and that is not the deliverable.

## When there is no clip yet
The Reel is normally made during the run, because the operator picks the video route in
`content-team` Step 0 and that choice is the go-ahead. If a piece reaches the console
without one — the browser was unreachable, or a script tripped the avatar refusal list —
the option is not publishable and this skill says so rather than improvising.

Getting one is a separate instruction from him, and it runs through the owning skill:

- **Presenter Reel** → `avatar`, which checks its gates, reads the locked avatar, voice,
  engine, speed and motion block from `brand/avatar-motion.md`, and drives HeyGen Studio
  through Generate per `${CLAUDE_PLUGIN_ROOT}/skills/post-runner/references/heygen-studio.md`.
  **Never render his likeness from here**, and never through a HeyGen API call — the API
  cannot select the Cartesia voice engine, so an API render is the wrong voice.
- **Clip edit from his own footage** → `videographer`, which drives Higgsfield per
  `${CLAUDE_PLUGIN_ROOT}/skills/videographer/references/higgsfield.md`. Edits only; a
  described scene is generation and it stops.

Either way the finished clip is delivered into the chat for him to watch before anything
is published. A render is billed and it is his face, but it is private and reversible.
Publishing is neither.

## Console and chat handoff
POST saves exact copy, ordered assets and authorization with status queued. The console tells the user: "Selected. Say post in this chat to publish your selected platforms."
The user's subsequent chat message runs this skill on demand. No autonomous click-to-agent service or repeated confirmation is needed. Never claim a console click itself published anything.
Snapshot selected requests at run start. Before submitting each platform, reread it; if the variant/text/assets changed, leave the new selection for the next chat trigger rather than posting a moving target.
Process Instagram, LinkedIn and X independently. A sign-in or upload blocker on one must not stop other ready platforms. Verify posted items by permalink, and report remaining blockers.

## Devices and portability
The workflow is device-independent when the project, saved selection files, media and Browser plugin are accessible on that device. Resolve asset paths relative to the current project, never a previous Windows username or drive. Verify account identity on each device. Localhost queues, files and browser sign-ins are not automatically synchronized; report missing inputs rather than claiming all-device support is configured. Run from one device at a time; cross-device concurrent dispatch is unsupported without shared locking. The request is to publish once per selected platform, not once per device.

## Never
- Post anything the operator did not select in the console.
- Edit the copy on the way to the composer.
- **Generate video, audio or a likeness from here.** Uploading is the whole mandate.
- Re-render a piece that already has a clip, or start a second render for one in flight.
- Substitute a still for a missing video, or the first slide for a carousel.
- Post to an account you did not verify against the configured handle.
- Click the final publish control twice, or resubmit on a timeout before inspecting.
- Record a post as published without a permalink you read back.
- Like, reply, repost, follow, bookmark, DM, or change any setting on his account.
- Create a schedule.
