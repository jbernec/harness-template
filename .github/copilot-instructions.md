# Copilot Instructions (autoload)

This file is **autoloaded** by AI coding agents working in this repository.
It defines **how to operate**, **what to read first**, and **how to keep repo docs current**.

**Last updated:** <!-- UPDATE THIS DATE -->

---

## Session Start Checklist (Do This First)

When starting a new session or conversation in this repo, **immediately** read these files before doing any work:

```
1. docs/AGENTS.md              — repo map, build commands, conventions
2. docs/LESSONS.md             — session history, pitfalls, accumulated knowledge
3. docs/architecture.md        — system-level spec
4. docs/design-decisions.md    — decision log (append-only, open + resolved)
5. .github/instincts/project.yaml — confidence-scored learned patterns; check before solving familiar problems
6. backlog task list           — run `backlog task list --plain` to see current task states
```

When picking up a backlog task, also read the matching epic / feature spec under `docs/specs/` if one exists.
For background on *why* the harness is structured this way, see `docs/harness-engineering-design.md` (reference reading, not session-start required).

---

## Available Skills

Skills live under `.github/skills/<name>/SKILL.md`. Read the SKILL.md for the
full instructions before invoking. Trigger phrases are listed in each file's
frontmatter `description`.

| Skill | When to use |
| --- | --- |
| [backlog](.github/skills/backlog/SKILL.md) | Any task involving the Backlog.md CLI — create/edit/view tasks, acceptance criteria, status changes. |
| [blog-editor](.github/skills/blog-editor/SKILL.md) | Writing or editing technical blog posts on AI, multi-agent systems, data engineering, cloud architecture. Triggers: "write a blog post", "edit my post", "polish this draft". |
| [claude-api](.github/skills/claude-api/SKILL.md) | Building, debugging, optimizing Claude/Anthropic SDK apps (prompt caching, tool use, Managed Agents, model migration 4.5→4.6→4.7). Skip for non-Anthropic SDKs. |
| [codebase-to-course](.github/skills/codebase-to-course/SKILL.md) | Turn any codebase into an interactive single-page HTML course (scroll-snap modules, code↔English translations, animated data flows, quizzes). Triggers: "turn this into a course", "explain this codebase interactively", "teach me how this code works". |
| [doc-coauthoring](.github/skills/doc-coauthoring/SKILL.md) | Structured Context → Refinement → Reader-Testing workflow for writing PRDs, design docs, decision docs, RFCs, technical specs. |
| [autoresearch](.github/skills/autoresearch/SKILL.md) | Autonomous iterative experiment loop for tasks with a measurable metric (perf, latency, bundle size, test pass rate). Defines goal + metric + scope, then loops change → test → measure → keep/discard. Skip for one-shot fixes. |
| [docx](.github/skills/docx/SKILL.md) | Creating, reading, editing Word `.docx` files — reports, memos, letters, templates with formatting, TOCs, headings. |
| [evolve](.github/skills/evolve/SKILL.md) | Promote mature instincts (confidence > 0.8) from `.github/instincts/project.yaml` into full Copilot skills under `.github/skills/learned-*/`. Run after `/learn` and `/instincts` show patterns are stable. |
| [frontend-design](.github/skills/frontend-design/SKILL.md) | Building or styling web components, pages, dashboards, landing pages. |
| [instincts](.github/skills/instincts/SKILL.md) | Show all learned instincts for this project with confidence scores, grouped by domain. Read-only dashboard over `.github/instincts/project.yaml`. |
| [karpathy-guidelines](.github/skills/karpathy-guidelines/SKILL.md) | Behavioral guardrails for any coding task — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Apply automatically when writing, reviewing, or refactoring code. |
| [learn](.github/skills/learn/SKILL.md) | Extract reusable patterns from recent work into `.github/instincts/project.yaml`. Run after completing features, fixing bugs, or at session end to capture what the project learned. |
| [mcp-builder](.github/skills/mcp-builder/SKILL.md) | Building high-quality MCP (Model Context Protocol) servers in Python (FastMCP) or TypeScript SDK that integrate external APIs/services. |
| [observe](.github/skills/observe/SKILL.md) | Start a focused observation session to analyze a specific domain or file pattern. Records findings to `.atv/observations.jsonl` for future `/learn` runs. |
| [office-hours](.github/skills/office-hours/SKILL.md) | New product ideas, "is this worth building?", brainstorming, design-doc kickoff. Invoke proactively before writing code for a new concept. |
| [pdf](.github/skills/pdf/SKILL.md) | Anything PDF — reading, extracting text/tables, merging, splitting, watermarks, forms, encryption, OCR, image extraction. |
| [pptx](.github/skills/pptx/SKILL.md) | Creating, reading, editing PowerPoint `.pptx` decks — slides, layouts, speaker notes, templates. |
| [skill-creator](.github/skills/skill-creator/SKILL.md) | Creating new skills, editing/improving existing ones, running evals, optimizing skill descriptions for better triggering. Use when iterating on anything in `.github/skills/`. |
| [unslop](.github/skills/unslop/SKILL.md) | Unified de-slop pass — code simplification + comment rot detection + design slop check. Run after completing a feature or before opening a PR to strip AI-generated generic patterns. |
| [webapp-testing](.github/skills/webapp-testing/SKILL.md) | Playwright-based testing of local web apps — verifying frontend, debugging UI, screenshots, browser logs. |
| [xlsx](.github/skills/xlsx/SKILL.md) | Spreadsheet work — `.xlsx`, `.xlsm`, `.csv`, `.tsv` reading/editing, formulas, charts, cleaning messy tabular data. |

