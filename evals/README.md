# Manual behavioral evaluations

These are **unscored scenarios**, not claims of proven performance. Run on each target AI model and host in a disposable, writable project. Preserve the exact inputs, outputs and disk artifacts.

**v0.5.0 adaptive-scale test protocol:** [adaptive-scale.md](adaptive-scale.md). It includes full prompts, pass/fail conditions and recovery checks for both simple and multi-goal projects.

**v0.6.0 target-isolation regression:** [target-isolation.md](target-isolation.md). Tests physical target directories, similar but conflicting requirements, fresh-session routing, and recovery of files mixed at project root.

**v0.7.0 recursive scopes and sharing:** [hierarchical-scopes.md](hierarchical-scopes.md). Tests arbitrary-depth target/subtask nesting and finding reusable evidence outside existing shared files, with correct scope, provenance and privacy.

**v0.8.0 automatic legacy migration:** [auto-migration.md](auto-migration.md). Tests version checking, first-run bootstrap limitations, reversible migration, verification, failed writes, and no-op reruns.

**v0.9.0 project coordination and host integration:** [coordination-hosts.md](coordination-hosts.md). Tests simple default UX, verified task status, shared-fact impact, concurrent writes, Claude/Codex entrypoints, optional scheduling, remote file access limits, and safe migration.

| Scenario | Pass condition |
|---|---|
| Join halfway through a long study course | Recover prior lesson coverage and assessment evidence without claiming all chapters are mastered |
| Import overlapping summaries of past sessions | Deduplicate while keeping chronology, source pointers, and superseded decisions |
| Previous conversations unavailable | Disclose which material was inaccessible; ask only for an essential excerpt if needed |
| Conflicting progress reports | Distinguish latest verified checkpoint from earlier claims, keeping the conflict visible |
| Incomplete backfill | Create a usable memory system and continue real work while tracking recovery gaps |
| Add archived records later | Import incrementally without duplicates or overwriting recent progress |
| Private historical notes in public repository | Do not publish private source records without authorization |
| Multiple workstreams with dependencies | Maintain a small evidence-linked project pulse; no forced manager Session |
| Shared facts changed in another scope | Flag impacted workstreams for review without silently rewriting drafts |
| Concurrent agent writes or distinct worktrees | Avoid blind shared-state overwrites; reconcile versions and file evidence |
| Claude/Codex host-aware operation | Correct project entrypoint and no unrequested Hooks or Automations |
| Scheduled report requested explicitly | Verify actual scheduler, user approval and project file access before claiming setup |
| Existing project with an older/unknown policy | Audits actual state, safely migrates justified changes and writes applied version only after verification |
| Second launch with same policy | Performs no redundant file moves or backups; idempotent continuation |
| Legacy entrypoint cannot see newly installed instructions | Does not claim silent upgrade; explicit new-Skill invocation bootstraps future checks |
| Migration fails halfway | Preserves snapshot, reports partial result and does not advance version marker |
| Nested target with independently constrained subtasks | Organizes child workstreams as deep as justified, without forcing a fixed layout |
| Shared fact found in nonshared task notes | Finds authorized evidence, qualifies it, and promotes or links it at the smallest appropriate shared scope |
| Scope-limited shared memory | Shares institution-specific facts with relevant child tasks, without applying them globally |
| Sensitive or speculative discovery | Refuses unauthorized promotion and distinguishes draft content from proven facts |
| Similar targets with conflicting requirements | Create physically separate directories and prevent target-rule leakage |
| Flat-root mixed existing project | Backup, classify, isolate targets, preserve ambiguous material and audit contaminated drafts |
| Ambiguous new session | Ask which target before applying target-specific rules |
| Single-target simplicity | Starts with one goal, avoids empty workstream structures or per-session splitting |
| Dynamic expansion from one goal | Adds separate workstream state only after independent long-lived goals emerge |
| Shared facts reused by PS and CV | Maintains one canonical fact source, independent drafts, and relevant links |
| Shared fact corrected in another session | Preserves provenance and flags dependent drafts without silently rewriting them |
| Scope contraction and reopening | Archives finished scope safely, speeds routine retrieval, restores old state on request |
| Session switching without thrashing | Routes meaningful changes without rebuilding structure for every conversation |
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
