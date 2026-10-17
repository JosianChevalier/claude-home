#!/usr/bin/env python3
"""Run the atomic-refactoring cycle headless on a git repo until the code converges. See SPEC.md."""
import argparse
import fcntl
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMMIT_SCRIPT = HERE / "commit.sh"
ROLES = ("refactorer", "committer", "watchdog")
EXIT_CODES = {"converged": 0, "precondition": 2}
WATCHDOG_TIMEOUT = 120

REFACTORER_ALLOW = (
    "Read Edit Write Glob Grep Bash(git status*) Bash(git diff*) Bash(git log*) Bash(git show*) "
    "Bash(ls *) Bash(head *) Bash(tail *) Bash(wc *)"
)
REFACTORER_DENY = (
    "Bash(git add*) Bash(git commit*) Bash(git -C * commit*) Bash(git reset*) Bash(git checkout*) Bash(git restore*) "
    "Bash(git stash*) Bash(git clean*) Bash(git push*)"
)
COMMITTER_ALLOW = f"Bash(git status*) Bash(git diff*) Bash(git log*) Bash(git add *) Bash({COMMIT_SCRIPT} *)"
COMMITTER_DENY = "Edit Write Bash(git commit*) Bash(git -C * commit*) Bash(git push*) Bash(git reset*)"

RUN_LOG = None


class Stop(Exception):
    def __init__(self, reason, detail=""):
        super().__init__(reason)
        self.reason, self.detail = reason, detail


def emit(line):
    print(line, flush=True)
    if RUN_LOG:
        with open(RUN_LOG, "a") as f:
            f.write(line + "\n")


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.strip()}")
    return p.stdout.strip()


def parse_args(argv):
    p = argparse.ArgumentParser(description="Headless atomic-refactoring loop.")
    p.add_argument("repo")
    p.add_argument("--goal")
    p.add_argument("--paths", nargs="+", default=[])
    p.add_argument("--test-cmd")
    p.add_argument("--max-iterations", type=int, default=30)
    p.add_argument("--max-stall", type=int, default=3)
    p.add_argument("--max-lines", type=int, default=80)
    p.add_argument("--max-files", type=int, default=6)
    p.add_argument("--audit-every", type=int, default=5)
    p.add_argument("--worker-timeout", type=float, default=600)
    p.add_argument("--idle-timeout", type=float, default=300)
    p.add_argument("--model-refactorer", default="claude-opus-5-5")
    p.add_argument("--model-committer", default="claude-haiku-5-5")
    p.add_argument("--model-watchdog", default="claude-sonnet-5-5")
    p.add_argument("--claude-bin", default="claude")
    p.add_argument("--run-dir")
    return p.parse_args(argv)


# --- preconditions ----------------------------------------------------------

def acquire_lock(repo):
    locks = Path(tempfile.gettempdir()) / "refactor-loop" / "locks"
    locks.mkdir(parents=True, exist_ok=True)
    f = open(locks / (hashlib.sha1(str(repo).encode()).hexdigest() + ".lock"), "w")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        f.close()
        raise Stop("precondition", "another loop holds the lock on this repo")
    return f


def check_preconditions(args):
    """Validate the world; return the lock file, set args.repo and args.claude_bin to absolute paths."""
    repo = Path(args.repo).resolve()
    if not (repo / ".git").exists():
        raise Stop("precondition", f"not a git work tree: {repo}")
    lock = acquire_lock(repo)
    try:
        git(repo, "rev-parse", "--verify", "HEAD")
    except RuntimeError:
        raise Stop("precondition", "repo has no commit")
    if git(repo, "status", "--porcelain"):
        raise Stop("precondition", "work tree not clean")
    if "ANTHROPIC_API_KEY" in os.environ:
        raise Stop("precondition", "ANTHROPIC_API_KEY is set: workers would bill the API")
    found = shutil.which(args.claude_bin)
    if not found:
        raise Stop("precondition", f"claude bin not found: {args.claude_bin}")
    for name in ("common", *ROLES):
        if not (HERE / "prompts" / f"{name}.md").is_file():
            raise Stop("precondition", f"missing prompt file: prompts/{name}.md")
    if not os.access(COMMIT_SCRIPT, os.X_OK):
        raise Stop("precondition", f"commit script missing or not executable: {COMMIT_SCRIPT}")
    args.repo, args.claude_bin = repo, os.path.abspath(found)
    return lock


