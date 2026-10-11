---
name: atomic-commit
description: Use whenever making changes to code, tests, rules, skills, or documentation — enforces one logical change per commit.
---

# Atomic Commit

One logical change = one commit.

## Core Principles

A commit contains exactly ONE logical change. If you notice something
else to change while working (refactor, cleanup, comment removal, TODO
update), do NOT bundle it with the current change.

Instead:
- **Make it a separate commit**, or
- **Update the plan** to include it as a distinct step

Every commit must be **tested and deployable to production**.
Never commit a change without its corresponding tests. Never
leave the codebase in a state that couldn't be shipped.

## What Counts as One Change

- Adding a feature step from a plan
- Fixing a bug
- One refactoring move (rename, extract, move)
- Adding/updating a rule or skill
- Removing dead code

## What Does NOT Count as One Change

- A feature + a refactoring that happen to touch the same file
- A bug fix + a cleanup you noticed nearby
- An implementation step + removing a TODO comment

## Red Flags

- "While I'm here, I'll also..." → **Stop. Separate commit.**
- "This is small, I'll include it" → **Small ≠ same concern.**
- "It touches the same file" → **Same file ≠ same change.**
- "I'll add tests later" → **No. Tests come with the change.**
- "It works, I'll clean up next" → **If it can't ship, don't commit.**
