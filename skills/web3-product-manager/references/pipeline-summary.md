# Pipeline summary (orchestrator)

Load this file at the start of `/web3-product-manager`. It does not replace child skills—it routes them.

---

## Step 1 — Strategy (`web3-product-strategy`)

**You must read:** `.cursor/skills/web3-product-strategy/SKILL.md` (or repo `skills/web3-product-strategy/SKILL.md`).

Then load **one reference at a time** from that skill’s `references/`:

| Phase | Open file |
|-------|-----------|
| 1 | `phase-guide.md` (Phase 1 section only) |
| 2 | `phase-guide.md` (Phase 2) + `data-sources.md` |
| 3 | `phase-guide.md` (Phase 3) |
| 4 | `strategy-memo-template.md` |
| 5 | `phase-guide.md` (Phase 5) — only if user asks post-ship |

**Domain (Phase 2, optional):** from specification skill (sibling folder):

- DeFi → `web3-product-specification/references/defi-product-surface.md`
- L2 → `web3-product-specification/references/l2-product-surface.md`
- Consumer → `web3-product-specification/references/consumer-product-surface.md`

**Stop Step 1 when:** user says memo is `confirmed` / `approved` / `proceed to spec`.

---

## Step 2 — Specification (`web3-product-specification`)

**You must read:** `.cursor/skills/web3-product-specification/SKILL.md`.

Prerequisites: strategy memo + **Source index** (`SRC-1` = memo).

Load gate reference sections from `references/gate-guide.md`:

| Gate | Action |
|------|--------|
| 0 | Ground truth audit |
| 1 | IA & flows |
| 2 | Three-layer stories |
| 2b | `tokenomics-checklist.md` if triggered (before Gate 2 ✅) |
| 3 | `compliance-surface.md` if triggered |
| 4 | Iteration plan |

Output: PRD from `references/prd-template.md`.

**Cross-chain products:** also load `references/cross-chain-risks.md`.

---

## Source IDs (both steps)

| ID | Assign |
|----|--------|
| SRC-1 | User brief / chat |
| SRC-2 | Strategy memo (after Step 1) |
| SRC-3+ | Screenshots, APIs, dashboards, interviews |

Tag claims: `(Source: SRC-n, tier: on-chain|report|first-party|sentiment)`.

---

## If child skill not installed

Tell user to run from repo root:

```bash
./skill.sh install .
# Windows: .\install.ps1 .
```

All three skills must exist side by side under `.cursor/skills/`.
