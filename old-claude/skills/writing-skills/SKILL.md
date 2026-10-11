---
name: writing-skills
description: Use when creating or modifying skills in .ai/skills/. Ensures skills are well-structured and load context only when invoked. Also load the writing-rules skill for the full picture.
---

# Writing Skills

Skills are on-demand context — loaded only when invoked. Use skills for temporal concerns: activities, processes, flows.

## Two Flavors

### Workflow Skills

Describe **how to do something** — a sequence of steps with a clear end (e.g., TDD cycle, commit flow). These have concrete steps and exit criteria.

### Context Skills

Provide **dynamic guidance** for an ongoing activity — coding style, review posture, logging policy. No defined end; they stay active as long as the activity is relevant.

Both flavors share the same structure — the difference is whether the skill has exit criteria or not.

## When to Use a Skill (Not a Rule)

If the guidance is **always true regardless of activity** → rule.
If it depends on **what you're currently doing** → skill.

## Structure

```markdown
---
name: skill-name
description: Trigger condition — when to invoke and when NOT to.
---

# Skill Title

[Concrete guidance — steps for workflows, principles for context skills]
```

## Principles

- **Trigger section** — clear invoke/don't-invoke conditions in the YAML description.
- **Concrete** — actionable guidance, not vague advice.
- **Self-contained** — carry enough context to execute; reference rules/files via `@` if needed.

## Checklist

1. Does an existing skill already cover this? → Update it.
2. Is this a permanent constraint, not activity-dependent? → It's a rule, not a skill.
3. Does the description clearly state when to trigger?
