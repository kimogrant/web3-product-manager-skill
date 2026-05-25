# Cross-chain risks (optional reference)

Load for products using **bridges, messaging layers, or multi-chain state**. Use at Gate 0–2 with [l2-product-surface.md](l2-product-surface.md) and/or [defi-product-surface.md](defi-product-surface.md).

---

## 1. Scope check

| Question | Answer |
|----------|--------|
| Chains involved | |
| Bridge / messaging protocol | |
| Who bears bridge risk? | User / protocol / third party |
| Canonical vs fast path | |

---

## 2. Product requirements

| Risk | Spec must include |
|------|-------------------|
| Stuck transfer | Status tracker, support playbook, ETA ranges |
| Wrong chain / address | Guards, checksum, chain-specific address book |
| Partial execution | Which leg succeeded; recovery UX |
| Replay / duplicate mint | Idempotency keys, tx history |
| Liquidity network failure | Fallback bridge or “wait” state |
| Message delay (optimistic / ZK) | Honest time copy; no “instant” if untrue |
| Supply sync | Token decimals, native vs wrapped symbols |
| Indexer lag cross-chain | Show pending until all legs confirmed |

---

## 3. Metrics

| Metric | Notes |
|--------|-------|
| Bridge completion rate | By route |
| Median time L1→L2 / L2→L1 | By path |
| Failed / stuck volume | $ or count |
| Support tickets / bridge | Trend |

---

## 4. Pre-ship checklist

- [ ] Each supported route tested on testnet/mainnet fork
- [ ] Explorer links per leg
- [ ] Runbook for stuck bridge (vendor + internal)
- [ ] UI never shows “complete” until destination chain credit confirmed

---

## Out of scope

Bridge smart contract audit and validator set economics (flag security / research).
