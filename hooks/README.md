# hooks

Scripts the harness runs on its own events, never called by agents, so absent from the tools list. Listed here for an audit now and then; each script's header says what it does.

- `make-tmpdir`: SessionStart, recreates the private `TMPDIR` folder after macOS empties `/tmp` on reboot.
- `document-tools-for-cloud-sessions`: SessionStart of the project settings, prints the tools list in a cloud session.

A hook added, changed or removed updates its line here.
