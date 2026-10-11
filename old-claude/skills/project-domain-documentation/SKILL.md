---
name: project-domain-documentation
description: Use when improving project harness domain information or documentation rules, especially .opencode/rules that explain business concepts, vocabulary, gotchas, or implementation orientation. NOT for application docs or code changes.
---

# Project Domain Documentation

Use this as a sub-skill during harness improvement for project-local domain rules and documentation.

## Target

Write project harness material that gives agents enough domain comprehension to reason correctly, without turning rules into reference docs.

Prefer project-local `.opencode/rules/` for stable agent guidance. Prefer `.opencode/rationale/` for why a rule exists or why a structure was chosen.

## Shape

Domain rules should usually contain only:

- **Domain**: the business concept and its boundaries.
- **Rationale**: pointers or short reasons; move deep why to `.opencode/rationale/`.
- **Gotchas**: traps likely to cause wrong edits or wrong explanations.
- **Implementation**: very high-level map of the existing implementation.

## Constraints

- Rework existing domain/vocabulary rules before adding files.
- Keep rules concise; omit field inventories, API walkthroughs, and code-level details unless they prevent recurring mistakes.
- Use the project vocabulary; names are the compression.
- If the user gives a reason or you discover one, preserve it in rationale, not in the operational rule body.
- If guidance is bounded to part of the repo, add `globs:` frontmatter; otherwise keep it project-wide.

## Exit Criteria

The updated project harness should answer: what is this domain thing, why does the rule exist, what will trip an agent, and where is the implementation at map-level zoom?
