# Structured evaluation records (v0.2)

An evaluation JSON includes a dynamically researched `profiles` registry plus an `evaluations` array. No school profile ships in the Skill. A `target_major` must point to the exact registry key for that university, programme, route and intake.

```json
{
  "profiles": {
    "example-major-2027": {
      "id": "example-major-2027",
      "version": "research-v1",
      "researched_on": "2026-11-02",
      "target_intake": "2027",
      "route": "international qualifications",
      "university": "Example University",
      "programme": "Example Major",
      "research_status": "unavailable",
      "submission": {"ps_status": "unknown", "limit": null, "shared_choices": null},
      "official_facts": [],
      "major_signals": [],
      "sources": [],
      "unknowns": ["No official sources available"],
      "interpretation_note": "Universal-only until official information can be reviewed"
    }
  },
  "evaluations": [
    {
      "document_id": "my-private-document-label",
      "target_major": "example-major-2027",
      "judge_id": "model-name",
      "judge_version": "precise-version-if-known",
      "rubric_versions": {"universal": "1.0.0", "major_fit": "1.0.0"},
      "profile_version": "research-v1",
      "scores": {
        "critical_reflection": {"score": 0, "evidence": [], "rationale": "No relevant reasoning in supplied draft"},
        "evidence_contribution": {"score": 0, "evidence": [], "rationale": "No specific role shown"},
        "intellectual_curiosity": {"score": 0, "evidence": [], "rationale": "No independent investigation shown"},
        "narrative": {"score": 0, "evidence": [], "rationale": "No coherent argument"},
        "language": {"score": 0, "evidence": [], "rationale": "Draft not provided"},
        "authenticity": {"score": 0, "evidence": [], "rationale": "No personal perspective available"}
      },
      "risks": ["Programme fit cannot be assessed without official sources"]
    }
  ]
}
```

Above is a schema illustration only; do not score a nonexistent document. See `examples/evaluations.synthetic.json` for parser fixtures.

### Profile status and outputs

- `verified`: sources + official facts + inferred major signals are present and applicable. Program fit may be scored, but does **not** establish official weights or correctness of the AI judgement.
- `partial`: some official sources exist; programme fit can be scored only with clearly marked provisional limitations.
- `unavailable`: universal-only record, omit all three major-fit score keys. `major_fit` and `total` are reported as `null` by the aggregator.
- `synthetic`: only for unit-test fixtures, requires `synthetic: true` and is always unverified.

Every scored criterion must contain integer `score` in range, `rationale`, and `evidence` array of at most two exact short quotations (or [] if absent). `aggregate_scores.py` validates structure and computes sums but **cannot** check external source accuracy, validate that quotations came from the PS, or test admissions prediction validity.

Benchmark inputs are separate JSON `observations` with `{case_id, judge_id, version_id, order: 'AB'|'BA', preferred: 'A'|'B'|'tie', score_a, score_b}`. Preferred A and B refer to canonical documents regardless of display order.
