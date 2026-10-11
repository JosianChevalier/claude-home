---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:** New features, bug fixes, behavior changes, large refactorings that cross component boundaries.

**Exceptions (ask your human partner):** Throwaway prototypes, generated code, configuration files.

Thinking "skip TDD just this once"? Stop. That's rationalization.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over. Don't keep it as "reference", don't "adapt" it while writing tests, don't look at it. Delete means delete.

## Two Modes

TDD operates differently depending on whether the code is **new** or **existing**.

| | New code | Existing code |
|---|---|---|
| **Test grouping** | One test (or a few tightly coupled ones) per cycle | One test per minimal shippable change |
| **GREEN step** | Only what the test requires | Only what the test requires |
| **Refactor step** | Full cleanup in one pass | Minimal — highlight functional change only |
| **Commit timing** | Every 1–3 RED-GREEN-REFACTOR cycles | After each RED-GREEN-REFACTOR cycle |
| **Goal** | Reviewer sees clean, minimal final code | Reviewer sees minimal functional diff |

**Default:** Ask the user which mode if unclear. New bounded contexts, new classes, new features = new code. Modifying live flows, changing existing behavior = existing code.

## Task Tracking — Mandatory

**Before starting any TDD cycle, create a task list using `TaskCreate` for every step in the orchestration flow.** Chain them with `addBlockedBy` so each step depends on the previous one. Mark each task `in_progress` before executing it and `completed` when done.

This is not optional. The task list is the execution checklist — it prevents skipping steps, makes progress visible, and forces sequential execution.

**Per cycle:** Create one task per orchestration step (tester, verify RED, green-implementor, verify GREEN, tdd-refactorer, verify GREEN, review test list, committer). Only proceed to the next task when the current one is completed.

**After all cycles:** Create tasks for test consolidation and harmonize refactoring.

## Language

**New tests must be written in Kotlin** (`src/test/kotlin`). Production code stays in Java unless the migration has reached that module.

## Pre-Loading

Before starting, read:

- The relevant `AGENTS.md` for the bounded context being changed
- The production code to be modified
- The existing tests for that code

If the current structure makes this change hard to slot in, stop — switch to **atomic-refactoring** to reshape the code first, then come back to TDD. The change should feel easy before you write the first test.

Pass relevant context to each subagent so they have what they need without exploring the codebase themselves.

## Test Exploration — Planning the Test Sequence

Before writing any test, list the behaviors to implement **in order of increasing complexity**. Each test should target the smallest possible behavior increment over the previous one.

Start from the simplest case (degenerate input, empty collection, default state) and build up one constraint at a time. The goal is that each GREEN phase requires only a small, obvious code change.

**After each REFACTOR step**, re-examine the production code and the remaining test list:

- Does the implementation suggest edge cases not yet listed? Add them.
- Has the design evolved in a way that changes what the next test should be? Reorder.

The test list is a living document, not a fixed plan. Update it as understanding grows. **Do not remove tests during cycles** — even if they seem redundant now. Consolidation happens once, after all cycles are complete.

## Orchestration — New Code

Commit every **1–3 RED-GREEN-REFACTOR cycles**. Batch tightly coupled tests (e.g. two edge cases of the same rule), but never accumulate all behaviors into one commit.

```
loop per behavior:
    1. tester              — writes the next failing test(s) (RED)
                              List remaining behaviors as @TestToImplement
    2. verify RED          — confirm assertion failure
    3. green-implementor   — minimal code to pass THIS test (GREEN)
    4. verify GREEN        — confirm all tests pass
    5. tdd-refactorer      — full cleanup in one pass
    6. verify GREEN        — confirm tests still pass after refactor
    7. review test list    — update remaining @TestToImplement based on what was learned
    8. committer           — commits this batch (every 1–3 cycles)
                              Include what was done AND what it's building toward

after all behaviors are done:
    9. test consolidation  — review and tighten the test suite (separate commit)
```

## Orchestration — Existing Code

**Make the change easy, then make the easy change.**

Before the TDD cycle, reshape the existing code so the change slots in with minimal disruption. Use **atomic-refactoring** in **directed** mode — give it a goal like "make room for X" or "isolate Y so it can be swapped". Commit the reshaping separately. This keeps the functional diff tiny.

One commit per RED-GREEN-REFACTOR cycle. Each cycle's diff must be minimal and shippable.

```
0. atomic-refactoring   — make the change easy (separate commit(s))

loop per behavior:
    1. tester              — writes ONE failing test (RED)
                              List remaining behaviors as @TestToImplement
    2. verify RED          — confirm assertion failure
    3. green-implementor   — minimal code to pass THIS test (GREEN)
    4. verify GREEN        — confirm all tests pass
    5. tdd-refactorer      — minimal cleanup to keep code readable
    6. verify GREEN        — confirm tests still pass
    7. review test list    — update remaining @TestToImplement based on what was learned
    8. committer           — commits this cycle
                              Include what was done AND what it's building toward

after all behaviors are done:
    9. test consolidation  — review and tighten the test suite (separate commit)
   10. atomic-refactoring  — harmonize: step back, look at the new shape in context (separate commit(s))
```

The three phases catch different things:
- **Before (step 0):** reshape so the change slots in cleanly
- **During (step 5):** clean up what was just added
- **After (step 8):** the new shape may reveal opportunities or inconsistencies that neither step 0 nor step 5 could see

Remember: continuous deployment means every commit lands in production. Never leave code in an inconsistent state. Only group tests if the changes they concern cannot be shipped individually.

## RED — Tester Agent

**MANDATORY: Use the `tester` agent (Task tool with `subagent_type: "tester"`).**

