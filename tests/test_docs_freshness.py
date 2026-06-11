"""Doc-gardening: verify documentation references match reality."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _extract_backtick_paths(text: str) -> list[str]:
    """Extract file/dir paths from backtick-quoted references."""
    candidates = re.findall(r"`([a-zA-Z0-9_./-]+\.[a-zA-Z0-9]+)`", text)
    return [c for c in candidates if "/" in c and not c.startswith("http")]


def _extract_tree_paths(text: str) -> list[str]:
    """Extract full paths from ASCII tree diagrams, resolving nesting by indent."""
    paths = []
    stack: list[str] = []
    for line in text.splitlines():
        m = re.match(r"([│ ]*)[├└]── (.+?)(?:\s{2,}#.*)?$", line)
        if not m:
            continue
        depth = len(m.group(1)) // 4
        name = m.group(2).strip().rstrip("/")
        if name.startswith("(") or name == "...":
            continue
        stack = stack[:depth]
        stack.append(name)
        paths.append("/".join(stack))
    return paths


def test_agents_md_backtick_paths_exist():
    """Every backtick-quoted file path in AGENTS.md should exist on disk."""
    agents_md = ROOT / "docs" / "AGENTS.md"
    if not agents_md.exists():
        return
    text = agents_md.read_text()
    paths = _extract_backtick_paths(text)

    example_segments = {"foo", "module", "example", "bar", "baz"}
    missing = []
    for p in paths:
        if ":" in p or p.startswith("0.") or p.endswith(".run()"):
            continue
        if any(seg in p for seg in example_segments):
            continue
        if not (ROOT / p).exists():
            missing.append(p)

    assert not missing, "AGENTS.md references files that don't exist:\n" + "\n".join(
        f"  - {p}" for p in missing
    )


def test_agents_md_tree_paths_exist():
    """Every path listed in the AGENTS.md tree diagram should exist on disk."""
    agents_md = ROOT / "docs" / "AGENTS.md"
    if not agents_md.exists():
        return
    text = agents_md.read_text()

    tree_match = re.search(r"```\n\S+/\n(.+?)```", text, re.DOTALL)
    if not tree_match:
        return

    tree_paths = _extract_tree_paths(tree_match.group(1))
    missing = []
    for name in tree_paths:
        if not (ROOT / name).exists():
            missing.append(name)

    assert not missing, "AGENTS.md tree references missing paths:\n" + "\n".join(
        f"  - {p}" for p in missing
    )


def test_root_agents_md_stays_a_pointer():
    """Root AGENTS.md must stay a thin pointer to the initializer prompt.

    Operating content (rules, loops, checklists) lives ONLY in
    .github/copilot-instructions.md. Two copies of the same rules = drift.
    Copilot Code Review can't follow pointers, so content must stay there;
    agents that read AGENTS.md can follow the pointer.
    """
    root_agents = ROOT / "AGENTS.md"
    assert root_agents.exists(), "Root AGENTS.md entrypoint is missing"
    text = root_agents.read_text()

    assert ".github/copilot-instructions.md" in text, (
        "Root AGENTS.md must point at .github/copilot-instructions.md"
    )

    forbidden_headings = [
        "Golden Rules",
        "Working Loop",
        "Definition of Done",
        "Session Start Checklist",
        "Skills",
    ]
    offending = [
        h
        for h in forbidden_headings
        if re.search(rf"^#+ .*{re.escape(h)}", text, re.MULTILINE)
    ]
    assert not offending, (
        "Root AGENTS.md is growing operating content (headings: "
        f"{offending}). Move it to .github/copilot-instructions.md and keep "
        "this file a pointer."
    )

    line_count = len(text.splitlines())
    assert line_count <= 40, (
        f"Root AGENTS.md has {line_count} lines (cap 40). It must stay a thin "
        "pointer — move content to .github/copilot-instructions.md."
    )
