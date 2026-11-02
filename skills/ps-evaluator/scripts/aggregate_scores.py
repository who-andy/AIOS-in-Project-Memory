#!/usr/bin/env python3
"""Check structured judge evaluations and summarize scores deterministically."""
import argparse
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

from validate_profiles import ValidationError, load_json, rubric_from_file, validate


def summarize(root, payload):
    validate(root)
    rubrics = {r: rubric_from_file(Path(root) / "rubrics" / (r + ".json")) for r in ("universal", "major_fit")}
    profile_map = {load_json(p)["id"]: load_json(p) for p in (Path(root) / "profiles").glob("**/*.json")}
    criteria = {c["id"]: (r, c["max_points"]) for r, rubric in rubrics.items() for c in rubric["criteria"]}
    entries = payload.get("evaluations")
    if not isinstance(entries, list) or not entries:
        raise ValidationError("Expected nonempty evaluations array")
    processed = []
    seen = set()
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValidationError(f"Evaluation {i} is not an object")
        for field in ("document_id", "target_major", "judge_id", "judge_version"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ValidationError(f"Evaluation {i}: missing {field}")
        major = entry["target_major"]
        if major not in profile_map:
            raise ValidationError(f"Evaluation {i}: unknown target_major {major}")
        if entry.get("profile_version") != profile_map[major]["version"]:
            raise ValidationError(f"Evaluation {i}: profile_version mismatch")
        if entry.get("rubric_versions") != {r: x["version"] for r, x in rubrics.items()}:
            raise ValidationError(f"Evaluation {i}: rubric_versions mismatch")
        key = (entry["document_id"], major, entry["judge_id"], entry["judge_version"])
        if key in seen:
            raise ValidationError(f"Evaluation {i}: duplicate document/major/judge/version")
        seen.add(key)
        score_dict = entry.get("scores")
        if not isinstance(score_dict, dict) or set(score_dict) != set(criteria):
            raise ValidationError(f"Evaluation {i}: scores must contain exactly {sorted(criteria)}")
        subtotals = {"universal": 0, "major_fit": 0}
        for criterion_id, (rubric_id, maximum) in criteria.items():
            val = score_dict[criterion_id]
            if not isinstance(val, dict) or type(val.get("score")) is not int or not (0 <= val["score"] <= maximum):
                raise ValidationError(f"Evaluation {i}: invalid score for {criterion_id}")
            if not isinstance(val.get("rationale"), str) or not val["rationale"].strip():
                raise ValidationError(f"Evaluation {i}: missing rationale for {criterion_id}")
            evidence = val.get("evidence")
            if not isinstance(evidence, list) or any(not isinstance(s, str) or not s.strip() for s in evidence) or len(evidence) > 2:
                raise ValidationError(f"Evaluation {i}: invalid evidence for {criterion_id}")
            subtotals[rubric_id] += val["score"]
        if not isinstance(entry.get("risks"), list) or any(not isinstance(s, str) for s in entry["risks"]):
            raise ValidationError(f"Evaluation {i}: invalid risks")
        if type(entry.get("major_profile_checked")) is not bool:
            raise ValidationError(f"Evaluation {i}: major_profile_checked must be boolean")
        processed.append({"document_id": entry["document_id"], "target_major": major,
                          "judge_id": entry["judge_id"], "judge_version": entry["judge_version"],
                          "universal": subtotals["universal"], "major_fit": subtotals["major_fit"],
                          "total": sum(subtotals.values()), "risks": entry["risks"],
                          "major_profile_checked": entry["major_profile_checked"]})
    groups = defaultdict(list)
    for p in processed:
        groups[(p["document_id"], p["target_major"])].append(p)
    summaries = []
    for (document, major), values in sorted(groups.items()):
        totals = [p["total"] for p in values]
        summaries.append({"document_id": document, "target_major": major,
                          "judge_count": len(values), "mean_total": round(mean(totals), 2),
                          "range_total": max(totals) - min(totals),
                          "reliability_note": "Agreement only; no admissions calibration or accuracy validation."})
    return {"evaluations": processed, "groups": summaries, "notes": [
        "The numeric weights are experimental, not official admissions weights.",
        "No LLM was called by this script.",
        "Model agreement cannot validate admissions outcomes."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rubrics", default=".", help="Skill root containing rubrics and profiles")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = summarize(args.rubrics, load_json(args.input))
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
