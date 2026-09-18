# First run — what has to exist before the team can work

The plugin is the skills. **The memory is a folder on the operator's own computer**
(see `memory-map.md` for how `<root>` is resolved), and a fresh install has none of it. Nothing in this team works properly until these files exist, because
every employee reads before it writes.

`brand-setup` creates all of them. This file is the contract it fulfils, and the
checklist any employee uses to tell whether it has been run.

## The files

| Path | Created by | Without it |
|---|---|---|
| `brand/brand-config.md` | brand-setup interview | **Hard stop.** Every employee reads it first. Generic content otherwise. |
| `brand/voice-master.md` | brand-setup, from a voice document the operator supplies — **optional, and the strongest input here when it exists** | Register, post architecture, hook formulas and the do-not list are all inferred per run instead of read. Drafts drift between registers. |
| `brand/voice-profile.md` | brand-setup, from `sources/corpus/` | Voice comes from two or three pasted samples instead of their whole body of work. Drafts read generic. |
| `brand/proof.md` | brand-setup | Writers invent numbers. This is the only list of assertable facts. |
| `brand/offers.md` | brand-setup, if they have an offer | CTAs get invented |
| `brand/avatar-motion.md` | the operator, drafted by brand-setup | Voice, speed and motion get chosen per run instead of read. Two versions of the same person. |
| `brand/reel-style.md` | the operator, drafted on the first Higgsfield run | Transitions get picked from whatever the gallery features that week, and the feed stops looking like one person. Only needed if he cuts his own clips. |
| `library/idea-bank.md` | scaffold | No pipeline — this is the spine |
| `library/hooks.md` | scaffold | Hook choices are not recorded, so nothing is learned |
| `library/swipe-file.md` | scaffold | References are lost |
| `content/calendar.md` | scaffold | Nothing gets slotted |
| `performance/log.md` | scaffold | Numbers have nowhere to go |
| `performance/patterns.md` | scaffold | Employees have no evidence to weight toward |
| `state/analytics-cursor.json` | scaffold | Every run rescans analytics from the start |
| `state/comments-cursor.json` | scaffold | Every run re-reads every comment on every post |
| `state/ingested.json` | scaffold | Scraped exports get re-read every run |
| `sources/corpus/` | scaffold (empty dir) | Nowhere for the operator to drop their own posts — the strongest voice signal available |
| `sources/cs-scrape/` | scaffold (empty dir) | Nowhere for the operator to drop other people's exports |

Scaffolds are created **empty but structured** — headers, table columns, and a line
saying they are empty. An empty file with the right shape is useful; a missing file
breaks a read.

## The rule about empty files

An employee that opens a scaffold and finds no rows says so in one line and proceeds
on `brand/brand-config.md` alone. It does **not**:

- invent a pattern from nothing
- estimate a metric
- treat "no data" as "no signal, do whatever"

`performance/patterns.md` empty means every posting time and format choice is a
hypothesis. Say that once, then move on.

## Optional capabilities — check, do not assume

None of these are required. The system works without all of them; it just does less.
Check at the start of a run and say plainly which are on.

| Capability | Provided by | Absent → |
|---|---|---|
| Live social listening | a browser automation connector (`~~browser`) | Web search only. Say the live scan did not run. |
| Mining your own IG comments for ideas | the same connector | No comment ideas. Say the mining did not run — do not substitute search results for it. |
| Clip Reels — his own footage cut with transitions | a `~~browser` connector, a Higgsfield subscription, and clips he pastes in chat | Cut plan only, one line per joint |
| Presenter video — the operator on screen | `brand/avatar-motion.md` with a confirmed avatar and voice, **plus a `~~browser` connector** — the Reel is rendered by driving HeyGen Studio, because the API cannot select the voice engine | Reels ship as script + spec, left `awaiting_render` |
| Atmospheric B-roll | not generated — it is filmed, pulled from the archive, or bought | Shot list, one line per beat |
| Analytics | operator pastes exports; or a platform API | Manual paste. Never estimate. |

**Scheduled runs never have browser access** — the tools are absent from the session
entirely, not merely disconnected. That is structural. Live listening is an
interactive-session capability only.

## Verifying an install

Ask for **"content status"**. A correct install answers with a pipeline count. If it
reports the brand config missing, `brand-setup` has not been run.

Publishing override: use skills/post-runner/SKILL.md and connected Chrome. Console POST authorizes the exact selected existing content; no repeated approval. No CLI publishing route remains.
