# Installation

## Requirements

- Cursor (or another agent that loads `SKILL.md` from skill directories)
- Bash for `skill.sh` (Git Bash / WSL on Windows), or manual copy

## Project-scoped install

```bash
./skill.sh install /path/to/your/repo
```

Result (three skills):

```text
your-repo/.cursor/skills/web3-product-manager/SKILL.md
your-repo/.cursor/skills/web3-product-strategy/SKILL.md
your-repo/.cursor/skills/web3-product-specification/SKILL.md
# Each folder includes references/ and examples/
```

Commit `.cursor/skills/` if you want teammates to get the same agent behavior.

## User-scoped install

```bash
./skill.sh install --personal
```

Installs under `~/.cursor/skills/` (Unix-like). Skills apply across projects.

## Verify discovery

1. Reload Cursor after install.
2. In Agent chat, type `/web3-product-manager` (full pipeline) or a child skill name.
3. Confirm the agent loads the skill (it should follow phase checkpoints and ask for missing inputs).

## Remote rule (GitHub URL)

1. Cursor Settings → Rules
2. Project Rules → Add Rule → Remote Rule (GitHub)
3. Paste the repository URL

Use this when you prefer not to vendor skills into the repo.

## Claude Code / Codex

Copy the same folder structure to the agent’s skills path, for example:

| Agent | Typical path |
|-------|----------------|
| Claude Code | `~/.claude/skills/<skill-name>/` |
| Codex | `~/.codex/skills/<skill-name>/` |

Always copy `references/` with `SKILL.md`.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Agent ignores skill | Ensure folder name matches `name:` in frontmatter |
| Missing templates | Re-run install; do not copy only `SKILL.md` |
| Skill too verbose | Ask agent to load only the relevant `references/*.md` for the current phase |
