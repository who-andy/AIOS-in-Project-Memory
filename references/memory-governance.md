# Memory governance: feedback, authority, correction and real reuse

**Read this reference on demand**, not for every routine message. Use it when feedback may become a reusable rule; an authoritative statement is corrected, contradicted or superseded; several sessions share facts; a reproducible failure could prevent repeated work; or a high-value cross-session / cross-device reuse needs verification. Ordinary one-goal projects should remain minimal.

This reference adds **decision rules**, not mandatory folders, schemas, registry files, automated scripts, approval dashboards, or a separate memory manager. Normal user conversation remains the interface. Apply the lightest useful safeguard inside files that already exist. Follow the current user request, host instructions, actual access boundary and safety requirements; memory is evidence and project guidance, never a way to override higher-priority instructions.

## 1. Separate epistemic confidence from operational status

Do not use one label to mean both "true" and "currently applicable".

**Epistemic/source axis** (what supports a claim):
- `verified`: checked against a relevant primary document, real artifact, test or explicit authoritative evidence within its scope, with a traceable pointer and date/revision where needed.
- `user-reported`: faithfully attributed personal facts or preferences from the user. This does not assert independent external confirmation.
- `tentative`: proposal, draft inference, recalled but uncertain material, or untested workaround.
- `unknown/conflicted`: insufficient, expired or contradictory evidence; preserve what is unresolved.

**Operational/decision axis** (whether to follow a rule or reuse a method):
- `candidate`: observation, suggestion, speculative method or unclear-scope feedback. May be retained, but **not** made a persistent instruction or current universal method.
- `active`: an explicitly confirmed applicable preference/decision or suitably accepted, tested rule for a **defined scope and condition**. Active means "use in this workflow", **not** "externally verified fact".
- `superseded/retired`: no longer current; keep the reason, replacement pointer and recoverable history. Do not allow old entrypoints, drafts or summaries to silently reactivate it.

Not all memory items are "rules". A dated project status can be current but user-reported; a verified historical result may remain true even though its corresponding process is retired. No mandatory status field in every note. Use the smallest labels needed for consequential ambiguity.

## 2. Turn feedback into reusable guidance without overgeneralizing

1. **Hear the scope and intent**: one-time exception, current deliverable acceptance, target-specific preference, project-wide repeated practice, or a fact correction. Exact expressions like "for this one" and "from now on for all X" have different implications.
2. **Check support**: a user's statement supports *their preference*; a claimed external award, benchmark, rule, environment fix or performance result may need source validation for externally verified status.
3. **Choose applicability**: record at the narrowest scope justified by the evidence and authorization; use a link rather than copying into all siblings.
4. **Apply proportionately**: a clear, authorized, non-risky user instruction can take effect without another approval prompt. Promote uncertain generalizations or materially consequential practices only after appropriate user confirmation or real evidence. Do not auto-promote a pattern solely because a model repeated it.
5. **Capture only when valuable**: no notes for trivial tone tweaks or every transient reaction; only durable, consequential preferences, corrections, decisions, reusable methods, mistakes and evidence matter.
6. **Follow precedence**: more recent explicit user corrections within the same applicable scope normally replace older preferences, subject to higher-priority policy and unresolved contradictions. A new school-specific preference does not supersede a different school's valid rule.

Examples:
- "I like this paragraph; keep it for now." → local accepted *draft version*, **not** global writing policy.
- "For all my application statements, avoid inventing achievements." → active scoped writing rule attributable to user, not a claim of external verification.
- "This release passed tests." → status is **unverified** until actual test evidence is inspected; source and revision matter.
- "One environment variable fixed this error once." → local dated observation; wider applicability stays candidate until reproduced or adequately supported.

## 3. One canonical current authority, recoverable history

Within a meaningful **scope and rule family**, keep at most one **unambiguously current authoritative instruction** for the same issue. Multiple distinct compatible rules can coexist. A global rule and local exception can coexist if precedence and applicability are explicit. Do not impose an inventory or fixed `registry.json` on a small project.

When evidence changes:
1. Locate the canonical current source and any known aliases, references, inherited rules and affected targets. Do not rewrite unrelated siblings.
2. Compare exact old and new claims/constraints, source authority, evidence, date/revision, scope and possible concurrency.
3. Update the canonical source **once**, preserve a recoverable previous revision or concise replacement history, and mark old guidance superseded if needed.
4. Repair navigation/links and add **needs review** pointers to impacted downstream scopes. Other deliverables are not silently edited or published; ask when consequential.
5. Reread the changed content, links and representative affected paths; record what was verified and what still needs application testing.

