# Example: strategy memo excerpt (fictional)

Redacted pattern for a **Pilot** recommendation. Not real market data.

---

## Executive summary

**Recommendation: Pilot** a one-chain “gasless first swap” onboarding flow on Base for retail wallets, 6 weeks, capped incentives.

We should run a limited pilot because on-chain evidence shows strong DEX volume but weak **repeat funded-wallet retention** for our category (tier: on-chain, 90d window). Track B argues incentive spend will attract mercenary wallets unless paired with retention mechanics. Opportunity cost: pauses multi-chain expansion by one sprint.

Top risk: emissions without fee-backed yield. Kill if 90d repeat rate stays below 15% among pilot cohort.

---

## Decision statement

Should we build a gas-sponsored first-swap funnel for new EOAs on Base?

---

## Assumptions & falsification

| ID | Assumption | Falsification signal |
|----|------------|----------------------|
| A1 | Users abandon due to gas confusion | Support tickets drop; step-2 connect rate +20% |
| A2 | Sponsor budget ≤ $50k for pilot | Burn rate exceeds weekly cap |
| A3 | Base liquidity sufficient for <$500 swaps | Slippage >2% on 80% of test swaps |

---

## Kill conditions

| ID | Condition | Threshold |
|----|-----------|-----------|
| K1 | Repeat swap within 14d | <15% of funded pilot wallets |
| K2 | Cost per retained wallet | >$40 at week 6 |

---

## Handoff

Memo status: **Example only** — confirm with stakeholders before `web3-product-specification`.
