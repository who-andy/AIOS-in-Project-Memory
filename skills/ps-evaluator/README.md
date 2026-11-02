# PS Evaluator Skill v0.1.0

[中文说明](README.zh-CN.md)

An experimental, **major-aware** undergraduate personal statement evaluator, packaged as a portable Agent Skill for file-capable agents such as Claude Code and Codex. First profiles: HKU BBA Accounting and Finance, HKUST BSc Economics and Finance.

**What it does:** evidence-based rubric scoring (70 points universal quality + 30 points programme fit); same-PS cross-major comparison; pairwise version reviews; aggregate/check independent judge scores; descriptive benchmark diagnostics.

**What it does not do:** no admission probability estimation, no verified university PS grade, no API call or automatic multi-model orchestration, no claim of psychometric calibration. The agent performs the qualitative judgement; local Python scripts validate and aggregate structured results.

## Install

Copy the entire `ps-evaluator` folder to the skill directory used by your agent, for example:

- Codex: `~/.agents/skills/ps-evaluator/` or a project `.agents/skills/ps-evaluator/` (check your Codex release's skill discovery settings).
- Claude Code: `~/.claude/skills/ps-evaluator/` or `.claude/skills/ps-evaluator/` in a project.

If installed from an AIOS checkout, only copy the `skills/ps-evaluator` directory. AIOS is **not** required.

Then ask: `Use ps-evaluator to evaluate this PS for HKUST BSc Economics and Finance. Explain your evidence and do not predict admission probability.`

## Commands

```bash
python3 scripts/validate_profiles.py --root .
python3 -m unittest discover -s tests -v
python3 scripts/aggregate_scores.py --rubrics . --input examples/evaluations.synthetic.json
python3 scripts/benchmark.py --input examples/benchmark.synthetic.json
```

All scripts use the Python 3 standard library. No API key or dependency installation required. These CLI commands are run from this directory. See `references/output-schema.md` for the record format. The example data is **synthetic, for CLI testing only**; do not regard it as an actual model evaluation.

## Major profiles

University curriculum statements and the project's own evaluation signals are intentionally separated. Source URL, verification date, intended intake, and version are in each profile. Recheck official English-language pages at assessment time. Programme fit scores never assume that a finance keyword proves readiness for economics or accounting.

## Privacy

Do not commit actual applicant PS drafts or identifying admission documents. Keep private input/output files outside this public source tree. Reports and records should be shared only with the user's authorization.

## Validation roadmap

v0.1: deterministic schema checks and synthetic regression tests.
v0.2: human-labelled reference sample with adjudication and more majors.
v0.3: controlled multi-model assessments and documented agreement metrics.

MIT license is inherited from the host repository when published under that repository.
