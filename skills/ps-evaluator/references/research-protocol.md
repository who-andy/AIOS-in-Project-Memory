# Dynamic University and Major Research Protocol

Research the requested target at runtime. **Do not assume a bundled profile or a fixed Hong Kong university-wide rubric.** The agent should adapt the research, not invent standards.

## Research order

1. **Identity and scope**: full university name, exact degree/programme, intake (e.g. 2027), qualification route (e.g. International A-Level/Non-JUPAS), nationality/local status when it changes the route, and number of programme choices sharing one statement.
2. **Official admissions instructions**: whether PS is required, optional, or unconfirmed; required prompt(s), word/character/page limits, shared-statement rules, exceptions, and special application materials. Look for exact route-specific wording.
3. **Official programme curriculum and goals**: degree aims, required modules, disciplinary methods, relevant learning outcomes, programme options. A course list establishes academic scope, **not** an admissions preference or evaluation weight.
4. **Official selection statements**: verify any expressly published criteria, interview requirements, or special portfolios. If PS importance or rubric weights are unpublished, set them to `unknown`.
5. **Interpretation**: infer 2–5 `major_signals` as research hypotheses from grounded curriculum facts. Each signal must explain the ability it seeks and the source fact from which it was inferred. Avoid mere keyword matching. Do not assume accounting, economics, management, engineering and design share academic fit criteria.
6. **Cross-choice check**: if only one PS can be uploaded, analyse whether it authentically covers all intended programmes. Do not sacrifice the user's primary reason for studying merely to list every module.

## Source rules

Prefer the current official English admissions site, programme website and department syllabi. Record the original URLs (not only search result IDs), page title and date reviewed. Do not rely on Chinese-language sources for research. If several official pages conflict, report the conflict and mark partial, rather than choosing a convenient rule. A current-year undergraduate rule may differ across Non-JUPAS, international non-local and JUPAS routes. A missing source is **unknown**, never proof that a document is optional.

## Snapshot contract

A dynamic profile uses an arbitrary stable ID (e.g. a slug derived from school, programme, route, intake) and a version for the specific research snapshot. Example fields, with statuses that should reflect evidence:

```json
{
  "id": "example-university-example-degree-2027-international",
  "version": "research-2026-11-02-a",
  "researched_on": "2026-11-02",
  "target_intake": "2027",
  "route": "international qualifications",
  "university": "Example University",
  "programme": "Example Degree",
  "research_status": "partial",
  "submission": {"ps_status": "unknown", "limit": null, "shared_choices": null},
  "official_facts": [],
  "major_signals": [{"topic": "example only", "look_for": "illustrative evidence", "basis": "Unverified synthetic fixture"}],
  "sources": [],
  "unknowns": ["Exact PS submission requirement", "No official sources gathered"],
  "interpretation_note": "Synthetic shape example. Do not treat as verified university guidance."
}
```

- `research_status = verified` requires applicable official sources and grounded factual claims for the exact programme and route. This status means research inputs are checked, **not that admissions weights or the AI judge are validated**.
- `partial` means some applicable evidence exists but important admissions/programme facts are unresolved.
- `unavailable` means there is no usable official evidence for the target in the current run; prefer universal-only output.
- `official_facts` must distinguish descriptions from evaluation inferences. `major_signals` are inferred criteria and must not be reported as official PS requirements.
- A profile can be persisted with a hash in a private work directory for repeatability. Before another intake or major, check freshness rather than blindly reusing it.

## What to say in the final report

Show: target + intake + route; official submission constraints with citations; research status and unknowns; universal writing score; fit score only with sufficient programme research; explanation of programme signals linked to source facts; and the reason for any caveats. Do not assume the user's existing admissions route from a past case without checking applicability.
