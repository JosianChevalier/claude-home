"""Black-box tests for loop.py: exit code, LOOP END line, git log subjects only.

Run from the refactor-loop dir: python3 -m unittest discover -s tests
"""
import os
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOOP = HERE.parent / "loop.py"
COMMIT_SH = HERE.parent / "commit.sh"
FAKE = HERE / "fake_claude.py"
RUN_TIMEOUT = 90


def step(n):
    return f"♻️ Fake step {n}"


class LoopTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="refactor-loop-test-"))
        self.repo = self.tmp / "repo"
        self.state = self.tmp / "state"
        self.run_dir = self.tmp / "run"
        self.repo.mkdir()
        self.state.mkdir()
        empty_gitconfig = self.tmp / "gitconfig"
        empty_gitconfig.write_text("")
        self.env = {k: v for k, v in os.environ.items()
                    if k not in ("ANTHROPIC_API_KEY", "CLAUDE_CODE_SESSION_ID")}
        self.env.update(GIT_CONFIG_GLOBAL=str(empty_gitconfig), GIT_CONFIG_NOSYSTEM="1",
                        FAKE_STATE=str(self.state))
        self.git("init", "-q")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        (self.repo / "file.txt").write_text("original\n")
        self.git("add", "file.txt")
        self.git("commit", "-q", "-m", "init")

    def tearDown(self):
        for pid in self.grandchild_pids():
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        subprocess.run(["rm", "-rf", str(self.tmp)])

    # --- helpers -------------------------------------------------------

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env, check=True,
                              capture_output=True, text=True).stdout

    def subjects(self):
        return self.git("log", "--format=%s").splitlines()

    def grandchild_pids(self):
        path = self.state / "grandchild.pids"
        return [int(x) for x in path.read_text().split()] if path.exists() else []

    def run_loop(self, scenario, *args, env=None):
        env = dict(env or self.env, FAKE_SCENARIO=scenario)
        cmd = [sys.executable, str(LOOP), str(self.repo), "--claude-bin", str(FAKE),
               "--run-dir", str(self.run_dir),
               "--worker-timeout", "20", "--idle-timeout", "20", *args]
        proc = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True)
        try:
            out, err = proc.communicate(timeout=RUN_TIMEOUT)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate(timeout=10)
            self.fail(f"loop.py timed out\n--- stdout\n{out}\n--- stderr\n{err}")
        self.out, self.err = out, err
        return proc.returncode

    def dump(self):
        return f"\n--- stdout\n{self.out}\n--- stderr\n{self.err}"

    def assertEnd(self, code, expected_code, reason):
        lines = self.out.strip().splitlines()
        last = lines[-1] if lines else ""
        self.assertEqual(code, expected_code, self.dump())
        self.assertTrue(last.startswith(f"LOOP END: {reason} "), self.dump())

    def assertSubjects(self, n_commits):
        expected = [step(i) for i in range(n_commits, 0, -1)] + ["init"]
        self.assertEqual(self.subjects(), expected, self.dump())

    # --- scenarios -----------------------------------------------------

    def test_converge(self):
        code = self.run_loop("converge")
        self.assertEnd(code, 0, "converged")
        self.assertSubjects(2)

    def test_hang_stalls_and_kills_the_process_group(self):
        code = self.run_loop("hang", "--worker-timeout", "2", "--max-stall", "1")
        self.assertEnd(code, 1, "stalled")
        self.assertSubjects(0)
        pids = self.grandchild_pids()
        self.assertTrue(pids, "fake never spawned its grandchild" + self.dump())
        deadline = time.monotonic() + 3
        for pid in pids:
            while True:
                try:
                    os.kill(pid, 0)
                except ProcessLookupError:
                    break
                if time.monotonic() > deadline:
                    self.fail(f"grandchild {pid} survived the kill" + self.dump())
                time.sleep(0.1)

    def test_oversize_stalls_and_resets(self):
        code = self.run_loop("oversize", "--max-lines", "80", "--max-stall", "2")
        self.assertEnd(code, 1, "stalled")
        self.assertSubjects(0)
        self.assertEqual(self.git("status", "--porcelain"), "", self.dump())

    def test_failing_test_cmd_stalls_and_resets(self):
        code = self.run_loop("broken", "--test-cmd", "test ! -f broken.txt", "--max-stall", "1")
        self.assertEnd(code, 1, "stalled")
        self.assertSubjects(0)
        self.assertEqual(self.git("status", "--porcelain"), "", self.dump())

    def test_oscillation(self):
        code = self.run_loop("oscillation")
        self.assertEnd(code, 1, "oscillation")

    def test_commit_check_failed(self):
        code = self.run_loop("commit-check-failed")
        self.assertEnd(code, 1, "commit-check-failed")
        self.assertSubjects(0)

    def test_watchdog_stop(self):
        code = self.run_loop("watchdog-stop", "--audit-every", "2", "--max-iterations", "10")
        self.assertEnd(code, 1, "watchdog-stop")
        self.assertSubjects(2)

    def test_max_iterations(self):
        code = self.run_loop("max-iterations", "--max-iterations", "3", "--audit-every", "2")
        self.assertEnd(code, 1, "max-iterations")
        self.assertSubjects(3)

    def test_precondition_dirty_tree(self):
        (self.repo / "stray.txt").write_text("uncommitted\n")
        code = self.run_loop("converge")
        self.assertEnd(code, 2, "precondition")
        self.assertSubjects(0)

    def test_precondition_api_key(self):
        code = self.run_loop("converge", env=dict(self.env, ANTHROPIC_API_KEY="x"))
        self.assertEnd(code, 2, "precondition")
        self.assertSubjects(0)

    # --- commit.sh -----------------------------------------------------

    def test_commit_sh_refuses_long_subject(self):
        (self.repo / "file.txt").write_text("changed\n")
        self.git("add", "-A")
        proc = subprocess.run([str(COMMIT_SH), "x" * 73], cwd=self.repo, env=self.env,
                              capture_output=True, text=True, timeout=10)
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertEqual(self.subjects(), ["init"])


if __name__ == "__main__":
    unittest.main()
