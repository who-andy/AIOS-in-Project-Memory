"""Deterministic package tests; not an evaluation of model behavior."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = SKILL.read_text(encoding="utf-8")
        cls.front, cls.body = cls.content.split("\n---\n", 1)

    def test_valid_agent_skills_frontmatter(self):
        self.assertTrue(self.front.startswith("---\n"))
        metadata = dict(re.findall(r"(?m)^(name|description|license|compatibility):\s*(.*)$", self.front))
        self.assertEqual(metadata["name"], "aios-in-project-memory")
        self.assertRegex(metadata["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(metadata["name"]), 64)
        self.assertGreater(len(metadata["description"]), 10)
        self.assertLessEqual(len(metadata["description"]), 1024)
        self.assertLessEqual(len(metadata["compatibility"]), 500)
        self.assertIn('version: "0.9.0"', self.front)
        self.assertLessEqual(len(self.body.splitlines()), 500)

    def test_required_runtime_contract(self):
        required = [
            "capture has not been requested or enabled",
            "provisional", "officially", "host loads automatically",
            "AGENTS.md", "CLAUDE.md",
            "capture meaningful new information promptly",
            "check that writes succeeded", "during work",
            "save important details", "resume", "reorganize",
            "privacy", "verified", "user-reported", "tentative",
            "unknown/conflicted", "existing instruction files",
            "public", "without the original conversation",
        ]
        normalized = self.content.lower()
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), normalized)

    def test_failure_truthfulness_contract(self):
        for phrase in [
            "never claim files were saved before checking",
            "host cannot automatically load", "unsaved handoff",
            "the host made it inaccessible", "do not silently start recording",
            "do not silently discard evidence",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_retrospective_onboarding_contract(self):
        required = [
            "retroactive onboarding",
            "detect this situation proactively",
            "actually accessible",
            "reconstruct progressively",
            "source-linked project timeline",
            "calibrate confidence and coverage",
            "partially inspected",
            "bootstrap from the real present",
            "continue backfill safely",
            "do not repeatedly re-import",
            "do not upload past conversations",
            "continue from the user's actual present position",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_adaptive_scale_single_goal_guardrail(self):
        required = [
            "complexity on demand",
            "a single goal",
            "never create a workstream",
            "just because a new chat starts",
            "do not plan hypothetical future tasks",
            "when uncertain, save valuable information without adding structure",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_scoped_shared_memory_and_contamination_rules(self):
        required = [
            "shared project knowledge",
            "workstream-specific state",
            "provisional or disputed material",
            "one session may affect several workstreams",
            "store once",
            "fact, interpretation, and drafted wording distinct",
            "propagate changes without cross-task contamination",
            "do not silently edit or finalize unrelated deliverables",
            "scope-aware resume",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_contraction_and_non_destructive_migration(self):
        required = [
            "contract safely as needs decrease",
            "explicitly removed",
            "mere silence",
            "never infer permission to delete historical evidence",
            "reorganize constantly",
            "snapshot originals",
            "verify read-back",
            "blind last-writer-wins",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_adaptive_scale_evaluation_exists(self):
        scenarios = (ROOT / "evals" / "adaptive-scale.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "minimal single-goal project",
            "independent deliverables",
            "cross-scope correction",
            "shrink after a goal is finished",
            "noisy scope changes",
            "concurrency and read-only failure",
            "cross-ai checkpoint recovery",
            "partial old history",
        ]:
            with self.subTest(scenario=phrase):
                self.assertIn(phrase, scenarios)
        self.assertIn("disk", scenarios)

    def test_mandatory_target_directory_isolation(self):
        required = [
            "mandatory separation when targets conflict",
            "separate discoverable directories",
            "two or more durable targets",
            "project root",
            "one-target project",
            "requirements, drafts, decisions",
            "not equivalent to session, filename, or artifact type",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_target_scope_gate_prevents_rule_leakage(self):
        required = [
            "determine the active target before retrieval and writes",
            "verify its recorded",
            "scope and provenance",
            "do not automatically import sibling or other target instructions",
            "ask one brief disambiguating question",
            "restrict cross-target reuse",
            "word limits",
            "unassigned or needing verification",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_flat_root_repair_and_regression_coverage(self):
        required = [
            "detect root-level sprawl and repair existing projects",
            "inventory filenames",
            "recoverable snapshot",
            "confidently classified material",
            "review area",
            "flag the affected draft for review",
            "target-aware handoff and regression check",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())
        manual = (ROOT / "evals" / "target-isolation.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "single target remains small",
            "two similar targets require physical separation",
            "fresh session targeting and ambiguity",
            "reuse facts without importing constraints",
            "recover a root folder",
            "generalize beyond schools",
            "alpha", "beta", "500-word", "700-word",
        ]:
            with self.subTest(evaluation=phrase):
                self.assertIn(phrase, manual)

    def test_recursive_scope_tree_with_adaptive_depth(self):
        required = [
            "recursive, meaningful nesting",
            "nesting may continue",
            "no fixed two-level limit",
            "no mandatory school-first or deliverable-first",
            "a one-target project",
            "explicit cross-links",
            "scope path",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_relative_shared_memory_and_on_demand_discovery(self):
        required = [
            "shared is relative to scope",
            "least common appropriate ancestor",
            "discover missing information before declaring it unavailable",
            "parent, sibling and related scope",
            "candidate source",
            "promote or link reusable discoveries incrementally",
            "canonical record",
            "original scope",
            "read-only",
            "user's authorized sharing boundary",
            "never silently convert a school-specific word limit",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_hierarchical_scope_behavior_protocol_exists(self):
        doc = (ROOT / "evals" / "hierarchical-scopes.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "start small, then nest progressively",
            "statement and interview under one institution",
            "on-demand promotion from a nonshared note",
            "shared is relative to the consumer group",
            "candidate is not automatically a fact",
            "authorization and sensitive boundaries",
            "growing and refactoring an existing tree",
            "cross-cutting workstream",
        ]:
            with self.subTest(scenario=phrase):
                self.assertIn(phrase, doc)
        self.assertIn("65", doc)
        self.assertIn("500 words", doc)
        self.assertIn("700", doc)

    def test_version_aware_self_migration_contract(self):
        required = [
            "version-aware self-migration",
            "trigger, not a background daemon",
            "minimal version handshake",
            "aios memory policy: 0.9.0",
            "bootstrap realities",
            "inspect, classify and plan before writes",
            "auto-apply reversible changes only",
            "require user approval for risky operations",
            "verify, commit and remain idempotent",
            "do not advance the policy marker",
            "make this capability survive future sessions",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_migration_version_claims_are_honest(self):
        required = [
            "newer actually loaded",
            "not installation or remote updates",
            "marker is absent",
            "unknown",
            "cannot force a legacy entrypoint",
            "new skill at least once",
            "without blocking work",
            "continue with the existing self-contained project instructions",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())

    def test_migration_behavior_scenarios_are_documented(self):
        doc = (ROOT / "evals" / "auto-migration.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "upgrade old flat-root project",
            "idempotent second run",
            "safe incremental task growth without version change",
            "first updated launch from a legacy entrypoint",
            "no new skill installed or inaccessible package",
            "risky deletion and permissions",
            "failed write, broken link and rollback",
            "healthy single-goal project, newer skill",
        ]:
            with self.subTest(scenario=phrase):
                self.assertIn(phrase, doc)
        self.assertIn("without invoking the new skill", doc)

    def test_project_coordination_default_is_lightweight(self):
        expected = [
            "lightweight project coordination and optional host capabilities",
            "keep normal chatting as the sole required user interface",
            "project-state pulse for real multi-task work",
            "derived, source-linked view",
            "without a dedicated master session",
            "progressive disclosure",
            "only when",
        ]
        for phrase in expected:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())
        self.assertIn("references/project-coordination.md", self.content)
        doc = (ROOT / "references" / "project-coordination.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "project pulse", "cross-session change notices",
            "one writer", "worktrees", "source evidence",
            "verified", "stale", "tiny projects",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, doc)

    def test_host_adapters_are_optional_and_host_checked(self):
        self.assertIn("references/host-adapters.md", self.content)
        required = [
            "optional host-aware enhancements; default off",
            "do not install hooks",
            "actual",
            "permissions",
            "not assumed to share the same local memory files",
            "skill description alone does not create a runnable scheduler",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content.lower())
        doc = (ROOT / "references" / "host-adapters.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "claude code", "codex", "claude.md", "agents.md",
            "sessionstart", "precompact", "/loop",
            "cloud", "desktop", "worktree", "user-language automation pathway",
            "no default hooks", "no phantom automation",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, doc)

    def test_coordinator_eval_exists(self):
        doc = (ROOT / "evals" / "coordination-hosts.md").read_text(encoding="utf-8").lower()
        for phrase in [
            "single-goal", "two independent", "shared change",
            "stale", "concurrent", "claude", "codex", "scheduled",
            "remote", "legacy", "zero",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, doc)

    def test_lean_distribution(self):
        for folder in ("assets", "templates"):
            self.assertFalse((ROOT / folder).exists())
        for file in ("README.md", "README.zh-CN.md", "LICENSE", "evals/README.md"):
            self.assertTrue((ROOT / file).exists())

    def test_local_markdown_links_resolve(self):
        for doc in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                path = target.split("#", 1)[0]
                with self.subTest(doc=str(doc.relative_to(ROOT)), target=target):
                    self.assertTrue((doc.parent / path).exists())

    def test_no_private_samples_or_runtime_secrets(self):
        for p in ROOT.rglob("*"):
            forbidden = {".env", "node_modules", "__pycache__"} if p.is_file() else {".env", "node_modules"}
            self.assertNotIn(p.name, forbidden)

    def test_public_skill_name_matches_repository(self):
        import re
        name = re.search(r"(?m)^name: ([a-z0-9-]+)$", self.front)
        self.assertIsNotNone(name)
        self.assertEqual(name.group(1), "aios-in-project-memory")
        self.assertNotIn("adaptive-project-memory", self.content)

    def test_local_project_memory_is_primary_goal(self):
        self.assertIn("local project folder", self.content)
        self.assertIn("new chat or a different AI", self.content)
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("local project", english.lower())
        self.assertIn("local project folder", english.lower())
        self.assertIn("本地项目目录", chinese)
        self.assertIn("更换 AI", chinese)

    def test_readme_language_switch_and_cli_install(self):
        command = "npx skills add who-andy/AIOS-in-Project-Memory"
        language_switch = "[English](README.md) | [简体中文](README.zh-CN.md)"
        for filename in ("README.md", "README.zh-CN.md"):
            with self.subTest(filename=filename):
                content = (ROOT / filename).read_text(encoding="utf-8")
                self.assertTrue(content.startswith(language_switch))
                self.assertIn(command, content)
                self.assertIn(command + " -g", content)
                self.assertIn(command + " --list", content)

    def test_documentation_covers_discussion_and_capture(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cn = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("Discuss", readme)
        self.assertIn("capture", readme.lower())
        self.assertIn("持续", cn)
        self.assertIn("讨论", cn)

if __name__ == "__main__":
    unittest.main()
