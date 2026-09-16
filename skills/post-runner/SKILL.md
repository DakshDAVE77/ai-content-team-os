---
name: post-runner
description: Send the option the operator picked in the console to the live platform by driving Claude in Chrome - open the composer, fill the copy, submit, capture the URL and close the loop. Use when the user says post, post it, post them, send it, publish it, post the LinkedIn one, go, post all three, or after they say they clicked POST in the console.
---

# The Post Runner

The console records the pick. This skill sends it. It is the only place in the system
that acts on a live account, and it exists because the operator asked for it — driving
his own browser, signed into his own accounts, on copy he chose.

Read `${CLAUDE_PLUGIN_ROOT}/references/memory-map.md` and
`${CLAUDE_PLUGIN_ROOT}/skills/post-runner/references/composers.md`.

## 1. Find out what to post

`read_db` the console artifact for `post_request/instagram`, `post_request/linkedin`,
`post_request/x`.

- **Docs with `status: "queued"`** are the job. Take them all unless he named one
  platform ("post the LinkedIn one" → that doc only).
- **No queued docs** → say so in one line and stop. Do not guess a variant, do not
  post the first option, do not re-post something already `posted`.
- **A doc already `posted`** → skip it, name it, do not post twice.

Each doc carries `text` verbatim. **Post that text exactly.** No edits, no added
hashtags, no emoji, no "improvements". If something in it looks wrong, stop and say so
rather than fixing it silently — the whole point of the pick is that he chose those
words.

## 2. Check the gates before touching the browser

Refuse, and say which gate, if:

- the variant is locked in the console (unresolved placeholder, or an unapproved
  constructed first-person claim with no `approval/<pieceId>__<variant>` doc)
- the copy contains `[NUMBER: ...]`, `TODO`, or any bracketed placeholder
- it touches a topic in `brand/brand-config.md` → `## Off limits`
- it asserts a number about him or his company that is not in `brand/proof.md`, or is
  in there under **Targets**

These gates run here as well as in the page. This is the last moment before his name
is on it.

## 3. Check who is logged in

Open the platform and read the signed-in account **before** composing. Posting to the
wrong account is unrecoverable in a way nothing else here is. If the browser is signed
into an account that is not his, stop and say which account it found.

## 4. Run the three in parallel — do not let one wait for another

LinkedIn and X post in seconds. An Instagram Reel has to be rendered first, which takes
minutes. **Do not serialise them**, and do not hold the text posts back so everything
lands together — "simultaneously" here means started together, not landing on the same
second.

```
say "post"
├─ LinkedIn ──── compose ── submit ── URL        seconds
├─ X ─────────── compose ── submit ── URL        seconds
└─ Instagram ─── render ── clip into chat ─┐            minutes
                                           └─ he says post ── upload ── URL
```

**Each platform succeeds or fails on its own.** A failed render does not stop LinkedIn.
A wrong-account stop on X does not stop the Reel. Never abandon two good posts because
the third broke, and never re-post a platform that already landed because a sibling
failed.

### The Instagram chain

**First: does a video already exist?** Read the doc before assuming this click
commissions anything. The engine now asks for a video route at the top of every run, so
the Reel is often already cut or already rendered by the time he clicks POST.

| Doc says | Do this |
|---|---|
| `status: "rendered"`, or a video file/URL on the doc | **Upload what is there.** Skip the whole render chain — go to step 5. Never re-render a piece that already has a clip: it is billed twice and can come back subtly different from the one that was approved and watched. |
| Clip edit from the Higgsfield route | Same — the file exists. Upload it. Nothing in this chain applies. |
| `status: "awaiting_render"` | No clip yet — the run had no browser, or the piece was staged ahead of one. **The click is the go-ahead: render immediately and do not stop to ask anything else.** The chain below runs in full. |
| No video at all — caption and cover only | Post the copy with the cover. Do not invent a Reel. |

The rest of this chain is for `awaiting_render` only.

1. **Record who clicked.** Read `requestedBy` on the doc and carry it into the piece
   file for the audit trail. If `brand/avatar-motion.md` records an approver identity,
   check the click against it and say so if it does not match — but **do not refuse the
   render for identity alone.** The approver is whoever the operator named, commonly a
   social media manager.
2. **Get the render spec from `avatar`.** Never call a HeyGen generation tool — the API
   cannot select the voice engine, so an API render is the wrong voice. `avatar` reads the
   locked values from `brand/avatar-motion.md` and emits the spec. Set
   `status: "generating"`.
3. **Drive HeyGen Studio in the browser.** Follow
   `${CLAUDE_PLUGIN_ROOT}/skills/post-runner/references/heygen-studio.md` step by step:
   open Studio, confirm the account and the avatar look, paste the script verbatim, **set
   the Voice Engine and Model dropdowns from `brand/avatar-motion.md`**, re-set Speed and
   paste the motion block on every scene, set 9:16, preview, then Generate once.

   **The engine dropdown is the step that keeps going wrong.** Studio can assign a
   different engine to the same voice; the voice name still reads correctly and the
   delivery is a different man. Read it, do not assume it.

   No `~~browser` connector → stop, set `status: "awaiting_render"`, and surface the spec
   for a human. Do not fake this step.
