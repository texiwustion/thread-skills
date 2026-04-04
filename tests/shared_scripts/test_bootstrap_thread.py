import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "shared" / "scripts" / "bootstrap_thread.py"


class BootstrapThreadCliTest(unittest.TestCase):
    def test_initializes_memory_and_interrupt_from_templates(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            threads_dir = repo / "threads"
            template_dir = threads_dir / "_template"
            target_dir = threads_dir / "landing-redesign-t01"

            template_dir.mkdir(parents=True)
            (template_dir / "memory.md").write_text(
                "# Thread Memory\n- Thread: <thread-id>\n- Goal: <中文，一句话目标>\n",
                encoding="utf-8",
            )
            (template_dir / "interrupt.md").write_text(
                "# Interrupt Record\n- Thread: <thread-id>\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--thread-id",
                    "landing-redesign-t01",
                    "--goal",
                    "重做落地页",
                    "--threads-dir",
                    str(threads_dir),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertTrue((target_dir / "memory.md").exists())
            self.assertTrue((target_dir / "interrupt.md").exists())
            self.assertIn("landing-redesign-t01", (target_dir / "memory.md").read_text(encoding="utf-8"))
            self.assertIn("重做落地页", (target_dir / "memory.md").read_text(encoding="utf-8"))
            self.assertIn("landing-redesign-t01", (target_dir / "interrupt.md").read_text(encoding="utf-8"))
            self.assertFalse((target_dir / "memory-proposal.md").exists())


if __name__ == "__main__":
    unittest.main()
