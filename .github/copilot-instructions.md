# Copilot Instructions (autoload)

This file is **autoloaded** by AI coding agents working in this repository.
It defines **how to operate**, **what to read first**, and **how to keep repo docs current**.

**Last updated:** <!-- UPDATE THIS DATE -->

---

## Session Start Checklist (Do This First)

When starting a new session or conversation in this repo, **immediately** read these files before doing any work:

```
1. docs/AGENTS.md        — repo map, build commands, conventions
2. docs/LESSONS.md       — session history, pitfalls, accumulated knowledge
3. docs/architecture.md  — system-level spec
4. backlog task list      — run `backlog task list --plain` to see current task states
```

---

## Project Identity

**Project Name:** <!-- YOUR PROJECT NAME -->
**Description:** <!-- One-line description -->

---

## Golden Rules (Non-Negotiable)

<!-- Add your project's non-negotiable rules here. Examples: -->
- **No secrets in code** — use environment variables for all credentials.
- **No module-level network calls** — create clients lazily via singletons.
- **Async-first** — all I/O operations use async. Don't nest `asyncio.run()` inside an active event loop.

When in doubt, prefer **failing fast with a descriptive error** over silent fallbacks.

---

## Standard Working Loop (Follow Every Time)

1) **Plan**
   - Restate the task in 1-2 lines.
   - Identify the smallest diff that satisfies acceptance criteria.
   - Identify test coverage required and what must be mocked.

2) **Implement (minimal diff)**
   - Touch the fewest files possible.
   - Reuse existing patterns.

3) **Validate**
   Run in this order:

   ```bash
   # Add your lint command here
   # Add your test command here
   ```

4) **Document (only if needed)**
   Update repo docs per rules below.

5) **Compound (after meaningful work cycles)**
   Before ending a session or closing a task, answer these questions:
   - **What worked?** Record the pattern so it can be reused.
   - **What broke or was harder than expected?** Add a pitfall entry to `docs/LESSONS.md`.
   - **Would the system catch this automatically next time?** If not, add a test, a linter rule, or a convention to `docs/AGENTS.md`. Turning a lesson into a mechanical check is the highest-value compound action.

   Prioritize findings: **P1** (must fix now), **P2** (should fix soon), **P3** (nice to have).

---

## Definition of Done

A change is done only when:

- Acceptance criteria (from backlog task or the request) are satisfied
- Linter passes
- Tests pass
- No secrets added (keys/tokens/passwords/connection strings)
- Documentation updated if behavior/architecture changed

---

## Backlog Task Management

**NEVER edit task files directly — always use the `backlog` CLI.**

For task management, the full CLI reference is in the **backlog skill** at `.github/skills/backlog/SKILL.md`.

**Essential commands:**

```bash
backlog task list --plain                          # List all tasks
backlog task 42 --plain                            # View task details
backlog task create "Title" --ac "Criterion"       # Create task
backlog task edit 42 -s "In Progress" -a @myself   # Start work
backlog task edit 42 --check-ac 1                  # Check acceptance criterion
backlog task edit 42 -s Done                       # Mark done
```

---

## Updating Repo Memory Files (When to Edit What)

Keep docs accurate without creating duplication drift.

### Update `docs/LESSONS.md` when
- You discover a **new pitfall** that would save future time
- You resolve a tricky issue and want a short "don't repeat this" entry
- You want a concise session summary of impactful changes

### Update `docs/AGENTS.md` when
- Repo structure changes (new directories, moved files)
- Build/run commands change
- New conventions are introduced

### Update `docs/architecture.md` when
- Architecture changes (new layers, changed data flow)
- Major design decisions are made or revised

---

## Testing Rules

- Tests must **not** make real network calls.
- Always mock external services.
- Prefer mocking at the boundary (client/tool call site), not deep internals.

---

## If You're Unsure

- Search the repo for an existing pattern and follow it.
- Prefer the more restrictive security posture.
- Write a small test to validate assumptions before refactoring.

---
End.
