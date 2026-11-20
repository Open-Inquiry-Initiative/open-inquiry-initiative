import unittest
from datetime import date
from intake import generate, fingerprint, validate

FIXTURE = dict(title='Synthetic room', summary='Test room proposal', questions=['Can it load?'], hypotheses=['It may load'], evidence=['No experiment yet'], next_steps=['Create fixture'])
DAY = date(2026, 11, 19)
ID = 'OII-B-20261119-001'

class IntakeTests(unittest.TestCase):
    def test_determinism(self):
        self.assertEqual(generate(FIXTURE, ID, DAY), generate(dict(reversed(list(FIXTURE.items()))), ID, DAY))
    def test_missing_field(self):
        with self.assertRaises(ValueError): validate({'title': 'Only title'})
    def test_invalid_id(self):
        with self.assertRaises(ValueError): generate(FIXTURE, 'bad', DAY)
    def test_wrong_date(self):
        with self.assertRaises(ValueError): generate(FIXTURE, 'OII-B-20261118-001', DAY)
    def test_secret_flag(self):
        r = {**FIXTURE, 'summary': 'api_key=example_secret'}
        self.assertIn('possible_secret', generate(r, ID, DAY)['review_flags'])
    def test_no_auto_approval(self):
        self.assertFalse(generate(FIXTURE, ID, DAY)['publication_approved'])
    def test_fingerprint_changes(self):
        self.assertNotEqual(fingerprint(FIXTURE), fingerprint({**FIXTURE, 'title': 'Other'}))
    def test_render_sections(self):
        m = generate(FIXTURE, ID, DAY)['markdown']
        self.assertIn('Hypotheses (unverified)', m)
        self.assertIn('Not reviewed', m)

if __name__ == '__main__': unittest.main()
