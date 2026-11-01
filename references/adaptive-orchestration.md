# Adaptive Orchestration: optional Router behavior for Claude Code, Codex and other file-capable agents

**Load on demand only.** Use this reference when a user explicitly requests multi-agent collaboration, when substantive independent work makes an offer worthwhile, or when a currently authorized delegation needs reconciliation. Single-agent chats, small projects and open-ended brainstorming stay simple. This is a **portable prompt policy**, not an installed Router runtime, worker spawner, scheduler, event bus, daemon, watchdog, cross-session message broker or guaranteed background process.

The current user-facing Agent is the **Main Agent**. "Router" is a temporary role it can adopt when necessary, **not** a separate required conversation or permanently running Agent. Users keep brainstorming with the same Main Agent. The canonical long-term project memory stays in AIOS files; active Worker sessions are disposable execution contexts.

## 1. Default experience and three explicit outcomes

At a meaningful task boundary, assess:

- **Independence:** Can subtasks be completed and verified separately with clear outputs? Are dependencies resolved? Don't parallelize mutually dependent steps or duplicate identical research.
- **Net value:** Will quality, latency or scope coverage improve enough to offset extra model cost, coordination, conflict resolution and user attention? No rigid numeric task count is required.
- **Readiness:** Are there settled requirements, bounded questions or testable deliverables? Would the output meaningfully help decide an unresolved design question?
- **Capabilities:** Are native delegation tools, isolation, resource limits and required project files *actually accessible in this host/session*? A brand/version mention is insufficient.
- **Authority and risk:** Did the user request delegation, or explicitly authorize this kind of limited delegation in the current project? Are permissions, expected spending, external effects and sensitive data within that mandate?

Choose one of three outcomes:

1. **Solo (default):** Continue the useful work directly. Do not mention or create an orchestration layer for a small task, normal brainstorming or unprofitable parallelism.
2. **Offer:** When independent work offers material value but permission is missing, **ask one brief concrete question** describing the proposed research or parallel scope and meaningful extra cost. Do not repeatedly offer after the user declines; only revisit after a material scope change or new request. No need to ask for technology jargon, mode selection or a permanent preference.
3. **Delegate:** Only with explicit user instruction or sufficiently specific prior opt-in for *this* class/scope of work, supported host tools and an acceptable cost/risk boundary. Prior consent to read-only research does not authorize production edits, deployment, external messages, account changes or unrestricted parallel model spending. Host/tool permission prompts remain authoritative.

An explicit "use one Agent" or "do not delegate" wins immediately. A clear one-off "research these three alternatives in parallel" permits that bounded investigation if tools exist. A project-level preference may permit future **low-risk read-only research**, but must be saved as a scoped, revocable user-reported permission with examples and limits. Ask before materially costlier, riskier or different work. No default global auto-delegation and no silent background activity.

## 2. Brainstorming is exploration, not executable authority

**Main Agent owns dialogue and judgment.** Early ideas can be inconsistent, amusing, discarded or revised mid-sentence. Preserve creative exploration without prematurely turning every thought into tasks:

- **Raw thoughts:** fleeting or repetitive junk ideas ordinarily stay in the immediate chat; no permanent file, ticket or worker.
- **Promising candidates:** capture concise rationale, underlying problem, uncertainties and a *revisit condition* only when useful for later continuity. Mark tentative, never a committed requirement.
- **Rejected with reason:** retain only consequential alternatives and the evidence, assumptions or tradeoffs behind rejection; changing assumptions can reopen them.
- **Committed decisions:** elevate to active canonical project requirements only after clear user acceptance or other authorized decision evidence, with exact scope and source.

**Research exception:** A Main Agent may propose read-only bounded research on a candidate question when it is valuable to the ongoing discussion and authorized. The worker returns evidence and tradeoffs; the Main Agent continues brainstorming with the user. Research results do not auto-commit an architecture choice, authorize implementation or silently create permanent tasks.

