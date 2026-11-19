"""Exercise known pixel changes, alpha visibility and evidence preservation."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/pixel_diff.py'


class PixelDiffTests(unittest.TestCase):
    def test_comparison_contract(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            expected = root / 'expected.png'
            actual = root / 'actual.png'
            Image.new('RGBA', (2, 2), (0, 0, 0, 255)).save(expected)
            image = Image.open(expected).convert('RGBA')
            image.putpixel((1, 1), (0, 0, 0, 254))
            image.save(actual)

            def compare(name, *extra):
                return subprocess.run([sys.executable, str(SCRIPT), str(expected), str(actual),
                                       '--output', str(root / name), *extra], capture_output=True, text=True)

            difference = compare('alpha.png')
            self.assertEqual(difference.returncode, 1, difference.stderr)
            self.assertEqual(json.loads(difference.stdout)['changedFraction'], 0.25)
            with Image.open(root / 'alpha.png') as diff:
                self.assertEqual(diff.getpixel((1, 1)), (1, 1, 1))
            self.assertEqual(compare('tolerated.png', '--threshold', '1').returncode, 0)
            self.assertEqual(compare('alpha.png').returncode, 2)
            self.assertEqual(compare('bad-threshold.png', '--threshold', '-1').returncode, 2)
            self.assertEqual(compare('expected.png').returncode, 2)
            Image.new('RGBA', (3, 2)).save(actual)
            mismatch = compare('size.png')
            self.assertEqual(mismatch.returncode, 2)
            self.assertIn('dimensions differ', mismatch.stderr)
            self.assertFalse((root / 'size.png').exists())


if __name__ == '__main__':
    unittest.main()
