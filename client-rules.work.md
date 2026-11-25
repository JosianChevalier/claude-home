---
ongoing_work_file: "Each rule loaded where its reader needs it: Claude's main session, Claude's subagents, or OpenCode. Empty when the steps below are done."
rank: 9
---

# Client rules

```
 rule                              home                         reaches
 writing                     ✔     output-styles/writing.md     Claude main session + forks
 delegation                        CLAUDE.md, in clear sections main + general/custom subagents (not Explore, Plan)
 subtraction + no decision logs    rules/                       main + general/custom subagents
 OpenCode                          AGENTS.md or prompts         OpenCode only
```

## Steps

- [ ] 2. Delegation from `rules/claude/delegation.md` into `CLAUDE.md`, the file reorganized into clear sections. Half the rule addresses the worker receiving a brief, so subagents need it. **← next: propose the section layout to the user first.**
- [ ] 3. A rule for subagents against additive bias and decision logs, reusing `rules/subtraction.md` and the kickstart-harness wording: not a secret diary, not a bureaucrat's record, not the trial; write the conclusion. Repeating the main session's prompts is fine.
- [ ] 4. OpenCode writing rules, written for its model from `~/Projects/kickstart-harness/prompts/` (`map`, `draw`, `hierarchy`, `write-lean`), replacing the stopgap copy `opencode-rules/writing.md`. GPT needs `draw.md` in full; Claude needs little push to draw. Coupled to `opencode-agents.work.md`.

## Decided

- Rules differ per client: the models answer differently. Prompts may be shared where they fit both.
- Caching does not decide placement: system prompt, CLAUDE.md and rules all sit in the cached prefix, shared across sessions in the same folder within the TTL (docs: code.claude.com/docs/en/prompt-caching).
- Restarting to load an edited rule costs nothing.

## Parked

- The git status snapshot at startup differs between sessions and cuts the cross-session cache. Ideally it comes after CLAUDE.md and rules.
