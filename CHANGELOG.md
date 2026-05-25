# Changelog

## [1.3.0] — 2026-05-25

### Added

- Orchestrator `references/pipeline-summary.md` with explicit child-skill read paths
- `evidence-tiers.md` and `cross-chain-risks.md` (specification references)
- GitHub Actions CI (`.github/workflows/ci.yml`)
- `.github/llms.txt` for agent discovery
- Windows `install.ps1`
- `metadata.version` on all three skills

### Changed

- Examples canonical in repo `examples/` only; enriched with Source index and SRC tags
- `skill.sh` / `install.ps1` copy examples into each installed skill
- L2 module links to self-contained `evidence-tiers.md` (no fragile cross-skill path)
- Phase guide uses `.cursor/skills/...` paths for domain modules

## [1.2.0] — 2026-05-25

### Added

- `web3-product-manager` orchestrator skill (full pipeline routing)
- DeFi / L2 / Consumer domain reference modules (1.1.0)
- Source traceability (`SRC-n`) across strategy and specification
- `docs/skill-catalog.md`, expanded tests (`test_quality.py`)
- `When NOT to use` sections on all skills

### Changed

- Gate flow narrative aligned: Gate 2 completes requirements, then Gate 2b tokenomics before exiting Gate 2; Gate 3 compliance; Gate 4 iteration
- `skill.sh` copies repo `examples/` into every installed skill bundle
- README clone URL points to published repository

## [1.1.0] — 2026-05-25

- Domain specialist references: defi, l2, consumer product surfaces

## [1.0.0] — 2026-05-25

- Initial `web3-product-strategy` and `web3-product-specification` skills
