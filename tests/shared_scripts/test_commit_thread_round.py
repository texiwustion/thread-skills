import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "shared" / "scripts" / "commit_thread_round.py"


class CommitThreadRoundCliTest(unittest.TestCase):
    def setUp(self) -> None:
        self.git_env = os.environ.copy()
        self.git_env.update(
            {
                "GIT_AUTHOR_NAME": "Thread Skills Test",
                "GIT_AUTHOR_EMAIL": "thread-skills-test@example.com",
                "GIT_COMMITTER_NAME": "Thread Skills Test",
                "GIT_COMMITTER_EMAIL": "thread-skills-test@example.com",
            }
        )

    def test_commits_round_changes_with_thread_message(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            self.init_repo(repo)

            (repo / "notes.txt").write_text("round one\n", encoding="utf-8")

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--repo-root",
                    str(repo),
                    "--thread-id",
                    "landing-redesign-t01",
                    "--summary",
                    "advance one bounded round",
                ],
                capture_output=True,
                text=True,
                check=False,
                env=self.git_env,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertEqual(
                self.git("log", "-1", "--pretty=%B", cwd=repo).stdout.strip(),
                "thread(landing-redesign-t01): advance one bounded round",
            )
            self.assertEqual(self.git("status", "--short", cwd=repo).stdout.strip(), "")

    def test_noop_when_no_changes_exist(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            self.init_repo(repo)

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--repo-root",
                    str(repo),
                    "--thread-id",
                    "landing-redesign-t01",
                    "--summary",
                    "advance one bounded round",
                ],
                capture_output=True,
                text=True,
                check=False,
                env=self.git_env,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertEqual(
                self.git("rev-list", "--count", "HEAD", cwd=repo).stdout.strip(),
                "1",
            )

    def git(self, *args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True,
            env=self.git_env,
        )

    def init_repo(self, repo: Path) -> None:
        self.git("init", "-b", "main", cwd=repo)
        (repo / "README.md").write_text("seed\n", encoding="utf-8")
        self.git("add", "README.md", cwd=repo)
        self.git("commit", "-m", "seed", cwd=repo)


if __name__ == "__main__":
    unittest.main()
