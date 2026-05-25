# Example: PRD outline (fictional, table of contents)

Skeleton showing how v1.4 artifacts fit together. Expand each section in a real project; do not treat placeholders as facts.

**Builds on:** [strategy-memo-sample.md](strategy-memo-sample.md) (Pilot → SRC-2 in this doc).

---

```markdown
# PRD: Gas-sponsored first swap (Base)

| Field | Value |
|-------|-------|
| Version | 0.2 |
| Status | Ready for engineering |
| Strategy memo | SRC-2 (Pilot memo 2026-05-01) |
| Chains | Base (8453) |

## 0. Source index
| ID | Description | Tier |
|----|-------------|------|
| SRC-2 | Approved strategy memo | first-party |
| SRC-7 | Paymaster API draft | first-party |
| SRC-8 | Competitor UX screenshot set | first-party |

## 1. Summary
Pilot: first swap gas-sponsored for new EOAs `(Source: SRC-2)`.

## 2. Goals & non-goals
Goals: activation, 14d repeat swap metric K1.
Non-goals: multi-chain, perpetuals, fiat on-ramp.

## 3. Users & personas
New EOA retail swapper.

## 4. Context & ground truth (Gate 0)
Current: connect + swap exists; no sponsorship.
Delta: add paymaster path + sponsor badge.

## 5. Information architecture (Gate 1)
Journey: Land → Connect → Swap → Success → Portfolio.

## 5b. Domain appendix
| Domain | Module | Status |
|--------|--------|--------|
| Consumer | consumer-product-surface.md | checklist done |
| L2 | l2-product-surface.md | N/A (Base only, no bridge UX) |

## 6. Requirements (Gate 2)
### Epic: Sponsored first swap
#### US-014 … (see prd-story-sample.md)
#### US-015 Wallet limit messaging …

## 7. Prototype validation (Gate 3.5)
- Mode: HTML vibe prototype in `/prototypes/first-swap/`
- Review: 2026-05-10 — Approved with PRD edit to US-015

## 8. Wallet & chain requirements
Base only; EOA; paymaster policy SRC-7.

## 9. Failure & edge cases
Revert, wrong network, sponsor exhausted.

## 10. Tokenomics appendix
N/A — no new token `(signed PM 2026-05-08)`

## 11. Compliance surface
Yield marketing N/A; fund movement: non-custodial routing.

## 12. Metrics & instrumentation
K1 repeat swap; sponsor cost per activation.

## 13. Iteration plan (Gate 4)
| Slice | Stories | Exit |
| MVP | US-014 | Testnet + 50 internal wallets |
| +1 | US-015 | Public pilot |

## 14. Open questions
| Q1 | Paymaster SLA doc from vendor | Eng | 2026-05-12 |

## 15. Approvals
PM ✅ | Eng 🔄
```

---

## Methodology log (optional)

| Method | Used? | Note |
|--------|-------|------|
| M3 Epic hypothesis | Yes | Epic section above |
| M4 Story split | Yes | US-014 / US-015 |
| M1 OST | No | — |
