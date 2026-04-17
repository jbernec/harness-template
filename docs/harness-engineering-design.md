# Harness Engineering Design for AI-Assisted Development

> A reference architecture for structuring repositories so AI coding agents can work effectively across sessions, context windows, and team members.
>
> Based on principles from Anthropic's [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) and [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps).

---

## The Problem

AI coding agents lose coherence across context windows. Without structured harnesses, they:

- **One-shot** — try to do everything at once, run out of context mid-feature
- **Declare victory early** — see partial progress and stop
- **Re-litigate decisions** — propose approaches already rejected
- **Leave broken state** — no documentation for the next session to pick up from
- **Self-evaluate poorly** — praise their own mediocre work

The solution is a **layered harness**: structured files checked into the repo that tell agents what exists, what's been done, what to do next, and what NOT to do. These files serve the same role as a thorough onboarding doc for a new engineer joining mid-project — except the "new engineer" arrives every context window.

---

## Design Principles

1. **Proximity** — context files live in the repo, next to the code. External docs (Confluence, Google Docs, Notion) are invisible to agents.
2. **Layered scope** — system-level docs for orientation, epic-level specs for workstream context, task-level AC for execution.
3. **Structured over narrative** — bullet points and tables over prose. JSON for agent-updatable state. Agents parse structure faster and corrupt it less.
4. **Append-only decisions** — decision logs are never edited, only appended. This prevents agents from re-proposing rejected approaches.
5. **Separation of generation and evaluation** — the agent doing the work should not be the agent judging it.
6. **Incremental progress** — one feature at a time, with clean handoff artifacts after each.

---

## Harness Components

### 1. Initializer Prompt

**File:** `.github/copilot-instructions.md` (auto-loaded by GitHub Copilot, Claude Code, and similar tools)

**What it is:** The first thing every agent reads. Equivalent to Anthropic's "initializer agent prompt."

**What it holds:**
- **Session Start Checklist** — ordered list of files to read before any work
- **Repo structure map** — project layout at a glance
- **Golden Rules** — non-negotiable constraints (no secrets, bounded scope, etc.)
- **Standard Working Loop** — the repeatable cycle agents follow (Plan → Implement → Validate → Document → Learn)
- **Definition of Done** — hard pass/fail criteria for when a change is complete
- **Skill and agent registries** — what specialized capabilities are available

**Why it matters:** Every new context window starts cold. This file ensures the agent orients itself identically every time, regardless of which model or tool spawns it.

**Example structure:**
```markdown
## Session Start Checklist
1. Read docs/AGENTS.md          — repo map, build commands, conventions
2. Read docs/LESSONS.md         — session history, pitfalls, accumulated knowledge
3. Read docs/architecture.md    — system-level spec
4. Check task list              — current task states

## Golden Rules
- No secrets in code — use environment variables
- Bounded scope — each agent/module has a finite responsibility
- Fail fast with descriptive errors over silent fallbacks
```

---

### 2. Repo Map

**File:** `docs/AGENTS.md`

**What it is:** A concise map of the project for agents. Not a manual — a GPS.

