#!/usr/bin/env python3
"""Every path a skill tells an employee to read must actually be readable.

Two failure modes, both silent at runtime and both easy to introduce while editing
prose:

1. A `${CLAUDE_PLUGIN_ROOT}/...` reference pointing at a file that does not ship.
2. A memory path (`brand/x.md`, `state/y.json`) that no row in references/memory-map.md
   owns -- the map is the contract, so a path missing from it has no owner and no reader.

Run from the plugin root: python check-refs.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = sorted(ROOT.rglob("*.md"))

PLUGIN_REF = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+)")
MEMORY_REF = re.compile(r"`(brand|library|content|performance|state|research|sources|runs)/([\w./<>-]*)`")

# Paths that are patterns or operator-supplied, not fixed files.
MEMORY_EXEMPT = {
    "content/<slug>.md",
    "research/trends-YYYY-MM-DD.md",
    "research/x-scan-YYYY-MM-DD.md",
    "runs/YYYY-MM-DD.md",
}


def check_plugin_refs():
    bad = []
    for doc in DOCS:
        for m in PLUGIN_REF.finditer(doc.read_text(encoding="utf-8")):
            target = ROOT / m.group(1)
            if not target.exists():
                bad.append(f"{doc.relative_to(ROOT)}: {m.group(1)}")
    return bad


def memory_map_paths():
    text = (ROOT / "references" / "memory-map.md").read_text(encoding="utf-8")
    # Every path the map names anywhere in it, in backticks.
    return {f"{m.group(1)}/{m.group(2)}" for m in MEMORY_REF.finditer(text)}


def check_memory_refs():
    owned = memory_map_paths()
    bad = []
    for doc in DOCS:
        if doc.name == "memory-map.md":
            continue
        for m in MEMORY_REF.finditer(doc.read_text(encoding="utf-8")):
            path = f"{m.group(1)}/{m.group(2)}"
            if path in MEMORY_EXEMPT or path in owned:
                continue
            # A bare folder (`brand/`, `state/`) names no file and owns nothing.
            if m.group(2) in ("", "/"):
                continue
            bad.append(f"{doc.relative_to(ROOT)}: {path}")
    return bad


if __name__ == "__main__":
    plugin_bad = check_plugin_refs()
    memory_bad = check_memory_refs()

    for label, rows in (("dangling ${CLAUDE_PLUGIN_ROOT} reference", plugin_bad),
                        ("memory path with no row in memory-map.md", memory_bad)):
        for row in sorted(set(rows)):
            print(f"{label}: {row}")

    if plugin_bad or memory_bad:
        sys.exit(1)
    print(f"OK - {len(DOCS)} docs, every plugin reference resolves, every memory path is owned")
