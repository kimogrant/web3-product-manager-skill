# Evidence sources — Web3 product strategy

Use this hierarchy when collecting Phase 2 evidence. Tag every finding with its tier.

---

## Source tiers

| Tier | Label | Use | Caveat |
|------|-------|-----|--------|
| 1 | `on-chain` | Primary for protocol/market truth | Define window; note chain |
| 2 | `report` | Structured industry analysis | Publication lag |
| 3 | `first-party` | Your product analytics, support, sales | Sample bias |
| 4 | `sentiment` | Social, KOL, forums | Narrative risk |
| 5 | `analogy` | Cross-industry comparison | Weakest; hypothesis only |

Never promote tier 4–5 to tier 1 without verification.

---

## On-chain & market (tier 1)

| Source type | Typical metrics | Notes |
|-------------|-----------------|-------|
| DefiLlama | TVL, fees, volume by protocol | Cross-check chain breakdown |
| Dune / custom SQL | Retention, cohorts, wallet flows | Document query link or description |
| Token Terminal | Revenue, active users (where supported) | Protocol coverage varies |
| Nansen / Arkham (if available) | Wallet labels, smart money flows | Privacy and cost |
| Explorers | Contract deploy dates, tx counts | Not UX quality alone |

**Wallet-centric products:** funded wallets, transacting wallets, repeat rate, median hold time, gas spent per active user.

**DeFi protocols:** TVL trajectory, utilization, liquidations, oracle dependency, concentration (top depositors).

---

## Reports & research (tier 2)

Messari, The Block Research, a16z crypto, protocol foundation reports, grant program evaluations.

Record: publisher, date, claim, whether replicated by on-chain data.

---

## First-party (tier 3)

Product analytics, support tickets, sales calls, beta waitlist, prior experiment results.

Segment by: chain, wallet type (EOA vs smart account), geo if known.

---

## Sentiment (tier 4)

X/Telegram/Discord narratives, KOL takes, conference themes.

Use for **timing and positioning hypotheses**, not demand proof.

---

## Competitive scan structure

For each competitor (max 5 in Express, 10 in Full):

| Field | Content |
|-------|---------|
| Name | Protocol or product |
| Positioning | One line |
| Chain / deployment | |
| Strength | Evidence tier |
| Weakness | Evidence tier |
| Implication for us | Build / differentiate / avoid |

---

## Contrarian scan (S8)

Explicitly seek:

- Bear case reports or post-mortems of similar products
- On-chain data contradicting bullish narrative (e.g. rising TVL, falling unique users)
- Regulatory actions in adjacent categories
- Technical incidents (exploits, oracle failures) in the category

Document at least **2** contrarian inputs in Full mode.

---

## Domain-specific benchmarks (Phase 2)

When the decision is vertical-specific, load the matching specification reference for metric definitions and risk prompts:

| Vertical | Reference | Priority metrics |
|----------|-----------|------------------|
| DeFi | `defi-product-surface.md` | TVL, volume, revenue, utilization, bad debt |
| L2 | `l2-product-surface.md` | Bridge flow, TTFX, tx success, sequencer uptime |
| Consumer | `consumer-product-surface.md` | Activation, D7/D30, funded wallets, support rate |

---

## Data hygiene

- State `as-of` date for all metrics
- Prefer rates and ratios over single-point TVL
- When APIs unavailable, mark `PENDING` and ask user for export
- Do not cite wallet addresses as “users” without defining the counting rule