The tester writes the **next functional increment only** — one test, or a few if they are tightly coupled (e.g. two edge cases of the same rule). All remaining behaviors are listed as `@TestToImplement`, not implemented.

Include in prompt:

- What behavior to test (the next increment, not the whole feature)
- Which class/method is under test
- The expected outcome
- The remaining behaviors to list as `@TestToImplement`

The tester agent handles everything else: test structure, stubs, compilation, and verification that the test fails at assertion level.

**Live flow safety:** If the test requires adding methods to an SPI or modifying an adapter that is already called in production, invoke the **safe-rollout** skill to pick the right strategy (no-op, safe default, etc.). Never ship `UnsupportedOperationException` on a live path. See the `continuous-deployment` rule.

## Verify RED — Watch It Fail

**MANDATORY. Never skip.**

Confirm the tester agent's output:
- Test fails (not errors)
- Failure is an **assertion failure** (e.g. "expected true but was false")
- Fails because stub returns wrong value (not typos, not compilation)

**RED means execution failure, not compilation failure.** The test must compile, run, and fail at the assertion. A compilation error is not RED — it's broken code.

**Test passes?** You're testing existing behavior. Fix test.

**Test errors or doesn't compile?** Fix error, re-run until it fails correctly at assertion.

## GREEN — Green-Implementor Agent

Dispatch with `subagent_type: "green-implementor"`. Include in prompt:

- The failing test (file path and content)
- The production class to modify
- "Write the MINIMAL code to make THIS test pass. Do not implement the whole feature — solve for this one test only."

The GREEN step should be **tiny**. Hardcoded values, single `if` branches, and trivial returns are all valid — the next test will force generalization. If the diff exceeds ~20 lines of production code, the test is probably too big or the implementor is working ahead.

<Good>
```java
// Test: empty list returns zero
public double total() { return 0; }
```
Hardcoded — next test will force the real logic
</Good>

<Bad>
```java
// Test: empty list returns zero — implementor writes the full algorithm "while at it"
public double total() {
    return items.stream().mapToDouble(Item::price).sum();
}
```
Implementing ahead of tests
</Bad>

## Verify GREEN — Watch It Pass

**MANDATORY.**

Run tests. Confirm the new test passes and all existing tests still pass. If failing: fix production code, not the test.

## REFACTOR — TDD Refactorer (No Commits)

**Always dispatch. Never skip.** The refactorer carries clean code rules you don't have in context. You cannot judge whether refactoring is needed — only the refactorer can. "Looks clean to me" is not an acceptable reason to skip. If the code is already clean, the refactorer will say `NOTHING_TO_REFACTOR` — that's its call, not yours.

Dispatch with `subagent_type: "tdd-refactorer"`. Include in prompt:

- The production and test code just changed (content, not just paths)
- The mode: **new code** (full cleanup) or **existing code** (minimal cleanup to keep readable)
- "Enforce clean code. If the code is already clean, say NOTHING_TO_REFACTOR and stop."
- "Do NOT commit. Changes will be committed later."

The tdd-refactorer cleans up in **one pass** — it is NOT the atomic refactorer. It knows clean code principles but does not divide into tiny steps.

## Test Consolidation — After ALL Cycles

**Only consolidate after all RED-GREEN-REFACTOR cycles are complete.** Never delete or merge tests during the cycles — earlier tests serve as safety nets while the implementation evolves.

Once all behaviors are implemented, review the test suite for opportunities to tighten it.

**Overlapping tests.** A test for "empty list returns zero" may be a strict subset of "list with mixed values returns weighted average." If the complex test already exercises the simple case's code path, the simple test adds no safety — drop it.

**Mergeable tests.** Two tests that assert different facets of the same scenario (same setup, different assertions) can be merged into one test with multiple assertions. This reduces setup duplication without losing coverage.

**When NOT to consolidate:**
- A simple test documents an important edge case that isn't obvious from the complex test's name
- A simple test fails with a clearer error message than the complex one would
- The tests exercise genuinely different code paths, even if they look similar

Consolidation is refactoring the test suite. Same rules apply: keep tests green, one change at a time, commit after each move.

## Why Order Matters

Tests written after code pass immediately. Passing immediately proves nothing — might test wrong thing, might test implementation not behavior, might miss edge cases. You never saw it catch the bug.

Tests-after answer "What does this do?" Tests-first answer "What should this do?" Tests-after are biased by your implementation.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "I'll write the test myself inline" | Use the tester agent. That's why it exists. |
| "The tester agent is overkill for this" | The tester agent enforces the stub-first workflow. Use it. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to test. Hard to test = hard to use. |
| "Too simple to refactor" | You don't carry the clean code rules. The refactorer does. Dispatch it. |

## Red Flags — STOP and Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Compilation error instead of assertion failure
- Skipped the tester agent
- Skipped the refactorer ("looks clean enough")
- Rationalizing "just this once"

**All of these mean: Delete code. Start over with TDD.**

## @TestToImplement Discipline

A TDD cycle is **not complete** while `@TestToImplement` annotations remain in the test class. Before committing:

1. Implement each inventoried test case through its own RED-GREEN cycle
2. Or explicitly defer it with a comment explaining why (and inform the user)

Never move on to plan updates or "stage complete" with outstanding `@TestToImplement` cases.

## Verification Checklist

Before marking work complete:

- [ ] Used the tester agent for each RED phase
- [ ] Each test failed at **assertion level** (not compilation)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Dispatched tdd-refactorer after each GREEN (never skipped)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered
- [ ] No `@TestToImplement` left unaddressed

Can't check all boxes? You skipped TDD. Start over.

## Debugging Integration

Bug found? Write failing test reproducing it. Follow TDD cycle. Never fix bugs without a test.
