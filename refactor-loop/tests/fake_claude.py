#!/usr/bin/env python3
"""Fake `claude` CLI for the refactor-loop black-box tests.

Ignores its arguments. Behaviour comes from env:
  REFACTOR_LOOP_ROLE  refactorer | committer | watchdog
  FAKE_SCENARIO       see REFACTORERS below
  FAKE_STATE          dir holding per-role call counters and scenario files
cwd is the target repo. Writes stream-json to stdout.
"""
import json
import os
import subprocess
import sys
import time
import uuid
from pathlib import Path

STATE = Path(os.environ["FAKE_STATE"])
SCENARIO = os.environ.get("FAKE_SCENARIO", "")
ROLE = os.environ.get("REFACTOR_LOOP_ROLE", "")
TARGET = Path("file.txt")
MAX_SLEEP = 30
COMMIT_SH = Path(__file__).resolve().parent.parent / "commit.sh"


def emit(event):
    sys.stdout.write(json.dumps(event) + "\n")
    sys.stdout.flush()


def bump(name):
    path = STATE / f"{name}.count"
    n = int(path.read_text()) + 1 if path.exists() else 1
    path.write_text(str(n))
    return n


def report(changed, status, next_):
    return f"Done.\nCHANGED: {changed}\nSTATUS: {status}\nNEXT: {next_}"


def append_line(n):
    with TARGET.open("a") as f:
        f.write(f"step {n}\n")
    return report(f"append step {n}", "MORE_TO_DO", "append another line")


def converge(n):
    if n <= 2:
        return append_line(n)
    return report("nothing", "NOTHING_TO_REFACTOR", "n/a")


def hang(n):
    sleeper = subprocess.Popen(
        [sys.executable, "-c", f"import time; time.sleep({MAX_SLEEP})"]
    )
    with (STATE / "grandchild.pids").open("a") as f:
        f.write(f"{sleeper.pid}\n")
    time.sleep(MAX_SLEEP)
    return report("never", "MORE_TO_DO", "n/a")


def oversize(n):
    Path("big.txt").write_text("".join(f"line {i}\n" for i in range(200)))
    return report("add big.txt", "MORE_TO_DO", "n/a")


def oscillation(n):
    original = STATE / "original.txt"
    if not original.exists():
        original.write_text(TARGET.read_text())
    if n % 2:
        TARGET.write_text("content A\n")
        return report("write content A", "MORE_TO_DO", "restore")
    TARGET.write_text(original.read_text())
    return report("restore original", "MORE_TO_DO", "write content A")


def broken(n):
    Path("broken.txt").write_text("fails the test cmd\n")
    return report("add broken.txt", "MORE_TO_DO", "n/a")


REFACTORERS = {
    "broken": broken,
    "converge": converge,
    "hang": hang,
    "oversize": oversize,
    "oscillation": oscillation,
    "commit-check-failed": append_line,
    "watchdog-stop": append_line,
    "max-iterations": append_line,
}


def committer(n):
    if SCENARIO == "commit-check-failed":
        return "I decided not to commit."
    # Output captured: only stream-json reaches stdout, like the real CLI.
    for cmd in (["git", "add", "-A"], [str(COMMIT_SH), f"♻️ Fake step {n}"]):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode:
            return f"{' '.join(cmd)} failed:\n{proc.stdout}{proc.stderr}"
    return f"Committed ♻️ Fake step {n}"


def watchdog(n):
    if SCENARIO == "watchdog-stop":
        return "The run drifts.\nVERDICT: stop — drift"
    return "All fine.\nVERDICT: continue — on track"


def main():
    n = bump(ROLE or "unknown")
    emit({"type": "system", "subtype": "init", "session_id": str(uuid.uuid4())})
    emit({"type": "assistant", "message": {"role": "assistant",
          "content": [{"type": "text", "text": f"{ROLE} call {n}"}]}})
    if ROLE == "refactorer":
        text = REFACTORERS[SCENARIO](n)
    elif ROLE == "committer":
        text = committer(n)
    elif ROLE == "watchdog":
        text = watchdog(n)
    else:
        sys.stderr.write(f"fake_claude: unknown role {ROLE!r}\n")
        return 1
    emit({"type": "result", "subtype": "success", "is_error": False, "result": text})
    return 0


if __name__ == "__main__":
    sys.exit(main())
