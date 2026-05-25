# Web3 Product Manager Skills

Agent Skills for **Web3 product management**: strategy decisions, on-chain signal review, tokenomics checkpoints, and shippable PRD-style specifications.

Built for the [Agent Skills](https://agentskills.io) format (`SKILL.md` + on-demand `references/`). Works with **Cursor**, Claude Code, Codex, and other agents that discover skills from `.cursor/skills/` or `~/.cursor/skills/`.

**Version:** see [`VERSION`](VERSION)

---

## What you get

| Skill | Question it answers |
|-------|---------------------|
| [`web3-product-strategy`](skills/web3-product-strategy/SKILL.md) | Should we build this? Why now? What do we stop doing? |
| [`web3-product-specification`](skills/web3-product-specification/SKILL.md) | How do we specify it for engineering, design, and compliance review? |

Run **strategy first**, then **specification** once the strategy memo is confirmed.

```
web3-product-strategy  →  confirmed strategy memo
        ↓
web3-product-specification  →  PRD + tokenomics / compliance gates + iteration plan
```

---

## Repository layout

```text
web3-product-manager-skill/
├── VERSION
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── skill.sh
├── docs/
│   └── installation.md
├── skills/
│   ├── web3-product-strategy/
│   │   ├── SKILL.md
│   │   └── references/
│   └── web3-product-specification/
│       ├── SKILL.md
│       └── references/
├── examples/
└── tests/
```

---

## Install

### Script (recommended)

Requires Bash (Git Bash, WSL, macOS, or Linux):

```bash
git clone https://github.com/YOUR_ORG/web3-product-manager-skill.git
cd web3-product-manager-skill
chmod +x skill.sh
./skill.sh list
./skill.sh install /path/to/your/project
```

Copies each skill bundle into `TARGET/.cursor/skills/<skill-name>/` (includes `references/`).

Reload the editor, then invoke by name, for example:

- `/web3-product-strategy`
- `/web3-product-specification`

### Manual

Copy **entire** skill folders (not only `SKILL.md`):

```text
your-project/.cursor/skills/web3-product-strategy/
your-project/.cursor/skills/web3-product-specification/
```

### Personal (all projects)

```bash
./skill.sh install --personal
```

Installs to `~/.cursor/skills/` on Unix-like systems. On Windows, use Git Bash or WSL, or copy folders manually to `%USERPROFILE%\.cursor\skills\`.

### Cursor remote rule

Cursor Settings → Rules → Add Rule → Remote Rule (GitHub) → paste this repository URL.

---

## When to use which skill

| You say… | Start with |
|----------|------------|
| "Should we build X?", "go/no-go", "market sizing", "competitive scan" | `web3-product-strategy` |
| "Write a PRD", "spec this feature", "tokenomics review", "scope the sprint" | `web3-product-specification` |
| Full greenfield feature | Strategy (Express or Full) → Specification |

---

## Design principles

- **On-chain first** — Treat verifiable chain metrics as primary evidence; label lagged reports and sentiment separately.
- **Progressive disclosure** — Lean `SKILL.md`; load `references/` only for the active phase or gate.
- **Human checkpoints** — No silent skip of strategy confirmation or compliance / tokenomics gates.
- **Ground before generate** — No fabricated contract names, event signatures, or addresses in specs.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE](LICENSE).
