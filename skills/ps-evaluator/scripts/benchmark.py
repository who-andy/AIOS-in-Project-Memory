#!/usr/bin/env python3
"""Descriptive pairwise judge stability diagnostics; not predictive calibration."""
import argparse
import json
from collections import defaultdict
from itertools import combinations
from statistics import mean


def diagnose(payload):
    observations = payload.get("observations")
    if not isinstance(observations, list) or not observations:
        raise ValueError("Expected nonempty observations array")
    by_judge_case = defaultdict(dict)
    by_case_version = defaultdict(list)
    for idx, obs in enumerate(observations):
        if not isinstance(obs, dict):
            raise ValueError(f"Observation {idx}: invalid object")
        for field in ("case_id", "version_id", "judge_id"):
            if not isinstance(obs.get(field), str) or not obs[field].strip():
                raise ValueError(f"Observation {idx}: missing {field}")
        if obs.get("order") not in ("AB", "BA") or obs.get("preferred") not in ("A", "B", "tie"):
            raise ValueError(f"Observation {idx}: invalid order/preferred")
        for field in ("score_a", "score_b"):
            value = obs.get(field)
            if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 100):
                raise ValueError(f"Observation {idx}: invalid {field}")
        key = (obs["case_id"], obs["version_id"], obs["judge_id"])
        if obs["order"] in by_judge_case[key]:
            raise ValueError(f"Observation {idx}: repeated order for same case/version/judge")
        by_judge_case[key][obs["order"]] = obs
        by_case_version[(obs["case_id"], obs["version_id"])].append(obs)
    flips, paired = 0, 0
    for orders in by_judge_case.values():
        if set(orders) == {"AB", "BA"}:
            paired += 1
            if orders["AB"]["preferred"] != orders["BA"]["preferred"]:
                flips += 1
    disagreements = []
    for (case_id, version_id), entries in sorted(by_case_version.items()):
        # Compare different judges on the same order to avoid counting order effects as inter-judge disagreement.
        for order in ("AB", "BA"):
            items = [p for p in entries if p["order"] == order and p.get("score_a") is not None and p.get("score_b") is not None]
            for a, b in combinations(items, 2):
                if a["judge_id"] == b["judge_id"]:
                    continue
                disagreements.append({"case_id": case_id, "version_id": version_id, "order": order,
                                      "judges": sorted([a["judge_id"], b["judge_id"]]),
                                      "absolute_difference_a": abs(a["score_a"] - b["score_a"]),
                                      "absolute_difference_b": abs(a["score_b"] - b["score_b"])})
    return {"observation_count": len(observations), "paired_order_trials": paired,
            "order_preference_flips": flips,
            "flip_rate": round(flips / paired, 4) if paired else None,
            "mean_abs_score_disagreement": round(mean([p[k] for p in disagreements for k in ("absolute_difference_a", "absolute_difference_b")]), 2) if disagreements else None,
            "inter_judge_pairs": len(disagreements),
            "notes": ["Preference labels refer to canonical A and B regardless of display order.",
                      "Descriptive consistency only. No human ground truth or outcome validation is implied."]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    args = p.parse_args()
    with open(args.input, encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(diagnose(data), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