**What it holds:**
- Project identity and scope (what this project is, what's in/out of scope)
- Bootstrap order — which files to read and in what sequence
- Build/run/test commands
- Directory layout with brief descriptions
- Skill index — table mapping each skill to its purpose
- Security mandates and conventions

**Why it matters:** An agent arriving fresh can understand the project structure, conventions, and available tools in under 30 seconds of reading.

---

### 3. Progress File

**File:** `docs/LESSONS.md` or `docs/progress.md`

**What it is:** Running log of what happened across sessions. Equivalent to Anthropic's `claude-progress.txt`.

**What it holds:**
- **Pitfalls** — "don't repeat this" entries
- **Architecture Decisions** — brief rationale for choices made (supplements the Decision Log)
- **Session History** — per-session summaries: what was accomplished, key insights, status at end, what's next

**Why it matters:** When an agent reads this, it knows what was tried, what failed, and where to pick up. Prevents the failure mode where an agent spends tokens rediscovering solved problems.

**Tip:** Consider adding a structured JSON block at the top for fast machine parsing:
```json
{
  "last_session": "2026-04-16",
  "current_phase": "Phase 1",
  "blocked_on": ["Item X", "Item Y"],
  "next_actions": ["Task A", "Task B"],
  "completed_tasks": 3,
  "total_tasks": 13
}
```

---

### 4. System Spec

**File:** `docs/architecture.md`

**What it is:** The system-level truth. Components, data flow, constraints, and boundaries.

**What it holds:**
- Architecture diagram (ASCII, Mermaid, or image reference)
- Component descriptions and responsibilities
- Data model and layer definitions
- API shapes and integration points
- Deployment model

**Why it matters:** Scopes the entire system. An agent working on any feature can reference this to understand how their piece connects to everything else. Changes to this file should be rare — it represents stable, system-level decisions.

---

### 5. Decision Log

**File:** `docs/design-decisions.md`

**What it is:** Append-only record of architectural decisions. Follows the ADR (Architecture Decision Record) pattern.

**What it holds per entry:**
- **Context** — what problem or question prompted this decision
- **Decision** — what was chosen
- **Rationale** — why
- **Alternatives rejected** — what was considered and why it was ruled out

**Why it matters:** This is one of the highest-value harness files. Without it, agents will confidently propose approaches that were already evaluated and rejected. The "alternatives rejected" section is critical — it gives agents the negative constraints they need.

---

### 6. Epic Specs

**File:** `docs/specs/EPIC-*.md` (one per epic or large feature)

**What it is:** Per-workstream specifications. Equivalent to Anthropic's Planner output — the expanded spec that bridges architecture and individual tasks.

**What it holds:**
- Problem statement (2-3 sentences)
- Scope boundaries (what's in, what's explicitly out)
- User stories and acceptance criteria at epic level
- Technical approach (how, not why — the "why" lives in the Decision Log)
- Edge cases, risks, and dependencies on other epics

**Why it matters:** This is the layer most repos are missing. Without it, agents either read all of `architecture.md` (too broad → diluted signal → AI slop) or just the task description (too narrow → missing context). Epic specs give agents exactly the right scope for their current workstream.

```
                    SCOPE
                    ─────
architecture.md     Whole system         "What are the components?"
        │
        ▼
docs/specs/         Per epic/feature     "What are we building in this workstream?"
        │
        ▼
backlog/tasks/      Per task             "What's the acceptance criteria for this unit?"
```

---

### 7. Feature List / Task Backlog

**File:** `backlog/tasks/` or `features.json`

**What it is:** Per-feature items with acceptance criteria and completion status.

**What it holds per entry:**
- Task title and description
- Numbered acceptance criteria (checkable)
- Status (Backlog → In Progress → Done)
- Dependencies

**Why it matters:** Equivalent to Anthropic's `features.json`. Each task is a discrete unit of work with clear pass/fail criteria. Anthropic found that **agents are less likely to corrupt JSON than Markdown**, so consider JSON for any file that agents update directly.

---

### 8. Domain Skills

**File:** `.github/skills/<skill-name>/SKILL.md`

**What it is:** Specialized knowledge packages. Each skill folder contains tested instructions for a specific domain (e.g., database migrations, API design, testing patterns, deployment workflows).

**What it holds per skill:**
- Trigger phrases — when the skill should activate
- Step-by-step workflows
- Reference material and examples
- Known pitfalls

**Why it matters:** Skills scope domain knowledge. Instead of embedding all platform-specific knowledge in a single instructions file, skills are loaded on demand when a relevant task is detected. This keeps context focused and reduces noise.

---

### 9. Evaluator Agents

**File:** `.github/agents/<agent-name>.agent.md`

**What it is:** Specialized reviewer agents that evaluate work from different angles. Implements the **generator-evaluator separation** from Anthropic's harness design.

**Example agents:**
- **Code Reviewer** — language-specific patterns, testability, maintainability
- **Security Reviewer** — secrets exposure, input validation, OWASP compliance
- **Architecture Reviewer** — boundary integrity, coupling, design compliance
- **Simplicity Reviewer** — YAGNI enforcement, over-engineering detection
- **Data Reviewer** — data integrity, migration safety, PII handling

**Why it matters:** Anthropic found that agents praise their own work. Separating generation from evaluation — and tuning evaluators to be skeptical — catches issues the generator misses. A standalone evaluator is far easier to calibrate for high standards than making a generator self-critical.

---

### 10. Compound Knowledge

**File:** `docs/solutions/` + `.github/instincts/`

**What it is:** Institutional memory. Solutions to past problems and confidence-scored patterns extracted from work sessions.

**What it holds:**
- **Solutions** — problem → solution pairs documented after resolving tricky issues
- **Instincts/Patterns** — reusable patterns extracted from work, with confidence scores
- Mature patterns can be promoted into full skills

**Why it matters:** Closes the learning loop. Without this, the same mistakes repeat across sessions. With it, each session builds on the last — the team's (and the agent's) knowledge compounds.

