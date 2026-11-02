#!/usr/bin/env python3
"""Validate rubric arithmetic and the minimal major-profile contract (stdlib only)."""
import argparse
import json
import re
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
    if not ids or len(ids) != len(set(ids)) or any(not isinstance(x, str) for x in ids):
        raise ValidationError(f"Criteria IDs missing or duplicated: {path}")
    points = [c.get("max_points") for c in rubric["criteria"]]
    if any(type(p) is not int or p <= 0 for p in points):
        raise ValidationError(f"max_points must be positive integers: {path}")
    if sum(points) != rubric.get("total_points"):
        raise ValidationError(f"Rubric total does not equal criteria points: {path}")
    if not isinstance(rubric.get("version"), str):
        raise ValidationError(f"Rubric version missing: {path}")
    return rubric


def validate(root):
    root = Path(root)
    rubric1 = rubric_from_file(root / "rubrics" / "universal.json")
    rubric2 = rubric_from_file(root / "rubrics" / "major_fit.json")
    if rubric1["total_points"] != 70 or rubric2["total_points"] != 30:
        raise ValidationError("v1.0 rubrics must total 70+30 points")
    shared = {c["id"] for c in rubric1["criteria"]} & {c["id"] for c in rubric2["criteria"]}
    if shared:
        raise ValidationError(f"Duplicate IDs across rubrics: {sorted(shared)}")
    files = sorted((root / "profiles").glob("**/*.json"))
    if not files:
        raise ValidationError("No major profiles found")
    seen = set()
    for path in files:
        item = load_json(path)
        for key in ("id", "version", "verified_on", "target_intake", "university", "programme", "interpretation_note"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValidationError(f"Invalid {key}: {path}")
        if item["id"] in seen:
            raise ValidationError(f"Duplicate profile id: {item['id']}")
        seen.add(item["id"])
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["verified_on"]):
            raise ValidationError(f"Invalid verified_on: {path}")
        if not isinstance(item.get("official_facts"), list) or not item["official_facts"]:
            raise ValidationError(f"Missing official_facts: {path}")
        if not isinstance(item.get("major_signals"), list) or not item["major_signals"]:
            raise ValidationError(f"Missing major_signals: {path}")
        for signal in item["major_signals"]:
            if not isinstance(signal, dict) or not signal.get("topic") or not signal.get("look_for"):
                raise ValidationError(f"Invalid major signal: {path}")
        if not isinstance(item.get("sources"), list) or not item["sources"]:
            raise ValidationError(f"No sources: {path}")
        for source in item["sources"]:
            uri = urlparse(source.get("url", ""))
            if uri.scheme != "https" or not uri.netloc or not source.get("title") or not source.get("kind"):
                raise ValidationError(f"Invalid source: {path}")
    return {"profiles": len(files), "total_points": rubric1["total_points"] + rubric2["total_points"], "profile_ids": sorted(seen)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    print(json.dumps(validate(args.root), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
