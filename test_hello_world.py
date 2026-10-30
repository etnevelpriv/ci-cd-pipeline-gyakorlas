import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

APP = Path(__file__).with_name("hello-world.py")
spec = importlib.util.spec_from_file_location("hello_world", APP)
hello_world = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hello_world)


class SumTests(unittest.TestCase):
    def test_addition(self):
        for a, b, expected in [(10, 5, 15), (0, 5, 5), (5, 0, 5),
                               (0, 0, 0), (-4, 2, -2), (-3, -2, -5),
                               (1.5, 2.5, 4.0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(hello_world.sum(a, b), expected)

    def test_script_output(self):
        result = subprocess.run(
            [sys.executable, str(APP)], capture_output=True,
            text=True, encoding="utf-8", check=True,
        )
        self.assertEqual(result.stdout.strip(), "10+5 eredménye: 15")


if __name__ == "__main__":
    unittest.main()
