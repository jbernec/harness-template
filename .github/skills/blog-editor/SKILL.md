---
name: blog-editor
description: "Write or edit technical blog posts about AI, agentic systems, multi-agent workflows, LLMs, RAG, data engineering, or cloud architecture. Make sure to use this skill whenever the user asks for help producing or reviewing a long-form Markdown article — including phrases like 'write a blog post', 'draft a post', 'edit my post', 'review my draft', 'editorial review', 'proofread', 'polish this draft', 'turn this outline into a blog', or 'turn this README into a post'. Also trigger when the user does not say 'blog' explicitly but the deliverable is a public-audience long-form prose article (1000+ words) — for example 'write up what we just built for our engineering site' or 'expand these notes into an article'. Do NOT trigger for: short README updates, internal docs (use doc-coauthoring), tweets / LinkedIn posts / social copy, marketing landing pages, code comments, or commit messages."
argument-hint: "Path to a markdown file, or a topic/outline for a new post"
---

# Blog Editor

Two modes: draft a new post from an outline, or review an existing draft and produce an editorial markdown file alongside it.

## Modes

This skill operates in two modes depending on what the user provides.

### Mode 1: Write a New Post

The user provides an outline, topic, rough notes, or repository artifacts.

1. Clarify the goal: ask what the reader should walk away understanding.
2. Propose a short outline (5-8 sections max) and get approval before drafting.
3. Write the full post following the Voice and Style rules below.
4. Target 1200-2000 words. If the topic demands more, split into a series and draft part one.
5. Save the draft as a Markdown file in the location the user specifies, or next to the source material if not specified.
6. Run a self-review pass using the Editing Checklist before delivering.

### Mode 2: Edit an Existing Post

The user provides a path to a Markdown file.

1. Read the file.
2. Analyze it against every section in the Editing Checklist below.
3. Produce an editorial review saved as `{post-slug}-editorial-review.md` in the same directory as the post.
4. Summarize the key findings to the user after saving.

## Voice and Style

These rules apply to both writing and editing. When editing, flag violations with the original text quoted and a concrete rewrite.

### Tone
- Conversational. Write like you are explaining something to a smart colleague over coffee.
- Direct. Say what you mean in the fewest words that preserve meaning.
- Confident but honest. State what you know. Acknowledge what you do not.
- Accessible. The audience spans senior engineers and non-technical stakeholders. Avoid assuming deep domain knowledge without a brief explainer.

### Voice Models

The target voice blends two influences: the reported clarity of a *New York Times* feature writer and the narrative craft of a novelist. Use these as concrete techniques, not as labels to imitate.

**From the *New York Times* feature writer:**
- **Lead with a concrete scene or finding, not a thesis.** Open on a specific person, system, incident, or surprising number. The general claim earns its place in paragraph two or three, after the reader is already in.
- **Attribute claims.** When you make a non-obvious assertion, name the source: a paper, a benchmark, a deployment, a postmortem, your own experiment. Vague authority ("studies show", "experts agree") is forbidden.
- **Translate jargon on first use.** Treat every technical term as if a thoughtful reader outside the field is looking over your shoulder. A one-clause translation is enough; do not over-explain.
- **Use the nut graf.** Within the first three or four paragraphs, one paragraph should tell the reader what the piece is really about and why it matters. State the stakes plainly.
- **Show the reporting.** Concrete numbers, dates, names, code paths, and quoted log lines do more work than adjectives. Replace "fast" with "120 ms p50".
- **End with consequence, not summary.** The closing should answer "so what changes now?" — a decision, a prediction, a call to act, an open question worth holding.

**From the novelist:**
- **Scenes over summaries.** When you can dramatize a moment (a debugging session, a launch, a meeting where the design changed), do. Scene + reflection beats abstract claim + supporting bullet.
- **Specific over general.** "A senior engineer pushed back" is fiction. "Maya, three weeks from her parental leave, said the retry logic would fan out under load" is craft. Reach for the telling detail.
- **Rhythm.** Vary sentence length on purpose. A long, accumulating sentence that builds a picture, layers a qualifier, and reaches its point near the end can be followed by four words. Like that.
- **Concrete sensory or operational detail.** Even in technical writing: the color of a dashboard graph at 3am, the shape of a flame chart, the exact error message. Detail is what makes prose feel alive instead of generated.
- **A through-line.** A novelist always knows what the story is about underneath what it is about. Decide your through-line before you draft, and let every section pull on it. If a section does not, cut it.
- **Restraint.** Novelists trust the reader to do work. Resist the urge to spell out every implication. Leave one beat unsaid.

