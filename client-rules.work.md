---
ongoing_work_file: "Each rule loaded where its reader needs it: Claude's main session, Claude's subagents, or OpenCode. Empty when the steps below are done."
rank: 9
---

# Client rules

```
 rule                              home                         reaches
 writing (Extended mind)     ✔     output-styles/extended-mind.md Claude main session + forks
 delegation                  ✔     CLAUDE.md, one section       main + general/custom subagents (not Explore, Plan)
 subtraction + no decision logs    rules/                       main + general/custom subagents
 OpenCode                          AGENTS.md or prompts         OpenCode only
```

## Steps

- [ ] 3. A rule for subagents against additive bias and decision logs, reusing `rules/subtraction.md` and the kickstart-harness wording: not a secret diary, not a bureaucrat's record, not the trial; write the conclusion. Repeating the main session's prompts is fine.
- [ ] 4. `output-styles/extended-mind.gpt.md`, the GPT version of `extended-mind.md`: same five parts, more verbose, part 3 with `~/Projects/kickstart-harness/prompts/draw.md` in full (shapes, Tufte, Lakoff, both example drawings). Loaded by `{file:}` in OpenCode's agent prompts, replacing the stopgap copy `opencode-rules/writing.md`. No plain-language lines (Gowers, Feynman). Coupled to `opencode-agents.work.md`.

## Decided

- Rules differ per client: the models answer differently. Prompts may be shared where they fit both.
- Caching does not decide placement: system prompt, CLAUDE.md and rules all sit in the cached prefix, shared across sessions in the same folder within the TTL (docs: code.claude.com/docs/en/prompt-caching).
- Restarting to load an edited rule costs nothing.

## Parked

- The git status snapshot at startup differs between sessions and cuts the cross-session cache. Ideally it comes after CLAUDE.md and rules.
