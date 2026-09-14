# Memory map — where the team keeps its work

Every employee reads and writes the same set of files. This file is the contract.
An employee that invents its own path breaks the pipeline.

## Where memory lives

**Memory is a folder on the operator's own computer**, reached through the
remote-devices bridge. Not a Claude project — the Projects tool is not available in
this environment, and a folder is inspectable, editable and backed up by the operator.

**Resolving the root, once per run, quietly:**

1. Call `get_device_info`. Read `connectedFolders`.
2. If any connected folder contains a `ContentEngine` directory, that is the root.
3. Otherwise the root is `<first connected folder>/ContentEngine`. Create it.
4. **No connected folders at all** → call `device_request_folder_access` once for a
   sensible folder and say, in one line, that memory needs a connected folder.
   If the request is declined or unanswered, run **stateless for this session**:
   build from `brand/brand-config.md` alone if it can be read, say so in one line,
   and do not pretend to have read history.

Refer to the root as `<root>` below. In `device_bash` it is mounted at
`$HOME/mnt/<folder-name>/ContentEngine`.

**Read and write it with `device_bash`** — `cat`, `grep`, `sed -i`, short python.
Never stage a memory file into the cloud container just to read or edit it. Stage
only when a step needs a cloud-only tool (image rendering, a skill's script).

## The tree

| Path under `<root>` | Owner (writes) | Readers |
|---|---|---|
| `brand/brand-config.md` | brand-setup | everyone |
| `brand/voice-profile.md` | brand-setup, from `sources/corpus/` | every writing employee |
| `brand/proof.md` | brand-setup | everyone |
| `brand/offers.md` | brand-setup | script-writer, publisher |
| `brand/avatar-authorization.md` | the operator | avatar — optional, scope only |
| `brand/avatar-motion.md` | the operator | avatar, videographer, script-writer |
| `research/trends-YYYY-MM-DD.md` | researcher | manager, hook-writer |
| `research/competitors.md` | researcher | hook-writer, analyst |
| `library/idea-bank.md` | researcher creates rows; every employee updates status | everyone |
| `library/hooks.md` | hook-writer | script-writer, analyst |
| `library/swipe-file.md` | researcher, analyst | hook-writer, designer |
| `content/<slug>.md` | script-writer creates; designer and publisher append | everyone |
| `content/calendar.md` | publisher | manager, analyst |
| `performance/log.md` | analyst | everyone |
| `performance/patterns.md` | analyst | hook-writer, script-writer, researcher |
| `state/analytics-cursor.json` | analyst | manager |
| `state/comments-cursor.json` | researcher | manager, hook-writer |
| `state/ingested.json` | analyst, researcher | manager |
| `sources/corpus/` | **the operator drops their own posts here** | brand-setup, every writing employee, avatar |
| `sources/cs-scrape/` | **the operator drops other people's posts here** | analyst, researcher, hook-writer |
| `runs/YYYY-MM-DD.md` | manager | manager |

`<slug>` is kebab-case, derived from the idea title, max 6 words.

## The three cursors — why nothing is ever rescanned from the start

Re-reading the whole history every day is the single biggest cost in a daily run and
it buys nothing. Three small JSON files remove it. They share one rule: **read forward
only, and write the cursor after the rows land, never before.**

### `state/analytics-cursor.json`

```json
{
  "updated": "2026-09-12",
  "linkedin": { "last_scan": "2026-09-11", "last_post_urn": "urn:li:activity:7..." },
  "instagram": { "last_scan": "2026-09-11", "last_post_id": "C9x..." },
  "x":         { "last_scan": "2026-09-11", "last_post_id": "18412..." },
  "log_rows": 41,
  "patterns_computed_from_rows": 41
}
```

**The rule: read forward only.** A run reads the platform for posts newer than
`last_post_id` / `last_scan` and stops as soon as it hits a post already in
`performance/log.md`. It never pages back past the cursor.

Patterns are **recomputed from `performance/log.md`**, never from the platform. The
log is the store of record; the platform is only ever a source of new rows. So a run
touches the browser for a handful of new posts and computes everything else from a
local file, which costs nothing.

Only two things justify going back past the cursor, and both must be said out loud:

- the operator asks for a full re-read
- `log_rows` disagrees with the actual row count in `performance/log.md`, which means
  a run died mid-write — repair, then reset the cursor

Write the cursor **after** the log rows are written, never before. A cursor ahead of
the log silently loses posts forever.

### `state/comments-cursor.json`

The researcher mines the comments under the operator's own Instagram posts for ideas
(method: `browser-listening.md` → *Mining the operator's own Instagram comments*). The
same forward-only rule applies, per post rather than per platform.

```json
{
  "updated": "2026-09-12",
  "instagram": {
    "last_scan": "2026-09-11",
    "posts": {
      "C9xAbc123": { "last_comment_id": "17984…", "mined": "2026-09-11", "captured": 3 },
      "C9wDef456": { "last_comment_id": "17962…", "mined": "2026-09-09", "captured": 0 }
    }
  },
  "ideas_from_comments": 14
}
```

A run opens posts newest-first and **stops at the first post whose newest comment is
already recorded**. A post with `captured: 0` was read and had nothing worth a row —
that is a real result, and recording it is what stops the next run re-reading it
hopefully.

Comment threads keep growing for about a week, so **re-mine posts from the last seven
days** and update their entries in place. Older posts are settled.

Going back past this cursor happens for the same two reasons as the others: he asks, or
`ideas_from_comments` disagrees with the number of `ig-comments` rows in the idea bank,
which means a run died mid-write.

### `state/ingested.json`

The operator drops scraped post exports into `sources/cs-scrape/`. Ingest each file
exactly once.

```json
{ "files": {
    "cs-scrape/cs-linkedin-2026-09.json": { "sha": "ab12…", "ingested": "2026-09-10", "rows": 214 },
    "corpus/posts/linkedin-2026-07-26-wrong-finish-line.md": { "sha": "cd34…", "ingested": "2026-09-12" }
} }
```

**Keys are paths relative to `sources/`**, because the folder a file sits in decides
what it teaches. Each run: list both folders, hash each file, ingest only files whose
hash is absent or changed, then record the hash. A file already ingested is skipped
without being read.

| folder | what its files feed |
|---|---|
| `sources/corpus/` | the operator's **own** writing → `brand/voice-profile.md` and proof candidates, per `voice-corpus.md` |
| `sources/cs-scrape/` | **anyone's** posts → `library/swipe-file.md` and `performance/patterns.md` → `## From the scrape` |

Never cross them. A competitor's post ingested as voice teaches the operator to sound
like their competitor, which is the failure this whole system exists to prevent.
Method, and what to measure: `voice-corpus.md`.

## The idea bank is the spine

`library/idea-bank.md` is one markdown table. Every piece of content is a row from
birth to post-mortem. Never delete rows — change the status.

```markdown
| id | title | pillar | platforms | status | source | hook | slug | updated |
|----|-------|--------|-----------|--------|--------|------|------|---------|
| 014 | Why my first funnel failed | build-in-public | IG, LI | scripted | scan | h-032 | why-my-first-funnel-failed | 2026-09-07 |
| 015 | What people keep asking about pricing | pricing | IG, X | new | ig-comments | — | — | 2026-09-12 |
```

`source` is where the idea came from: `scan` (live listening), `search` (web),
`ig-comments` (mined from his own comment section), `scrape`, or `operator`. It exists
so the analyst can say which source actually produces posts that land — the cheapest
way to find out whether the comment mining is worth the browser time.

An `ig-comments` row carries the comment it came from, verbatim and attributed, in the
row's notes. Their phrasing is the raw material for the hook.

**Status ladder** — an employee may only advance a row one rung, and only its own rung:

| status | set by | means |
|---|---|---|
| `new` | researcher | idea captured, nothing written |
| `hooked` | hook-writer | a winning hook is chosen and logged in `library/hooks.md` |
| `scripted` | script-writer | full script/copy exists at `content/<slug>.md` |
| `designed` | designer | visuals rendered and listed in the piece file |
| `staged` | publisher | in the console, ready for a pick |
| `published` | post-runner (or the operator) | live, URL recorded |
| `analysed` | analyst | metrics in `performance/log.md`, lesson in `performance/patterns.md` |
| `killed` | anyone | with a one-line reason in the row's title cell |

## The piece file

`content/<slug>.md` is the single artefact a post is built from. Sections are
appended by whoever owns them — never rewrite another employee's section.

```markdown
# <title>
id: 014 · pillar: build-in-public · status: staged · updated: 2026-09-12

## Hook (hook-writer)
chosen: h-032 — "My first funnel made $0. Here is the line item that killed it."
runners-up: h-033, h-034

## Script (script-writer)
### Instagram Reel
### LinkedIn post
### X post

## Assets (designer)

## Publish (publisher)
console pieceId: ig-2026-09-12
variants: A / B / C — full text, one per angle

## Result (analyst)
```

## Rules

- **Read before you write.** Append; never clobber another employee's work.
- **One writer per section.**
- **Date-stamp everything.**
- **Never rescan past a cursor** without saying so. All three, same rule.
- **Write every cursor after its rows, never before.**
- **If `brand/brand-config.md` does not exist, stop** and run `brand-setup`.
- **Read the voice precedence chain in the order given in `voice-corpus.md`.** Voice
  corrections beat the measured profile, which beats the onboarding profile, which
  beats `voice-rules.md`.
