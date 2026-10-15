# Changelog

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
