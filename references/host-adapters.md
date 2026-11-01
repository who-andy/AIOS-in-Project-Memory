# Optional host-aware enhancements (Claude Code and Codex)

**Read only** when the user explicitly requests scheduling/monitoring, a host-specific persistence safeguard, multi-agent delegation, or a genuine independent-work opportunity warrants a one-time delegation offer, or when the current workspace needs such an integration. AIOS's core memory remains usable without these features. At runtime, inspect the actual host, version, feature flags, permissions, tools and accessible project path; public documentation does not prove the current installation exposes a feature. Never fabricate a tool command or claim to have registered a task/hook until the host confirms it.

## Capability matrix: understand surfaces, not just brand names

| Capability | Claude Code | Codex | Default AIOS behavior |
| --- | --- | --- | --- |
| Portable local project memory | Host-readable `CLAUDE.md` plus scoped notes | Host-readable `AGENTS.md` plus scoped notes | Create/adapt the supported entrypoint, verify later session recovery |
| Event-driven safeguards | Supported lifecycle Hooks, e.g. `SessionStart`, `PreCompact`, `Stop` where available | Host-dependent lifecycle hooks/plugin support; check the actual surface | Prompt-first saving; no hooks installed by default |
| Delegation | Subagents / agent teams / background agents, depending on host/version | Multi-agent where enabled; parallel sessions and worktrees in relevant surfaces | A single Agent works by default; worker handoffs cite source and revision |
| Repeated work | Claude Code /loop is session-scoped; Desktop or cloud scheduled tasks are separate | Codex app Automations or compatible Agents API scheduling, if provided | No recurring schedule until explicitly requested and authorized |

Official reference pages (recheck before configuration):
- Claude Code Skills: https://code.claude.com/docs/en/skills
- Claude Code Hooks: https://code.claude.com/docs/en/hooks
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code scheduling choices: https://code.claude.com/docs/en/scheduled-tasks
- Codex app and long-term workflow: https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- Codex managed Agents API scheduled automations: https://developers.openai.com/api/docs/guides/agents-api/sessions/automations
- Multi-agent in the Agents API: https://developers.openai.com/api/docs/guides/agents-api/multi-agent

## Adaptive delegation contract across hosts

When optional [adaptive orchestration](adaptive-orchestration.md) becomes relevant, **separate what AIOS decides from what the host can execute**. Detect the real native delegation affordance, message-return mechanism, workspace/revision visibility, authorization model and cost boundary before choosing native Worker execution. A host name or feature announcement is never evidence that the current session has those tools.

| Decision | Portable AIOS policy | Host-specific responsibility |
| --- | --- | --- |
| Should work be split? | Solo by default; offer only for meaningful independent work | Tell AIOS whether native delegation is actually available |
| Can it run? | Check explicit scoped current/prior consent, budget and safety | Enforce real tool/host permissions and launch tasks |
| What must Worker know? | Goal, current approved scope, inputs/revision, read/write bounds, expected evidence, stopping conditions | Translate to native task or subagent options |
| Where do results go? | Main Agent verifies, then updates canonical AIOS memory | Deliver the report through a real channel, or expose a file the Main Agent can read |
| What if unavailable? | Continue sequentially, no invented Worker status | Return an unsupported/blocked result |

For Claude Code, use supported Subagent/Agent Team features only when exposed in this particular runtime. For Codex, use its currently exposed multi-agent and worktree facilities; do not assume a particular CLI command or remote API is available. Generic hosts can implement the same task contract with sequential work. Never silently install a plugin or runtime to make delegation possible.

**Consent distinguishes exploration from execution.** Read-only research on a candidate may be scoped and pre-authorized; changing code, installing dependencies, pushing a branch, sending messages or triggering high-cost work requires the actual user's and host's applicable permission. If the user declines an offer, record that for the current task and stop suggesting it until materially different work warrants it.

**No real event source, no autonomous recovery.** A session-local subagent does not become a 24/7 Router. CI comments, pull requests, email triggers, unattended retries and watchdogs require separately connected infrastructure and permission. AIOS can persist handoffs and resumable status without claiming that an interrupted Worker continues in the background.

## Runtime selection

