# Branch Hygiene

## Trunk-Based Development

The main approach is **trunk-based development** — all work targets `main`.

Branches exist only to **avoid commit conflicts** when multiple agents work in parallel via **git worktrees** (see `scripts/sidequest.sh`). Changes are rebased and fast-forward merged back onto `main` via `end_quest`, or cherry picked manually by the developper as your work.

## Rebase on Local Main

When working on a branch, **rebase on local `main` periodically** — ideally at each refactoring/TDD cycle boundary (i.e. after each commit).

```sh
git fetch origin main && git rebase main
```

This keeps the branch close to trunk and avoids divergences to ensure agents are working in sync.

## Worktree Path Discipline

When working in a worktree (`Projects/worktrees/*`), **all file operations must use worktree paths**. The IDE may provide paths pointing to the main repo (`Projects/bms-supervision-service/`) via system reminders — never use those paths directly. Translate them to the worktree equivalent before reading, editing, or committing.
