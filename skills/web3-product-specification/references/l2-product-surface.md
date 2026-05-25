# L2 / rollup product surface — specialist reference

Load when the product ships on or **depends on an L2, rollup, app-chain, or cross-rollup** experience. Use at **Gate 0–2** and when specifying **bridges, deposits, withdrawals, gas abstraction, or sequencer behavior**.

If the product is also DeFi-heavy, load [defi-product-surface.md](defi-product-surface.md) in parallel.

---

## 1. Stack classification

Identify stack (multi-select if hybrid):

| Stack | User-facing implication |
|-------|-------------------------|
| Optimistic rollup (OP Stack, Arb Orbit, etc.) | 7d challenge window for canonical bridge (unless fast path) |
| ZK rollup | Proof latency, different withdrawal UX |
| Validium / off-chain DA | Extra trust on DA committee |
| App-chain / L3 | Native gas token, custom precompiles |
| Based / shared sequencing | MEV and ordering assumptions change |

Record: **chain ID**, **native gas token**, **canonical bridge contract(s)**, **block explorer**, **sequencer status page**.

---

## 2. Gate 0 — L2 ground truth audit

| Area | Capture |
|------|---------|
| Deployment target | Mainnet L2 name, testnet parity |
| RPC / indexer | Primary, fallback, rate limits |
| Bridge | Official bridge only or third-party (Across, Stargate, etc.) |
| Deposit path | L1→L2 messaging, time estimate, failure modes |
| Withdrawal path | Standard vs fast; challenge period if optimistic |
| Gas token | ETH, custom token, paymaster sponsorship |
| AA / paymaster | ERC-4337 vendor, policy limits |
| Sequencer | Single vs decentralized roadmap; recent downtime |
| Finality | Soft vs hard confirmations shown in UI |

**Trust assumptions (explicit in PRD appendix):**

- Sequencer liveness and ordering
- DA layer (Ethereum blobs, alt-DA, etc.)
- Bridge validator / proof system
- Governance upgrade keys

---

## 3. Gate 1 — L2 user journeys

### Required journey annotations

| Step | L2 fields |
|------|-----------|
| Network switch | Add chain to wallet; wrong-chain guard |
| Fund on L2 | Bridge in, on-ramp, or receive transfer |
| Act on L2 | Core product action |
| Exit | Bridge out, CEX off-ramp, or keep on L2 |

### Withdrawal UX matrix

| Path | Time | Cost | When to offer |
|------|------|------|---------------|
| Canonical | Long (e.g. 7d OP) | Lower | Default “secure” |
| Fast / liquidity network | Minutes | Fee + LP spread | Power users, urgency |
| CEX deposit | Varies | KYC | Fiat off-ramp markets |

**Edge journeys**

- [ ] User on L1 tries to interact with L2-only contract
- [ ] Sequencer down / degraded (read-only mode spec)
- [ ] Bridge message stuck (status tracker, support playbook)
- [ ] Insufficient L2 gas for first tx (faucet / paymaster / top-up CTA)
- [ ] Reorg or re-sync (tx status ambiguity)

---

## 4. Gate 2 — L2 requirement extensions

| Topic | Spec detail |
|-------|-------------|
| Confirmations | Blocks to show “pending” vs “confirmed”; L1 finality if relevant |
| Gas estimation | L2 gas + L1 data fee (EIP-4844 blob cost) if applicable |
| Paymaster | Sponsor limits per user, per day, asset whitelist |
| Batch / intent | If using intent solver — solver failure UX |
| Multi-L2 | Same address, different chain IDs; portfolio aggregation rules |
| Contract addresses | Per-chain address table; no copy-paste across chains |

**Cross-rollup / multi-L2 product table (template)**

| Feature | Chain A | Chain B | Parity? |
|---------|---------|---------|---------|
| | | | full / partial / N/A |

---

## 5. Strategy & metrics (L2)

| Metric | Pitfall |
|--------|---------|
| “Users” | Count funded addresses on **this** chain only |
| TVL | Avoid double-count bridged assets on L1 and L2 |
| Tx success rate | Split sequencer errors vs reverts |
| Bridge volume | In vs out; net flow signal |
| Time-to-first-tx | Include bridge wait in funnel |

Phase 2 research: tag sources with chain scope. Use [evidence-tiers.md](evidence-tiers.md) in this skill; optional deep dive: sibling `web3-product-strategy/references/data-sources.md` if both skills are installed.

---

## 6. Tokenomics & governance (L2)

| Item | PM question |
|------|-------------|
| Native gas token | Utility vs speculative marketing |
| Sequencer revenue share | Who receives MEV / fees |
| Governance on L2 | What upgrades affect user funds |
| Grants / incentives | Chain-level vs app-level — stacking rules |

---

## 7. Compliance & ops (L2)

| Item | Product note |
|------|--------------|
| Bridge partners | Disclose third-party bridge in UI |
| Sanctions | Address screening at bridge or app layer |
| Incidents | Sequencer outage banner + status link |
| Explorers | Link correct explorer per chain ID |

---

## 8. Pre-ship L2 checklist

- [ ] Wrong-network detection on all wallet entry points
- [ ] Bridge/deposit ETA and failure states documented
- [ ] Withdrawal paths tested (canonical + fast if offered)
- [ ] Paymaster budget caps and exhaustion UX
- [ ] Address book per chain in config (no cross-chain address reuse errors)
- [ ] Runbook: sequencer down, bridge delayed, RPC outage

---

## Out of scope

- Proving system implementation
- Node operator runbooks
- Bridge smart contract audit