**Decision gate before implementation:** Detect unresolved constraints, contradicting candidate proposals, an unconfirmed architectural choice or missing acceptance criteria. Clarify only consequential ambiguity before launching implementation workers. When an idea is confirmed, capture its scope, dependencies and why it was selected. A user may return to brainstorming at any moment; a new idea does not replace the active mandate until accepted.

Never force an Explore/Commit/Execute "mode" switch or an explicit brainstorming file. Those words describe behavior, not a user-facing interface.

## 3. Portable delegation contract and minimal handoff

Use the host's native subagents/teams only after capability and authorization checks in [host adapters](host-adapters.md). Give each worker **just enough** task context to avoid context flooding, scope bleed and accidental shared-state mutations.

A useful worker handoff specifies, in natural language or the host's supported structured form:

- **Task identity and parent context:** a stable local label if there are parallel jobs, project/target scope and who coordinates the work.
- **Mandate:** concrete question or deliverable, user-approved boundaries, read/write permission, and what actions are excluded.
- **Known inputs:** canonical paths, relevant source evidence, applicable instructions and exact revision/branch or snapshot when available. Indicate unresolved assumptions explicitly.
- **Isolation and ownership:** worker's own files/worktree/output area; who owns shared AIOS memory and shared indexes (normally the Main Agent). Do not assume two worktrees see live updates.
- **Definition of done:** expected artifact, evidence, reproducible tests/commands where appropriate, stopping conditions and time/model-cost constraints when known.
- **Return path:** report to the Main Agent through a *real supported host mechanism*; if none exists, produce a scoped handoff note in the authorized workspace and let the Main Agent retrieve it. Do not claim invisible cross-session delivery.

A worker return contains **observed status** (`done`, `partial`, `blocked`, `failed` or `canceled`), actual artifact paths and revision IDs, tests run and results, sources and uncertainty, unresolved questions, possible conflicts/affected scopes, and the proposed next step. A status label without evidence is an unverified report. Keep ordinary one-off research responses short; no mandatory JSON manifest, per-worker folder or elaborate task database.

**Delegation is not endorsement.** On receipt, the Main Agent checks meaningful outputs against the mandate and real files/tests, resolves contradictions, validates applicable project memory, and only then updates canonical status and user-visible conclusions. Parallel outputs can disagree; compare evidence rather than blindly averaging opinions.

## 4. Concurrency, changed requirements and recovery

**Single authority for shared state.** Workers preferably edit distinct scoped outputs. Assign one canonical writer (usually Main Agent) for the project pulse, shared knowledge and any rules that cross scopes. When concurrent shared writes are unavoidable, reconcile actual revisions through the available version-control/file mechanisms; do not overwrite on a last-write-wins assumption.

**Branch/worktree isolation is real.** Claude Code/Codex workers may operate with separate filesystem copies, permissions, tool outputs and chat histories. Validate paths, base revisions, merge routes and visibility before reporting that a worker "saved to AIOS". A local worker note can be unavailable to the Main Agent until explicitly handed back or merged.

**Changing decisions mid-flight:** If new brainstorming challenges an active requirement, record the idea as tentative. Detect whether ongoing workers could waste significant effort or produce unsafe/stale results; ask the user for a material pause/cancel/replan decision when needed. Pause, stop or reassign **only through real supported tools and authorization**. If cancellation cannot be delivered, mark the job/output **possibly stale**, do not integrate it as current, and reconcile on its return. An actual approved decision revision invalidates any older worker assumptions it supersedes.

**Failure and interruption:** Preserve observed job identity, mandate/revision, partial artifacts, safe recovery path, retries already attempted and blockers in the existing project state only when useful. Do not announce auto-recovery unless the host actually provides durable job control. Avoid duplicate expensive work: first check observed output/revision, whether the job is still running and whether continuation is supported. Do not repeat external side effects without explicit idempotency guarantees and permission.

