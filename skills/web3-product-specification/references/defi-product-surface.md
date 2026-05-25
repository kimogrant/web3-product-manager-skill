# DeFi product surface — specialist reference

Load when the initiative touches **lending, borrowing, DEX, LP, vaults, perps, stablecoins, or protocol-native yield**. Use at **Gate 0–2** (audit, flows, requirements) and during **Gate 2b tokenomics** if incentives interact with pools or emissions.

Pair with [tokenomics-checklist.md](tokenomics-checklist.md) and [compliance-surface.md](compliance-surface.md).

---

## 1. Product archetype

Mark one primary archetype (secondary allowed):

| Archetype | User promise | Spec must nail |
|-----------|--------------|----------------|
| Spot DEX / aggregator | Best execution for swap | Routing, slippage, MEV, approvals |
| Lending / borrowing | Supply earn / borrow against collateral | Health factor, liquidation, caps |
| LP / AMM pool | Provide liquidity, earn fees | IL disclosure, range, withdrawal delay |
| Vault / strategy | Deposit into managed strategy | Curator trust, strategy transparency, pause |
| Perps / derivatives | Leveraged exposure | Funding, margin, oracle, liquidation |
| Stablecoin / RWA yield | Stable unit or real-world yield | Peg, reserve, redemption, attestations |

---

## 2. Gate 0 — DeFi ground truth audit

| Area | Capture | Common `PENDING` |
|------|---------|------------------|
| Core contracts | Pool, router, oracle, incentives distributor | Proxy address, implementation |
| Oracles | Source, heartbeat, deviation threshold | Fallback behavior |
| Collateral set | Listed assets, LTV, liquidation bonus | Governance add process |
| Fee model | Protocol fee, LP fee, flash fee | Fee switch authority |
| Pause / guardian | What pauses (deposits, borrows, all) | Who can unpause |
| Indexing | Subgraph lag, event set for balances | Reorg handling |
| Composability | Listed integrations (aggregators, bridges) | Allowlist |

**Risk snapshot (1 paragraph):** oracle manipulation, governance capture, insolvency cascade, depeg, smart-contract upgrade.

---

## 3. Gate 1 — DeFi journeys

Annotate each journey with:

| Step | DeFi fields |
|------|-------------|
| Connect | Chain, wallet type, read-only preview |
| Approve | Token, spender, permit vs tx, infinite approval warning |
| Deposit / supply | Cap, utilization, expected APY **methodology** |
| Borrow | Health factor preview, liquidation price |
| Swap | Route, price impact, min out, deadline |
| Withdraw / repay | Cooldown, queue, penalty |
| Claim rewards | Emission schedule, claim gas, merge vs separate tx |

**Mandatory edge journeys**

- [ ] First-time depositor (no prior approval)
- [ ] Near-liquidation borrower
- [ ] Pool at cap or paused
- [ ] Oracle stale / sequencer down (L2 — cross-load [l2-product-surface.md](l2-product-surface.md) if applicable)

---

## 4. Gate 2 — DeFi requirement extensions

Add to each story’s **Business & integration** layer:

| Topic | Acceptance pattern |
|-------|-------------------|
| Slippage | User-set or default; revert message on excessive impact |
| Health factor | Display formula inputs; block borrow if HF < threshold |
| Liquidation | User notification threshold; public liquidation bot fairness |
| Utilization | Show pool utilization; explain rate curve if variable |
| IL (LP) | Static disclaimer + optional calculator link |
| Approvals | Min allowance default; revoke path documented |
| Simulation | Preview via `eth_call` / SDK simulate where possible |

**Metrics (tie to strategy memo)**

| Metric | Definition |
|--------|------------|
| TVL | Asset-side, chain-split, double-count rule |
| Volume | 24h, include/exclude wash policy |
| Revenue | Protocol fees, not gross volume |
| Active positions | Unique positions, not tx count |
| Bad debt | Post-incident tracking |

---

## 5. Tokenomics (DeFi-specific Gate 2b add-ons)

| Check | Question |
|-------|----------|
| Emission vs fees | Are rewards funded by real fees or inflation only? |
| Gauge wars | Can external bribes distort emissions? |
| Mercenary LPs | TVL drop if emissions end — modeled? |
| ve-token | Lock duration, decay, vote markets |
| Points → token | Conversion rules, sybil, cliff |

---

## 6. Compliance & comms (DeFi)

| Surface | Product requirement |
|---------|---------------------|
| APY display | Gross/net, fee, emission component, period |
| “Deposit” language | Custody vs non-custody accurate |
| Leverage | Risk warnings before first borrow |
| Stablecoin | No “guaranteed peg” unless legally cleared |
| Geo | Restricted actions if sanctions/KYC policy exists |

---

## 7. Pre-ship DeFi checklist

- [ ] Liquidation path tested on testnet/fork
- [ ] Oracle failure runbook linked in PRD
- [ ] Pause tested with user-visible message
- [ ] Indexer matches contract events for balances
- [ ] No guaranteed yield in UI copy
- [ ] Kill conditions from strategy memo on dashboard

---

## Out of scope for this module

- Smart contract audit scope (reference security team)
- Formal economic modeling (quant / token engineer)
- Legal token classification
