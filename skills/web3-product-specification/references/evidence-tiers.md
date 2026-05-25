# Evidence tiers (self-contained)

Use when tagging findings in PRD or domain appendices. Same rules as strategy `data-sources.md`—duplicated here so specification and L2/DeFi modules do not depend on another skill’s files.

| Tier | Label | Use | Caveat |
|------|-------|-----|--------|
| 1 | `on-chain` | Primary for protocol/market truth | State chain + time window |
| 2 | `report` | Messari, The Block, foundation reports | Publication lag |
| 3 | `first-party` | Your analytics, support, sales | Sample bias |
| 4 | `sentiment` | Social, KOL | Not demand proof alone |
| 5 | `analogy` | Cross-industry compare | Hypothesis only |

**Tag format:** `(Source: SRC-n, tier: on-chain, as-of: YYYY-MM-DD)`

For full research playbook, strategy skill: `web3-product-strategy/references/data-sources.md` (requires both skills installed).
