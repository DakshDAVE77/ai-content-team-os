# Composers — driving each platform with Claude in Chrome

Web UIs move. Everything below is a starting point to be verified by reading the page,
never a script to run blind. If a step does not match what the page shows, read the
page and adapt; do not force a selector.

---

## LinkedIn — personal feed post

1. `navigate` to `https://www.linkedin.com/feed/`.
2. Read the page. Confirm the signed-in name in the top-right identity block matches
   the operator. **Wrong account → stop.**
3. Click **Start a post**. A modal opens with a rich-text editor
   (`div[role="textbox"]`, Quill-based).
4. Click into the editor, then type the copy with `computer` type actions.
   **Do not set the text with JavaScript.** The editor keeps its own model; an
   injected `innerHTML` leaves the Post button disabled and the post empty.
5. Line breaks matter on LinkedIn and are part of the copy. Type them; do not collapse
   the post into one paragraph.
6. Read the page. Confirm the full text is present — LinkedIn silently truncates a
   paste that arrives faster than the editor commits. Confirm the **Post** button is
   enabled; a disabled button means the editor did not register the text.
7. Click **Post**. One click.
8. The new post appears at the top of the feed. Open its **⋯ → Copy link to post** or
   read the permalink from the post's timestamp anchor to get the URL.

**Known failure modes.** LinkedIn has no URL that prefills post text, so typing is the
only route. A very long post can take a while to type — let it finish rather than
re-clicking. If a "Add media" or "Rethink this post" interstitial appears, read it and
report it rather than dismissing it blind.

---

## X — post

1. `navigate` to `https://x.com/compose/post`.
2. Read the page. Confirm the signed-in handle is the operator's. **Wrong account →
   stop.**
3. The composer is a Draft.js `div[role="textbox"]` with
   `data-testid="tweetTextarea_0"`. Click it, then type the copy.
4. Read the page. Confirm the character counter is not over the limit and the
   **Post** button (`data-testid="tweetButton"`) is enabled.
5. Click **Post**.
6. The posted item appears on the profile timeline. Read its permalink
   (`/<handle>/status/<id>`) for the URL.

**Threads.** If the copy is a thread, each part is a separate box — use the **+** to
add the next one and confirm every box holds its part before posting. Post the thread
as one submit, never as separate posts.

**Known failure modes.** `x.com/intent/tweet?text=` prefills but only opens a composer
for a human — it is not a route to posting and must not be used here. Links in the
copy consume characters differently from their visible length; trust the counter, not
a local count.

---

## Instagram — Reel

Instagram is the one that genuinely may not complete, and saying so is better than
half-doing it.

1. The Reel needs a **video file on the operator's own machine**. By the time this step
   runs the chain in `SKILL.md` §4 has rendered it through `avatar` and downloaded it, so
   read `localPath` off the doc and confirm the file is really there.
   No file, and no render possible (no connector, or Gate 2 stopped it) → stop, say which,
   and leave the doc `queued`. Never open the composer hoping the file turns up.
   **Confirm the clip is 9:16 before uploading.** `avatar` sets `aspectRatio: "9:16"` on
   the call, so this should pass — but a landscape file means the field was dropped, and
   a cropped-too-late file is a wasted render.
2. `navigate` to `https://www.instagram.com/`. Confirm the signed-in account.
3. Click **Create** → **Post**, and use `file_upload` to supply the video. Never
   trigger the OS file picker any other way; a native dialog freezes the extension.
4. Instagram offers crop and cover steps. Take the defaults unless the piece file
   names a cover, then advance with **Next**.
5. Paste **that variant's** caption into the caption field. Captions are per variant and
   never borrowed across A/B/C. The Reel script is **not** the caption — the script is
   what the avatar said, and it belongs only in the artifact and the piece file.
6. Read the page, confirm the caption is complete, then click **Share**.
7. Read the new post's permalink for the URL.

**Known failure modes.** The web uploader rejects some encodings that the phone app
accepts; a rejected upload shows an inline error rather than failing loudly. Cover
selection sometimes resets on the way back from an earlier step. If the flow stalls at
any point, stop and hand the caption and the file over rather than retrying — say
which step it stalled at.

---

## What is deliberately not done here

- No liking, replying, reposting, following, bookmarking or DMing.
- No editing or deleting an existing post.
- No settings, audience or visibility changes — whatever the account defaults to is
  what it posts as.
- No scheduling through a platform's own scheduler.
- No posting to an account other than the one the operator is signed into.

## The standing caveat, said once and not repeated

Automating a personal account through a browser is not what these platforms designed
for, and a UI change can break any of the above between one run and the next. That is
why every step reads the page instead of trusting a selector, why nothing is ever
clicked twice, and why a run that cannot confirm a URL reports a failure rather than a
success.
