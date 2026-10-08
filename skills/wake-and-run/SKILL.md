---
name: wake-and-run
description: Trigger: "wake and run in X".
version: 1.0.0
---

# wake-and-run

Keep the Mac awake for a delay, then re-invoke this agent to run a task — unattended.

## Core principle (why this exists)

A past failure used ONE object as both keep-awake AND timer (`caffeinate -t sleep`):
it expired and the Mac idle-slept the same second, so the resume couldn't be acted on.
**Fix: keep-awake and the resume timer are two SEPARATE background processes.**

- **Object A — keep-awake**: a `caffeinate`, sized to X **+ a thin bridge (2 min)**, just
  enough to still be alive when the resume fires. No resume logic depends on it. Each
  resume re-arms A for its own leg, so the bridge stays small.
- **Object B — resume timer**: a separate `sleep X` background task. Its completion
  re-invokes the agent (the reliable resume signal). When it fires, A is still holding
  the machine awake.

## Procedure

### 1. Parse args
- `X` = the delay (hours/minutes → seconds: `X_SEC`).
- `<task>` = what to do on resume. If absent, ask once.

### 2. Power fail-safe — DO THIS FIRST, never skip
Run `pmset -g batt`.
- **"AC Power"** → proceed.
- **"Battery Power"** → **STOP and tell Josian up front** (do not silently arm):
  - `caffeinate -i` does NOT prevent clamshell sleep on battery, and idle sleep isn't
    guaranteed → the resume may never fire.
  - Ask him to plug into AC. For a bulletproof guarantee on AC he can also run once
    (needs his password): `sudo pmset -c disablesleep 1` (revert with `... 0`).
  - Only proceed on battery if he explicitly accepts the risk.

### 3. Arm keep-awake (Object A) — background
Bridge = 120 s (just outlives the resume). Run in background:
```
caffeinate -dimsu -t $((X_SEC + 120))
```
Flags: `-d` no display sleep · `-i` no idle system sleep · `-m` no disk-idle sleep ·
`-s` no system sleep (AC only) · `-u` user-active · `-t` auto-expire safety net.

### 4. Arm resume timer (Object B) — background, SEPARATE call
```
sleep $X_SEC
```
Its completion re-invokes the agent. (Don't use ScheduleWakeup: clamped to 1h and does
NOT keep the machine awake — it's not the mechanism here.)

### 5. Confirm to Josian, then go quiet
State: armed for X, on AC, will resume ~`<clock time>` and run `<task>`. Note the one
prerequisite: **keep this Claude Code session / terminal alive** (resume needs the
session, not just the machine, awake).

### 6. On resume (sleep task completes → agent re-invoked)
- Sanity-check the machine is awake (it is, if A is alive).
- **Run `<task>`.**
- When done, kill the keep-awake so it doesn't linger / re-ping:
  `pkill -f 'caffeinate -dimsu -t'`
- Report the outcome.

## Overnight on a capped task (e.g. the consolidation orchestrator): ANTICIPATE, don't react

You **cannot act while capped**. When the session/credit cap hits, the agent is suspended
— it can't watch for a drain wave or re-arm anything mid-cap. So nothing here is reactive.
**Everything is pre-armed while the agent is alive, sized to outlast the cap.**

Each alive leg anticipates the next cap instead of reacting to it:
1. On resume (agent alive), launch the task.
2. **Immediately** also re-arm Object A (keep-awake) and Object B (`sleep`) for the *next*
   leg — before doing anything else, so the schedule survives even if this leg gets capped
   seconds later.
3. Size Object B to the **reset cadence** (~1h observed, unverified → retry rather than
   assume). The resume then fires after the window has reset, and relaunches the task.
4. Repeat until the task reports a genuine **queue-drain** (nothing left → stop), or morning.

So the night is a chain of pre-laid wake points, not a monitor loop. One sparse health
poll per resume is fine; never per-agent streaming (context-safe).

## One-time recipe for Josian
1. Plug into AC.
2. (Optional, bulletproof) `sudo pmset -c disablesleep 1`.
3. Say: **"wake up in 6h and run the orchestrator"** (or any task).
4. Leave the terminal/session open. Done.
