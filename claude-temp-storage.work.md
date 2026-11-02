---
ongoing_work_file: "Claude's launcher supplies a private HARNESS_TMPDIR to the shared scripts; empty when the environment, ownership, permissions and actual tool execution are verified."
rank: 1
---

# Claude's private temporary-storage environment

## Target

This side task configures Claude's environment after shared-script support is available. The scripts read `HARNESS_TMPDIR`; Claude supplies its own directory, owned by the invoking OS user with mode `0700`. This isolates other ordinary users, not processes running under the same account or a privileged administrator.

Claude should use a directory under a valid `XDG_RUNTIME_DIR`, or a private `~/.cache/harness/claude` directory when no runtime directory is available. The cache fallback needs an explicit cleanup policy; it is not automatically temporary. Configure the inherited launch environment rather than assuming shell expansion inside a settings file.

Shared-script implementation and OpenCode container setup belong to the separate temporary-storage implementation task. Configure Claude against the scripts' actual contract; do not duplicate that implementation here.

## Remaining work

- [ ] Inspect Claude's actual launcher and environment setup with the user. Choose the private directory and how the variable reaches tool subprocesses. The shared scripts now accept a nonempty `HARNESS_TMPDIR` as an absolute path with existing non-symlink parents; they create the final directory if missing, require ownership by the invoking OS user, set mode `0700`, and reject unsafe state files. An unset variable retains legacy `/tmp` paths. Do not inspect credentials. ← next
- [ ] Configure Claude's inherited launch environment and narrowly scoped filesystem permissions where required. Verify directory ownership and mode; preserve Claude's instruction text and unrelated permissions. Shell exports cannot change an already running session's environment.
- [ ] Apply the scripts' state-transition procedure, or coordinate a fresh Claude session. Verify notebook reuse and philosophy-exploration state through real tool calls, with storage separate from OpenCode's. If using the home-cache fallback, settle cleanup.

## Boundaries

No blanket `/tmp` allowance. OpenCode external-directory permissions govern tool approval, not a shell filesystem sandbox. No change to `CLAUDE.md`, `AGENTS.md`, the conversational rules or the agent prompts is needed for this work.
