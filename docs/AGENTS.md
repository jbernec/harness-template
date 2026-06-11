# AGENTS.md — Instructions for AI Coding Agents

> This file tells AI agents (Copilot, Codex, Claude Code, etc.) how to work in this repository.
> Keep it under ~150 lines. This is a **map**, not a manual.
> Last updated: <!-- UPDATE THIS DATE -->

---

## Project

**Project Name:** <!-- YOUR PROJECT NAME -->
**Description:** <!-- One-line description -->
**Tech stack:** <!-- e.g., FastAPI, Next.js, PostgreSQL -->

---

## AI Agent Bootstrap

Before making changes, read these files in order:

1. `docs/AGENTS.md` (this file)
2. `docs/LESSONS.md`
3. `docs/architecture.md`
4. Relevant docs under `docs/` for the area you are touching

---

## Build & Run

```bash
# Add your build, lint, test, and run commands here
```

---

## Repository Layout

```
your-project/
├── AGENTS.md                            # Root entrypoint (Claude Code/Codex autoload)
├── LICENSE                              # MIT
├── .github/                             # Agent configuration (auto-loaded)
│   ├── copilot-instructions.md          # [1] Initializer prompt
│   ├── pull_request_template.md         # [9] Evaluator review checklist per PR
│   ├── workflows/                       # CI — enforce invariants mechanically
│   │   └── harness-checks.yml           #     doc-freshness + drift guard + registries + memory status
│   ├── skills/                          # [8] Domain skills (full registry in copilot-instructions.md)
│   │   ├── bootstrap/SKILL.md           # Apply template to a new project
│   │   ├── dream/SKILL.md               # [11] Memory curation
│   │   └── ...
│   ├── agents/                          # [9] Evaluator agents
│   │   ├── code-reviewer.agent.md
│   │   ├── security-reviewer.agent.md
│   │   └── architecture-reviewer.agent.md
│   └── instincts/                       # [10] Learned patterns (managed by /learn, /instincts, /evolve)
│       └── project.yaml                 # confidence-scored instincts (observations.jsonl + archive/ created on demand)
├── docs/                                # Project knowledge base
│   ├── AGENTS.md                        # [2] Repo map (this file)
│   ├── LESSONS.md                       # [3] Memory index + session history
│   ├── lessons/                         # [3] One lesson per file
│   │   └── TEMPLATE.md
│   ├── architecture.md                  # [4] System spec
│   ├── design-decisions.md              # [5] Decision log (append-only)
│   ├── harness-engineering-design.md    # Harness design reference
│   ├── specs/                           # [6] Epic / feature specs
│   │   └── EPIC-TEMPLATE.md
│   └── solutions/                       # [10] Compound knowledge
│       └── TEMPLATE.md
├── backlog/                             # [7] Task backlog
│   ├── config.yml
│   └── tasks/
├── scripts/                             # Harness utilities
│   └── memory_status.py                 # Dream-due check (make memory-status)
├── src/                                 # Implementation code
├── tests/                               # Tests + fixtures
├── Makefile                             # Build harness
└── README.md
```

Full file-level layout → `architecture.md`.

---

## Security Mandates

1. **No secrets in code** — use environment variables, never commit credentials.
2. **No module-level network calls** — create clients lazily via singletons.
3. **Input sanitization** — all user-facing text must be sanitized before rendering.

---

## Conventions

<!-- Add your project conventions here. Examples: -->
- **Async-first**: all I/O in async functions.
- **Tests mirror source**: `src/module/foo.py` → `tests/test_module/test_foo.py`.
- **One concern per file**: keep files focused.
