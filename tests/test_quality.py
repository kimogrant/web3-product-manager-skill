"""Quality checks for web3-product-manager-skill."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
MAX_DESCRIPTION_CHARS = 1024
SKILL_LINK_PATTERN = re.compile(r"\]\((references/[^)#]+)\)")
REF_LINK_PATTERN = re.compile(r"\]\(([^)#]+\.md)\)")


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


def resolve_ref_link(base_file: Path, target: str) -> Path | None:
    if target.startswith("http"):
        return None
    if target.startswith("references/"):
        return base_file.parent / target
    if "/" not in target and target.endswith(".md"):
        return base_file.parent / target
    return None


class TestQuality(unittest.TestCase):
    EXPECTED_SKILLS = {
        "web3-product-manager",
        "web3-product-strategy",
        "web3-product-specification",
    }

    def test_all_skills_have_when_not_to_use(self) -> None:
        for name in self.EXPECTED_SKILLS:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("## When NOT to use", text, f"{name} missing When NOT to use")

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
            for rel in SKILL_LINK_PATTERN.findall(text):
                target = skill_dir / rel
                self.assertTrue(target.is_file(), f"broken link in {skill_md}: {rel}")

    def test_orchestrator_has_pipeline_reference(self) -> None:
        path = SKILLS / "web3-product-manager" / "references" / "pipeline-summary.md"
        self.assertTrue(path.is_file())
        skill = (SKILLS / "web3-product-manager" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("pipeline-summary.md", skill)

    def test_specification_reference_links(self) -> None:
        ref_dir = SKILLS / "web3-product-specification" / "references"
        for md in ref_dir.glob("*.md"):
            text = md.read_text(encoding="utf-8")
            for target in REF_LINK_PATTERN.findall(text):
                resolved = resolve_ref_link(md, target)
                if resolved is None:
                    continue
                self.assertTrue(
                    resolved.is_file(),
                    f"broken link in {md}: {target}",
                )

    def test_repo_examples_exist(self) -> None:
        examples = REPO / "examples"
        self.assertTrue((examples / "strategy-memo-sample.md").is_file())
        self.assertTrue((examples / "prd-story-sample.md").is_file())
        memo = (examples / "strategy-memo-sample.md").read_text(encoding="utf-8")
        self.assertIn("## Source index", memo)
        self.assertIn("SRC-1", memo)
        story = (examples / "prd-story-sample.md").read_text(encoding="utf-8")
        self.assertIn("Source: SRC-", story)

    def test_skill_sh_declares_example_copy(self) -> None:
        script = (REPO / "skill.sh").read_text(encoding="utf-8")
        self.assertIn("EXAMPLES_SRC", script)
        self.assertIn("copy_examples", script)

    def test_install_ps1_exists(self) -> None:
        self.assertTrue((REPO / "install.ps1").is_file())

    def test_no_duplicate_example_copies_in_repo(self) -> None:
        """Samples live only under repo examples/, not under skills/*/examples/*.md samples."""
        for skill in self.EXPECTED_SKILLS:
            for name in ("strategy-memo-sample.md", "prd-story-sample.md"):
                path = SKILLS / skill / "examples" / name
                self.assertFalse(path.exists(), f"remove duplicate {path}; use repo examples/")


if __name__ == "__main__":
    unittest.main()
