# Why `.claude/` inside `~/.claude`

This repo is also a knowledge base: a cloud session or a clone in another folder
opens it as a project, to read and work on its philosophy, rules and skills with
the harness they describe active. As a project, Claude Code discovers rules,
skills, agents and commands only under `.claude/`. The four symlinks point it
back at the real folders one level up.

Opened as home (`~/.claude` itself), the links resolve to the user-level files
and load once. Checked: no duplicate in context.

A clone on a machine where this repo is also `~/.claude` loads twice, user and
project. Test setup only, not a real case.