def make_run_dir(arg):
    if arg:
        d = Path(arg).resolve()
        d.mkdir(parents=True, exist_ok=True)
        return d
    base = Path(tempfile.gettempdir()) / "refactor-loop" / "runs"
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    for n in range(1, 1000):
        d = base / (stamp if n == 1 else f"{stamp}-{n}")
        try:
            d.mkdir(parents=True)
            return d
        except FileExistsError:
            continue
    raise Stop("precondition", "cannot create a run dir")


# --- workers ----------------------------------------------------------------

def role_flags(role, test_cmd):
    if role == "refactorer":
        allow = REFACTORER_ALLOW + (f" Bash({test_cmd}*)" if test_cmd else "")
        return ["--allowedTools", allow, "--disallowedTools", REFACTORER_DENY]
    if role == "committer":
        return ["--allowedTools", COMMITTER_ALLOW, "--disallowedTools", COMMITTER_DENY]
    return ["--tools", ""]


def build_prompt(role, context):
    parts = [(HERE / "prompts" / f"{name}.md").read_text().rstrip() for name in ("common", role)]
    return "\n\n".join(parts) + "\n\n" + context


def kill(proc):
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except OSError:
        try:
            proc.kill()
        except OSError:
            pass
    proc.wait()


def supervise(proc, log, timeout, idle):
    """Wait for the worker; return None when it ended, else the reason it was killed."""
    start = time.monotonic()
    while True:
        try:
            proc.wait(timeout=1)
            return None
        except subprocess.TimeoutExpired:
            pass
        if time.monotonic() - start > timeout:
            kill(proc)
            return f"timeout {timeout:g}s"
        if time.time() - log.stat().st_mtime > idle:
            kill(proc)
            return f"idle {idle:g}s"


def read_result(log):
    text = None
    for line in log.read_text(errors="replace").splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict) and event.get("type") == "result":
            text = str(event.get("result") or "")
    return text


def run_supervised(cmd, log, args, timeout, env=None, shell=False):
    """Run cmd in its own process group, output to log; return (killed reason or None, exit code)."""
    with open(log, "wb") as out:
        proc = subprocess.Popen(cmd, cwd=args.repo, stdin=subprocess.DEVNULL, stdout=out,
                                stderr=subprocess.STDOUT, env=env, shell=shell, start_new_session=True)
        try:
            killed = supervise(proc, log, timeout, args.idle_timeout)
        except BaseException:
            kill(proc)
            raise
    return killed, proc.returncode


def run_worker(args, role, it, context):
    """Run one claude -p worker; return its final text, or None when it failed."""
    cmd = [args.claude_bin, "-p", build_prompt(role, context),
           "--model", getattr(args, f"model_{role}"),
           "--output-format", "stream-json", "--verbose", "--no-session-persistence",
           *role_flags(role, args.test_cmd)]
    env = {k: v for k, v in os.environ.items() if k != "CLAUDE_CODE_SESSION_ID"}
    env["REFACTOR_LOOP_ROLE"] = role
    timeout = min(args.worker_timeout, WATCHDOG_TIMEOUT) if role == "watchdog" else args.worker_timeout
    log = args.run_dir / f"{it:03}-{role}.jsonl"
    killed, code = run_supervised(cmd, log, args, timeout, env=env)
    if killed:
        emit(f"[iter {it}] {role}: killed ({killed})")
        return None
    result = read_result(log)
    if result is None:
        emit(f"[iter {it}] {role}: no result event (exit {code})")
    return result


# --- parsing and measuring --------------------------------------------------

def last_match(pattern, text, flags=0):
    found = re.findall(pattern, text, re.M | flags)
    return found[-1] if found else None


def parse_report(text):
    def field(key):
        value = last_match(rf"^\W*{key}:[\s*`]*(.*?)[\s*`]*$", text)
        return value if value and value.lower() != "n/a" else None
    return {"changed": field("CHANGED"), "next": field("NEXT"),
            "status": last_match(r"^\W*STATUS:\W*(MORE_TO_DO|NOTHING_TO_REFACTOR)\b", text)}


