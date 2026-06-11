---
name: dream
description: >
  Memory curation — consolidate, dedupe, and reorganize the repo's accumulated
  memory (lessons, solutions, instincts) the way Anthropic's Dreams API curates
  agent memory stores. Trigger phrases: "dream", "curate memory", "consolidate
  lessons", "clean up lessons", "memory maintenance". Also run proactively when
  the lesson index exceeds ~20 entries, when you notice duplicate or
  contradictory lessons, or every ~10 sessions.
---

# Dream — Memory Curation Skill

Agents write to repo memory as they work, but those writes are **local and
incremental**: over many sessions the memory surfaces accumulate duplicates,
contradictions, and stale entries. A *dream* is a dedicated curation session
that reads all memory surfaces plus recent session history and produces a
**reorganized memory set**: duplicates merged, contradicted entries resolved in
favor of the most recent value, stale entries pruned, and cross-session
patterns surfaced.

This mirrors Anthropic's [Dreams API](https://platform.claude.com/docs/en/managed-agents/dreams)
(Managed Agents, research preview) applied to a file-based harness. Two of its
safety properties are **non-negotiable** here:

1. **Never destroy inputs in place.** All curation happens on a dedicated
   branch (`dream/<date>`), delivered as a reviewable diff/PR. Git history
   preserves the pre-dream state; the human reviews and merges or discards.
2. **Synthesis, not line-editing.** A dream reorganizes and consolidates
   knowledge. It does not rewrite the meaning of a lesson, soften a pitfall,
   or invent entries with no evidence in the inputs.

---

## Inputs

Read **all** of these before changing anything:

| Surface | Path | Role in the dream |
| --- | --- | --- |
| Lesson files | `docs/lessons/*.md` | Primary curation target |
| Lesson index | `docs/LESSONS.md` | Must match the files on disk after the dream |
| Solutions | `docs/solutions/*.md` | Merge duplicates; promote recurring ones |
| Instincts | `.github/instincts/project.yaml` | Re-score; promote mature ones to skills |
| Decision log | `docs/design-decisions.md` | **Read-only.** Append-only by design — never edit existing entries |
| Session history | `docs/LESSONS.md` § Session History + `git log --since="<last dream>"` | Mine for patterns no single session could see |
| Skills | `.github/skills/*/SKILL.md` | Promotion target; check for drift against lessons |

Like the Dreams API (which caps input at 100 sessions), **bound the session
window**: mine history since the last dream, or the last ~30 sessions,
whichever is smaller. Older history has already been dreamed over.

## Steering

The user may pass focus instructions (e.g. "focus on testing pitfalls; leave
the frontend lessons alone"). Apply them throughout: what to read closely,
what to merge or drop, how to structure the output. Without instructions,
curate everything.

---

## The Pipeline

Work on a branch: `git checkout -b dream/<YYYY-MM-DD>`.

### 1. Inventory

List every memory entry (lessons, solutions, instincts) with its date and
one-line summary. Note entries that are: duplicated, contradicted, stale
(references files/commands/decisions that no longer exist), or vague.

### 2. Merge duplicates

Multiple lessons covering the same pitfall become one file carrying the best
explanation, the union of evidence, and the **earliest** discovery date with a
note of recurrence ("seen again in session N" — recurrence is signal).

### 3. Resolve contradictions

When two entries disagree, **the most recent value wins** — but check the
decision log first: if an ADR settled the question, the ADR is authoritative.
Mark the loser superseded and delete it; the git history of the dream branch
preserves it.

### 4. Prune stale entries

Delete lessons that reference removed code, retired tooling, or decisions
later reversed in the decision log. Verify before deleting: a lesson naming a
file that still exists is not stale just because it is old.

### 5. Promote mature knowledge

- **Instinct → skill:** instincts with `confidence >= 0.8` that keep proving
  out become a `.github/skills/<name>/SKILL.md`; remove them from
  `project.yaml` and note the promotion.
- **Recurring solution → instinct:** a `docs/solutions/` entry whose pattern
  appeared in 3+ sessions becomes a confidence-scored instinct.
- **Lesson → mechanical check:** the highest-value promotion. If a pitfall
  could be caught by a test, linter rule, or doc-freshness check, write the
  check, then delete the lesson — the system now remembers so the agent
  doesn't have to.

### 6. Surface new patterns

This is what distinguishes a dream from cleanup. Walk the session history and
git log looking for what no single session could see:

- **Recurring mistakes** — the same class of error across sessions → new lesson.
- **Converged workflows** — the same approach independently reached for
  different jobs → new instinct or skill candidate.
- **Shared preferences** — conventions repeatedly applied but never written
  down → add to `docs/AGENTS.md` § Conventions.

### 7. Rebuild the index and report

- Regenerate the Lesson Index in `docs/LESSONS.md` to exactly match
  `docs/lessons/` on disk.
- Append a **Dream Report** to the Session History:

```markdown
### Dream — YYYY-MM-DD
- Inputs: N lessons, N solutions, N instincts, sessions S..S
- Merged: <list>
- Resolved (most-recent wins): <list>
- Pruned: <list, with reasons>
- Promoted: <instinct → skill, lesson → test, ...>
- Surfaced: <new patterns, with evidence>
```

### 8. Deliver for review

Commit on the dream branch and present the diff (or open a PR). **Do not merge
to main yourself** — the human reviews the curated memory and adopts or
discards it, exactly as the Dreams API leaves the output store for review.

---

## Pitfalls

- **Don't create archive/backup folders for pruned memory.** Git history *is*
  the backup (the local equivalent of the Dreams API's immutable memory
  versions): the dream branch + review gate preserve the pre-dream state, and
  the Dream Report is the human-readable index of what was removed and why.
  Dead files left under `docs/` stay visible to glob/grep, pollute recall, and
  let superseded values get resurrected — the live memory surface must contain
  only live memory.
- **Don't curate the decision log.** It is append-only; pruning "stale" ADRs
  destroys the negative constraints that stop agents re-proposing rejected
  designs.
- **Don't dream mid-task.** Curation competes for context with real work. Run
  it as its own session.
- **Don't over-prune.** When in doubt whether a lesson is stale, keep it and
  flag it in the Dream Report for the human to decide.
- **Don't skip the report.** The report is the audit trail that makes the
  reorganization trustworthy.

---

## If this project runs on Managed Agents

When agents run as Anthropic **Managed Agents** sessions with a cloud memory
store instead of repo files, use the real Dreams API rather than this local
pipeline: `client.beta.dreams.create(inputs=[{memory_store}, {sessions}], model=...)`
with beta headers `managed-agents-2026-04-01,dreaming-2026-04-21` (SDK sets
them automatically). Poll the dream to `completed`, review the **output**
memory store, then attach it to future sessions in place of the input store.
Limits at preview: ≤100 sessions per dream, `instructions` ≤4,096 chars,
models `claude-opus-4-8` / `claude-opus-4-7` / `claude-sonnet-4-6`.
