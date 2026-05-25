---
name: web3-product-strategy
description: >
  Web3 product strategy workflow for go/no-go decisions, market and competitive
  analysis, on-chain signal review, and investor-ready strategy memos. Use when
  deciding whether to build a product or feature, sizing a market, comparing
  protocols, evaluating timing, or producing a strategy memo. Triggers include
  go/no-go, should we build, market research, competitive analysis, protocol
  comparison, trend scan, prioritization, strategy memo, opportunity cost.
  Pair with web3-product-specification after the memo is confirmed.
metadata:
  version: "1.4.0"
  package: web3-product-manager-skill
---

# Web3 Product Strategy

## Purpose

Answers: **Should we build this, why now, and what do we stop doing?**

Structured decision workflow for small teams, fast cycles, and deliverables that survive investor and engineering scrutiny.

**Handoff:** When the memo is confirmed → run `web3-product-specification` with the memo as input (or use `web3-product-manager` for the full pipeline).

---

## When NOT to use

- User already has an **approved strategy memo** and only needs a PRD → `web3-product-specification`
- **Implementation, audit, or ticket coding** requests → engineering workflows
- **Definitive legal or tax advice** on tokens → counsel
- **Price / APY predictions** or investment advice → refuse
- User wants **full pipeline** without switching skills → `web3-product-manager`

---

## Modes

| Mode | Use when | Typical effort |
|------|----------|----------------|
| **Full** | New product line, large bet, unfamiliar market | Multi-day; all phases |
| **Express** | Mid-size feature; partial prior research | 1–3 days; Phases 1–4 |
| **Pulse** | Small scope; strong priors; need a fast bias check | Hours; Phases 1, 3 (light), 4 |

State the mode at kickoff. Do not run Full checkpoints in Pulse mode.

---

## Workflow

```
Phase 1: Frame & reframe the decision
  ↓
Phase 2: Evidence (Track A opportunity + Track B challenge, parallel)
  ↓
Phase 3: Synthesis (matrix, pre-mortem, kill conditions)
  ↓
Phase 4: Strategy memo (human confirmation required)
  ↓
Phase 5: Track & retrospective (optional, post-ship)
```

**Parallel tracks rule:** Track A and Track B share raw inputs only—not draft conclusions. Track B must argue the strongest credible “do not build” case.

Detail: [references/phase-guide.md](references/phase-guide.md)  
Memo output: [references/strategy-memo-template.md](references/strategy-memo-template.md)  
Data sources: [references/data-sources.md](references/data-sources.md)  
Domain lenses (Phase 2): DeFi / L2 / Consumer — load from sibling skill  
`.cursor/skills/web3-product-specification/references/{defi|l2|consumer}-product-surface.md`  
(both skills must be installed; see orchestrator `pipeline-summary.md`).

---

## Core principles

| ID | Principle | Rule |
|----|-----------|------|
| S1 | Conclusion first | Lead with recommendation, then evidence |
| S2 | Adversarial parallel | Independent A/B tracks before synthesis |
| S3 | On-chain anchor | Prefer verifiable metrics; tag source tier |
| S4 | Time-boxed claims | Every trend claim needs a window (e.g. 90d) |
| S5 | Opportunity cost | “Yes” implies what pauses or deprioritizes |
| S6 | Falsifiable bets | Key assumptions have disproof signals |
| S7 | Reframe before answer | Validate the decision question itself |
| S8 | Contrarian scan | Seek non-consensus and weak signals explicitly |
| S9 | Source traceability | Tag claims with `(Source: SRC-n, tier)`; see phase guide |
| S10 | On-demand methods | Run M1/M2 only when triggers fire — see methodology toolkit |

**Methodology (M1 OST, M2 PoL):** sibling skill  
`.cursor/skills/web3-product-specification/references/methodology-toolkit.md`

---

## Source registry (Phase 1)

Assign IDs to every input; reuse across phases:

| ID | Typical input |
|----|----------------|
| SRC-1 | User brief / this conversation |
| SRC-2+ | Each document, URL, dataset, or interview transcript |

---

## Phase 1 gate (minimum inputs)

Do not start Phase 2 until the user confirms or supplies:

- [ ] Decision statement (one sentence)
- [ ] Target user / wallet persona
- [ ] Chain(s) and product surface (app, protocol, API, agent)
- [ ] Success metric hypothesis (on-chain or product analytics)
- [ ] Constraints (timeline, budget, regulatory sensitivity: low/med/high)

If inputs are missing, ask up to **5** focused questions, then pause.

---

## Phase 4 gate (memo confirmation)

Before handoff to specification:

- [ ] Recommendation explicit (Build / Pilot / Defer / Kill)
- [ ] Pre-mortem top failures listed with mitigations
- [ ] Kill conditions measurable and time-bound
- [ ] User explicitly confirms memo (“confirmed”, “approved”, “proceed to spec”)

Without confirmation, do not invoke `web3-product-specification`.

---

## Out of scope

- Writing full PRDs or user-story backlogs (use `web3-product-specification`)
- Legal opinions or token classification rulings (flag for counsel; use compliance surface in spec skill)
- Smart contract implementation or audit execution
- Price predictions or guaranteed returns

---

## Agent behavior

1. Read this file, then load **only** the reference file for the active phase.
2. Cite `Source: SRC-n` and data tier (on-chain / report / first-party / sentiment) per finding.
3. Mark unknowns as `PENDING`—never invent TVL, addresses, or user counts.
4. End each phase with a short checkpoint block (status, open questions, next phase).
5. Pass source index with memo at handoff to specification.

---

## References

| File | When to load |
|------|----------------|
| [phase-guide.md](references/phase-guide.md) | Executing Phases 1–5 |
| [strategy-memo-template.md](references/strategy-memo-template.md) | Phase 4 output |
| [data-sources.md](references/data-sources.md) | Phase 2 research |

Related skill: `web3-product-specification`
