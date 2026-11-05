---
name: hooks
description: Writing a hook.
---

# Hooks

A hook's script is never reached by agents, so it stays out of the tools list (no `# platforms:` line). It still has to be understood: it lives in `hooks/`, carries a header saying what it does, and gets a line in `hooks/README.md`, the list audited now and then.
