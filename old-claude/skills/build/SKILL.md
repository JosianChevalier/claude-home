---
name: build
description: Run Maven build with tests. Use for quick feedback during development.
---

# Build

Run Maven build with fast iteration by default, skipping ArchUnit tests.

## Usage

Use for quick feedback during development iterations.

## Default Command (Fast Build)

```bash
mvn clean test -T 4
```

**When to use:**
- During active development for fast feedback
- Iterating on code changes
- Quick validation after edits

**Benefits:**
- Skips ArchUnit architecture tests (saves significant time)
- Uses parallel execution with 4 threads (`-T 4`)
- Runs all unit, integration, and E2E tests

**Notes:**
- This is integrated in the pre-commit hook

## Full Build

```bash
mvn clean install
```

**When to use:**
- After structural changes

**Includes:**
- All tests (unit, integration, E2E, ArchUnit)
- ArchUnit tests

**Notes:**
- This is integrated in the pipeline
