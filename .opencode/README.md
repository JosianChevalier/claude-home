# Why `.opencode/` is here

This repository keeps its agents, commands, rules and skills in canonical
top-level folders. The links in this directory expose them through OpenCode's
project discovery layout without maintaining duplicate copies.

`AGENTS.md` and `opencode.json` are project-only: OpenCode loads them when the
repository itself is the working directory, not when the repository serves as
`~/.config/opencode` for work elsewhere.