---

## Recommended Folder Structure

> File and folder names below are **suggested conventions**, not requirements. Use whatever naming fits your team. The roles (numbered [1]–[10]) are what matter.

```
your-project/
│
├── .github/                             # Agent configuration (auto-loaded)
│   │
│   ├── copilot-instructions.md          # [1] INITIALIZER PROMPT
│   │                                    #     Session checklist, golden rules,
│   │                                    #     working loop, definition of done
│   │
│   ├── skills/                          # [8] DOMAIN SKILLS
│   │   ├── <your-domain>/               #     One folder per knowledge area
│   │   │   └── SKILL.md                 #     Instructions, workflows, pitfalls
│   │   └── ...
│   │
│   ├── agents/                          # [9] EVALUATOR AGENTS
│   │   ├── <reviewer-role>.agent.md     #     One file per reviewer persona
│   │   └── ...
│   │
│   └── instincts/                       # [10] LEARNED PATTERNS
│       └── project.yaml                 #      Confidence-scored instincts
│
├── docs/                                # Project knowledge base
│   │
│   ├── <repo-map>.md                    # [2] REPO MAP
│   │                                    #     Project identity, build commands,
│   │                                    #     directory layout, conventions
│   │
│   ├── <progress-file>.md               # [3] PROGRESS FILE
│   │                                    #     Pitfalls, session history,
│   │                                    #     what happened & what's next
│   │
│   ├── <architecture>.md                # [4] SYSTEM SPEC
│   │                                    #     Components, data flow,
│   │                                    #     constraints, deployment
│   │
│   ├── <decisions>.md                   # [5] DECISION LOG (append-only)
│   │                                    #     Context, decision, rationale,
│   │                                    #     rejected alternatives
│   │
│   ├── specs/                           # [6] EPIC / FEATURE SPECS
│   │   ├── EPIC-<workstream-a>.md       #     Per-workstream scope, user stories,
│   │   ├── EPIC-<workstream-b>.md       #     edge cases, dependencies
│   │   └── ...
│   │
│   └── solutions/                       # [10] COMPOUND KNOWLEDGE
│       ├── <solved-problem>.md          #      Problem → solution pairs
│       └── ...
│
├── backlog/                             # [7] FEATURE LIST / TASK BACKLOG
│   └── tasks/                           #     Per-feature AC + status
│       └── ...                          #     (or use features.json)
│
├── src/                                 #     Implementation code
├── tests/                               #     Automated verification
└── Makefile / package.json / etc.       #     Build harness
```

---

## How It Flows

