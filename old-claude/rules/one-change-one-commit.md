# One Change, One Commit

## Workflow Triggers

| User says | You MUST do |
|---|---|
| "refactor", "reshape", "clean up" | Invoke **atomic-refactoring** skill |
| "implement", "fix", "feature", "add" | Invoke **test-driven-development** skill |
| "switch to refactoring" / "switch to TDD" | Change flow immediately |
| Rules, skills, docs, config changes | Invoke **atomic-commit** skill |

**Do NOT write production code without invoking the corresponding skill first.**

## Workflow Sequence

For every functional change, follow this order:

1. **Refactor first** — invoke atomic-refactoring in **directed** mode to reshape code toward the goal
2. **Implement** — invoke test-driven-development. The change is not done until the TDD cycle is complete (red-green-refactor)
3. **Clean up after** — invoke atomic-refactoring in **cleanup** mode to polish the result

**Atomic refactoring happens before and after TDD, not during.** The TDD refactor step uses the `tdd-refactorer` agent which cleans up in one pass.

## Committing

Never commit directly. Always delegate to the **committer** subagent (`subagent_type: committer`) using the Task tool.

## Test Refactoring Is a Separate Commit

Extracting test helpers (factories, builders) from existing tests is **refactoring** — commit it separately from adding new test cases. Never bundle test cleanup with new behavior in the same commit.

## Philosophy

See [workflow-rhythm.md](../../docs/docs/practices/workflow-rhythm.md) for the reasoning behind this rhythm.
