"""Opt-in browser integration check on an owned local fixture."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(os.environ.get('RUN_BROWSER_TESTS') == '1', 'Set RUN_BROWSER_TESTS=1 for the live browser check')
class BrowserCaptureTests(unittest.TestCase):
    def test_runtime_evidence(self):
        if not shutil.which('agent-browser'):
            self.skipTest('agent-browser is not installed')
        session = 'cats-paw-test-' + uuid.uuid4().hex[:12]

        def browser(*arguments, source=None):
            result = subprocess.run(['agent-browser', '--session', session, *arguments],
                                    input=source, text=True, capture_output=True, timeout=45)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            return result.stdout

        def inspect():
            source = (ROOT / 'scripts/inspect-element.js').read_text()
            return json.loads(browser('eval', '--stdin', source=source))

        try:
            browser('open', (ROOT / 'tests/inspection-fixture.html').as_uri())
            before = inspect()
            self.assertEqual(before['nodes'][0]['styles']['padding'], '17px')
            self.assertEqual(before['nodes'][0]['before']['color'], 'rgb(120, 30, 60)')
            self.assertTrue(any(node['shadow'] and node['styles']['font-size'] == '13px'
                                for node in before['nodes']))
            self.assertNotIn('fixture-secret-must-not-export', json.dumps(before))
            moving = next(node for node in before['nodes'] if node['animations'])
            self.assertEqual(moving['animations'][0]['currentTime'], '200')
            browser('find', 'role', 'button', 'click', '--name', 'Toggle motion')
            after = inspect()
            changed = next(node for node in after['nodes'] if node['animations'])
            self.assertEqual(changed['animations'][0]['currentTime'], '400')
            self.assertNotEqual(moving['styles']['transform'], changed['styles']['transform'])
            browser('eval', 'globalThis.CATS_PAW_OPTIONS.maxNodes = 1')
            bounded = inspect()
            self.assertEqual(len(bounded['nodes']), 1)
            self.assertTrue(bounded['truncated'])
            browser('eval', 'globalThis.CATS_PAW_OPTIONS.selector = "#missing"')
            missing = subprocess.run(['agent-browser', '--session', session, 'eval', '--stdin'],
                                     input=(ROOT / 'scripts/inspect-element.js').read_text(),
                                     capture_output=True, text=True, timeout=45)
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn('target not found', missing.stdout + missing.stderr)
        finally:
            subprocess.run(['agent-browser', '--session', session, 'close'],
                           capture_output=True, text=True, timeout=45)


if __name__ == '__main__':
    unittest.main()
