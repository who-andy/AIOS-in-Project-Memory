---
name: ps-evaluator
description: Review and compare undergraduate personal statements using evidence-grounded writing rubrics and university-major profiles. Use for Hong Kong undergraduate PS evaluation, major-fit analysis, pairwise comparisons, and scoring reliability checks.
---

# PS Evaluator

Evaluate a personal statement as a piece of evidence about an applicant's intellectual development and programme fit. Never claim that the experimental scores are university admissions scores or predict admission probability.

## Before scoring

1. Determine the **exact university, programme name, qualification route, intake year**, and whether a single PS serves multiple choices. Ask only for missing information that materially blocks a valid programme assessment; otherwise state assumptions and continue.
2. Read `references/methodology.md`, `rubrics/universal.json`, `rubrics/major_fit.json`, and the relevant profile in `profiles/`. Treat profile assessment signals as **researcher interpretations**, not official admissions criteria.
3. Check the `verified_on` date and official `sources` in the profile. For time-sensitive requirements, verify against current official university English-language sources if browsing is available. If verification is unavailable or a profile is missing/stale, disclose it and use an explicitly provisional major fit assessment. Never invent admission requirements.
4. For user-provided statements, preserve privacy. Do not publish, upload, or add them to an external/public repository without explicit permission. All bundled samples are synthetic.

## Evaluate mode

1. Read the entire PS before scoring. Note submission constraints only if verified for the route and year; flag word count, inconsistencies, inaccurate terminology, and high-risk claims separately.
2. Score every universal criterion using `rubrics/universal.json`, then each fit criterion using `rubrics/major_fit.json`, on integer scales from 0 to maximum points. The anchors are qualitative guidance, not fake psychometric calibration.
3. For each criterion, provide `score`, a concise `rationale`, and 1–2 **verbatim quotations** from the PS as evidence. Distinguish missing evidence from weak evidence. If there is no support, set `evidence` to [] and explain the deduction.
4. Apply `major_signals` from the programme profile to interpret fit without keyword counting. Demonstrated reasoning matters more than name-dropping courses. A strong finance project may have limited evidence for economics; do not assume otherwise.
5. Report high-risk concerns separately: unsupported accomplishments, contradiction, misuse of academic concepts, material factual problems, and unverified constraints. Do not silently correct the student's biography.
6. **No admission prediction.** Never turn a 90 vs 80 PS score into estimated offers or acceptance percentages. Report score uncertainty and the non-validated nature of weights.
7. Produce a clear report with (a) universal subtotal /70, (b) major fit subtotal /30, (c) provisional total /100, (d) strongest evidence, (e) highest-impact changes, (f) risks, (g) profile source URLs and verification state.
8. If structured evaluation data is needed for aggregation, use the JSON schema described in `references/output-schema.md`, then run `python3 scripts/aggregate_scores.py --rubrics . --input evaluations.json --output report.json`. Do not fabricate evaluator runs.

## Compare mode

1. Anonymize labels to A/B. Independently evaluate each under the **same target major** and rubric version.
2. Compare substantive evidence and major fit before discussing prose polish. Explicitly check if the difference is bigger than scoring disagreement.
3. Reverse A/B presentation order in a second judge pass when possible; log judge identity, date, and model/version. Avoid treating multiple runs by the same model as independent human evidence.
4. For a multi-major submission, **reuse the same universal scores** for an unchanged draft and score each major fit separately; disclose per-major trade-offs.

## Benchmark mode

1. Use synthetic or consented anonymized cases, human-rated reference judgements when available, and explicit counterfactual edits (cosmetic vs substantive, major swaps, order swaps).
2. Record prompts, rubric/profile versions, model names, temperatures where available, random seeds where supported, and exact PS version hashes. Do not claim these settings guarantee reproducibility.
3. Run `python3 scripts/benchmark.py --input benchmark_results.json` for descriptive disagreement / rank-flip diagnostics. Scores without expert ground truth measure **agreement**, not accuracy or admissions validity.
4. Run `python3 -m unittest discover -s tests -v` before shipping changes.

## Additional guidance

- Read `references/methodology.md` for anchor interpretations, source hierarchy and fairness.
- Read `references/output-schema.md` for machine-readable evaluator records and examples.
- Keep the skill independent of AIOS or any one model provider; no mandatory APIs or paid tools.
