---
ongoing_work_file: "Ideas for the headless atomic-refactoring loop's next iterations. Empty when each is built into loop.py and SPEC.md, or dropped."
rank: 7
---

# refactor-loop

`loop.py` runs refactorer → script checks → committer until the code converges, on a target git repo. Contract in `SPEC.md`. Tested against a fake `claude` only.

Current step → 1.

- [ ] 1. **Structured exit via `--json-schema`, every worker.** Today the script parses `CHANGED/STATUS/NEXT` and `VERDICT` from free text; a malformed exit is invisible to the agent and costs a reset. With a schema the agent submits its exit, gets a validation error back, and retries in-session. Rules live in the schema: `status` an enum, `subject` maxLength 72.
  - First: one Haiku call to confirm an invalid exit comes back to the agent as an error, and where the result lands in stream-json (`structured_output`?).
- [ ] 2. **Committer drafts only.** Haiku receives the diff from the script and returns `{subject, body}`; the script commits. What the old committer (`old-claude/agents/committer.md`) carried moves:
  - to the prompt: ♻️ gitmoji, imperative, ≤72 chars, no period, body only when the why isn't obvious, no Co-Authored-By;
  - to the script: stage by name (never `-A`), skip secret-looking files (`.env`, credentials), hook reformatted files → re-stage and new commit (never amend), other hook failure → stop, hook timeout ~3 min;
  - `commit.sh` refuses the message → re-ask Haiku once with the error;
  - `commit.sh` quirks: ♻️ counts 2 chars in the subject length; a body line `Word: text` is taken for a footer.
- [ ] 3. **Model escalation passes.** Fast loops first, slower ones when the moves stop being obvious: Haiku → Sonnet → Opus for the final cleanup. A tier hands over when it converges or stalls.
  - Each pass gets a North Star: a general direction on how to get there, which may already describe the target code.
- [ ] 4. **Shared main vs own worktree.** ⚠️ Today worktree or branch only: on a reject, `git reset --hard` + `git clean -fd` wipe other agents' uncommitted work. Kept as is for now. A shared main needs:
  - the refactorer declaring its files; reset and commit scoped to them;
  - HEAD moves under the loop, so the one-new-commit and oscillation checks break.
- [ ] 5. **`commit.sh` is shared.** Other agents will call it too, and later it does the synchronization (the rebase on main, dropped for now from the old script). Decide where it lives once it serves more than the loop.
- [ ] 6. **Worker isolation.** Workers inherit the user's `settings.json` allow rules (hence the deny lists) and probably the global CLAUDE.md and rules. Check `--setting-sources` or equivalent for a clean worker context.
- [ ] 7. **First real run.** Never run against the real `claude`. How to test: to decide.
- [ ] 8. **Reviewer agent** between refactorer and committer: fresh session, gets the exact diff, returns `ok|flagged`; `flagged` → reset. (pattern nn-validation)
- [ ] 9. **Semantic audit** of a running worker's log tail. (pattern layered-watchdog)
- [ ] 10. **Heartbeat env var** for long silent test runs. (pattern heartbeat-env-var)
