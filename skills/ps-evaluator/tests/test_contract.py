"""Unit tests for structural validators and descriptive score statistics."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from aggregate_scores import summarize
from benchmark import diagnose
from validate_profiles import ValidationError, load_json, validate


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.payload = load_json(ROOT / "examples" / "evaluations.synthetic.json")
        self.pairs = load_json(ROOT / "examples" / "benchmark.synthetic.json")

    def test_profiles_and_weights(self):
        got = validate(ROOT)
        self.assertEqual(got["profiles"], 2)
        self.assertEqual(got["total_points"], 100)

    def test_score_aggregation(self):
        got = summarize(ROOT, self.payload)
        self.assertEqual(len(got["evaluations"]), 2)
        self.assertEqual(got["groups"][0]["judge_count"], 2)
        for x in got["evaluations"]:
            self.assertEqual(x["universal"] + x["major_fit"], x["total"])

    def test_out_of_range_rejected(self):
        data = copy.deepcopy(self.payload)
        data["evaluations"][0]["scores"]["language"]["score"] = 6
        with self.assertRaises(ValidationError):
            summarize(ROOT, data)

    def test_missing_score_rejected(self):
        data = copy.deepcopy(self.payload)
        del data["evaluations"][0]["scores"]["academic_direction"]
        with self.assertRaises(ValidationError):
            summarize(ROOT, data)

    def test_wrong_major_rejected(self):
        data = copy.deepcopy(self.payload)
        data["evaluations"][0]["target_major"] = "nonexistent"
        with self.assertRaises(ValidationError):
            summarize(ROOT, data)

    def test_order_flip_and_disagreement(self):
        got = diagnose(self.pairs)
        self.assertEqual(got["paired_order_trials"], 2)
        self.assertEqual(got["order_preference_flips"], 1)
        self.assertEqual(got["flip_rate"], 0.5)
        self.assertEqual(got["inter_judge_pairs"], 2)

    def test_missing_pairs_not_treated_as_stable(self):
        got = diagnose({"observations": self.pairs["observations"][:1]})
        self.assertIsNone(got["flip_rate"])

    def test_duplicate_observation_rejected(self):
        p = copy.deepcopy(self.pairs)
        p["observations"].append(copy.deepcopy(p["observations"][0]))
        with self.assertRaises(ValueError):
            diagnose(p)

    def test_boolean_score_rejected(self):
        p = copy.deepcopy(self.payload)
        p["evaluations"][0]["scores"]["language"]["score"] = True
        with self.assertRaises(ValidationError):
            summarize(ROOT, p)


if __name__ == "__main__":
    unittest.main()
