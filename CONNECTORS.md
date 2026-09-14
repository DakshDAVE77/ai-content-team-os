# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that
category. The plugin describes workflows by what they need, not by product name, so it
works whatever you have connected — and works, in reduced form, with nothing connected
at all.

## Connectors for this plugin

**All of these are optional.** The team runs without any of them.

| Category | Placeholder | Options | What it unlocks |
|---|---|---|---|
| Browser automation | `~~browser` | Claude in Chrome, the built-in browser | Live social listening; mining your own Instagram comments for ideas; reading your own analytics pages |
| Video generation | `~~video generation` | **HeyGen** | Verifying avatar and voice ids, credits, and reading back finished renders. **Rendering itself happens in HeyGen Studio, by a human** — see below |
| Scheduler / posting | `~~scheduler` | n8n, Zapier, Buffer, a platform API | Posting from a packaged slate instead of copy-paste |
| Email | `~~email` | Gmail, Outlook, any mail connector | Confirmation to the operator when a post goes live |
| Analytics | `~~analytics` | A platform API, or a warehouse connector | Automatic performance logging instead of pasted exports |

## Notes per category

**`~~browser`** — the single highest-value one. It is what lets the researcher see
engagement counts and reply threads, which web search cannot — and it is the only way
to reach the comment section under your own posts, which is the one idea source that is
your actual audience rather than a proxy for it. Note that it works in
interactive sessions only; a scheduled run cannot reach a browser at all.

**`~~video generation`** — `skills/videographer/references/heygen.md` documents HeyGen
specifically: the five tools this team calls, the limits, and how everything else is
routed away.

What this team uses HeyGen for is **one** thing — the operator on screen, speaking, from an
avatar and voice already built and consented to inside HeyGen. It does not produce
atmosphere, stock footage, images or thumbnails, and nothing here expects it to.

The official connector is large — around 150 tools, including voice cloning, avatar
creation, translation, lipsync and templates. **This team calls five of them, and none
of them generate.** That is scope plus one hard constraint: the gates in
`skills/avatar/SKILL.md` keep a founder's face and voice under his own control, and the
Cartesia limitation below keeps his voice actually his.

⚠ **If you connected the older community HeyGen MCP server**, its tool names
(`generate_avatar_video`, `get_voices`, `get_remaining_credits` and the rest) do not
match this plugin any more. Connect the official HeyGen connector.

Two consequences worth knowing before you connect it:

- **Covers, thumbnails and article headers belong to `designer`**, which lays type out
  from measured geometry rather than asking a model to spell.
- **B-roll is filmed, not generated.** Pieces that need atmosphere get a shot list — one
  prompt-shaped line per beat — to film, pull from the archive, or buy as stock.

**The connector does not render presenter Reels, and is not expected to.** The operator's
voice is a Cartesia voice, and HeyGen's API synthesises only through Starfish — so an API
render returns the right voice identity in the wrong engine. Renders happen in HeyGen
Studio, by a human, from a spec this team produces. The connector is used to verify ids
still resolve and to read back a finished video. See
`skills/videographer/references/heygen.md` → *Why the API does not render*.

The consent basis comes from HeyGen's own on-camera recording, which it requires before
building a twin at all; this team does not ask for it twice.

**`~~analytics`** — read the hard limit in `skills/analyst/SKILL.md` first. No
analytics API returns *who* engaged, only how many. If your brand config ranks on
audience quality rather than reach, half of that job stays manual by nature.

**`~~scheduler`** — the plugin never posts on its own initiative. A connector here
changes copy-paste into one approved action; it does not remove the approval.

Note that the **posting console needs no connector at all.** It opens the platform's own
composer with the copy ready and a human presses Post — see
`skills/publisher/references/console.md`. A scheduler connector is the upgrade from that,
not a prerequisite for it.

**`~~email`** — used for one thing: a confirmation when a piece goes live, carrying the
URL and which variant was chosen. Without it the same record still lands in
`content/calendar.md` and `performance/log.md`, which is what the analyst actually reads.
The email is for the human who was not watching.
