---
name: web3-product-specification
description: >
  Web3 product specification workflow for PRDs, gate-based requirements, wallet
  and chain constraints, tokenomics review checkpoints, and compliance surface
  mapping. Use when writing a PRD, scoping a feature, breaking down user stories,
  planning an iteration, or prototyping from a confirmed strategy. Triggers include
  PRD, product requirements, user stories, feature spec, scope sprint, on-chain
  feature, wallet flow, tokenomics design, governance feature, compliance review.
  Requires a confirmed strategy memo from web3-product-strategy. Not for pure
  smart contract coding or visual design tokens alone.
---

# Web3 Product Specification

## Purpose

Answers: **How do we specify and ship this safely?**

Turns a **confirmed strategy memo** into engineering-ready requirements, optional prototype brief, and explicit tokenomics / compliance checkpoints.

**Prerequisite:** Confirmed output from `web3-product-strategy` (or user-provided equivalent memo with recommendation and kill conditions).

---

## Gate flow

```
Gate 0: Ground truth audit (product + chain surface)
  ↓
Gate 1: Information architecture & flows
  ↓
Gate 2: Three-layer requirements + tokenomics gate (if applicable)
  ↓
Gate 3: Compliance & abuse surface (if applicable)
  ↓
Gate 4: Iteration plan & acceptance criteria
```

Each gate ends with a **checkpoint** (see below). Do not advance with blocking `PENDING` items unresolved unless the user explicitly accepts risk.

Detail: [references/gate-guide.md](references/gate-guide.md)  
PRD template: [references/prd-template.md](references/prd-template.md)  
Tokenomics: [references/tokenomics-checklist.md](references/tokenomics-checklist.md)  
Compliance surface: [references/compliance-surface.md](references/compliance-surface.md)

---

## Core principles

| ID | Principle | Rule |
|----|-----------|------|
| P1 | Reality before design | Audit current product; mark unknowns `PENDING` |
| P2 | Delta first | Prefer extending existing flows over new surfaces |
| P3 | Explicit assumptions | `Assumes X. If false → impact Y` on decisions |
| P4 | Progressive gates | No Gate 2 detail before Gate 1 confirmed |
| P5 | Challenge each requirement | Exists? Necessary? Cheaper alternative? |
| P6 | No fabricated chain facts | Real contract names, events, IDs—or `TBD` |
| P7 | Checkpoint at boundaries | Resumable state for parallel workstreams |

---

## Three-layer requirement model (Gate 2)

For each feature or epic, specify:

| Layer | Covers |
|-------|--------|
| **Presentation & data** | Fields, states, empty/error, ordering, data sources |
| **Interaction** | Triggers, transitions, confirmations, wallet prompts, edge cases |
| **Business & integration** | Rules, approvals, API/contract calls, failure handling, indexing |

Out of scope here: pixel-level visual design (colors, spacing).

---

## Conditional gates

| Gate | Run when |
|------|----------|
| Tokenomics (Gate 2b) | Token, points, fees, incentives, governance weight, or emissions touched |
| Compliance (Gate 3) | Users fund value, KYC/AML sensitivity, geo restrictions, securities-like marketing |

Load [tokenomics-checklist.md](references/tokenomics-checklist.md) or [compliance-surface.md](references/compliance-surface.md) when triggered.

---

## Grounding protocol (Gate 0)

Before generating requirements, verify context:

| Need | Acceptable evidence |
|------|---------------------|
| Current UI / flows | Screenshots, Figma, live URL walkthrough |
| Contracts / APIs | ABI snippet, Swagger, official docs link |
| Competitor pattern | Named protocol + feature link or screenshot |
| Metrics baseline | Dashboard export, Dune query description, or `PENDING` |

If evidence is insufficient, request specific artifacts—do not invent schemas or event names.

---

## Checkpoint format

```markdown
## CHECKPOINT: [WORKSTREAM-ID] @ Gate [N] — [YYYY-MM-DD]

Gates:
- Gate 0 Audit:           ✅ | 🔄 | ⬜
- Gate 1 IA/Flows:        ✅ | 🔄 | ⬜
- Gate 2 Requirements:    ✅ | 🔄 | ⬜
- Gate 2b Tokenomics:     ✅ | 🔄 | ⬜ | N/A
- Gate 3 Compliance:      ✅ | 🔄 | ⬜ | N/A
- Gate 4 Iteration plan:  ✅ | 🔄 | ⬜

Confirmed decisions:
Assumptions (confirmed / pending / invalidated):
Blocking 🔴:
Pending 🟡:
Deliverables:
Next action:
```

---

## Pre-handoff checklist (engineering)

- [ ] Every user story has acceptance criteria and test notes
- [ ] Wallet/network requirements explicit (chain id, AA, paymaster, etc.)
- [ ] Failure modes: rejected tx, reorg, RPC down, insufficient gas
- [ ] Tokenomics gate completed or marked N/A with reason
- [ ] Compliance surface completed or marked N/A with reason
- [ ] No `TBD` on safety-critical paths without accepted risk flag
- [ ] PRD sections match [prd-template.md](references/prd-template.md)

---

## Out of scope

- Go/no-go market strategy (use `web3-product-strategy`)
- Production smart contract code or formal audit
- Marketing copy and community campaign plans
- Legal sign-off (surface risks; user engages counsel)

---

## Agent behavior

1. Confirm strategy memo exists; if not, stop and ask user to run strategy skill first.
2. Load gate guide for active gate only.
3. Run Gate 2b / 3 when triggers match—do not skip silently.
4. Output PRD using template; save checkpoint at each gate.

---

## References

| File | When to load |
|------|----------------|
| [gate-guide.md](references/gate-guide.md) | Gate 0–4 execution |
| [prd-template.md](references/prd-template.md) | Gate 2+ document output |
| [tokenomics-checklist.md](references/tokenomics-checklist.md) | Gate 2b |
| [compliance-surface.md](references/compliance-surface.md) | Gate 3 |

Related skill: `web3-product-strategy`
