---
name: ps-evaluator
description: Evaluate and compare undergraduate personal statements with evidence-based writing criteria and live, programme-specific university research. Use for Hong Kong or other undergraduate PS review, programme fit, multi-choice statements, and evaluation reliability tests.
---

# PS Evaluator

An evidence-grounded, research-first PS evaluation skill. The same Skill handles different universities, programmes, application routes and intake years. It does **not** contain university-specific grading weights or assume that every university gives a PS the same admissions importance.

## Intake and research: required before programme-fit scoring

1. Identify the target **university**, **exact programme title**, **intake year**, **qualification/admissions route**, and **all programme choices sharing this statement**. Prefer the supplied application details; ask only if a missing distinction materially changes the evaluation. A school name alone is insufficient when programme requirements vary.
2. Read `references/research-protocol.md`, `references/methodology.md`, `rubrics/universal.json`, and `rubrics/major_fit.json`. Research the live, official, English-language university admissions pages and target programme/department curriculum pages if browsing is available. Search admissions instructions first, then programme learning objectives/courses, then official subject prerequisites and interview/portfolio information if relevant. Never substitute generic search snippets for exact requirements when the full official page is accessible.
3. Produce a **dynamic programme research snapshot** following `references/research-protocol.md`. Separate (a) directly sourced official application requirements, (b) official curriculum descriptions, (c) researcher-inferred `major_signals`, and (d) unknowns. Save a locally generated snapshot outside the installed Skill when the user has a writable project; otherwise include a short source-linked snapshot in the report. No bundled school profile is mandatory.
4. Confirm which admissions route the rules cover. Record URLs and retrieval date; do not imply an undated or earlier-cycle page governs the user's intake. If research tools are unavailable, sources contradict each other, or the programme cannot be verified, mark `research_status: partial` or `unavailable`, explicitly lower confidence, and do not invent a word limit or marking criteria. You may still provide universal-only scoring, with programme fit marked provisional or omitted.
5. Inspect whether **one shared PS** must serve several programme choices. Evaluate the same original prose once under the universal rubric, then assess fit and coverage for each relevant programme independently. Distinguish school-level submission constraints from programme-level preparation signals.

## Evaluate

1. Read the entire PS. Report *verified* length/format/prompt constraints separately from subjective quality scores. Flag material factual inconsistencies, unsupported claims to verify, academic misuse, and missing programme coverage without inventing biographical facts.
2. Use `rubrics/universal.json` for shared PS quality (0–70) and `rubrics/major_fit.json` for programme fit (0–30). **70/30 is an experimental editorial design**, not any university's internal weight. Do not make the numerical breakdown contingent on a guessed university preference. If a verified published assessment rubric exists, report it separately and explicitly; never silently overwrite the comparative 70/30 baseline.
3. Judge fit from **accurate disciplinary understanding, relevant reasoning/evidence, and plausible academic direction** tied to verified programme context. Do not reward course name-dropping, prestige, jargon, or raw achievement counts. Major signals are heuristic interpretations, never official admissions criteria unless literally published as such.
4. For every criterion give an integer score, 1–2 short exact PS quotations where available, and a concise rationale. Unsupported criteria receive `evidence: []` and an explanation. Keep grounded uncertainty visible. Do not infer originality, truth or personal characteristics from prose style.
5. Provide universal subtotal, per-programme fit subtotal, optional experimental total, evidence-backed strengths, prioritized substantive changes, submission checks, source URLs and research status. When major research is unavailable, present a **universal-only** assessment and do not imply a validated major-fit score.
6. Never translate PS 90/100 vs 80/100 into admissions probabilities, offer predictions or fixed school-specific importance. Academic qualifications, references, interviews and programme context can matter independently.

## Modes

- **Evaluate**: one statement and one/multiple programme contexts; research each target first.
- **Compare**: blind A/B rating for the *same* programme, then reverse presentation order where feasible. Discuss meaningful substantive differences beyond cosmetic score noise.
- **Cross-major**: hold universal scores constant for the exact same draft, research each chosen programme separately, and report programme-specific fit and shared-statement trade-offs.
- **Benchmark**: run consented/anonymized or synthetic cases, record model/version, prompts, rubric versions, source snapshot/hash, and compare judge disagreements/order reversals. Use `python3 scripts/benchmark.py --input examples/benchmark.synthetic.json`. Agreement is not proof of admissions validity.

## Structured records and checks

For machine-readable results, follow `references/output-schema.md`; include a dynamically generated `profiles` registry in each evaluation JSON, rather than relying on built-in profile IDs. Then use:

```bash
python3 scripts/validate_profiles.py --root .
python3 scripts/aggregate_scores.py --rubrics . --input examples/evaluations.synthetic.json
python3 -m unittest discover -s tests -v
```

Scripts validate rubric arithmetic and result schema; they do not browse, call an LLM, or verify PS quotations against an original draft. No model, browser access or paid API is bundled by this Skill.

## Privacy and evidence discipline

Do not commit actual PS drafts, identifiable application documents or research reports to public repositories without explicit consent. Treat application essays as confidential by default. Prefer official English-language sources. If unavailable, explain that fit is provisional. Never cite a curriculum page as evidence of a university's secret PS scoring weights. Keep this Skill usable independently of AIOS and of any particular agent provider.
