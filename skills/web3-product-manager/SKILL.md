---
name: web3-product-manager
description: >
  Orchestrates the full Web3 product workflow from strategy through specification.
  Routes to web3-product-strategy then web3-product-specification in order with
  mandatory human checkpoints. Use when starting a greenfield feature end-to-end,
  running go/no-go through PRD, or when the user asks for the full Web3 PM pipeline.
  Triggers include full product workflow, end to end PM, from idea to PRD,
  web3 product manager, web3-product-strategy, web3-product-specification,
  strategy then spec. Do not use for single-phase tasks that should invoke a child
  skill directly.
metadata:
  version: "1.3.0"
  package: web3-product-manager-skill
---

# Web3 Product Manager (Orchestrator)

## Purpose

Single entry point for **strategy → confirmed memo → specification → engineering-ready PRD**.

Child skills hold the detailed playbooks; this skill **routes, enforces order, and tracks state**.

**Start here:** [references/pipeline-summary.md](references/pipeline-summary.md) — then **read each child `SKILL.md` on disk** (paths in pipeline summary). Do not simulate child skills from memory.

---

## When NOT to use

- User only wants a **PRD** and already has an approved strategy memo → `/web3-product-specification`
- User only wants **go/no-go or market research** → `/web3-product-strategy`
- User wants **smart contract code, audit, or legal opinion** → out of scope
- User wants **one-off copy or UI pixel specs** → out of scope

---

## Pipeline (mandatory order)

```
Step 1: web3-product-strategy
        → output: strategy memo + explicit user confirmation
        ↓ (blocked until confirmed)
Step 2: web3-product-specification
        → output: PRD + gates + optional domain appendices
```

**Never** start Step 2 without Step 1 confirmation keywords: `confirmed`, `approved`, `proceed to spec`.

---

## Kickoff checklist

Ask or infer:

1. Decision / feature one-liner
2. Mode: Full | Express | Pulse (strategy) — default Express for features
3. Domain: DeFi | L2 | Consumer | combination
4. Artifacts available: screenshots, contracts, metrics (`PENDING` if none)

Assign **source IDs** at kickoff (carry through both skills):

| ID | Input |
|----|--------|
| SRC-1 | User brief / chat |
| SRC-2+ | Each file, URL, dashboard, or interview added later |

---

## Orchestration rules

1. Load [pipeline-summary.md](references/pipeline-summary.md).
2. **Step 1:** Read `.cursor/skills/web3-product-strategy/SKILL.md` (or repo path); load that skill’s `references/` per phase only.
3. **Checkpoint:** After Phase 4 memo, stop until user confirms.
4. **Step 2:** Read `.cursor/skills/web3-product-specification/SKILL.md`; gates 0→4; memo = SRC-2 in new index.
5. **Domain / cross-chain:** Load specification `references/*-product-surface.md` and `cross-chain-risks.md` when applicable.
6. **Traceability:** `(Source: SRC-n, tier)` on material claims (see child skills).
7. **Status block** at end of each step:

```markdown
## ORCHESTRATOR STATUS
- Strategy: ✅ confirmed | 🔄 in progress | ⬜ not started
- Specification: ✅ PRD ready | 🔄 gate N | ⬜ blocked (reason)
- Sources registered: SRC-1 … SRC-n
- Next: [exact next action + which skill]
```

---

## Child skills

| Skill | Invoke |
|-------|--------|
| Strategy | `web3-product-strategy` |
| Specification | `web3-product-specification` |

Examples (after install): `examples/strategy-memo-sample.md`, `examples/prd-story-sample.md`

## References

| File | When |
|------|------|
| [pipeline-summary.md](references/pipeline-summary.md) | Every orchestrator session (first) |

---

## Out of scope

Same boundaries as child skills: no legal rulings, no contract implementation, no guaranteed returns.