---

## Available Evaluator Agents

Evaluator agents live under `.github/agents/<name>.agent.md`. Invoke the relevant agent(s) **before declaring work done** for any non-trivial change. They are read-only reviewers, not implementers — surface their findings, then fix or justify each one.

| Agent | Invoke when |
| --- | --- |
| [code-reviewer](.github/agents/code-reviewer.agent.md) | Any code change. Reviews quality, maintainability, correctness. |
| [security-reviewer](.github/agents/security-reviewer.agent.md) | Any change touching auth, secrets, input handling, network calls, file I/O, deserialization, or dependencies. |
| [architecture-reviewer](.github/agents/architecture-reviewer.agent.md) | Changes that cross module boundaries, introduce a new layer, or alter data flow. |

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
   Run in this order (commands are defined in the `Makefile`):

   ```bash
   make lint                              # static analysis
   make test                              # test suite
   pytest tests/test_docs_freshness.py    # doc-gardening: verifies AGENTS.md references exist on disk
   ```

4) **Document (only if needed)**
   Update repo docs per rules below.

5) **Compound (after meaningful work cycles)**
   Before ending a session or closing a task, answer these questions:
   - **Has this problem been solved here before?** Check `docs/solutions/` first. If yes, link the existing solution doc instead of duplicating.
   - **What worked?** Record the pattern so it can be reused. If the pattern is novel and reusable, add a problem→solution doc to `docs/solutions/` (low-confidence patterns can land in `.github/instincts/project.yaml` instead, then graduate to a skill or solution doc once confidence ≥ 0.8).
   - **What broke or was harder than expected?** Add a pitfall entry to `docs/LESSONS.md`.
   - **Was a non-trivial design choice made?** Append it to `docs/design-decisions.md` with context, options considered, and rationale.
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

### Update `docs/design-decisions.md` when (append-only)
- A non-trivial design choice is made (record context, options considered, decision, rationale)
- A previously open decision is resolved — add a new entry; do not edit history
- A prior decision is reversed — add a new entry citing the original

### Update `docs/specs/` when
- An epic or feature scope changes — edit the matching spec
- A new workstream begins — copy `docs/specs/EPIC-TEMPLATE.md` and fill it in before starting implementation

### Update `docs/solutions/` when
- A novel, reusable problem→solution pair has been demonstrated to work — write it up so the next session finds it

### Update `.github/instincts/project.yaml` when
- A pattern is emerging but not yet proven (low confidence). Promote to a skill or `docs/solutions/` entry when confidence ≥ 0.8

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