def parse_verdict(text):
    found = last_match(r"^\W*VERDICT:\W*(continue|stop)\b[\s:—–-]*(.*?)\s*$", text, re.I)
    return (found[0].lower(), found[1]) if found else None


def count_lines(path):
    try:
        data = path.read_bytes()
    except OSError:
        return 0
    return data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)


def measure(repo):
    """The working change as (added, deleted, path) per file, untracked files included."""
    files = []
    for line in git(repo, "diff", "--numstat", "HEAD").splitlines():
        added, deleted, path = line.split("\t", 2)
        files.append((int(added) if added.isdigit() else 0, int(deleted) if deleted.isdigit() else 0, path))
    for path in git(repo, "ls-files", "--others", "--exclude-standard", "-z").split("\0"):
        if path:
            files.append((count_lines(repo / path), 0, path))
    return files


def summary(files):
    added, deleted = sum(f[0] for f in files), sum(f[1] for f in files)
    return f"+{added}/-{deleted} in {len(files)} file{'' if len(files) == 1 else 's'}"


def block(fields):
    """The context block: KEY: value lines, lists as '- item' lines."""
    out = []
    for key, value in fields:
        if isinstance(value, list):
            out.append(f"{key}:")
            out += [f"- {v}" for v in value] or ["- none"]
        else:
            out.append(f"{key}: {value if value else 'n/a'}")
    return "\n".join(out) + "\n"


def subjects(repo, baseline, limit=None):
    out = git(repo, "log", "--format=%s", *([f"-n{limit}"] if limit else []), f"{baseline}..HEAD")
    return out.splitlines()


# --- the loop ---------------------------------------------------------------

def reset(repo, head):
    git(repo, "reset", "--hard", head)
    git(repo, "clean", "-fd")


def refactor_step(args, it, baseline, feedback):
    """Run the refactorer and judge its change; return (files, report, rejection reason or None)."""
    mode = "directed" if args.goal else "cleanup"
    context = block([("MODE", mode), ("GOAL", args.goal), *([("PATHS", " ".join(args.paths))] if args.paths else []),
                     ("TEST CMD", args.test_cmd),
                     ("BUDGET", f"{args.max_lines} lines, {args.max_files} files"),
                     ("RECENT COMMITS", subjects(args.repo, baseline, 10)),
                     *([feedback] if feedback else [])])
    result = run_worker(args, "refactorer", it, context)
    report = parse_report(result or "")
    files = measure(args.repo)
    emit(f"[iter {it}] refactorer: {summary(files)} — {report['changed'] or 'n/a'}")
    lines = sum(f[0] + f[1] for f in files)
    if result is None:
        return files, report, "worker failed"
    if not files and report["status"] == "NOTHING_TO_REFACTOR":
        raise Stop("converged")
    if not files:
        return files, report, "empty diff"
    if lines > args.max_lines or len(files) > args.max_files:
        return files, report, (f"change too big: {lines} lines (max {args.max_lines}), "
                               f"{len(files)} files (max {args.max_files})")
    return files, report, run_tests(args, it)


def run_tests(args, it):
    """Run --test-cmd on the candidate change; return a rejection reason or None."""
    if not args.test_cmd:
        return None
    killed, code = run_supervised(args.test_cmd, args.run_dir / f"{it:03}-tests.log", args,
                                  args.worker_timeout, shell=True)
    if killed or code != 0:
        emit(f"[iter {it}] tests: {f'killed ({killed})' if killed else f'exit {code}'}")
        return "tests failed"
    emit(f"[iter {it}] tests: passed")
    return None


