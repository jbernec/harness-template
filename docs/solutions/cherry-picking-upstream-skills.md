# Cherry-Picking Skills From an Upstream Multi-Skill Repo

**Applies when:** You want to install a subset of skills from a large upstream skill collection (e.g., All-The-Vibes ATV-StarterKit, anthropics/skills) without taking on the full installer or its global side effects.

---

## Problem

Upstream multi-skill repos ship in two flavors:

1. **Installer-driven**: a CLI (`npx atv-starterkit init`, `pip install ...`) that copies dozens of skills, agents, MCP config, hooks, and root-level instructions into your project. Side effects are global and overwriting.
2. **Source layouts**: skills live as individual `SKILL.md` files in a documented directory (e.g., `pkg/scaffold/templates/skills/<name>/SKILL.md`).

The full installer is the wrong tool when you only want 3-7 specific skills, when your repo already has its own `copilot-instructions.md` it doesn't want overwritten, or when the upstream uses paths (e.g., `.atv/instincts/`) that conflict with your own layout.

---

## Solution

Three steps. Total time: a few minutes per skill.

### 1. Sparse-clone the upstream repo

Avoids downloading the full history or unrelated directories.

```bash
cd /tmp && rm -rf upstream-tmp
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/<owner>/<repo>.git upstream-tmp
cd upstream-tmp
git sparse-checkout set <path-to-skills-dir>
ls <path-to-skills-dir>
```

For ATV-StarterKit specifically: `pkg/scaffold/templates/skills/`.

### 2. Copy the skills you want

```bash
for s in skill-a skill-b skill-c; do
  mkdir -p ".github/skills/$s"
  cp "/tmp/upstream-tmp/<path>/$s/SKILL.md" ".github/skills/$s/SKILL.md"
done
```

### 3. Remap upstream-specific paths

Skills that read or write project state (learning loops, observation logs, archive directories) hard-code the upstream installer's paths. Grep before declaring done:

```bash
grep -rn '\.atv/\|\.upstream-name/' .github/skills/<just-installed>/
```

Apply a `sed` remap once per path:

```bash
sed -i \
  -e 's|\.atv/instincts/project\.yaml|.github/instincts/project.yaml|g' \
  -e 's|\.atv/instincts/archive|.github/instincts/archive|g' \
  -e 's|\.atv/instincts/|.github/instincts/|g' \
  -e 's|\.atv/observations\.jsonl|.github/instincts/observations.jsonl|g' \
  .github/skills/<skill-1>/SKILL.md \
  .github/skills/<skill-2>/SKILL.md
```

Verify the grep returns empty.

---

## Schema alignment (sometimes required)

If your repo already has a placeholder file at the remapped path (e.g., `.github/instincts/project.yaml`), check whether its schema matches what the upstream skill expects:

```bash
head -20 .github/instincts/project.yaml
grep -A 20 'YAML in' .github/skills/<skill>/SKILL.md
```

If they differ and your placeholder is empty, adopt the upstream schema verbatim. If your placeholder has real data, write a one-shot migration before installing.

---

## Register and verify

1. Add a row to the skills registry table in `.github/copilot-instructions.md`.
2. Run any doc-freshness tests (`pytest tests/test_docs_freshness.py`).
3. Manually invoke one of the new skills with a trivial argument to confirm path resolution.

---

## Anti-patterns to avoid

- **Don't run the upstream installer "just to test"** — it will overwrite your `copilot-instructions.md` and add dozens of unwanted skills with no clean uninstall.
- **Don't hand-translate upstream paths inside your own wrapper layer** — that's a maintenance burden that blocks future skill updates. Remap once at install time.
- **Don't skip the grep verification** — a single missed `.atv/` reference means the skill silently creates a parallel directory and ignores your existing state.

---

## When this doesn't apply

- Skills that only ship as part of a runtime engine (hooks-driven, requires a daemon). These need the full install or a custom shim.
- Skills with binary dependencies (Rust CLI, Go binary) — copy the SKILL.md but you still need to install the underlying tool.
- Skills that depend on each other through slash-command dispatch (e.g., ATV's `/ce-plan` calls `learnings-researcher` agent). Either install the full chain or accept graceful degradation.
