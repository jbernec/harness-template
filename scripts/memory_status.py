#!/usr/bin/env python3
"""Memory status: is a dream (memory curation) due?

Prints lesson count and sessions since the last dream, and flags DREAM DUE
when either threshold from the dream skill is crossed. Informational only —
always exits 0. Run via `make memory-status` (part of the session-start
checklist) or in CI.

Thresholds mirror .github/skills/dream/SKILL.md.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSON_THRESHOLD = 20
SESSION_THRESHOLD = 10


def count_lessons() -> int:
    lessons_dir = ROOT / "docs" / "lessons"
    if not lessons_dir.exists():
        return 0
    return len([p for p in lessons_dir.glob("*.md") if p.name != "TEMPLATE.md"])


def sessions_since_last_dream() -> int:
    """Count '### Session' headings after the last '### Dream' heading."""
    lessons_md = ROOT / "docs" / "LESSONS.md"
    if not lessons_md.exists():
        return 0
    headings = re.findall(r"^### (Session|Dream)", lessons_md.read_text(), re.MULTILINE)
    count = 0
    for kind in headings:
        if kind == "Dream":
            count = 0
        else:
            count += 1
    return count


def main() -> None:
    lessons = count_lessons()
    sessions = sessions_since_last_dream()

    print(f"lessons indexed:           {lessons} (threshold {LESSON_THRESHOLD})")
    print(f"sessions since last dream: {sessions} (threshold {SESSION_THRESHOLD})")

    if lessons > LESSON_THRESHOLD or sessions > SESSION_THRESHOLD:
        print(
            "\nDREAM DUE — run the dream skill (.github/skills/dream/SKILL.md) "
            "as its own session to consolidate memory."
        )
    else:
        print("\nmemory OK — no dream due.")


if __name__ == "__main__":
    main()
