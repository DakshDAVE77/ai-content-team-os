# AI Content Team OS 3.1.1 — Codex starter project

## Start here
1. Clone this repository, or extract the release ZIP into a new folder. Keep the hidden
   .agents, .claude-plugin and .codex-plugin folders — they carry the Codex wrappers and
   the plugin manifests.
2. Open the extracted ai-content-team-os folder as a local project in Codex. The project skills are in .agents/skills; the plugin source is in plugins/ai-content-team-os. This is a starter project, not a claim of one-click marketplace installation.
3. Enable the Browser plugin in Codex. Sign into your own intended Instagram, LinkedIn and X accounts inside that browser. Logins and permissions are not included.
4. Ask: "Set up my brand using the supplied documents." Supply your own brand identity, voice, proof, visual guidance and account handles. No original owner's brand data is included. Review the bundled editorial templates against your brand.
5. Ask: "Run the content engine — topic: [your topic]. Make a carousel, no video."

## Installing as a Claude Code plugin
This repository is also a plugin marketplace. In Claude Code:

    /plugin marketplace add DakshDAVE77/ai-content-team-os
    /plugin install ai-content-team-os@cs-content

The manifest is `.claude-plugin/marketplace.json` at the repository root, and the plugin
source is `plugins/ai-content-team-os`. The Codex starter flow above and the Claude Code
plugin install are two ways into the same skills.

## Rendering dependencies
Install Python 3.10+ on the computer. From this project folder:

    python -m venv .venv

Windows:

    .venv\Scripts\python -m pip install -r requirements.txt
    .venv\Scripts\python -m playwright install chromium

macOS/Linux:

    .venv/bin/python -m pip install -r requirements.txt
    .venv/bin/python -m playwright install chromium

The console server uses the Python standard library. Renderers use Playwright. Optional video tools and paid services are separate and are not installed or authorized by this ZIP.

## Posting
The publisher writes outputs/current-content.json (schema in tools/CONSOLE.md), then runs python tools/build_console.py. Start python tools/console_server.py and open http://127.0.0.1:8767/content-console.html in Codex Browser.

Press POST on one option per platform, then say "post" in the project chat. The agent reads saved selections, verifies the account, uploads existing media, submits exact copy and verifies a permalink. It must not ask for the same authorization again. Browser login, unsupported uploads and platform challenges can still block posting. No unattended background agent or scheduler is installed.

Do not run publication from several devices at once. Each device needs this project, its current content and selection files, dependencies, Browser support and account sign-ins. These do not synchronize automatically.

## Included and excluded
Includes the 12 role skills, source references, renderers/assets, Codex wrappers, a generic local posting console service, console builder and integration instructions. Does not include brand PDFs, private operator memory, previous content, account credentials, browser sessions or publication approvals.

## Validation and limits
Plugin manifest and local packaging are validated. The console has been checked locally; actual publishing is performed by an active Codex agent through available browser controls, not by the Python service. End-to-end live publication and installation on another device have not been verified. Existing editorial/video references contain examples; setup must not adopt example identities, account IDs or claims as the recipient's facts.
