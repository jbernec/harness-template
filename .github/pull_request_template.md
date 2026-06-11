## Summary

<!-- What changed and why, 1-3 lines. Link the backlog task. -->

## Evaluator Review (generator–evaluator separation)

The agent (or human) that wrote this diff must not be the only one judging it.
Run the relevant evaluator agents from `.github/agents/` against the diff and
check off:

- [ ] **code-reviewer** — always required (`.github/agents/code-reviewer.agent.md`)
- [ ] **security-reviewer** — required if this touches auth, input handling, secrets, dependencies, or data exposure (`.github/agents/security-reviewer.agent.md`)
- [ ] **architecture-reviewer** — required if this changes boundaries, layers, data flow, or public interfaces (`.github/agents/architecture-reviewer.agent.md`)
- [ ] Findings triaged as P1 (fixed before merge) / P2 (task filed) / P3 (noted)

## Definition of Done

- [ ] Acceptance criteria satisfied
- [ ] Lint passes, tests pass (`make test`)
- [ ] No secrets added
- [ ] Docs updated if behavior/architecture changed
- [ ] New lessons captured in `docs/lessons/` and indexed in `docs/LESSONS.md`
