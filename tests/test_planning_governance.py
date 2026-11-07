"""Verify planning records remain discoverable in portable governance artifacts."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PlanningGovernanceTests(unittest.TestCase):
    def test_role_snapshots_deliver_planning_and_audience_rules(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'snapshot'
            result = subprocess.run([
                sys.executable, str(ROOT / 'tools/build_governance_snapshot.py'),
                '--product', 'Planning verification', '--context-revision', 'test-fixture',
                '--classification', 'internal', '--roles', 'Chinedu', 'Ada', 'Samuel',
                '--output', str(target),
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((target / 'manifest.json').read_text())
            sources = manifest['files']['core.md']['sources']
            for source in ('governance/requirements-and-process-planning.md',
                           'governance/case-management-and-help-knowledge.md'):
                self.assertIn(source, sources)
                self.assertIn((ROOT / source).read_text().strip(),
                              (target / 'core.md').read_text())
            verified = subprocess.run([
                sys.executable, str(ROOT / 'tools/verify_governance_snapshot.py'), str(target)
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(verified.returncode, 0, verified.stderr)
            # A stale or altered policy must not pass portable snapshot validation.
            with (target / 'core.md').open('a') as stream:
                stream.write('\nUnapproved policy change\n')
            rejected = subprocess.run([
                sys.executable, str(ROOT / 'tools/verify_governance_snapshot.py'), str(target)
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0)

    def test_new_template_local_links_resolve(self):
        paths = list((ROOT / 'templates/planning').glob('*.md'))
        paths += list((ROOT / 'templates/operations').glob('*.md'))
        paths += [ROOT / 'governance/requirements-and-process-planning.md',
                  ROOT / 'governance/case-management-and-help-knowledge.md',
                  ROOT / 'templates/product-context/planning-index.md',
                  ROOT / 'templates/product-context/actor-action-register.md']
        for path in paths:
            for destination in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
                if '://' in destination or destination.startswith('#'):
                    continue
                with self.subTest(source=path.name, destination=destination):
                    self.assertTrue((path.parent / destination.split('#')[0]).exists())

    def test_word_visual_masters_are_valid_and_have_expected_orientation(self):
        for name, orientation in [('prd', 'portrait'), ('2a', 'portrait'), ('fars', 'landscape')]:
            with self.subTest(template=name):
                with zipfile.ZipFile(ROOT / f'templates/planning/{name}.docx') as document:
                    self.assertIsNone(document.testzip())
                    xml = document.read('word/document.xml').decode()
                    self.assertIn('w:tbl', xml)
                    if orientation == 'landscape':
                        self.assertIn('w:orient="landscape"', xml)
                    else:
                        self.assertNotIn('w:orient="landscape"', xml)


if __name__ == '__main__':
    unittest.main()
