import importlib.util
import pathlib
import unittest

spec = importlib.util.spec_from_file_location("rpr_predict", pathlib.Path(__file__).with_name("predict.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PredictorTests(unittest.TestCase):
    def test_readiness(self):
        events = [
            {"id":"a","timestamp":"2026-01-01T00:00:00Z","dependencies":[]},
            {"id":"b","timestamp":"2026-01-03T00:00:00Z","dependencies":["a"]},
            {"id":"c","timestamp":"2026-01-04T00:00:00Z","dependencies":["a","b"]},
        ]
        result = module.rank(events, module.parse_time("2026-01-02T00:00:00Z"))
        self.assertEqual([x["id"] for x in result], ["b","c"])
        self.assertEqual(result[0]["readiness"], 1.0)
        self.assertEqual(result[1]["readiness"], 0.5)

    def test_missing_dependency(self):
        with self.assertRaises(ValueError):
            module.rank([{"id":"a","timestamp":"2026-01-01T00:00:00Z","dependencies":["missing"]}], module.parse_time("2026-01-02T00:00:00Z"))

    def test_duplicate_id(self):
        with self.assertRaises(ValueError):
            module.rank([{"id":"a","timestamp":"2026-01-01T00:00:00Z"}, {"id":"a","timestamp":"2026-01-02T00:00:00Z"}], module.parse_time("2026-01-03T00:00:00Z"))

if __name__ == "__main__":
    unittest.main()
