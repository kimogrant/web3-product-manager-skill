# Web3 Product Manager Skills

Agent Skills for **Web3 product management**: strategy decisions, on-chain signal review, tokenomics checkpoints, and shippable PRD-style specifications.

Built for the [Agent Skills](https://agentskills.io) format (`SKILL.md` + on-demand `references/`). Works with **Cursor**, Claude Code, Codex, and other agents that discover skills from `.cursor/skills/` or `~/.cursor/skills/`.

**Version:** [`1.3.0`](VERSION) · [Changelog](CHANGELOG.md) · [Skill catalog](docs/skill-catalog.md)

---

## What you get

| Skill | Question it answers |
|-------|---------------------|
| [`web3-product-manager`](skills/web3-product-manager/SKILL.md) | **Orchestrator** — route full pipeline with enforced order |
| [`web3-product-strategy`](skills/web3-product-strategy/SKILL.md) | Should we build this? Why now? What do we stop doing? |
| [`web3-product-specification`](skills/web3-product-specification/SKILL.md) | How do we specify it for engineering, design, and compliance review? |

**Recommended:** `/web3-product-manager` for greenfield work, or invoke child skills directly for single phases.

```
web3-product-manager
  Step 1: web3-product-strategy  →  confirmed strategy memo (SRC index)
  Step 2: web3-product-specification  →  PRD + gates + domain appendices
```

---

## Repository layout

```text
web3-product-manager-skill/
├── CHANGELOG.md
├── VERSION
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── skill.sh
├── docs/
│   ├── installation.md
│   └── skill-catalog.md
├── skills/
│   ├── web3-product-manager/
│   ├── web3-product-strategy/
│   └── web3-product-specification/
├── examples/
└── tests/
```

---

## Install

```bash
git clone https://github.com/kimogrant/web3-product-manager-skill.git
cd web3-product-manager-skill
chmod +x skill.sh
./skill.sh install /path/to/your/project
```

Windows (PowerShell):

```powershell
.\install.ps1 -Target D:\path\to\your\project
# or: .\install.ps1 -Personal
```

Copies each skill bundle into `TARGET/.cursor/skills/<skill-name>/` including `references/` and `examples/` (from repo `examples/`).

Reload Cursor, then invoke:

- `/web3-product-manager` — full pipeline
- `/web3-product-strategy` — strategy only
- `/web3-product-specification` — PRD only (requires confirmed memo)

See [docs/installation.md](docs/installation.md) for personal install and remote rules.

---

## When to use which skill

| You say… | Start with |
|----------|------------|
| "From idea to PRD", "full PM workflow" | `web3-product-manager` |
| "Should we build X?", go/no-go, market scan | `web3-product-strategy` |
| "Write a PRD", tokenomics review, scope sprint | `web3-product-specification` (memo required) |

Each workflow skill includes a **When NOT to use** section to reduce mistaken auto-invocation.

---

## Design principles

- **On-chain first** — Verifiable chain metrics primary; label report/sentiment tier.
- **Progressive disclosure** — Lean `SKILL.md`; load `references/` per phase/gate only.
- **Human checkpoints** — Memo confirmation before specification; tokenomics/compliance gates explicit.
- **Ground before generate** — No fabricated contracts/events; use `TBD` and `PENDING`.
- **Source traceability** — `SRC-n` tags from inputs through memo and PRD.

### Domain specialist references

| Module | Path |
|--------|------|
| DeFi | `skills/web3-product-specification/references/defi-product-surface.md` |
| L2 / rollup | `skills/web3-product-specification/references/l2-product-surface.md` |
| Consumer | `skills/web3-product-specification/references/consumer-product-surface.md` |

---

## Quality checks

```bash
python -m unittest discover -s tests -v
```

CI runs the same on push (see `.github/workflows/ci.yml`).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE](LICENSE).
