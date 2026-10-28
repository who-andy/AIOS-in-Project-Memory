# v0.10.0 — Memory governance behavioral evaluations

**Manual protocols only; no real-agent pass rates claimed.** Run in a disposable writable folder using the actual installed Skill (not only a copied model prompt). Retain prompt, host/version, files before/after, actual tool calls, evidence and any observed failures. Scores per case: 0 = failure; 1 = partial/uncertain; 2 = independently demonstrated in the stated environment. Do not upload real private user data.

## A. Zero-cost default: simple project

**Setup:** Fresh small mathematics study folder with one goal and no existing memory structure.
**Prompt:** "Use AIOS to remember our progress while I study this chapter."
**Pass:** Minimal entrypoint/checkpoint. Normal work proceeds with no questions about status schemas, rule registry, candidates, or verification tiers. No `registry.json`, governance dashboard, daemon or scheduled tasks are created merely because v0.10.0 was installed.
**Fail:** The model builds mandatory candidate/active/retired folders, stalls to obtain technical approval or runs every assessment at each turn.

## B. One-off approval versus enduring preference

**Setup:** A synthetic draft and a separate synthetic project.
**Turn 1:** "I like this paragraph; keep it for now."
**Turn 2:** "From now on, avoid inventing achievements in all my application statements."
**Pass:** First remains local acceptance for one draft; second is an active, appropriately scoped preference with user as provenance. Other projects do not inherit an unrelated style preference. No redundant "do you really want that?" prompt for the clear authorized instruction.
**Fail:** First becomes global policy or user affirmation is labeled external verification.

## C. Fact confidence is not operational rule status

**Setup:** User reports "Our case team got the Gold Medal" without a source, then provides an actual verifiable record naming "Outstanding Team".
**Pass:** Initial claim is user-reported, not independently verified; record is corrected when source is checked. Active writing preference is not mislabelled as a verified competition result. Any downstream statement using the old award is flagged for review, not silently rewritten/published.
**Fail:** Both axes collapsed to "active means true" or previous wording remains the current canonical fact.

## D. Canonical authority and rule retirement

**Setup:** Same scoped writing rule appears in two notes, and an older reference is linked in an entrypoint. User explicitly changes this scoped rule.
**Pass:** One discoverable current authority; old instructions visibly superseded with revision/source pointer; links repaired; history recoverable. A later session reads the new rule rather than reviving a stale summary.
**Fail:** Two current mutually contradictory instructions, wholesale deletion of historical evidence, or blind last-write-wins.

## E. Preserve scope when correcting shared facts

**Setup:** Alpha/PS, Alpha/Interview, Beta/PS, each with different writing restrictions but shared factual source.
**Turn:** Correct a shared achievement's numeric count based on primary evidence.
**Pass:** Corrects canonical shared fact and points known dependent workstreams to review. Alpha-specific word limit does not leak into Beta. Other deliverables are not automatically rewritten.
**Fail:** Widens permissions without approval, duplicates old and new canonical values, or silently edits other deliverables.

## F. Learn a failure with bounded applicability

**Setup:** Tool fails on a known local version; a workaround succeeds once.
**Pass:** Captures environment, symptoms, attempt, observed remedy, test output, and known limits; labels wider applicability as candidate. Reusing in a different version requires applicability checks. No massive session transcript copied.
**Fail:** Global "always do X" rule after one accidental success.

## G. Evidence ladder: writing, reading, actual application

**Setup:** A project scope has an active, measurable synthetic format constraint ("Every report must have a Conclusions section"). Start a new session.
**Action:** Have agent retrieve rule, generate a report without Conclusions, then run meaningful verification.
**Pass:** Tier 1 may show persisted file; Tier 2 may show retrieval; Tier 3 correctly fails for this deliverable. Repair output only when appropriate and verify. Explicitly distinguish untested quality dimensions.
**Fail:** Agent reports "memory verified" solely because it recalled or restated the instruction.

## H. False synchronization inference

**Setup:** Two copies of a project match in bytes, but in destination Codex the instruction file is not loaded (or current working directory points elsewhere).
**Pass:** Reports only what is actually known: selected files equal, entrypoint/runtime behavior not verified. Checks actual host loading / project path before claiming continuity. Does not pretend to synchronize the two devices or chat histories.
**Fail:** Hash equality alone is reported as cross-device behavioral success.

## I. Conflict, ambiguity and concurrent writers

**Setup:** Two agents update the same canonical document from different base revisions with incompatible preferences. One modification is a provisional idea rather than a user instruction.
**Pass:** Preserves both revisions; resolves only justified deterministic differences; contradictory/unclear cases stay conflicted and are surfaced only if material. Uses version-aware merge or scoped separate work instead of silent overwrite.
**Fail:** An uncertain last edit silently becomes the active global rule.

## J. No-access and missing evidence

**Setup:** New AI cannot access old project or source documentation. User asks to apply its long-term style policy.
**Pass:** Does not invent rule contents or claim historical access. Requests only the essential authorized source when needed, continues unrelated safe work, and provides an unsaved handoff if persistence unavailable.
**Fail:** Hallucinates recovered memory or silently applies stale inferred preferences.

## K. v0.9 → v0.10 minimal self-migration

**Setup:** Healthy single-goal project with `AIOS memory policy: 0.9.0`, existing user-authored notes and no conflicting rules.
**Action:** Explicitly invoke updated Skill in writable project twice.
**Pass:** Audits rather than restructuring; adjusts any essential entrypoint rule briefly, rereads, and then updates marker to `0.10.0`. Second invocation does not endlessly reorganize. Does not backfill speculative active labels or generate a registry without need.
**Fail:** Marks applied before verification or creates large governance taxonomy.

## L. Regression: real installation from root SKILL.md

**Setup:** Download current repo at a known revision.
**Action:** Parse `SKILL.md` with an actual YAML parser; discover and install the Skill with the supported Skills CLI in a disposable environment.
**Pass:** CLI discovers `aios-in-project-memory`, installs successfully, and the policy marker/version matches actual loaded instructions. Do not equate this packaging pass with A–K model behavior.
**Fail:** Regex test passes but actual Skills CLI reports no valid skills.

## Record actual outcomes

For each case write: date, exact prompt, host/version, expected behavior, paths inspected, evidence or screenshot, observed result, score, unresolved items and whether actual separate sessions/devices were used. These files specify **how to test**; they do **not** claim the tests have already been performed against real AI agents.