```
┌─────────────────────────────────────────────────────────────┐
│                    NEW SESSION STARTS                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
            ┌───────────────────┐
            │ [1] INITIALIZER   │  "Read these files first..."
            │     PROMPT        │
            └────────┬──────────┘
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
┌───────────┐  ┌──────────┐  ┌───────────┐
│ [2] REPO  │  │ [3]      │  │ [5]       │
│    MAP    │  │ PROGRESS │  │ DECISION  │
│           │  │ FILE     │  │ LOG       │
└───────────┘  └──────────┘  └───────────┘
      │              │              │
      └──────────────┼──────────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  AGENT UNDERSTANDS  │
          │  • What exists      │
          │  • What happened    │
          │  • What NOT to do   │
          └──────────┬──────────┘
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
┌───────────┐  ┌──────────┐  ┌───────────┐
│ [4]       │  │ [6]      │  │ [7]       │
│ SYSTEM    │  │ EPIC     │  │ FEATURE   │
│ SPEC      │  │ SPEC     │  │ LIST      │
└───────────┘  └──────────┘  └───────────┘
      │              │              │
      └──────────────┼──────────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  AGENT PICKS TASK   │
          │  Works one feature  │
          │  at a time          │
          └──────────┬──────────┘
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
┌───────────┐  ┌──────────┐  ┌───────────┐
│ [8]       │  │          │  │ [9]       │
│ DOMAIN    │  │  IMPL.   │  │ EVALUATOR │
│ SKILLS    │  │ Code &   │  │ AGENTS    │
│           │  │  Test    │  │           │
└───────────┘  └──────────┘  └───────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  SESSION ENDS       │
          │  Update:            │
          │  • Progress file [3]│
          │  • Instincts    [10]│
          │  • Git commit       │
          └─────────────────────┘
```

---

## Alignment with Anthropic's Research

| Anthropic Principle | Harness Implementation |
|---|---|
| Initializer agent sets up environment | [1] Initializer Prompt with Session Start Checklist |
| Progress file carries state across sessions | [3] Progress File with session history |
| Feature list prevents premature completion | [7] Feature List with acceptance criteria |
| Incremental progress, one feature at a time | Standard Working Loop in [1] Initializer Prompt |
| Git history as context | Agents read `git log` during bootstrap |
| Structured artifacts for handoff | [3] Progress File session summaries + git commits |
| Planner expands prompt into spec | [4] System Spec + [6] Epic Specs |
| Generator-evaluator separation | [9] Evaluator Agents (specialized reviewers) |
| Evaluator tuned to be skeptical | Reviewer agents prompted with high standards |
| Sprint contract defines "done" per chunk | Task-level acceptance criteria in [7] Feature List |
| Context resets with clean handoff | [3] Progress File session summaries + structured status |
| Decision log prevents re-litigation | [5] Decision Log (append-only ADRs) |
| Skills scoped to domain | [8] Domain Skills loaded on demand by trigger phrases |
| Compound knowledge across sessions | [10] Compound Knowledge (solutions + instincts) |

---

## Getting Started

To adopt this pattern in your own repo:

1. **Start with the initializer prompt.** Create `.github/copilot-instructions.md` with a Session Start Checklist and your project's golden rules. This single file gives you the biggest immediate lift.

2. **Add a repo map.** Create `docs/AGENTS.md` with your project identity, directory layout, and build commands.

3. **Start a progress file.** Create `docs/LESSONS.md`. After each work session, write 3-5 lines: what you did, what broke, what's next. This is the minimum viable harness.

4. **Add the decision log when you make your first non-obvious choice.** Don't pre-populate it — add entries as decisions happen.

5. **Add epic specs when task context isn't enough.** You'll feel when this is needed: the agent starts producing generic output because it doesn't understand the workstream's purpose.

6. **Add skills and evaluator agents as complexity grows.** These are optimizations, not prerequisites.

The goal is not to fill out every file on day one. Start with the initializer prompt and progress file, then layer in components as the project's complexity demands them.

---

## Key Takeaways

- **Docs in the repo > docs in external tools.** If the AI agent can't see it, it doesn't exist.
- **Scoped specs > one big PRD.** Epic-level specs give agents the right context density. A single large PRD dilutes signal and produces AI slop.
- **Structured > narrative.** Bullets, tables, and JSON over prose paragraphs.
- **Append-only decisions > editable specs.** Never delete a rejected alternative — the negative constraint is as valuable as the positive one.
- **Separate generator from evaluator.** The agent doing the work should not judge the work.
- **Every session should leave the repo better for the next session.** Progress files, git commits, and compound knowledge ensure agents (and humans) build on previous work instead of repeating it.
