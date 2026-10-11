---
name: writing-rules
description: Use when creating or modifying rules in .ai/rules/ or .ai/composable-rules/. Ensures rules are well-scoped and context-efficient. Also load the writing-skills skill for the full picture.
---

# Writing Rules

Rules are always-on context — every token counts. Before creating a rule, exhaust alternatives (update existing rule, use a skill instead, add to an AGENTS.md).

## Global vs Composable

**Global rules** (`../../ruleses`) are loaded automatically in every conversation. Reserve for constraints that truly apply everywhere.

**Composable rules** (`../../composable-ruleses`) are generic but context-dependent — referenced from a context's `AGENTS.md` when they apply. Use composable rules for architecture styles, coding conventions, or patterns that vary across bounded contexts. **If a rule does not apply everywhere, it must be composable** — otherwise it risks enforcing wrong standards in contexts where it doesn't belong.

## Principles

- **One concept per file.**
- **Lead with the constraint**, then explain why briefly.
- **Examples** only when the constraint is ambiguous without one. Pick the example that **best incarnates the principle** — a reader should immediately see why the bad version is wrong. State the **abstract rule first**, then illustrate with a concrete example.
- **Be concise** — rules are context; verbosity is cost.
- **Name after the concept**, not the symptom.

## Checklist

1. Does an existing rule already cover this? → Update it.
2. Is this a workflow step? → It's a skill, not a rule.
3. Does it apply everywhere? → Global rule. If not → composable rule.
