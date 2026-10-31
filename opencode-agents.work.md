---
ongoing_work_file: "Four primary OpenCode agents replace the shipped base prompt for the OpenAI models; empty when suit-astra, suit-sol, auto-astra, auto-sol run from opencode.json on the OpenCode laptop with AGENTS.md and the global rules gone."
rank: 100
---

# opencode-agents

The shipped base prompt for a GPT model id carries the posture OpenAI tunes for: persist until fully handled, bias to action, do not ask. Four agents of ours replace it wholesale, one per mode and model class, so Tab switches posture and model at once.

```
opencode.json
  suit-astra   model: astra   prompt: {prompts/system.md} {prompts/mecha-suit.md} {prompts/astra.md}
  suit-sol     model: sol     prompt: {prompts/system.md} {prompts/mecha-suit.md} {prompts/sol.md}
  auto-astra   model: astra   prompt: {prompts/system.md} {prompts/autopilot.md}  {prompts/astra.md}
  auto-sol     model: sol     prompt: {prompts/system.md} {prompts/autopilot.md}  {prompts/sol.md}
  build, plan: disable        general, explore stay
  default_agent: one of the four
```

## Decided

- An agent prompt replaces the shipped base prompt wholesale; a truthy check, so an empty prompt brings it back.
- Several `{file:…}` chain in one string inside `opencode.json` (each file read, trimmed, JSON-escaped). No include inside an agent `.md`, no per-agent `instructions` key, so the agents are declared in `opencode.json`, not as markdown files.
- AGENTS.md goes. `tools/docs/opencode.md` stays in `instructions`: the subagents need the tools too. How the rules reach the agents is open, the first step below.
- Mecha suit and autopilot share the doctrine; the autopilot module adds the handover of a whole stage and the disengagement at the first choice the plan does not settle (philosophy/collaborative-production, kairos-gates).
- Astra and Sol share the doctrine; the Sol module spells out what Astra does unprompted.
- The modules are plain text and carry over to OpenCode 2 unchanged; only `prompts/system.md` is redone there from the 2.x base, which the override also drops (see Facts).
- Each module is written with `kaizen`, after `philosophy-scout` returns the files bearing on it; one module per session.

## Hazards

- `agents/*.md` are read by OpenCode as agents too (`{agent,agents}/**/*.md`), default mode `all`, which Tab cycles. The scouts and worms need `mode: subagent` in their frontmatter.
- With build disabled and no `default_agent`, the first visible agent in alphabetical order opens the session.
- `~/.claude/CLAUDE.md` is read as the global instructions file when `~/.config/opencode/AGENTS.md` is absent. Removing the symlink is not enough if the repo serves as both homes; the Claude-compat env switch or a different layout decides.

## Steps

- [ ] One source for the rules across Claude Code and OpenCode, and the system prompt cached. Constraints: `instructions` reaches every agent, subagents included, and takes globs; a `{file:}` chain reaches only the primaries it is written in and takes no glob; Claude Code discovers `rules/` recursively (docs, memory page); a rule carrying posture, session-design, must not reach a subagent. To check in source before thinking: what varies per turn and per session in the composed system string (the environment block sits between the agent prompt and the instructions, `session/llm/request.ts` L58-78) and what OpenAI's prefix caching needs to hit. Parked: picked up after the modules.
- [ ] `prompts/mecha-suit.md`: CLAUDE.md Postures and session-design, in belt mode. gpt.txt forbade nested bullets; `rules/writing.md` asks for sub-lists; the TUI's rendering of them is unverified. ← next
- [ ] `prompts/autopilot.md`: the bounded exception, a word hands over a stage, disengage at the first unsettled choice.
- [ ] `prompts/astra.md`, `prompts/sol.md`: know-how per class.
- [ ] Wiring: `opencode.json` agents, `default_agent`, `mode: subagent` on `agents/*.md`, AGENTS.md symlink and `rules/*.md` out of `instructions`, verify on the OpenCode laptop (tools-opencode.work.md).

## Facts, verified in source

OpenCode 1.18.9, `packages/opencode/src/` (github.com/sst/opencode/blob/v1.18.9/packages/opencode/src/):

- Family prompt by substring on the model id, `session/system.ts` L27-42: muse-spark → meta.txt; gpt-4, o1, o3 → beast.txt; other gpt → codex.txt if the id has codex, else gpt.txt; gemini- → gemini.txt; claude → anthropic.txt; trinity, kimi; else default.txt. Files in `session/prompt/`.
- Composition per turn, `session/llm/request.ts` L58-78: [agent.prompt || family prompt], environment block, instructions (AGENTS.md or CLAUDE.md, config `instructions`), MCP instructions, skills, joined into one string, then the `experimental.chat.system.transform` plugin hook. Subagents go through the same loop, `tool/task.ts` L200-213; nothing gated on the parent session.
- `{file:}` substitution only through `loadConfig`, `config/variable.ts` L34-91; agent markdown is parsed raw, `config/markdown.ts` L20-34.
- Agent registry, `agent/agent.ts` L267-270: `disable: true` deletes the entry, built-ins included. Default agent L328-340. Frontmatter keys: model, mode (subagent | primary | all), prompt, permission, description, hidden, steps, temperature.
- Tab cycles `mode !== "subagent" && !hidden`, `packages/tui/src/context/local.tsx` L78.
- Astra and Sol ids are `gpt-6-astra`, `gpt-5.6-sol` (models.dev): they load gpt.txt, never beast.txt or codex.txt. An id containing `gpt-`, not `gpt-4`, not `oss`, gets `apply_patch` in place of Edit and Write, `tool/registry.ts` L292-295.
- `<system-reminder>` is emitted by the Read tool when a file carries instructions (`tool/read.ts` L356) and by the plan-mode and build-switch prompts; the only GPT-neutral line explaining it is `session/prompt/default.txt` L78, taken into `prompts/system.md`.
- Global instructions, `session/instruction.ts` L60-63, L115-120: first of `~/.config/opencode/AGENTS.md`, `~/.claude/CLAUDE.md`. Env switches: `OPENCODE_DISABLE_PROJECT_CONFIG`, `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT`.

OpenCode 2.2.4, `packages/core/src/` (github.com/sst/opencode/blob/v2.2.4/packages/core/src/):

- system[0] = agent.system || `runner/prompt/system.txt` rendered with per-tool guidance (shell, write, edit lines, `session/system-prompt.ts`), `session/model-request.ts` L111-115. system[1] = instructions joined.
- Family text by plugin, `plugin/optimize.ts`: gpt ids → `plugin/system-prompt/gpt.txt`, an id containing "astra" → gpt-astra.txt (the bias-to-action text); claude → anthropic.txt appended. An agent with `system` set: the plugin returns, nothing added (L92).
- Config keys renamed, old ones migrated: `agents`, `system`, `disabled`, `permissions`. `{file:}` chaining unchanged, `config/variable.ts` L76.
- Unverified: whether subagents still receive AGENTS.md and instructions.
