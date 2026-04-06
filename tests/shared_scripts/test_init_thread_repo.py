import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INIT_SCRIPT = ROOT / "shared" / "scripts" / "init_thread_repo.py"
BOOTSTRAP_SCRIPT = ROOT / "shared" / "scripts" / "bootstrap_thread.py"


class InitThreadRepoCliTest(unittest.TestCase):
    def test_initializes_threads_template_and_supports_thread_bootstrap(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)

            init_result = subprocess.run(
                ["python3", str(INIT_SCRIPT), "--repo-root", str(repo)],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(init_result.returncode, 0, msg=init_result.stderr)
            self.assertTrue((repo / "threads" / "_template" / "memory.md").exists())
            self.assertTrue((repo / "threads" / "_template" / "interrupt.md").exists())
            self.assertTrue((repo / "threads" / "_template" / "memory-proposal.md").exists())
            self.assertTrue((repo / "threads" / "_template" / "platform-memory-proposal.md").exists())

            bootstrap_result = subprocess.run(
                [
                    "python3",
                    str(BOOTSTRAP_SCRIPT),
                    "--thread-id",
                    "smoke-goal-t01",
                    "--goal",
                    "验证空目录也能先建线程系统再建线程",
                    "--threads-dir",
                    str(repo / "threads"),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(bootstrap_result.returncode, 0, msg=bootstrap_result.stderr)
            self.assertTrue((repo / "threads" / "smoke-goal-t01" / "memory.md").exists())
            self.assertTrue((repo / "threads" / "smoke-goal-t01" / "interrupt.md").exists())

    def test_initializes_git_repo_and_supports_thread_branch_creation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)

            init_result = subprocess.run(
                ["python3", str(INIT_SCRIPT), "--repo-root", str(repo)],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(init_result.returncode, 0, msg=init_result.stderr)
            self.assertTrue((repo / ".git").exists())

            branch_result = subprocess.run(
                ["git", "checkout", "-b", "thread/smoke-branch-t01"],
                cwd=repo,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(branch_result.returncode, 0, msg=branch_result.stderr)

    def test_respects_env_when_git_init_is_disabled(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            env = dict(os.environ)
            env["THREAD_REPO_BOOTSTRAP_INIT_GIT"] = "false"

            init_result = subprocess.run(
                ["python3", str(INIT_SCRIPT), "--repo-root", str(repo)],
                capture_output=True,
                text=True,
                check=False,
                env=env,
            )

            self.assertEqual(init_result.returncode, 0, msg=init_result.stderr)
            self.assertFalse((repo / ".git").exists())
            self.assertTrue((repo / "threads" / "_template" / "memory.md").exists())


if __name__ == "__main__":
    unittest.main()