**What this voice is not:**
- Not "literary" in the purple-prose sense. No metaphors stacked three deep. No words you would have to look up.
- Not detached or institutional. The first person is welcome when you actually did the thing.
- Not breathless or promotional. The NYT half kills the hype; the novelist half kills the boilerplate.

### Hard Rules (always flag or fix)
- **No emdashes.** Use a period, comma, colon, or parentheses instead.
- **No hedging words.** Remove "just", "simply", "basically", "obviously", "really", "very", "quite", "arguably", "somewhat". If the sentence needs them to work, rewrite it.
- **No filler intros.** Delete "In this blog post, we will...", "Let's dive in", "Without further ado", "In today's article". Start with the substance.
- **No exclamation marks.** Period.
- **No AI slop.** Avoid: "revolutionize", "game-changer", "cutting-edge", "leverage" (as a verb), "utilize", "delve", "tapestry", "landscape", "paradigm shift", "unlock the power of", "at the end of the day", "it's worth noting that", "in the realm of", "harness", "seamlessly", "robust" (unless describing an actual system property), "empower", "synergy", "elevate". If you catch yourself reaching for a buzzword, use a plain word instead.
- **No excessive adverbs.** If an adverb can be removed without changing meaning, remove it. "Extremely powerful" becomes "powerful". "Significantly improves" becomes "improves".
- **Prefer active voice.** Flag passive constructions and rewrite. Exception: passive is fine when the actor is genuinely unknown or irrelevant.
- **No overuse of bullet points.** If a section has more than two consecutive bullet lists, convert at least one to prose. Bullet lists are for scannable reference items, not for narrating a story.

### Soft Guidelines (use judgment)
- Sentence fragments are fine if they land with impact.
- Short paragraphs (2-4 sentences) work better on screens than long blocks.
- One idea per paragraph.
- Vary sentence length. Follow a long sentence with a short one.
- Use code snippets when they clarify. Do not use them as filler. If a post includes code, it should be explained, not just dumped.
- Analogies are good when they are precise. Loose analogies confuse more than they help.
- Use "you" to address the reader. Avoid "we" unless describing collaborative work you actually did.

## Editing Checklist

When editing a post, evaluate every dimension below. If a section has no issues, write "No issues found" in one line. Do not invent problems.

### Content
- **Verbosity:** Quote wordy passages. Provide a tighter rewrite.
- **Repetition:** Flag ideas that appear more than once. Note the line numbers of each occurrence.
- **Flow and Transitions:** Do sections connect logically? Flag abrupt jumps and suggest a bridge sentence.
- **Structure:** Are sections in the right order? Would reordering improve comprehension?
- **Length:** If over 2000 words, flag whether it should be condensed or split into a series.

### Technical Accuracy
- **Code examples:** Check for obvious syntax errors, anti-patterns, and missing context. Note: full validation requires execution, so flag anything uncertain rather than asserting correctness.
- **Technical claims:** Flag statements that seem wrong or would benefit from a source link.
- **Terminology:** Ensure terms are used correctly and consistently throughout.
- **Acronyms:** Every acronym should be expanded on first use.

### Writing Quality
- **Grammar and spelling:** Catch errors spell-checkers miss ("affect" vs "effect", "its" vs "it's").
- **Tone consistency:** Flag shifts between casual and formal.
- **Clarity:** Quote confusing sentences and rewrite them.
- **Jargon:** Flag unexplained technical terms. Remember the audience includes non-technical readers.

### Voice Models

Apply the seven dimensions defined in Voice and Style > Voice Models. For each, ask:

