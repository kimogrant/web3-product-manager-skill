"""Layout smoke tests for web3-product-manager-skill."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"

FRONTMATTER_NAME = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
FRONTMATTER_DESC = re.compile(r"^description:\s*.+", re.MULTILINE | re.DOTALL)


class TestLayout(unittest.TestCase):
    def test_version_file(self) -> None:
        version = (REPO / "VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def test_skill_directories(self) -> None:
        expected = {
            "web3-product-manager",
            "web3-product-strategy",
            "web3-product-specification",
        }
        found = {p.name for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists()}
        self.assertEqual(expected, found)

    def test_skill_frontmatter(self) -> None:
        for skill_dir in SKILLS.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            text = skill_md.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---"), f"{skill_md} missing frontmatter")
            name_match = FRONTMATTER_NAME.search(text)
            self.assertIsNotNone(name_match, f"{skill_md} missing name:")
            self.assertEqual(name_match.group(1), skill_dir.name)
            self.assertIsNotNone(
                FRONTMATTER_DESC.search(text),
                f"{skill_md} missing description:",
            )

    def test_references_exist(self) -> None:
        refs = {
            "web3-product-strategy": [
                "phase-guide.md",
                "strategy-memo-template.md",
                "data-sources.md",
            ],
            "web3-product-manager": [
                "pipeline-summary.md",
            ],
            "web3-product-specification": [
                "gate-guide.md",
                "prd-template.md",
                "tokenomics-checklist.md",
                "compliance-surface.md",
                "defi-product-surface.md",
                "l2-product-surface.md",
                "consumer-product-surface.md",
                "evidence-tiers.md",
                "cross-chain-risks.md",
                "methodology-toolkit.md",
                "prototype-gate.md",
            ],
        }
        for skill, files in refs.items():
            ref_dir = SKILLS / skill / "references"
            for fname in files:
                self.assertTrue(
                    (ref_dir / fname).is_file(),
                    f"missing {ref_dir / fname}",
                )

    def test_skill_sh_exists(self) -> None:
        self.assertTrue((REPO / "skill.sh").is_file())


if __name__ == "__main__":
    unittest.main()
