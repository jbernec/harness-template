# Harness Template

A GitHub template repository for bootstrapping AI-native projects with a structured engineering harness.

Bracketed role numbers (`[1]`–`[10]`) below map to the harness roles defined in [docs/harness-engineering-design.md](docs/harness-engineering-design.md).

## What's Included

| File / Directory | Purpose |
|------|---------|
| [AGENTS.md](AGENTS.md) | Root entrypoint autoloaded by Claude Code/Codex — a thin pointer to the initializer prompt (drift-guarded by test). |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | [1] AI agent operating guide (autoloaded by Copilot). Session checklist, golden rules, working loop, skill + agent registries. |
| [.github/skills/](.github/skills) | [8] Reusable agent skills loaded on demand by trigger phrases (backlog, doc-coauthoring, frontend-design, mcp-builder, pdf, pptx, xlsx, docx, claude-api, webapp-testing, blog-editor, codebase-to-course, office-hours, autoresearch, karpathy-guidelines, unslop, observe, learn, instincts, evolve, skill-creator, …). Full registry in copilot-instructions.md, enforced by test. |
| [.github/skills/bootstrap/](.github/skills/bootstrap/SKILL.md) | Apply the template to a new project — interview, fill placeholders, wire commands, prune skills, seed backlog. |
| [.github/skills/dream/](.github/skills/dream/SKILL.md) | [11] Memory curation — Dreams-style dedupe/resolve/prune/promote pass over repo memory. |
| [.github/agents/](.github/agents) | [9] Read-only evaluator agents: [code-reviewer](.github/agents/code-reviewer.agent.md), [security-reviewer](.github/agents/security-reviewer.agent.md), [architecture-reviewer](.github/agents/architecture-reviewer.agent.md). |
| [.github/instincts/project.yaml](.github/instincts/project.yaml) | [10] Confidence-scored learned patterns (managed by `learn` / `instincts` / `evolve` skills). |
| [.github/workflows/harness-checks.yml](.github/workflows/harness-checks.yml) | CI: runs harness invariant tests + memory status on every push/PR. |
| [.github/pull_request_template.md](.github/pull_request_template.md) | Evaluator review checklist — enforces generator–evaluator separation per PR. |
| [docs/AGENTS.md](docs/AGENTS.md) | [2] Repository map for AI agents (~150 lines — a map, not a manual). |
| [docs/LESSONS.md](docs/LESSONS.md) | [3] Memory index + session history. |
| [docs/lessons/](docs/lessons) | [3] Accumulated lessons — one per file, one-line summary at top (see [TEMPLATE.md](docs/lessons/TEMPLATE.md)). |
| [docs/architecture.md](docs/architecture.md) | [4] Engineering specification skeleton. |
| [docs/design-decisions.md](docs/design-decisions.md) | [5] Decision tracking — append-only (open and resolved). |
| [docs/specs/](docs/specs) | [6] Epic / feature specs (per-workstream scope). Copy [EPIC-TEMPLATE.md](docs/specs/EPIC-TEMPLATE.md) to start one. |
| [docs/solutions/](docs/solutions) | [10] Compound knowledge — problem → solution pairs, one per file (see [TEMPLATE.md](docs/solutions/TEMPLATE.md)). |
| [docs/harness-engineering-design.md](docs/harness-engineering-design.md) | Reference design document explaining the 11 roles. |
| [backlog/config.yml](backlog/config.yml) | Backlog.md CLI configuration. |
| [backlog/tasks/](backlog/tasks) | [7] Per-feature task files with acceptance criteria. Edit only via the `backlog` CLI. |
| [src/](src) | Implementation code. |
| [tests/test_docs_freshness.py](tests/test_docs_freshness.py) | Doc-gardening: repo-map references exist on disk; root AGENTS.md stays a pointer; skill/agent registries match disk. Fails CI on drift. |
| [scripts/memory_status.py](scripts/memory_status.py) | Dream-due check — lesson count + sessions since last dream (`make memory-status`). |
| [Makefile](Makefile) | Common commands (`make test`, `make lint`, `make format`, `make memory-status`). |
| [LICENSE](LICENSE) | MIT |

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

Start an agent session and say **"bootstrap this project"** — the
[bootstrap skill](.github/skills/bootstrap/SKILL.md) interviews you once
(name, stack, commands, golden rules, scope), fills every placeholder, prunes
irrelevant carry-along skills, seeds the backlog, and verifies with
`make test`.

Manual path, if you prefer:

1. Replace `<!-- YOUR PROJECT NAME -->` and `<!-- One-line description -->` placeholders in [.github/copilot-instructions.md](.github/copilot-instructions.md) and [docs/AGENTS.md](docs/AGENTS.md).
2. Update [backlog/config.yml](backlog/config.yml) with your project name.
3. Wire real commands into [Makefile](Makefile) (`test`, `lint`, `format`) and the build/run section of [docs/AGENTS.md](docs/AGENTS.md).
4. Add project-specific golden rules to [.github/copilot-instructions.md](.github/copilot-instructions.md).
5. Prune the [.github/skills/](.github/skills) you don't need — the template ships 25+; most projects use a handful. Update the skill registry in copilot-instructions.md to match (the registry test enforces sync).
6. Run `make test` to confirm the harness invariant tests pass against your edits.
7. Start your first session. The Compound step will accumulate project-specific knowledge automatically.

## Philosophy

This harness follows principles from:

- **OpenAI Harness Engineering**: AGENTS.md as table of contents, not encyclopedia. Progressive disclosure. Enforce invariants mechanically.
- **Compound Engineering (Every)**: Plan, Work, Review, Compound. Each unit of work makes subsequent work easier.
- **Anthropic Design Principles**: Workflows over agents. Start simple, add complexity only when measured improvement justifies it.

### The Working Loop

```
Plan → Implement → Validate → Document → Compound → Repeat
                                              │
              every ~10 sessions:           Dream
                              (curate memory: dedupe, prune, promote)
```

The **Compound** step is what separates this from traditional development:
- What worked? (Pattern to reuse)
- What broke? (Lesson file in `docs/lessons/`, indexed in LESSONS.md)
- Would the system catch this next time? (If not, add a test or linter rule)

The **Dream** step keeps compounded memory true. Inspired by Anthropic's
[Dreams API](https://platform.claude.com/docs/en/managed-agents/dreams): a periodic
curation session merges duplicate lessons, resolves contradictions toward the
most recent value, prunes stale entries, and promotes mature patterns into
skills or mechanical checks — on a branch, merged after human review.

### Key Principles

- **AGENTS.md is a map, not a manual** (~100-150 lines max)
- **Doc-gardening tests** catch stale references automatically
- **P1/P2/P3 prioritization** for all findings
- **Fail fast with descriptive errors** over silent fallbacks
- **Each session compounds** by capturing learnings mechanically
- **Memory is curated, not just appended** — periodic dream sessions keep it deduplicated, current, and small

## Requirements

- [Backlog.md CLI](https://github.com/backlog-md/backlog) for task management
- An AI coding agent (GitHub Copilot, Claude Code, Codex, etc.)
- Your project's language toolchain (Python/uv, Node/npm, etc.)

## License

MIT
