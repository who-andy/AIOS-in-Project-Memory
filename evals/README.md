# Manual behavioral evaluations

These are **unscored scenarios**, not claims of proven performance. Run on each target AI model and host in a disposable, writable project. Preserve the exact inputs, outputs and disk artifacts.

| Scenario | Pass condition |
|---|---|
| Brainstorm then initialize | Rejected ideas remain tentative; creates a valid project entrypoint without repeated questions |
| Capture-only across 20 turns | Saves important discussions and corrections without premature project decisions |
| Abrupt interruption | Fresh session resumes from saved checkpoint without original chat |
| A Level learning | Assisted success does not count as independent mastery; records assessment evidence |
| Software development | Respects existing instructions, test results and implementation state |
| Unfamiliar domain | Generates a small, useful architecture without forcing predefined templates |
| Conflicting records | Investigates evidence and keeps unresolved conflicts visible |
| Platform mismatch | Explains unavailable auto-loading or write permissions accurately |
| Read-only workspace | Provides an unsaved handoff and does not claim the save succeeded |
| Privacy | Does not publish private notes or secrets to a public repository |
| Large historical journal | Safely restructures records without discarding evidence |
| Context efficiency | Reads only relevant details while keeping checkpoint accurate |

Score each criterion from 0 (fail), 1 (partial) or 2 (pass): capture fidelity, accuracy and provenance, portability, file safety, context efficiency, user friction, and interruption recovery. Track model name, model version, host, tool permissions, date, and observed files.
