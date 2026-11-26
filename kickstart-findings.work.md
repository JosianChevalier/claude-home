---
ongoing_work_file: "Inconsistencies in the base harness noticed while building the kickstart harness: empty when the user has settled each one."
rank: 107
---

# kickstart-findings

Noticed while copying the base into `~/Projects/kickstart-harness`. None is settled here; the user settles each in this harness. The kickstart's own choice is given for reference only.

- [ ] **Store ladder said twice.** `prompts/doctrine.md` (the "State lives in…" paragraph) and `rules/documents.md` "Where it goes" hold the same ladder; OpenCode primaries load both. Kickstart: in `documents.md` only, since rules reach subagents.
- [ ] **Session design said twice.** The Doctrine section of `rules/session-design.md` repeats the "One beat per turn" paragraph of `prompts/mecha-suit.md` almost word for word.
- [ ] **Session design reaches the robot.** OpenCode loads `rules/*.md` into every agent, so the robot and the subagents get "one beat per turn", against `prompts/autopilot.md`. Kickstart: merged into `mecha-suit.md`, no rule file.
- [ ] **Two words for what the user keeps.** `session-design.md`: "the models and the harness"; `mecha-suit.md`: "the domain model and the tooling".
- [ ] **Delegation may forbid review gates.** `opencode-rules/delegation.md`: "rather than routinely rechecking the work or commissioning independent review". GPT can read it as a ban on gates run by a subagent, which the gates need (the writer does not review its own work). Kickstart: "it does not check again what the worker did", review not named.
- [ ] **Open decisions.** `rules/documents.md`: "An open decision keeps its options"; `old-claude/skills/write-plan` forbids recording unresolved questions.
- [ ] **Claude frontmatter in OpenCode.** `output-styles/extended-mind.md` is loaded by `{file:}` into the OpenCode chain with its `name`/`description` frontmatter; not verified whether OpenCode strips it.