- **Lead:** Concrete scene/finding/detail, or abstract thesis? Quote and rewrite if abstract.
- **Nut graf:** Is there one within the first ~3 paragraphs? If missing, suggest one.
- **Attribution:** Any non-obvious claim without a source? Vague authority ("studies show") is a hard violation.
- **Concrete detail:** Adjective-heavy passages that could be a number, name, code path, or log line? Quote and propose the replacement.
- **Through-line:** State the post's through-line in one sentence. Flag any section that doesn't pull on it.
- **Rhythm:** Three+ consecutive sentences of similar length? Suggest where a short sentence or fragment lands.
- **Ending:** Does it answer "so what changes now?", or just summarize? If the latter, propose a consequence-based ending.

### Blog-Specific
- **Frontmatter:** Title, description, and date present? Flag generic titles, descriptions over ~160 chars, or missing dates.
- **Introduction:** Does it hook the reader and state what they will learn? Does it avoid filler phrasing?
- **Conclusion:** Does it provide closure? Does the reader know what to do next?
- **Code-to-prose ratio:** Code blocks should not dominate. Each block needs surrounding explanation.
- **Links:** Verify link text is descriptive (no "click here"). Note that link targets cannot be validated without web access.
- **SEO:** Is the title specific enough to work in search results? Is the description compelling?

### Engagement
- **Reader value:** Is it clear what the reader gains?
- **Pacing:** Does interest hold throughout, or does it drag in the middle?
- **Examples:** Are they concrete and relatable?
- **Actionability:** For tutorials, can a reader follow along end to end?

## Editorial Review Output Format

Use this structure when producing a review in Mode 2.

```markdown
# Editorial Review: {Post Title}

**Date**: {current date}
**Word Count**: {count}
**Reading Time**: ~{minutes} minutes

## Summary

{2-3 sentences: what works, what needs attention.}

## Hard Rule Violations

{Flag every violation of the Hard Rules from Voice and Style. Quote the original text and provide a rewrite.}

## Content Issues

{Verbosity, repetition, flow, structure, length.}

## Technical Accuracy

{Code issues, questionable claims, terminology.}

## Writing Quality

{Grammar, tone, clarity, jargon.}

## Voice Models

{Lead, nut graf, attribution, concrete detail, through-line, rhythm, ending. Quote the original passage and propose a specific rewrite for each issue.}

## Blog-Specific

{Frontmatter, intro, conclusion, code-to-prose, links, SEO.}

## Strengths

{Be specific about what is working well.}

## Recommendations

### Must Address
- {item with line reference}

### Should Address
- {item with line reference}

### Nice to Have
- {item with line reference}

## Edit Tracker

| # | Priority | Item | Line(s) | Status |
|---|----------|------|---------|--------|
| 1 | High | {description} | {lines} | [ ] |
| 2 | Medium | {description} | {lines} | [ ] |
```

## Scope and Calibration

Weight issues by impact on the reader, not by editorial perfectionism. A conversational tone, a sentence fragment for emphasis, or an informal aside is not a problem if it fits the post.

- A clean post should have 3 or fewer Must Address items. If every section produces a high-priority flag, recalibrate.
- Should Address and Nice to Have can be longer, but only include items with clear reader benefit.
- Every piece of feedback must reference specific text. No generic observations like "could be tighter" without quoting the passage and offering a rewrite.

## Failure Modes to Avoid

- **Over-flagging style.** The tone is conversational on purpose. Do not flag sentence fragments, contractions, or informal phrasing as errors.
- **Inventing problems.** If a section is clean, say so. Do not manufacture feedback.
- **Generic feedback.** Every comment must quote specific text and suggest a concrete fix.
- **Scope creep.** Improve what exists. Do not propose new sections or restructure the thesis unless there is a comprehension problem.
- **Inconsistent depth.** Match the volume of feedback to the volume of issues. A tight 1500-word post might warrant 5-8 notes. A rough draft might warrant 20.
- **Applying rules the author rejected.** If the user explicitly chose a phrasing or structure, respect it. Flag it once at most; do not re-flag after being overruled.

## After Completing Work

- Tell the user where you saved the file.
- Give a brief summary (3-5 sentences max) of what you wrote or found.
- If editing, mention the top 2-3 items from Must Address.
- If the user asks to apply edits, work through the Edit Tracker items one at a time, marking each complete as you go.
