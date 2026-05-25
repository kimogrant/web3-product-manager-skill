---
name: web3-product-manager
description: >
  Orchestrates the full Web3 product workflow from strategy through specification.
  Routes to web3-product-strategy then web3-product-specification in order with
  mandatory human checkpoints. Use when starting a greenfield feature end-to-end,
  running go/no-go through PRD, or when the user asks for the full Web3 PM pipeline.
  Triggers include full product workflow, end to end PM, from idea to PRD,
  web3 product manager, strategy then spec. Do not use for single-phase tasks
  that should invoke a child skill directly.
---

# Web3 Product Manager (Orchestrator)

## Purpose

Single entry point for **strategy → confirmed memo → specification → engineering-ready PRD**.

Child skills hold the detailed playbooks; this skill only **routes, enforces order, and tracks state**.

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

1. **Step 1:** Follow `web3-product-strategy` (load its `references/` per phase only).
2. **Checkpoint:** After Phase 4 memo, stop and request confirmation.
3. **Step 2:** Pass memo + source index into `web3-product-specification`; follow gates 0→4.
4. **Domain modules:** If DeFi/L2/Consumer, load the matching `references/*-product-surface.md` during spec gates 0–2.
5. **Traceability:** Requirements and memo claims use `(Source: SRC-n, tier)` tags per child skill rules.
6. **Status block** at end of each step:

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

---

## Out of scope

Same boundaries as child skills: no legal rulings, no contract implementation, no guaranteed returns.
