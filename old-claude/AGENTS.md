# Parked: OpenCode-specific, out of scope for now

## OpenCode harness levels

- **Global/user**: `/mnt/opencode-host` — stands in for `~/.config/opencode` (the image-baked `/home/node/.config/opencode` is hardened, not extensible).
- **Project**: the repo's `.opencode/` — rules, skills, agents, config. Project always wins over global.

Project losing to global is a harness defect to fix, not precedence.
