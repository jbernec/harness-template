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
├── .github/              # copilot-instructions.md + skills/
├── docs/                 # AGENTS.md, LESSONS.md, architecture.md, design-decisions.md
├── backlog/              # Task management (CLI only)
├── tests/                # Tests + fixtures
└── ...                   # Your project directories
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
