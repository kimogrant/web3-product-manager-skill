"""Quality checks for web3-product-manager-skill."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
MAX_DESCRIPTION_CHARS = 1024
LINK_PATTERN = re.compile(r"\]\((references/[^)#]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip()
    data: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []
    for line in block.splitlines():
        if line and not line.startswith((" ", "  ")) and ":" in line and not line.startswith("-"):
            if key is not None:
                data[key] = "\n".join(buf).strip()
            key, val = line.split(":", 1)
            key = key.strip()
            buf = [val.strip()] if val.strip() else []
        elif key is not None:
            buf.append(line)
    if key is not None:
        data[key] = "\n".join(buf).strip()
    return data


class TestQuality(unittest.TestCase):
    EXPECTED_SKILLS = {
        "web3-product-manager",
        "web3-product-strategy",
        "web3-product-specification",
    }

    def test_all_skills_have_when_not_to_use(self) -> None:
        for name in self.EXPECTED_SKILLS:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(
                "## When NOT to use",
                text,
                f"{name} missing When NOT to use section",
            )

    def test_description_length(self) -> None:
        for skill_dir in SKILLS.iterdir():
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
            desc = meta.get("description", "")
            self.assertTrue(desc, f"{skill_md} empty description")
            self.assertLessEqual(
                len(desc),
                MAX_DESCRIPTION_CHARS,
                f"{skill_md} description {len(desc)} > {MAX_DESCRIPTION_CHARS}",
            )

    def test_skill_md_reference_links(self) -> None:
        for skill_dir in SKILLS.iterdir():
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            text = skill_md.read_text(encoding="utf-8")
            for rel in LINK_PATTERN.findall(text):
                target = skill_dir / rel
                self.assertTrue(
                    target.is_file(),
                    f"broken link in {skill_md}: {rel}",
                )

    def test_repo_examples_exist(self) -> None:
        examples = REPO / "examples"
        self.assertTrue((examples / "strategy-memo-sample.md").is_file())
        self.assertTrue((examples / "prd-story-sample.md").is_file())

    def test_each_skill_has_examples_dir(self) -> None:
        for name in self.EXPECTED_SKILLS:
            ex = SKILLS / name / "examples" / "strategy-memo-sample.md"
            self.assertTrue(ex.is_file(), f"missing bundled examples in {name}")


if __name__ == "__main__":
    unittest.main()
