# LESSONS.md — Memory Index & Session History

> Index of accumulated knowledge plus the running session log. Read this before every session.
> One lesson per file under `docs/lessons/` — this file is the **index**, never the content.
> Last updated: <!-- UPDATE THIS DATE -->

---

## Lesson Index

<!-- One line per lesson file. Format:
- [short-title](lessons/short-title.md) — one-line hook for recall
Keep this in sync with docs/lessons/ on disk; the dream skill rebuilds it.
-->

---

## Architecture Decisions

Decisions live in the append-only log: see `docs/design-decisions.md`.
Do not duplicate them here — link to the ADR number if a session summary needs one.

---

## Session History

<!-- Per-session summary. Format:

### Session N — YYYY-MM-DD
- Accomplished: ...
- Learned: ... (link new lesson files)
- Status at end / next actions: ...

Dream reports also land here — see .github/skills/dream/SKILL.md.
-->

### Session 1 — <!-- DATE -->

<!-- What was accomplished, what was learned -->

---

## Memory Maintenance

When the Lesson Index exceeds ~20 entries, you spot duplicates or
contradictions, or ~10 sessions have passed since the last dream: run the
**dream** skill (`.github/skills/dream/SKILL.md`) to consolidate, prune, and
promote. Dreams run on a branch and are merged after human review — memory is
never destructively rewritten in place.
