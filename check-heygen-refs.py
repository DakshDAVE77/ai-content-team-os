"""Guard the two HeyGen decisions that cost the most to rediscover.

Run: python check-heygen-refs.py   (from the plugin root)

1. Legacy community-MCP tool names must not come back.
2. The plugin must keep saying WHY it does not render through the API. That
   decision was reached after seven test renders; without the reasoning written
   down, the next person reads "there is a create_video tool" and wires it back
   in, and the founder's voice silently becomes a different engine.
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

# Files allowed to name legacy tools, because they say "these are gone".
LEGACY_OK = {"CONNECTORS.md"}

# The reasoning that must survive edits.
REQUIRED = {
    "skills/videographer/references/heygen.md": [
        "Why the API does not render",
        "Cartesia",
        "Starfish",
        "RENDER IN HEYGEN STUDIO",
    ],
    "skills/avatar/SKILL.md": [
        "does not render",
        "Cartesia",
    ],
    "skills/avatar/references/build.md": [
        "RENDER IN HEYGEN STUDIO",
        "Starfish",
        "ALWAYS CARTESIA",
    ],
}

# The motion-file TEMPLATE must not offer API engine names as the voice engine.
# Recording "elevenlabs" there is how a founder's voice silently changes engine.
TEMPLATE_BANNED = {
    "skills/avatar/references/build.md": ["engine: <starfish"],
}

# Cartesia / Sonic 3.6 is hardcoded. If these lines go missing or become
# placeholders, a render silently comes out in whatever engine Studio defaults to.
ENGINE_HARDCODED = {
    "skills/avatar/references/build.md": ["Voice Engine: Cartesia", "Model: Sonic 3.6"],
    "skills/videographer/references/heygen.md": ["Voice Engine:  Cartesia"],
    "skills/post-runner/references/heygen-studio.md": ["**Cartesia**", "Sonic 3.6"],
}

# Generation tools. Allowed only in files that explain why they are NOT used.
GENERATORS = [
    "create_video_from_avatar",
    "create_video_from_studio",
    "create_speech",
    "generate_from_template",
    "create_video_agent",
]
GENERATORS_OK = {
    "skills/videographer/references/heygen.md",
    "skills/avatar/SKILL.md",
    "skills/avatar/references/build.md",
    "CONNECTORS.md",
    "README.md",
}


def main():
    errors = []

    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8")

        if rel not in LEGACY_OK:
            for name in LEGACY:
                if name in text:
                    errors.append("%s names legacy tool %s" % (rel, name))

        if rel not in GENERATORS_OK:
            for name in GENERATORS:
                if name in text:
                    errors.append(
                        "%s mentions %s - renders belong in Studio, not the API"
                        % (rel, name)
                    )

    for rel, phrases in TEMPLATE_BANNED.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in text:
                errors.append(
                    "%s offers API engine names in the motion template (%r) - "
                    "the voice engine is read off HeyGen Studio" % (rel, phrase)
                )

    for rel, phrases in ENGINE_HARDCODED.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(
                    "%s no longer hardcodes the voice engine (%r missing)" % (rel, phrase)
                )

    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            errors.append("missing file: %s" % rel)
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append("%s no longer explains %r" % (rel, needle))

    if errors:
        print("FAIL")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("OK - no legacy tool names, no API rendering, reasoning intact")


main()
