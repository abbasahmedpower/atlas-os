import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from v4_eval import audit,REQUIRED
class ContractTest(unittest.TestCase):
 def test_package_structure(self):self.assertEqual(audit(),[])
 def test_expected_files(self):self.assertEqual(len(REQUIRED),9)
 def test_audit_detects_missing(self):
  from unittest.mock import patch
  with patch('v4_eval.REQUIRED',REQUIRED+['missing-does-not-exist.txt']):self.assertIn('missing-does-not-exist.txt',audit())
