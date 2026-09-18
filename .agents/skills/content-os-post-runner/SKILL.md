---
name: content-os-post-runner
description: Send the option the operator picked in the console to the live platform through the Browser plugin - upload the media, create the post, read it back and close the loop. Use when the user says post, post it, post them, send it, publish it, post the LinkedIn one, go, post all three, or after they say they clicked POST in the console.
---

# Project content OS: post-runner

Read `../../../CODEX-INTEGRATION.md` relative to this file first. Then read `../../../plugins/ai-content-team-os/skills/post-runner/SKILL.md` and its referenced resources. Resolve these paths from this skill directory. The project adapter governs host compatibility and current authorization. Apply the source workflow only to the user-requested task; loading this skill does not start a content run.

Current handoff: POST saves the selected option; the user then says post in chat. Process every authorized unpublished platform through the Browser plugin without repeated approval. Device sessions and local queues do not sync automatically. See post-runner/SKILL.md for execution and reconciliation.
