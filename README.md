# Harness Template

A GitHub template repository for bootstrapping AI-native projects with a structured engineering harness.

Bracketed role numbers (`[1]`–`[10]`) below map to the harness roles defined in [docs/harness-engineering-design.md](docs/harness-engineering-design.md).

## What's Included

| File / Directory | Purpose |
|------|---------|
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | [1] AI agent operating guide (autoloaded). Session checklist, golden rules, 5-step working loop. |
| [.github/skills/](.github/skills) | [8] 21 reusable agent skills loaded on demand by trigger phrases (backlog, doc-coauthoring, frontend-design, mcp-builder, pdf, pptx, xlsx, docx, claude-api, webapp-testing, blog-editor, codebase-to-course, office-hours, autoresearch, karpathy-guidelines, unslop, observe, learn, instincts, evolve, skill-creator). |
| [.github/agents/](.github/agents) | [9] Read-only evaluator agents: [code-reviewer](.github/agents/code-reviewer.agent.md), [security-reviewer](.github/agents/security-reviewer.agent.md), [architecture-reviewer](.github/agents/architecture-reviewer.agent.md). |
| [.github/instincts/project.yaml](.github/instincts/project.yaml) | [10] Confidence-scored learned patterns (managed by `learn` / `instincts` / `evolve` skills). |
| [docs/AGENTS.md](docs/AGENTS.md) | [2] Repository map for AI agents (~150 lines — a map, not a manual). |
| [docs/LESSONS.md](docs/LESSONS.md) | [3] Accumulated knowledge and session history. |
| [docs/architecture.md](docs/architecture.md) | [4] Engineering specification skeleton. |
| [docs/design-decisions.md](docs/design-decisions.md) | [5] Decision tracking — append-only (open and resolved). |
| [docs/specs/](docs/specs) | [6] Epic / feature specs (per-workstream scope). Copy [EPIC-TEMPLATE.md](docs/specs/EPIC-TEMPLATE.md) to start one. |
| [docs/solutions/](docs/solutions) | [10] Compound knowledge — problem → solution pairs. |
| [docs/harness-engineering-design.md](docs/harness-engineering-design.md) | Reference design document explaining the 10 roles. |
| [backlog/config.yml](backlog/config.yml) | Backlog.md CLI configuration. |
| [backlog/tasks/](backlog/tasks) | [7] Per-feature task files with acceptance criteria. Edit only via the `backlog` CLI. |
| [src/](src) | Implementation code. |
| [tests/test_docs_freshness.py](tests/test_docs_freshness.py) | Doc-gardening: fails CI when [docs/AGENTS.md](docs/AGENTS.md) references files that don't exist on disk. |
| [Makefile](Makefile) | Common commands (`make test`, `make lint`, `make format`). |

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

1. Replace `<!-- YOUR PROJECT NAME -->` and `<!-- One-line description -->` placeholders in [.github/copilot-instructions.md](.github/copilot-instructions.md) and [docs/AGENTS.md](docs/AGENTS.md).
2. Update [backlog/config.yml](backlog/config.yml) with your project name.
3. Wire real commands into [Makefile](Makefile) (`test`, `lint`, `format`) and the build/run section of [docs/AGENTS.md](docs/AGENTS.md).
4. Add project-specific golden rules to [.github/copilot-instructions.md](.github/copilot-instructions.md).
5. Prune the [.github/skills/](.github/skills) you don't need — the template ships 21; most projects use a handful.
6. Run `pytest tests/test_docs_freshness.py` to confirm the doc-gardening test passes against your edits.
7. Start your first session. The Compound step will accumulate project-specific knowledge automatically.

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
