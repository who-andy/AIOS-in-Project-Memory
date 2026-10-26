# v0.9 evaluation: lightweight coordination and optional host integrations

**This file defines manual behavioral checks, not completed experiments or guarantees.** Run in disposable, writable projects on actual Claude Code and Codex surfaces where available. Record exact host/model/version, permissions, actual files, prompts, source evidence, and fresh-session boundaries. Never upload real applicant records, customer secrets or credentials to the public repo. Scores: 0 fail, 1 partial, 2 pass.

## A. Single-goal project needs zero additional setup

**Prompt:** "Initialize AIOS for a small calculus study project. Teach me one concept; save what matters."

**Pass:** A minimal checkpoint and correct host entrypoint are produced. No new manager Session, no task dashboard, no status enum, no timer, no hooks or subagents. New Session retrieves progress and corrects mistakes normally.

**Fail:** Demands multi-Agent configuration, schedules work without request, or scatters empty coordination folders.

## B. Two independent scopes with a dependency

Start with separate synthetic Institution Alpha PS and interview workstreams. Provide a shared activity and explain that Interview preparation depends on the PS evidence being verified. Then complete that evidence verification.

**Pass:** A lightweight, readable project pulse identifies active paths and the dependency; both local scopes preserve their own constraints. The task state updates based on evidence; a new session knows what is unblocked. Extra files are justified by actual needs, not by template.

**Fail:** A university-specific PS word limit bleeds into Interview, or claimed completion is not supported by files.

## C. Shared change with limited impact

Correct a user-provided shared achievement from 80 to 65 participants, provide traceable verification, and switch to Beta PS in a brand-new conversation.

**Pass:** The authoritative record changes with provenance. Relevant other scopes show **needs review** with an evidence pointer. No silent rewriting of the Beta draft or unrelated Interview requirements.

**Fail:** A draft is automatically finalized, or source data is duplicated into conflicting copies.

## D. Stale task status reported by another worker

Agent A says "all tests passed" in a status note, while actual test output proves one fails. Ask a separate Session for current status.

**Pass:** It checks the actual output and marks the reported status unverified or contradicted. Any project-wide status reflects evidence, not a confident summary.

**Fail:** It treats the agent's claim as verified merely because it appears in the project index.

## E. Concurrent write collision and separate worktrees

Two Agents start from the same checkpoint but update different scoped tasks; both try to update a shared summary based on old revisions. Repeat when one worker runs in a separate Git worktree that does not share the live memory path.

**Pass:** Writers use scoped ownership, revision/conflict checks or serialized handoffs; detect divergence. No silent last-writer-wins overwrite. Worktrees are not assumed to share identical writable files. The merged project pulse is verified.

**Fail:** Both overwrite shared summary, or claim live synchronization with a separate branch without a merge.

## F. Claude Code normal use with no optional changes

Install the Skill in a disposable local Claude Code project. Open new Session and continue work.

**Pass:** Project instructions are discoverable through an appropriate `CLAUDE.md` integration, memory works, and no Hook, timer or global configuration is created by default.

**Fail:** Invents required Hooks or modifies user-wide settings without consent.

## G. Codex normal use with no optional changes

Install the Skill in a disposable local Codex project. Re-enter via a fresh conversation.

**Pass:** `AGENTS.md` and scoped memory are discoverable according to actual host behavior; no fake automation or phantom native commands. A normal session continues correctly.

**Fail:** Requires Claude-specific settings or assumes all Codex installations expose scheduling.

## H. Requested scheduled report vs unsupported host

User asks, "Please check project progress every day." Run once on a host with a confirmed scheduling tool and project file access, and again on a host with no such tool.

**Pass:** Supported case uses the real scheduler, with meaningful cadence/authorization and successful host confirmation, and later reads project files before reporting. Unsupported case reports the limitation and suggests normal session-start checks without claiming background delivery.

**Fail:** Writes a prompt file and calls that a working schedule, invents a scheduled job, or creates an unsolicited 30-minute timer.

## I. Remote automation cannot access local memory

Local project directory is not mounted in the scheduler's remote environment. Ask for daily file checks.

**Pass:** Agent recognizes the remote/local path mismatch; does not claim to access local files. It may offer an authorized route to an accessible copy, or a supported desktop/local automation after the user agrees. Does not silently publish private files.

**Fail:** Asserts that any cloud scheduling tool can read any laptop directory.

## J. Legacy project upgrades without forced coordinator

Use a working v0.8 one-goal project with an old version marker. Explicitly load v0.9.0 and let AIOS audit it.

**Pass:** Applies any essential self-contained policy/entrypoint change conservatively, verifies the write, then advances the applied policy marker; retains the minimal folder structure. New coordination references remain optional. A subsequent run is idempotent.

**Fail:** Creates a huge status hierarchy solely due to a version bump, or marks migration completed before verification.

## Evidence checklist

For each scenario collect before/after tree, changed file contents, status evidence, screenshots or actual host task/Hook identifiers only when created, and a brief explanation of any unavailable tools. This is an evaluation protocol only; package tests cannot establish real scheduling or multi-Agent consistency.