When two purported authorities conflict and neither clearly supersedes the other, retain both as `unknown/conflicted` rather than choosing the newest file timestamp. Source priority and human permission must be evaluated, not guessed. In concurrent worktrees or Agents, reconcile base revision/diffs or serialize writes instead of last-writer-wins.

A corrected fact is not automatically a new writing rule. Maintain distinct canonical sources for verified facts, project-local draft decisions and preferences as appropriate.

## 4. Capture failures as conditional knowledge

For recurring or expensive failures, save only enough to prevent relearning:
- **Trigger/environment**: version, target, input assumptions and observable symptoms.
- **What was tried**: failed approach and decisive evidence.
- **Working remedy**: steps actually tested, result and evidence pointer.
- **Limits/expiry**: where it might not apply, outstanding hypotheses, and when to recheck.
- **Status**: candidate if unconfirmed, narrowly active if reproducibly validated for that environment.

A successful command or anecdote in one environment is not a universally verified fix. Keep original failures and their provenance retrievable, avoid excessive play-by-play transcripts, and revalidate if software or constraints changed.

## 5. Three-tier verification: evidence of success must match the claim

**Tier 1 — Persistence** (routine, cheap): read back or validate what was written; ensure path, bytes or meaningful content, links, revision and scope still make sense. Report "saved and readable" **only** after this.

**Tier 2 — Retrieval** (on new session, significant correction, migration, host switch): check that the actual Agent can locate and read the correct *current* source and governing scope; look for obsolete competing instructions. Report "retrieved in this session" **only** if observed. Entrypoint existence or hash equality alone does not prove loading.

**Tier 3 — Application** (on relevant deliverable or high-impact change): test whether the real output used the applicable rule correctly — e.g. source citations in a draft, explicit length constraint, passing software tests or accurate facts. Check artifacts or user-accepted output, not model self-assertion. Report "applied and validated for this specific deliverable" **only** for observed tests. If the rule is subjective or cannot be checked safely, describe that limitation; do not claim semantic correctness from structural checks.

**Cost gating:** Tier 1 is normal. Tiers 2–3 are triggered by actual work where they matter, not an automatic repeated full-project audit. Verify only impacted paths or the current output; don't waste tokens or create a test deliverable just to certify an irrelevant preference. Failures are useful evidence, not permission for silent high-risk retries.

## 6. Cross-device and cross-host are distinct claims

Distinguish all of the following if a user requests cross-device continuity:
- The selected files **arrived** in the target workspace (path / hash / revision checks).
- The **right entrypoint** exists and is discoverable by the actual host.
- The current Agent **read** the relevant current memory, rather than an outdated cached copy.
- The environment has the necessary tools, versions, permissions, paths and dependencies.
- The **real task output** follows the rule in the target environment.

Git sync, matching hashes, shared chat titles, same-looking workspace labels, cloud access or a successful connection **alone** proves none of the later stages. Do not claim that running a local comparison tool syncs files, moves chat histories or harmonizes device state. Never copy entire host config folders, session databases, credentials or private directories to achieve "continuity". Offer or use existing authorized file sync only when explicitly needed and supported; on a single machine, no sync machinery.

## 7. Safe adoption and legacy migration

This is **policy evolution**, not an excuse for restructuring older project files:
- On a legitimately loaded updated Skill, inspect actual old records and permissions. For a healthy simple project, keep its layout.
- Preserve existing user instructions, unverified drafts, source links, original bytes and dissenting history. Do not mass-convert old notes into `active` facts merely because the policy version advanced.
- If a clear duplicate/current authority conflict exists, correct only the justified minimal part with a recoverable snapshot, then verify; ask only for materially ambiguous or irreversible changes.
- A project marker reports **applied and verified project instructions**, not that an Agent tested every future outcome.
- Keep the root entrypoint minimal: a sentence requiring separation of candidate vs accepted guidance, canonical authority with provenance, and proportionate verification. Load this detailed file only when the task warrants it.

## 8. Behavioral acceptance examples

- Ambiguous praise stays local; explicit reusable preference becomes active at the right scope.
- A user-reported award is not asserted as externally verified without a source.
- Updated award data supersedes the old value, but another school's requirements remain intact.
- A newly initialized simple study project gets no mandatory governance file/registry.
- A missing entrypoint is identified; a new session that cannot read memory does not claim continuity.
- Different worktrees don't silently share or overwrite the same memory.
- A correct rule loaded into a session but violated by the actual deliverable is an **application failure**, not "memory verified".
- Sync comparison of two file copies is not reported as device or cross-host behavioral verification.

**Adapt, do not transplant:** the candidate/active lifecycle and multi-stage evidence checks are useful design ideas from Codex Continuity, but this is an original, lightweight AIOS policy. Do not copy that repository's fixed templates or impose manual user workflows.
