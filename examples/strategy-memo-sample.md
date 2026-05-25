# Example: strategy memo (fictional)

Demonstrates **Source index**, tier tags, and handoff. Not real market data.

---

## Executive summary

**Recommendation: Pilot** — gas-sponsored first swap on Base for new EOAs, 6 weeks.

Category DEX volume is high but **repeat funded-wallet retention** is weak `(Source: SRC-3, tier: on-chain, as-of: 2026-03-01)`. Track B: incentives alone attract mercenary wallets `(Source: SRC-4, tier: report, as-of: 2026-02-15)`. Opportunity cost: pause multi-chain expansion one sprint `(Source: SRC-1, tier: first-party)`.

---

## Decision statement

Should we build a gas-sponsored first-swap funnel for new EOAs on Base?

---

## Assumptions & falsification

| ID | Assumption | Falsification signal | Source |
|----|------------|----------------------|--------|
| A1 | Users abandon due to gas confusion | Connect→swap +20% | SRC-5 (support sample) |
| A2 | Sponsor budget ≤ $50k | Weekly burn cap breach | SRC-1 |
| A3 | Base liquidity OK for <$500 swaps | Slippage >2% on 80% tests | SRC-6 (Implicit — run before build) |

---

## Kill conditions

| ID | Condition | Threshold | Source |
|----|-----------|-----------|--------|
| K1 | 14d repeat swap | <15% pilot cohort | SRC-3 |
| K2 | Cost per retained wallet | >$40 at week 6 | SRC-1 |

---

## Source index

| ID | Description | Tier | As-of |
|----|-------------|------|-------|
| SRC-1 | User brief + budget constraint | first-party | 2026-05-01 |
| SRC-3 | Dune: category retention dashboard (described) | on-chain | 2026-03-01 |
| SRC-4 | The Block: incentive farming report (described) | report | 2026-02-15 |
| SRC-5 | Support ticket themes (n=120, described) | first-party | 2026-04-01 |
| SRC-6 | Pending — swap slippage test script | Implicit | — |

---

## Handoff

- [ ] Memo confirmed by stakeholder → `web3-product-specification`
- Attach: SRC index above; strategy memo becomes **SRC-2** in PRD skill
