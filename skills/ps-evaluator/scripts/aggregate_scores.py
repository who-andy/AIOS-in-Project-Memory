#!/usr/bin/env python3
"""Validate research-linked evaluations and aggregate model-assigned scores."""
import argparse
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

from validate_profiles import ValidationError, load_json, rubric_from_file, validate, validate_research_profile


def summarize(root, payload):
    validate(root)
    rubrics = {r: rubric_from_file(Path(root) / "rubrics" / (r + ".json")) for r in ("universal", "major_fit")}
    criteria = {c["id"]: (r, c["max_points"]) for r, rub in rubrics.items() for c in rub["criteria"]}
    profiles = payload.get("profiles")
    if not isinstance(profiles, dict) or not profiles:
        raise ValidationError("Expected a nonempty dynamically researched profiles registry")
    for profile_id, research in profiles.items():
        validate_research_profile(profile_id, research)
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
        if major not in profiles:
            raise ValidationError(f"Evaluation {i}: unknown target_major {major}")
        research = profiles[major]
        if entry.get("profile_version") != research["version"]:
            raise ValidationError(f"Evaluation {i}: profile_version mismatch")
        if entry.get("rubric_versions") != {r: x["version"] for r, x in rubrics.items()}:
            raise ValidationError(f"Evaluation {i}: rubric_versions mismatch")
        key = (entry["document_id"], major, entry["judge_id"], entry["judge_version"])
        if key in seen:
            raise ValidationError(f"Evaluation {i}: duplicate document/major/judge/version")
        seen.add(key)
        scores = entry.get("scores")
        if not isinstance(scores, dict):
            raise ValidationError(f"Evaluation {i}: missing scores")
        universal_ids = {k for k, (rub, _) in criteria.items() if rub == "universal"}
        fit_ids = set(criteria) - universal_ids
        allowed = universal_ids if research["research_status"] == "unavailable" else set(criteria)
        if set(scores) != allowed:
            raise ValidationError(f"Evaluation {i}: scores must contain exactly {sorted(allowed)}")
        subtotals = {"universal": 0, "major_fit": 0}
        for criterion_id in allowed:
            rub, maximum = criteria[criterion_id]
            val = scores[criterion_id]
            if not isinstance(val, dict) or type(val.get("score")) is not int or not (0 <= val["score"] <= maximum):
                raise ValidationError(f"Evaluation {i}: invalid score for {criterion_id}")
            if not isinstance(val.get("rationale"), str) or not val["rationale"].strip():
                raise ValidationError(f"Evaluation {i}: missing rationale for {criterion_id}")
            evidence = val.get("evidence")
            if not isinstance(evidence, list) or any(not isinstance(s, str) or not s.strip() for s in evidence) or len(evidence) > 2:
                raise ValidationError(f"Evaluation {i}: invalid evidence for {criterion_id}")
            subtotals[rub] += val["score"]
        if not isinstance(entry.get("risks"), list) or any(not isinstance(s, str) for s in entry["risks"]):
            raise ValidationError(f"Evaluation {i}: invalid risks")
        if "major_profile_checked" in entry and entry["major_profile_checked"] is not (research["research_status"] == "verified"):
            raise ValidationError(f"Evaluation {i}: major_profile_checked contradicts research_status")
        fit_available = research["research_status"] != "unavailable"
        processed.append({
            "document_id": entry["document_id"], "target_major": major,
            "judge_id": entry["judge_id"], "judge_version": entry["judge_version"],
            "research_status": research["research_status"],
            "universal": subtotals["universal"],
            "major_fit": subtotals["major_fit"] if fit_available else None,
            "total": sum(subtotals.values()) if fit_available else None,
            "risks": entry["risks"], "major_profile_checked": research["research_status"] == "verified"
        })
    groups = defaultdict(list)
    for record in processed:
        groups[(record["document_id"], record["target_major"])].append(record)
    summaries = []
    for (document, major), values in sorted(groups.items()):
        totals = [x["total"] for x in values if x["total"] is not None]
        summaries.append({
            "document_id": document, "target_major": major, "judge_count": len(values),
            "mean_total": round(mean(totals), 2) if totals else None,
            "range_total": max(totals) - min(totals) if totals else None,
            "research_status": profiles[major]["research_status"],
            "reliability_note": "Agreement only; no admissions calibration or accuracy validation."
        })
    return {"evaluations": processed, "groups": summaries, "notes": [
        "70/30 are experimental editorial weights, not official admissions weights.",
        "Major research is dynamically provided; this script does not browse or verify citations.",
        "No LLM was called by this script. Model agreement cannot validate admissions outcomes."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rubrics", default=".")
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