1. **Detect**, do not assume: identify whether the current tool is Claude Code CLI, Claude Desktop, Codex CLI/app, a managed API harness, or a generic file-capable Agent. Different editions of the same brand may behave differently.
2. **Check affordances** through real supported tools, host documentation available locally, user-visible settings, or explicit user description. Never run unrecognized native commands hoping they exist.
3. **Choose least infrastructure**: current Agent + self-contained memory entrypoint is sufficient for ordinary study, writing and small code projects. Do not ask users to choose adapter names or file types.
4. **Constrain access**: if an automation or delegated Agent cannot read the canonical local project folder, explicitly identify the gap. A fresh cloud clone, remote sandbox or separate Git worktree is not automatically a shared writable local folder.
5. **Configure only when requested or clearly necessary and authorized**. Hook installation, user/global configuration edits, schedules, permissions changes, extra model usage and external effects require appropriate user intent/approval. Validate success; keep optional enhancements removable and avoid breaking existing settings.
6. **Fallback**: if unavailable, record a manual/on-session alternative in existing project instructions and continue work. No silent pseudo-automation.

## Claude-specific guidance

- The main project entrypoint is generally `CLAUDE.md`, but inspect existing project rules and host behavior; don't overwrite user instructions.
- Claude Code supports Skills and lifecycle Hooks, including events such as `SessionStart` and `PreCompact`. An optional hook may **suggest** memory refresh or confirm a checkpoint was attempted; it must not promise complete capture or mutate arbitrary files without safe commands and permissions. Hooks have installation and trust consequences. No default hooks.
- Claude Code subagents have separate contexts and permissions; do not assume they share the main Agent's entire chat state. Pass task scope, file locations, required outputs, and expected handoff evidence.
- Scheduling modes differ: `/loop` within a running session needs the session running; Claude Desktop scheduled tasks can have local file access when configured; cloud scheduled tasks may use remote project clones or connectors and cannot simply inspect arbitrary local folders. Pick an option only after identifying what it can actually access. No automatic 30-minute polling.

## Codex-specific guidance

- Prefer existing `AGENTS.md` and project-scoped navigation; adapt non-destructively.
- Some Codex surfaces offer Automations, other surfaces expose hosted session scheduling tools, and not all tools have the same capabilities. Do not claim that every Codex installation supports the same scheduling UI or lifecycle hook names.
- In multi-Agent mode, workers may have separate contexts or worktrees. Verify access to the same authoritative memory before relying on a common checkpoint. Have workers return scoped evidence; coordinate commit/merge and avoid simultaneous blind rewrites of the project index.
- If the host exposes a legitimate automation creation action, collect only essential cadence, target/project and approvals; use that action and trust its result. Merely adding scheduling instructions to `SKILL.md` does **not** create a runnable task.

## User-language automation pathway

A user may say “每天帮我检查项目进度” / “check this project every day.” Translate that request to a short plan:

- Clarify only **missing** schedule/permission/access details that materially affect execution; infer no secret or destructive authority.
- Define what to inspect (e.g., tests, PRs, critical shared facts), **where** the durable memory lives and what counts as a meaningful change.
- Prefer reporting on meaningful changes; avoid repeated “nothing happened” noise unless user requested a regular report.
- Use a supported host scheduler only if actually available and authorized. Don't attempt background work by leaving a prompt in a file.
- Every scheduled run must read the real project state, update it cautiously, avoid duplicate notices, and never claim a completed review without actual tool output.
- Users may change, pause or stop their schedule through the host; don't hide the schedule or create additional ones without consent.

## Optional Hooks: value and limits

Hooks can make recovery checkpoints more likely but never replace the in-conversation **persist → verify** loop. A stop event may never fire on a crash; a start event can only read saved files; a cloud run may operate on a different file snapshot. If the user opts in, choose an appropriate supported event and narrowly scoped action, test on a disposable project, avoid recursion/expensive repeated reprocessing, and document exactly how to disable the hook. Avoid installing privileged scripts from unknown sources.

## Safe acceptance tests

- No host or scheduler: memory works on a single Agent with no extra configuration.
- Claude Code CLI with project files: correct `CLAUDE.md` entrypoint, no unrequested Hooks.
- Codex with project files: correct `AGENTS.md` entrypoint, no phantom automation.
- Requested recurring report: run confirmed in supported host and can access files; no claim if unsupported.
- Remote vs local mismatch: give an honest limitation and safe alternative.
- Two independent workers: no silent shared-file overwrite, and next session sees verified merged status.
- No exposed delegation tool: Main Agent performs the task sequentially, and reports no Worker was launched.
- Brainstorming with unresolved requirements: no implementation Worker is launched on speculative ideas.
- Scoped research permission: an authorized read-only investigation is possible; deployment remains blocked without separate approval.
- New architectural decision while Worker is active: use available stop/replan tools, or flag its output as stale and verify before integration.
