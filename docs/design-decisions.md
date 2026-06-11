# Design Decisions

> Open and resolved design decisions. Use this to track choices and their rationale.
> Last updated: <!-- UPDATE THIS DATE -->

---

## Resolved Decisions

<!-- Format:
### 1. Decision Title
**Context:** Why this decision matters.
**Decision:** What was chosen.
**Rationale:** Why.
**Alternatives rejected:** What else was considered.
-->

### 1. Memory curation layer modeled on Anthropic's Dreams API (2026-06-11)

**Context:** The harness had strong *write* surfaces for memory (LESSONS.md, solutions/, instincts) but no maintenance process. Append-only memory accumulates duplicates, contradictions, and stale entries, degrading every future session that reads it. Anthropic's Dreams API (Managed Agents, May 2026) formalized the missing layer: a scheduled synthesis pass that reads a memory store + past sessions and produces a reorganized output store.

**Decision:** Add component [11] Memory Curation as a local analog of the Dreams pipeline — a `dream` skill that merges duplicates, resolves contradictions toward the most recent value (Decision Log as authority), prunes stale entries, promotes mature patterns (instinct → skill, lesson → mechanical check), and surfaces cross-session patterns. Restructure lessons to one-per-file under `docs/lessons/` with `docs/LESSONS.md` as the index, per Anthropic's file-based memory guidance. Add a root `AGENTS.md` entrypoint so Claude Code/Codex autoload the harness.

**Rationale:** Memory should compound, not rot. The two Dreams safety properties carry over: curation never destroys inputs in place (branch + human review; git history preserves pre-dream state), and curation is synthesis, not line-editing.

**Alternatives rejected:**
- *Hand-curating LESSONS.md ad hoc* — unscheduled, unauditable, and tends to silently rewrite history; no review gate.
- *Keeping one monolithic LESSONS.md* — can't update/delete individual lessons safely, and recall degrades as the file grows; contradicts current per-file memory guidance.
- *Letting work sessions curate as they go* — curation competes for context with the actual task; the Dreams model deliberately separates work sessions from curation sessions.
- *Depending on the hosted Dreams API directly* — it operates on Managed Agents memory stores, not repo files; it's a gated research preview. The skill documents the API path for projects that do run on Managed Agents.

---

## Open Questions

<!-- Format:
### N. Question Title
**Context:** Background.
| Question | Options | Notes |
|----------|---------|-------|
| **Question** | (a) Option A, (b) Option B | Considerations |

**Decision:** TBD
-->
