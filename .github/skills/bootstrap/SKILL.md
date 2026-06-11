---
name: bootstrap
description: >
  Apply the harness template to a new project — fill placeholders, wire real
  build/lint/test commands, seed the architecture spec and backlog, prune
  carry-along skills. Trigger phrases: "set up this project", "apply the
  template", "bootstrap", "initialize this repo". Invoke proactively on the
  first session in a fresh clone (unfilled <!-- --> placeholders are the
  signal).
---

# Bootstrap — Apply the Template to a New Project

The template ships with placeholders instead of project facts. This skill
turns "First Steps After Cloning" into an executable workflow: interview the
user once, then propagate the answers everywhere they belong. A half-filled
harness is worse than none — agents trust these files.

## 1. Detect what's unfilled

```bash
grep -rn "<!--" README.md Makefile backlog/config.yml .github/copilot-instructions.md docs/ \
  --include="*.md" --include="*.yml" | grep -iv "lessons/TEMPLATE\|solutions/TEMPLATE\|specs/EPIC-TEMPLATE\|^.*Format:"
```

Anything matching `YOUR PROJECT NAME`, `One-line description`, `UPDATE THIS
DATE`, or a TODO command stub is unfilled. If nothing is unfilled, say so and
stop — this skill is idempotent, not a re-run ritual.

## 2. Interview (one batched round, not a questionnaire)

Ask for, in a single message:

1. **Project name + one-line description**
2. **Tech stack** (language, framework, datastore)
3. **Build / lint / test / run commands** (or "let me infer from the stack" — propose, don't insist)
4. **Golden rules** — propose stack-appropriate defaults (the template's three
   are examples, not mandates) and ask what's non-negotiable for *this* project
5. **Scope** — what's explicitly in and out (feeds architecture.md)
6. **Which carry-along skills to keep** — list the current skill registry;
   domain skills irrelevant to this project (e.g. blog-editor on a backend
   service) should be deleted, folder *and* registry row (the registry test
   enforces sync)

## 3. Propagate the answers

| Target | What to fill |
| --- | --- |
| `.github/copilot-instructions.md` | Project Identity, Golden Rules, Validate commands in the working loop, Last updated date, skill registry (after pruning) |
| `docs/AGENTS.md` | Project block, tech stack, Build & Run commands, Conventions, date |
| `docs/architecture.md` | Seed from the scope answers: components, data flow, in/out of scope |
| `Makefile` | Real test/lint/format commands (keep the harness pytest line in `test`) |
| `backlog/config.yml` | Project name |
| `README.md` | Rewrite for the new project — the template's README describes the template, not your project. Keep the working-loop section if useful |
| `docs/LESSONS.md` | Date + Session 1 entry recording the bootstrap |
| `LICENSE` | Confirm MIT + copyright holder fit the new project; swap if not |

Delete pruned skill folders. Do **not** touch `docs/design-decisions.md`
entries or `docs/harness-engineering-design.md` (reference doc — keep or
delete whole, never partially edit).

## 4. Verify mechanically

```bash
make test            # harness invariants: doc-freshness, drift guard, registries
make memory-status   # should report memory OK
```

Both must pass before the bootstrap commit. If the project's own toolchain is
set up, run the real lint/test commands too.

## 5. Seed the backlog

Create the first 2–5 tasks from the interview's scope answers via the backlog
skill (`backlog task create ... --ac ...`), so the next session starts with
work, not setup.

## 6. Commit

One commit: `chore: bootstrap harness for <project name>`. Then summarize what
was filled, what was pruned, and what the first backlog task is.

## Pitfalls

- **Don't invent golden rules.** Propose, get confirmation. Rules nobody
  agreed to get ignored, and ignored rules teach agents the file is decorative.
- **Don't leave half-filled placeholders** — a file that's 80% real and 20%
  `<!-- YOUR ... -->` reads as authoritative and lies.
- **Don't delete the dream/backlog/bootstrap skills** — they're harness
  infrastructure, not carry-along domain skills.
