"""Unit tests for dynamic research and deterministic score diagnostics."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from aggregate_scores import summarize
from benchmark import diagnose
from validate_profiles import ValidationError, load_json, validate, validate_research_profile


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.payload = load_json(ROOT / "examples" / "evaluations.synthetic.json")
        self.pairs = load_json(ROOT / "examples" / "benchmark.synthetic.json")

    def test_dynamic_no_bundled_profile_required(self):
        got = validate(ROOT)
        self.assertFalse(got["bundled_profiles_required"])
        self.assertEqual(got["total_points"], 100)

    def test_score_aggregation(self):
        got = summarize(ROOT, self.payload)
        self.assertEqual(len(got["evaluations"]), 2)
        self.assertEqual(got["groups"][0]["judge_count"], 2)
        for x in got["evaluations"]:
            self.assertEqual(x["universal"] + x["major_fit"], x["total"])
            self.assertEqual(x["research_status"], "synthetic")

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

    def test_unknown_major_rejected(self):
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

    def test_verified_must_have_evidence(self):
        p = copy.deepcopy(self.payload)
        entry = next(iter(p["profiles"].values()))
        entry["research_status"] = "verified"
        entry["synthetic"] = False
        with self.assertRaises(ValidationError):
            summarize(ROOT, p)

    def test_unavailable_research_requires_universal_only(self):
        p = copy.deepcopy(self.payload)
        entry = next(iter(p["profiles"].values()))
        entry["research_status"] = "unavailable"
        for e in p["evaluations"]:
            for key in ("disciplinary_understanding", "relevant_evidence", "academic_direction"):
                del e["scores"][key]
        got = summarize(ROOT, p)
        for x in got["evaluations"]:
            self.assertIsNone(x["major_fit"])
            self.assertIsNone(x["total"])
            self.assertFalse(x["major_profile_checked"])

    def test_unavailable_research_rejects_fabricated_fit(self):
        p = copy.deepcopy(self.payload)
        next(iter(p["profiles"].values()))["research_status"] = "unavailable"
        with self.assertRaises(ValidationError):
            summarize(ROOT, p)

    def test_malformed_research_date_rejected(self):
        p = copy.deepcopy(self.payload)
        entry = next(iter(p["profiles"].values()))
        entry["researched_on"] = "2026-99-99"
        with self.assertRaises(ValidationError):
            summarize(ROOT, p)

    def test_profile_registry_mismatch_rejected(self):
        p = copy.deepcopy(self.payload)
        entry = next(iter(p["profiles"].values()))
        entry["id"] = "different"
        with self.assertRaises(ValidationError):
            summarize(ROOT, p)


if __name__ == "__main__":
    unittest.main()
