# Evaluation records

Create one JSON file containing an object with `evaluations` (array). Each entry:

```json
{
  "document_id": "synthetic-a",
  "document_sha256": "optional hex sha256 from local PS file",
  "target_major": "hku-accounting-finance",
  "judge_id": "model-or-human-label",
  "judge_version": "specific version if known",
  "rubric_versions": {"universal": "1.0.0", "major_fit": "1.0.0"},
  "profile_version": "1.0.0",
  "scores": {
    "critical_reflection": {"score": 15, "evidence": ["exact quote"], "rationale": "..."},
    "evidence_contribution": {"score": 12, "evidence": ["exact quote"], "rationale": "..."},
    "intellectual_curiosity": {"score": 11, "evidence": ["exact quote"], "rationale": "..."},
    "narrative": {"score": 8, "evidence": ["exact quote"], "rationale": "..."},
    "language": {"score": 4, "evidence": ["exact quote"], "rationale": "..."},
    "authenticity": {"score": 4, "evidence": ["exact quote"], "rationale": "..."},
    "disciplinary_understanding": {"score": 8, "evidence": ["exact quote"], "rationale": "..."},
    "relevant_evidence": {"score": 7, "evidence": ["exact quote"], "rationale": "..."},
    "academic_direction": {"score": 5, "evidence": ["exact quote"], "rationale": "..."}
  },
  "risks": ["claim needs verification"],
  "major_profile_checked": true
}
```

`aggregate_scores.py` rejects unknown criteria, missing required scores, non-integer or out-of-range scores, missing rationale, and unverifiable profile IDs. It computes subtotals deterministically. It does not run language models, validate whether a quotation appears in the original PS, or establish admission likelihood.

Benchmark input is a separate JSON object with `observations`: `{ "case_id": ..., "judge_id": ..., "version_id": ..., "order": "AB" | "BA", "preferred": "A" | "B" | "tie", "score_a": 0..100, "score_b": 0..100 }`. `preferred` always refers to canonical document IDs A and B, even after an order swap. For valid paired AB/BA observations from the same judge/version, the tool reports preference reversals; without both orders it reports insufficient coverage. It also aggregates absolute disagreement across judges for the same `case_id` and `version_id` when scores are present.
