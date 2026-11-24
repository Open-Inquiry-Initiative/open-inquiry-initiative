import unittest
from datetime import date
from staging import plan_stage, verify_before_write, DuplicateRecord

D = date(2026, 11, 19)
FP = 'a' * 64
class StagingTests(unittest.TestCase):
    def test_empty_registry(self):
        self.assertEqual(plan_stage(D, FP, [], 'Test')['identifier'], 'OII-B-20261119-001')
    def test_next_available(self):
        self.assertEqual(plan_stage(D, FP, [{'id':'OII-B-20261119-001','fingerprint':'b'*64}], 'Test')['identifier'], 'OII-B-20261119-002')
    def test_duplicate_fingerprint(self):
        with self.assertRaises(DuplicateRecord):
            plan_stage(D, FP, [{'id':'OII-B-20261118-001','fingerprint':FP}], 'Test')
    def test_duplicate_registry_id(self):
        e = {'id':'OII-B-20261119-001','fingerprint':'b'*64}
        with self.assertRaises(ValueError): plan_stage(D, FP, [e,e], 'Test')
    def test_stale_plan(self):
        p = plan_stage(D, FP, [], 'Test')
        with self.assertRaises(DuplicateRecord):
            verify_before_write(p,[{'id':p['identifier'],'fingerprint':'b'*64}])
    def test_safe_plan(self):
        p = plan_stage(D, FP, [], 'Test')
        self.assertTrue(verify_before_write(p, []))
        self.assertFalse(p['publication_approved'])
    def test_bad_fingerprint(self):
        with self.assertRaises(ValueError): plan_stage(D, 'bad', [], 'Test')

if __name__ == '__main__': unittest.main()
