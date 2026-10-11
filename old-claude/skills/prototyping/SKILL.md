---
name: prototyping
description: Use when the user says "let's prototype", "probe this", or design/planning alternatives resist discussion and need disposable code evidence. NOT for production implementation, tests, refactors, or polishing.
---

# Prototyping

A prototype is a **probe**: disposable code built to answer a design question. The code is evidence for a decision, never the implementation of it.

## Calibrate First

State:
- The one question the probe must answer.
- The stop line: the exact point where coding stops because the question has been answered.
- What is explicitly not being probed.
- For comparison probes: the 2-3 named approaches, one sentence each.
- Any consequential assumption: "Assuming X unless you object."

If the question is not clear enough to guide code, ask at most one question and stop. Do not create worktrees or edit code until the question is sharp enough.

## One Question Rule

A prototype answers exactly one stated question, then stops. The stop line is part of the probe contract: once the stated question is answered, do not continue into adjacent seams, runnable completeness, production behavior, tests, or semantic gaps unless that work is the named question.

Prototype end-to-end means end-to-end to the stated stop line, not a runnable production-shaped flow.

Report adjacent gaps as findings. Do not fill them with code unless they are inside the one stated question.

## Shapes

**Comparison probe**

- 2-3 named approaches.
- One branch/worktree per approach.
- Used when alternatives have trade-offs discussion cannot settle.

**Question probe**

- One branch/worktree.
- Used to answer feasibility, ordering, scaffolding cost, API shape, flow impact, or semantics.

## Workflow

1. Name the one probe question, stop line, and non-goals before writing code.
2. Create all required git worktrees before launching agents.
3. Use branch names `prototype/<approach-name>`.
4. Launch agents in parallel, one per worktree, and give each agent its exact worktree path.
5. Agents write only enough code to answer the stated question up to the stop line.
6. Each agent commits the prototype on its own branch.
7. Present findings, not code: trade-offs, ordering constraints, coupling exposed, scaffolding cost, surprises, IDE/worktree paths, and useful diff commands.
8. User decides.

Create all worktrees before presenting findings or asking the user to inspect. Never create comparison worktrees sequentially or on demand after the comparison has started.

## Commit Rule

Each prototype worktree must end with one commit on its `prototype/<approach-name>` branch.

Use a normal git commit with message:

```text
🧪 [PROTOTYPE] <approach description>
```

This commit is not production history. It exists so the user can inspect the prototype from an IDE, compare branches, and preserve the evidence until a decision is made.

The prototyping workflow is explicit permission to commit these prototype branches. Do not merge, rebase, squash, polish, or otherwise reshape prototype commits unless explicitly asked.

## Agent Prompt Template

```text
Prototype: [approach name]

Question:
[The question this probe answers]

Stop line:
[The exact point where coding stops because the question is answered]

Not probing:
[Adjacent seams, production behavior, tests, semantic gaps, or completeness concerns outside this probe]

Shape:
[What minimal code should exist to expose the approach]

Rules:
- Work only in: [worktree path]
- Write disposable prototype code only
- Ignore tests, edge cases, and polish
- Stop as soon as the stated question is answered; report adjacent gaps as findings, not code
- Commit once with: 🧪 [PROTOTYPE] <approach description>
- Focus on pipeline/API shape, ordering constraints, and maintainability signals
- Return findings, surprises, commit hash, worktree path, and useful diff commands
```

## Sensing The Probe

When the user asks what the prototype means, how it affects flow, what the core changes are, with/without shape, scaffolding cost, or decision drivers, switch to **study-making**.

Inspect the prototype as evidence. Do not edit it while studying; sense-making breaks if the evidence shifts underneath it.

## Landing The Decision

A prototype decision lands in a plan, separating:
- Observations from the prototype.
- Decisions accepted.
- Semantics still under review.
- Production implementation stages.

Public/API exposure is planned only after real behavior is effective and verified. Prototype code is a reference, not a stage and not a starting point to polish into production.

## Cleanup

After the user decides and before production implementation:
- Remove prototype worktrees.
- Delete `prototype/<approach-name>` branches.
- Delete any temporary worktree-agent branches created for the probe.

Confirm before destructive cleanup unless the user already explicitly requested it.

## Useful Review Commands

```bash
git worktree list
git log --oneline main..prototype/<approach-name>
git diff main...prototype/<approach-name>
```

Adjust `main` to the actual base branch when needed.

## Rationale

Rationale: @rationale/prototypes-are-probes.md
