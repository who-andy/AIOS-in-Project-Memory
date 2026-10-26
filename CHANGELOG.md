# Changelog

## 0.8.0 (2026-10-26)

- Added **Version-Aware Self-Migration**: when a newer AIOS Skill is actually loaded into an authorized existing project, it audits the current memory layout and automatically applies necessary low-risk, reversible upgrades.
- Added a lightweight applied-policy marker (`AIOS memory policy: 0.8.0`) in generated project entrypoints/checkpoints. Advance it only after verified successful application, never merely on installation or partial writes.
- Added legacy bootstrap behavior: when old project instructions do not yet know how to check for updates, explicitly invoke the installed new Skill once in the project. Future entrypoints can check locally discoverable trusted Skill versions without mandatory internet access.
- Defined snapshot, evidence classification, source/destination mapping, link repair, rollback, concurrency awareness, high-risk approval gates and idempotent reruns.
- Emphasized that no automatic background service or GitHub release event can directly migrate local project files.
- Added eight manual migration evaluation cases and deterministic contract tests, updated English and Chinese usage instructions.
- No mandatory hooks, install-time scripts, dedicated version-manifest file or fixed project directory template.

## 0.7.0 (2026-10-25)

- Introduced **recursive, model-designed project scopes**: independently evolving workstreams can nest under targets and subtargets without a hard-coded depth or directory order, while one-target projects remain minimal.
- Made sharing **relative to scope**, so evidence can be reusable within a parent target (e.g., its statement and interview) without becoming a global requirement for all targets.
- Added **on-demand evidence discovery**: when relevant information is missing from loaded shared records, agents inspect authorized related scope indexes and source notes, verify provenance, and link or promote genuinely reusable evidence to a suitable canonical shared scope.
- Explicitly protected scope-specific requirements, draft claims, and private material from unintended global promotion or cross-target reuse.
- Required navigation and source links to remain recoverable after progressive nesting, promotion, and safe reorganization.
- Added manual behavior tests for deep nesting, nonshared-source discovery, sharing boundaries, privacy, cross-cutting workstreams, and incremental migrations; expanded deterministic contract checks.
- No required runtime dependencies, background services, fixed folder templates, or mandatory Hooks. The installed Skill and existing project folders must be updated separately.

## 0.6.0 (2026-10-25)

- Fixed a real-world multi-target failure mode: distinct recipients or independently constrained goals can no longer remain as ambiguous records mixed at the project root.
- Added explicit **target directories** with a discoverable shared knowledge area when multiple persistent targets have conflicting requirements, drafts or checkpoints. A single-target project still remains minimal.
- Added **target-before-retrieval routing** and scope/provenance verification for limits, requirements, instructions, and decisions; unrelated targets must not silently inherit one another's rules.
- Added safer migration for already cluttered project roots: inspect and snapshot, classify, separate, repair references, verify saved results and flag drafts already contaminated by another target's constraints.
- Extended README documentation and regression scenarios for similar targets with deliberately conflicting requirements, ambiguous fresh sessions and unrelated industries.
- No mandatory runtime tools or fixed school-specific folder templates. Existing local projects require an explicit agent migration run after updating the Skill.

## 0.5.0 (2026-10-21)

- Added **Complexity on Demand**: minimal memory for a single goal, selective expansion only when real independent deliverables emerge.
- Introduced shared project knowledge plus isolated workstream state, with one authoritative source for reusable facts and independent drafts.
- Added adaptive contraction, archiving and safe consolidation when goals finish or are explicitly removed, without deleting recoverable history.
- Added source-aware propagation of factual corrections, with dependent drafts flagged for review rather than silently rewritten.
- Tightened scoped retrieval, non-destructive migration, version checks and concurrency safeguards.
- Added an eight-scenario behavioral protocol and deterministic contract tests covering minimal startup, growth, shrinkage, cross-session continuity and failure cases.
- Deferred optional host-specific Hooks and integrations to separate work; no new runtime dependencies or fixed project templates.

## 0.4.2 (2026-10-15)

- Renamed the Agent Skill identifier to `aios-in-project-memory` to match the GitHub repository.
- Updated example invocations, tests, and README migration notes. No changes required to existing project memory files.

## 0.4.1 (2026-10-15)

- Rewrote English and Chinese READMEs around the primary use case: AI creates and updates memory files in the local project directory, and later sessions or different AI agents resume from those files.
- Made local project storage and cross-AI recovery explicit in core Skill instructions.
- Added contract tests for the user-facing description and the project-folder focus.

## 0.4.0 (2026-10-15)

- Added retrospective onboarding for learning and software projects that began before the memory system was installed.
- Added source inventory, incremental historical reconstruction, evidence reconciliation, and partial recovery tracking.
- Preserved current progress while historical records are imported in stages.
- Documented limitations for inaccessible earlier sessions and private materials.

## 0.3.0 (2026-10-15)

- Rebuilt as a prompt-first Skill with a single authoritative `SKILL.md`.
- Made model-generated, host-loaded project entrypoints central to ongoing memory capture.
- Preserved discussion-first workflow with optional capture-only mode before initialization.
- Added high-recall capture, write verification, provenance, privacy, and safety contracts.
- Removed prescriptive templates and runtime dependencies; architecture is model-designed.
- Added deterministic contract tests and unscored behavioral evaluation scenarios.

Earlier v0.1.0 and v0.2.0 development bundles are not part of this distribution.
