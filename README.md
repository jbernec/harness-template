# Harness Template

A GitHub template repository for bootstrapping AI-native projects with a structured engineering harness.

## What's Included

| File | Purpose |
|------|---------|
| `.github/copilot-instructions.md` | AI agent operating guide (autoloaded). 5-step working loop with compound step. |
| `docs/AGENTS.md` | Repository map for AI agents (~100 lines, a map not a manual) |
| `docs/LESSONS.md` | Accumulated knowledge and session history |
| `docs/architecture.md` | Engineering specification skeleton |
| `docs/design-decisions.md` | Decision tracking (open and resolved) |
| `backlog/config.yml` | Backlog.md CLI configuration |
| `tests/test_docs_freshness.py` | Doc-gardening: verifies AGENTS.md references exist on disk |
| `.github/skills/` | Reusable AI agent skills (backlog, frontend-design) |
| `Makefile` | Common commands (test, lint, format) |

## Usage

### From GitHub

1. Click **"Use this template"** on the repo page
2. Name your new project
3. Clone and start building

### Manual

```bash
git clone https://github.com/YOUR_USERNAME/harness-template.git my-project
cd my-project
# Remove template git history
rm -rf .git && git init
```

## First Steps After Cloning

1. Update `<!-- YOUR PROJECT NAME -->` placeholders in all docs
2. Update `backlog/config.yml` with your project name
3. Add your build/lint/test commands to the `Makefile` and `copilot-instructions.md`
4. Add project-specific golden rules to `copilot-instructions.md`
5. Start your first session. The compound step will build project-specific knowledge automatically.

## Philosophy

This harness follows principles from:

- **OpenAI Harness Engineering**: AGENTS.md as table of contents, not encyclopedia. Progressive disclosure. Enforce invariants mechanically.
- **Compound Engineering (Every)**: Plan, Work, Review, Compound. Each unit of work makes subsequent work easier.
- **Anthropic Design Principles**: Workflows over agents. Start simple, add complexity only when measured improvement justifies it.

### The 5-Step Working Loop

```
Plan → Implement → Validate → Document → Compound → Repeat
```

The **Compound** step (step 5) is what separates this from traditional development:
- What worked? (Pattern to reuse)
- What broke? (Pitfall to record in LESSONS.md)
- Would the system catch this next time? (If not, add a test or linter rule)

### Key Principles

- **AGENTS.md is a map, not a manual** (~100-150 lines max)
- **Doc-gardening tests** catch stale references automatically
- **P1/P2/P3 prioritization** for all findings
- **Fail fast with descriptive errors** over silent fallbacks
- **Each session compounds** by capturing learnings mechanically

## Requirements

- [Backlog.md CLI](https://github.com/backlog-md/backlog) for task management
- An AI coding agent (GitHub Copilot, Claude Code, Codex, etc.)
- Your project's language toolchain (Python/uv, Node/npm, etc.)

## License

MIT
