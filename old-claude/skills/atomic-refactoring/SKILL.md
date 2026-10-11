---
name: atomic-refactoring
description: Use when refactoring code to enforce tiny incremental changes.
---

# Atomic Refactoring

Refactor in the smallest possible steps. Each step is a commit. Pre-commit hooks are the safety net.

## Roles

**Orchestrator (you):** Dispatch the refactorer, commit between cycles, decide when to stop based on the refactorer's reports. Never edit code directly.

**Refactorer agent:** Makes ONE tiny change per invocation. Knows clean code — trust its judgement.

**Committer agent:** Commits after each change.

## Two Modes

### Directed Refactoring

The orchestrator has a **high-level goal** (e.g. "reshape this class to separate aggregation from disaggregation"). Used when preparing code for a feature, following a plan, or aligning structure.

```
1. Pre-load: read AGENTS.md, production code, tests
2. Invoke refactorer with the goal (direction, not steps)
3. Commit
4. Read the refactorer's report — check direction, not code
5. Repeat 2-4 until the refactorer says NOTHING_TO_REFACTOR
   or its reports show the goal is reached
6. Optionally read the final code to verify
```

**The orchestrator gives direction, not instructions.** Describe where the code should end up, not how to get there. The refactorer picks the one smallest move toward the goal each cycle.

**Check via reports, not code.** The refactorer returns a structured summary each cycle. Use it to confirm direction without loading entire files. Only read code if the reports suggest the refactorer is stuck or drifting.

### Cleanup

The orchestrator points at code **without setting a target**. Used after a TDD cycle, after implementing changes, or when the user asks for cleanup.

```
1. Pre-load: read AGENTS.md, production code, tests
2. Invoke refactorer with just the files — no goal
3. Commit
4. Read the refactorer's report — if MORE_TO_DO, repeat 2-4
5. Stop when the refactorer says NOTHING_TO_REFACTOR
```

**The refactorer is the sole judge of what to clean.** The orchestrator does not define a target — only the refactorer knows clean code principles well enough to decide what needs work and when it's done.

## Refactorer Loop

Both modes use the same inner loop:

```
loop until refactorer says NOTHING_TO_REFACTOR:
    1. refactorer  — ONE tiny change (production + tests)
    2. committer   — commits the change
```

### Refactorer agent

Dispatch with `subagent_type: "refactorer"`. Include in prompt:

- **Directed mode:** the goal (high-level direction) + relevant file paths
- **Cleanup mode:** just the file paths, no goal
- Always: "If the code is already clean, say NOTHING_TO_REFACTOR and stop."

### Committer agent

Dispatch with `subagent_type: "committer"`. Include in prompt the context of what the refactorer changed and **why** — especially the goal driving the refactoring, so the commit body explains the upcoming change this step prepares for.

## Commit Convention

Each commit message describes the single refactoring move:

```
♻️ Rename `getTemperature` to `fetchTemperature`
♻️ Extract `detectAnomalies` method from `process`
♻️ Move `BatteryCheck` to supervision.batteries package
```

## When Pre-Commit Fails

1. Read the failure output
2. If it's your change that broke it -> fix or revert
3. If it's a pre-existing issue -> do NOT bypass with `--no-verify`
4. Ask the user if unclear
