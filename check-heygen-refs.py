"""Guard against the HeyGen docs drifting back to the legacy MCP server.

Run: python check-heygen-refs.py   (from the plugin root)

Fails if a legacy tool name reappears outside the two places that name them
deliberately, or if one of the three silently-failing request fields stops
being documented.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent

LEGACY = [
    "generate_avatar_video",
    "get_avatar_video_status",
    "get_avatar_groups",
    "get_avatars_in_avatar_group",
    "get_voices",
    "get_remaining_credits",
]

# The only files allowed to name legacy tools, because they say "these are gone".
ALLOWED = {"CONNECTORS.md", "skills/videographer/references/heygen.md"}

# Fields that fail silently or wrongly if omitted -> must stay documented.
REQUIRED = {
    "skills/videographer/references/heygen.md": [
        'aspectRatio', 'avatar_v', 'voiceSettings', 'create_video_from_avatar',
        'list_voices', 'get_current_user',
    ],
    "skills/avatar/references/build.md": [
        'aspectRatio', 'avatar_v', 'motionPrompt', 'create_video_from_avatar',
    ],
}


def main():
    errors = []

    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT).as_posix()
        if rel in ALLOWED:
            continue
        text = md.read_text(encoding="utf-8")
        for name in LEGACY:
            if name in text:
                errors.append("%s names legacy tool %s" % (rel, name))

    for rel, needles in REQUIRED.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append("%s no longer documents %s" % (rel, needle))

    if errors:
        print("FAIL")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("OK - no legacy HeyGen tool names, required fields documented")


main()