**Stop conditions:** permission uncertainty; a high-impact destructive action; absent canonical input; conflicting revisions; unclear owner; missing host delegation; runaway resource spending; canceled user mandate; unverified claims that would be material to delivery. Continue unrelated, safe work where possible.

## 5. Host adapters and graceful fallback

AIOS's **decision policy and handoff content are host agnostic**; spawning, messaging, lifecycle management and permissions are host-specific.

- **Claude Code:** inspect available Subagents or Agent Teams in the actual runtime; pass scoped task context, check tools/permissions and file visibility. Do not assume team messages, hooks or background execution are enabled. Avoid installing Hooks by default.
- **Codex:** inspect actual multi-agent tools/features, worktrees and accessible task session. Use supported native delegation only. Codex CLI/app, remote and other hosted surfaces may offer different abilities; never invent or hardcode a function name.
- **Other or unsupported host:** execute sequentially in the Main Agent or provide an authorized manual handoff. Keep the same AIOS records. Never report that a worker ran if no actual worker was created.

**Persistent memory ≠ persistent router process.** A new Main Agent can recover prior task/decision state from project files, but cannot assume an old worker process is still alive or send a message to it without a working host interface. Autonomous CI/PR/email triggers, 24/7 monitoring, retries, watchdogs and true background jobs require separately installed, authorized infrastructure. This Skill installs none.

## 6. Low-attention human interface

Default: keep talking naturally. No orchestration jargon or full status tables for ordinary requests. Offer a single sentence only when parallel research is materially beneficial and permission is missing. Do not force users to select Agent counts, execution modes, worktrees, context files, task IDs or configuration files. If a worker needs a consequential decision, present the precise choice once; otherwise return a verified result at the useful milestone. Declined offers remain declined for that task.

Examples:

- "Maybe Swift; maybe Electron; actually scrap that" → normal discussion, maybe one concise candidate, no Worker or committed implementation.
- "Could you compare their memory use from official sources?" → answer directly if cheap; offer bounded parallel read-only research only if significantly advantageous.
- "Research Swift and Tauri in parallel, use existing agents" → check native capability, authority and cost; delegate research if available, otherwise investigate sequentially with honest disclosure.
- "Implement the design we approved across independent modules" → ensure confirmed architecture and boundaries; ask before material new execution costs or external effects, assign independent scopes, verify before merging.
- "I changed the architecture while workers are coding" → keep new idea tentative until confirmed, highlight impacted tasks, use supported pause/replan where authorized, mark stale outputs.
- "Check every PR and fix CI around the clock" → explain that the Skill alone cannot do that; use real supported scheduling/events only with separate approval and accessible infrastructure.

## 7. Optional project policy and migration

A small project should usually have **no orchestration-specific files or config at all**. A multi-workstream project can reuse its existing scope index and checkpoint for worker handoffs. If the user authorizes repeated bounded research delegation, record the scoped, revocable preference where future Main Agents can find it, not in every subtask.

When moving from an older AIOS policy, inspect any actual existing delegation conventions; preserve the user's ownership and checkpoints. Add a brief portable optional-delegation rule to the project entrypoint only if needed for future sessions. Do not reclassify tentative brainstorming notes as approved tasks, create an always-on Router session, or mark the installed version as an applied policy before verifying actual changes. Old worker tasks do not magically become live after upgrade.

## 8. Honest evaluation boundary

Static checks can prove this guidance is packaged and correctly linked; actual orchestration reliability requires **real** runs on each host. Test solo mode, noisy brainstorming, candidate-only research, explicit consent, refusal, unsupported host fallback, worker isolation, conflicting results, new decisions mid-flight, actual verification, canceled tasks, migration and cost/attention overhead. Record the exact host/version, tool availability, actual Worker invocations and artifacts. No "parallel speedup" or "automatic recovery" claim without measured evidence.
