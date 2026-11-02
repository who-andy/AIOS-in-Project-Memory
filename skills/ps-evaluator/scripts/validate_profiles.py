#!/usr/bin/env python3
"""Validate stable rubrics and on-demand research snapshot contracts (stdlib only)."""
import argparse
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


class ValidationError(ValueError):
    pass


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def rubric_from_file(path):
    rubric = load_json(path)
    if not isinstance(rubric, dict) or not isinstance(rubric.get("criteria"), list):
        raise ValidationError(f"Invalid criteria: {path}")
    ids = [c.get("id") for c in rubric["criteria"]]
    if not ids or len(ids) != len(set(ids)) or any(not isinstance(x, str) or not x for x in ids):
        raise ValidationError(f"Criteria IDs missing or duplicated: {path}")
    points = [c.get("max_points") for c in rubric["criteria"]]
    if any(type(p) is not int or p <= 0 for p in points):
        raise ValidationError(f"max_points must be positive integers: {path}")
    if sum(points) != rubric.get("total_points"):
        raise ValidationError(f"Rubric total does not equal criteria points: {path}")
    if not isinstance(rubric.get("version"), str):
        raise ValidationError(f"Rubric version missing: {path}")
    return rubric


def validate_research_profile(profile_id, item):
    """Validate the evidence envelope, never claim that cited claims are true."""
    if not isinstance(item, dict):
        raise ValidationError(f"Invalid profile object: {profile_id}")
    for key in ("id", "version", "researched_on", "target_intake", "route", "university", "programme", "interpretation_note"):
        if not isinstance(item.get(key), str) or not item[key].strip():
            raise ValidationError(f"Invalid {key}: {profile_id}")
    if item["id"] != profile_id:
        raise ValidationError(f"Profile registry key/id mismatch: {profile_id}")
    try:
        date.fromisoformat(item["researched_on"])
    except ValueError as exc:
        raise ValidationError(f"Invalid researched_on: {profile_id}") from exc
    status = item.get("research_status")
    if status not in ("verified", "partial", "unavailable", "synthetic"):
        raise ValidationError(f"Invalid research_status: {profile_id}")
    if status == "synthetic" and item.get("synthetic") is not True:
        raise ValidationError(f"Synthetic fixture must be flagged explicitly: {profile_id}")
    for key in ("official_facts", "major_signals", "sources", "unknowns"):
        if not isinstance(item.get(key), list):
            raise ValidationError(f"Expected list {key}: {profile_id}")
    for signal in item["major_signals"]:
        if not isinstance(signal, dict) or not all(isinstance(signal.get(k), str) and signal[k].strip() for k in ("topic", "look_for", "basis")):
            raise ValidationError(f"Invalid major_signal: {profile_id}")
    for source in item["sources"]:
        if not isinstance(source, dict):
            raise ValidationError(f"Invalid source: {profile_id}")
        url = urlparse(str(source.get("url", "")))
        if (url.scheme != "https" or not url.netloc or not isinstance(source.get("kind"), str)
                or not isinstance(source.get("title"), str) or not source["title"].strip()):
            raise ValidationError(f"Invalid source: {profile_id}")
    if status == "verified" and (not item["sources"] or not item["official_facts"] or not item["major_signals"]):
        raise ValidationError(f"Verified research requires sources, facts, and major_signals: {profile_id}")
    if status == "partial" and not item["sources"]:
        raise ValidationError(f"Partial research requires at least one source: {profile_id}")
    return item


def validate(root):
    root = Path(root)
    a = rubric_from_file(root / "rubrics" / "universal.json")
    b = rubric_from_file(root / "rubrics" / "major_fit.json")
    if a["total_points"] != 70 or b["total_points"] != 30:
        raise ValidationError("Experimental baseline must total 70+30 points")
    if {x["id"] for x in a["criteria"]} & {x["id"] for x in b["criteria"]}:
        raise ValidationError("Duplicate IDs across rubrics")
    return {"total_points": 100, "research_mode": "dynamic", "bundled_profiles_required": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--profile", help="Optional JSON research snapshot to validate")
    args = parser.parse_args()
    result = validate(args.root)
    if args.profile:
        obj = load_json(args.profile)
        validate_research_profile(obj.get("id"), obj)
        result["validated_profile"] = obj["id"]
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
