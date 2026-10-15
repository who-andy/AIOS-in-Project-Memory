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
        self.assertEqual(metadata["name"], "adaptive-project-memory")
        self.assertRegex(metadata["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(metadata["name"]), 64)
        self.assertGreater(len(metadata["description"]), 10)
        self.assertLessEqual(len(metadata["description"]), 1024)
        self.assertLessEqual(len(metadata["compatibility"]), 500)
        self.assertIn('version: "0.3.0"', self.front)
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

    def test_lean_distribution(self):
        for folder in ("references", "assets", "templates"):
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

    def test_documentation_covers_discussion_and_capture(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cn = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("Discuss", readme)
        self.assertIn("capture", readme.lower())
        self.assertIn("持续", cn)
        self.assertIn("讨论", cn)

if __name__ == "__main__":
    unittest.main()