4. **Deliver the clip into the chat, and stop there.** Download the finished file and
   send it with `SendUserFile`, captioned with the piece id, the variant and the duration.
   Set `status: "rendered"` with the `videoUrl`. **Do not upload it to Instagram in the
   same breath.**

   This is the watch step and it belongs to him. The out-of-character list — hands above
   the lap, teeth held across a phrase, a grin, a scene at the wrong speed, a mangled
   term — is judged on the clip by the person whose face it is, not on a description of
   it. If something on that list is visible, say which and roughly which second in the
   one line that accompanies the file; **say it, do not withhold the clip over it.** The
   call is his.

   **Nothing re-renders on its own.** If he says it is wrong, set
   `status: "awaiting_render"`, fix the named cause, and drive Studio once more.
5. **Wait for him to say post, then publish.** "post the video", "post it", "yes post" —
   that is the word. Prefer HeyGen's own Instagram publishing if the account exposes it;
   otherwise download the file and use the Instagram composer in `composers.md`, which
   takes a local file, not a HeyGen URL.
6. **Use that variant's `caption`** — captions belong to their variant and are never
   borrowed across A/B/C. Then capture the live URL as below. **A HeyGen "published" state
   is not proof** — read the URL from Instagram itself.

**Cost note, said once:** a render is billed by output seconds and starts on his click.
Never start a second render for the same pieceId because the first looked slow — read
the doc's status instead.

**A render is not a post.** It is billed, and it is his face, but it is private and
reversible. Publishing is neither. That asymmetry is why the render runs on a click and
the upload waits for a word.

## 5. Post

Load the Chrome tools in one call:

```
ToolSearch: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__file_upload,mcp__claude-in-chrome__tabs_close_mcp
```

Tools absent, or the extension unreachable → say the browser is not available, leave
the docs `queued`, and stop. Do not retry, and do not fall back to opening a prefilled
composer and calling it posted.

Per-platform steps, selectors and the known failure modes are in
`references/composers.md`. Three rules apply to all of them:

1. **Read the page before submitting.** Confirm the composer holds the intended text,
   in full, and that it is the right composer. A truncated paste is the most common
   failure and it is silent.
2. **Submit once.** If the click appears not to register, read the page again before
   clicking anything. Never click Post twice — a duplicate post is worse than a failed
   one.
3. **Never trigger a native dialog.** No alerts, confirms or file-picker prompts
   outside `file_upload`; they freeze the extension.

Set the doc to `status: "posting"` before the submit and update it after, so a session
that dies mid-post leaves an honest record.

## 6. Capture the URL — nothing counts without it

After submitting, read the page for the live permalink. Instagram and X expose it from
the posted item; LinkedIn's is on the new feed entry's menu.

**Only a URL is evidence.** A click is not a post, a spinner is not a post, an empty
composer is not a post. If the URL cannot be found, set `status: "failed"` with the
reason, say plainly that it may or may not have gone live, and tell him to check —
never record a post you did not see land.

## 7. Close the loop

For every post that landed, all five writes, every time:

1. `db` → `post_request/<platform>` `status: "posted"`, with `url` and `postedAt`
2. `content/<slug>.md` → `## Publish` — the live URL; and the `## Variants` row for
   the chosen angle set to `chosen`, the other two `discarded`
3. `library/idea-bank.md` — row to `published`
4. `performance/log.md` — a new row with the date, slug, platform, format, pillar,
   **angle**, hook id and **confidence**, metrics left as `—` for the analyst. The
   `post_request` doc already carries `angle`, `confidence` and `confidenceLabel` —
   copy them from there rather than reopening the piece file. Without them the analyst
   cannot tell whether the number beside the POST button predicts anything.
5. `state/analytics-cursor.json` — leave `last_post_id` alone; the analyst sets it
   when it reads the numbers. Bump `log_rows`.

Step 2 is the one that gets skipped and the one that matters most: which angle he
keeps choosing is the single most useful thing this system learns about him, and it
only accumulates if it is recorded every time.

## 8. Report

```
POSTED
LI  <url>
X   <url>
IG  <url>

RENDERING
IG  <pieceId> — watch it in the console, then tap to post

FAILED
<platform> — <the exact thing that stopped it>
```

Nothing else. No summary of the copy, no congratulations. Omit any section that is empty.

## Never

- Post anything the operator did not pick in the console.
- Render his likeness on a click that was not his.
- Post a Reel nobody watched. He watches it in the chat; that is what the clip is sent
  for.
- **Stop an approved render to ask a question.** A POST click on an Instagram option is
  the go-ahead. Render it, send it, and ask afterwards — the place to raise a doubt is
  the line that carries the file, not a pause before Generate.
- Hold a finished LinkedIn or X post back because the Reel is still rendering.
- Start a second render for a pieceId that already has one in flight, **or one that
  already finished during the run.** Read the doc; the clip is usually already made.
- Edit the copy on the way to the composer.
- Post to an account you did not verify.
- Click Post twice.
- Like, reply, repost, follow, bookmark, DM, or change any setting on his account.
  Reading and posting the queued copy is the entire mandate.
- Record a post as published without a URL you read from the page.
- Schedule a post for later. This skill posts now or reports that it did not.