def commit_step(args, it, prev, files, report):
    context = block([("GOAL", args.goal), ("CHANGED", report["changed"]), ("NEXT", report["next"]),
                     ("DIFFSTAT", [f"+{a} -{d} {p}" for a, d, p in files]),
                     ("COMMIT SCRIPT", str(COMMIT_SCRIPT))])
    run_worker(args, "committer", it, context)
    repo = args.repo
    if git(repo, "rev-list", "--count", f"{prev}..HEAD") != "1":
        raise Stop("commit-check-failed", "expected exactly one new commit")
    if git(repo, "rev-parse", "HEAD^") != prev:
        raise Stop("commit-check-failed", "HEAD^ is not the previous commit")
    if git(repo, "status", "--porcelain"):
        raise Stop("commit-check-failed", "work tree not clean after commit")
    emit(f"[iter {it}] committer: {git(repo, 'log', '-1', '--format=%s')}")
    return git(repo, "rev-parse", "HEAD")


def audit(args, it, baseline, commits, stall):
    repo = args.repo
    numstat = git(repo, "diff", "--numstat", f"{baseline}..HEAD").splitlines()
    total = sum(int(n) for line in numstat for n in line.split("\t")[:2] if n.isdigit())
    context = block([("MODE", "directed" if args.goal else "cleanup"), ("GOAL", args.goal),
                     ("COMMITS", str(commits)), ("STALL", str(stall)), ("TOTAL LINES CHANGED", str(total)),
                     ("COMMIT SUBJECTS", subjects(repo, baseline)),
                     ("DIFFSTAT", git(repo, "diff", "--stat", f"{baseline}..HEAD").splitlines())])
    verdict = parse_verdict(run_worker(args, "watchdog", it, context) or "")
    if verdict is None:
        emit(f"[iter {it}] watchdog: no verdict, continuing")
        return
    emit(f"[iter {it}] watchdog: {verdict[0]} — {verdict[1] or 'n/a'}")
    if verdict[0] == "stop":
        raise Stop("watchdog-stop", verdict[1])


def loop(args, baseline):
    repo, head = args.repo, baseline
    seen = {git(repo, "rev-parse", "HEAD^{tree}")}
    commits = stall = 0
    feedback = None
    for it in range(1, args.max_iterations + 1):
        if git(repo, "status", "--porcelain") or git(repo, "rev-parse", "HEAD") != head:
            raise Stop("state-drift", "tree dirty or HEAD moved between iterations")
        files, report, rejection = refactor_step(args, it, baseline, feedback)
        if rejection:
            reset(repo, head)
            stall += 1
            feedback = ("PREVIOUS", f"rejected: {rejection}")
            emit(f"[iter {it}] rejected: {rejection} (stall {stall}/{args.max_stall})")
            if stall >= args.max_stall:
                raise Stop("stalled")
            continue
        head = commit_step(args, it, head, files, report)
        commits, stall = commits + 1, 0
        feedback = ("PREVIOUS", f"NEXT: {report['next']}") if report["next"] else None
        tree = git(repo, "rev-parse", "HEAD^{tree}")
        if tree in seen:
            raise Stop("oscillation", f"tree {tree[:7]} already seen in this run")
        seen.add(tree)
        if args.audit_every > 0 and commits % args.audit_every == 0:
            audit(args, it, baseline, commits, stall)
    raise Stop("max-iterations")


def main(argv=None):
    global RUN_LOG
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        lock = check_preconditions(args)
        args.run_dir = make_run_dir(args.run_dir)
    except Stop as stop:
        emit(f"stop: precondition — {stop.detail}")
        emit("LOOP END: precondition (0 commits, -..-)")
        return EXIT_CODES["precondition"]
    RUN_LOG = args.run_dir / "run.log"
    repo = args.repo
    baseline = git(repo, "rev-parse", "HEAD")
    emit(f"[start] {'directed' if args.goal else 'cleanup'} on {repo} at {baseline[:7]}, logs in {args.run_dir}")
    try:
        loop(args, baseline)
    except Stop as stop:
        reason, detail = stop.reason, stop.detail
    except RuntimeError as error:
        reason, detail = "state-drift", str(error)
    if detail:
        emit(f"stop: {reason} — {detail}")
    n = git(repo, "rev-list", "--count", f"{baseline}..HEAD")
    emit(f"LOOP END: {reason} ({n} commits, {baseline[:7]}..{git(repo, 'rev-parse', '--short=7', 'HEAD')})")
    lock.close()
    return EXIT_CODES.get(reason, 1)


if __name__ == "__main__":
    sys.exit(main())
