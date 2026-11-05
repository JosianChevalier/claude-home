# hooks

Scripts the harness runs on its own events, never the agent: each is wired in a `settings.json` hook, and none appears in the tools list agents receive. What agents call lives in `tools/`.

- `make-tmpdir`: SessionStart hook of `settings.json` and its template. Recreates the private folder `TMPDIR` names (`/tmp/claude`, mode `0700`) after macOS empties `/tmp` on reboot, through the shared check `tools/harness_temp_dir.py`.
- `document-tools-for-cloud-sessions`: SessionStart hook of the project's `.claude/settings.json`. In a cloud session, where no home `settings.json` prints the tools list, it prints it; silent locally.

A hook added, changed or removed is documented here in the same commit: one line naming the script, the event and settings file that run it, and what it is for. The script's own comment header carries the detail.
