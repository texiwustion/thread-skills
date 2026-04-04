import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "shared" / "scripts" / "allocate_thread_id.py"


class AllocateThreadIdCliTest(unittest.TestCase):
    def test_allocates_next_suffix_for_matching_slug(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            threads_dir = Path(tmpdir) / "threads"
            (threads_dir / "_template").mkdir(parents=True)
            (threads_dir / "landing-redesign-t01").mkdir()
            (threads_dir / "landing-redesign-t02").mkdir()
            (threads_dir / "other-goal-t01").mkdir()

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--slug",
                    "landing redesign",
                    "--threads-dir",
                    str(threads_dir),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertEqual(result.stdout.strip(), "landing-redesign-t03")


if __name__ == "__main__":
    unittest.main()
