# Tokenomics design checklist (Gate 2b)

Product-facing review before engineering implements economic mechanisms. Not a substitute for economic modeling or legal review.

---

## When required

Run this gate if the change touches any of:

- New or modified token
- Emissions, vesting, or unlock schedules
- Fee switches, revenue share, or buyback/burn
- Points, credits, or off-chain rewards redeemable on-chain
- Governance power (including vote-escrow)
- Liquidity mining or referral incentives
- Staking, restaking, or receipt tokens

Mark **N/A** only with user confirmation and one-line reason.

---

## 1. Objective & bounds

| Question | Answer |
|----------|--------|
| What behavior should incentives change? | |
| What behavior must NOT be rewarded? | |
| Time horizon (bootstrap vs steady state)? | |
| Budget cap (tokens, USD equivalent, or % supply)? | |

---

## 2. Participant map

| Actor | Incentive | Risk if over-incentivized |
|-------|-----------|---------------------------|
| Users | | |
| LPs | | |
| Integrators | | |
| Team / insiders | | |
| Governance | | |

---

## 3. Value flow

Sketch (bullets or ASCII):

```text
User fees → [treasury | burn | LPs | stakers] → ...
```

| Flow | Rate / rule | Who controls knob? | On-chain enforceable? |
|------|-------------|--------------------|------------------------|
| | | | |

---

## 4. Supply & dilution

| Item | Detail |
|------|--------|
| Total supply cap | |
| Initial float | |
| Emission schedule | |
| Vesting cliffs | |
| Insider allocation % | |
| FDV / float implications | `PENDING` if unknown |

---

## 5. Sustainability & mercenary capital

| Check | Status (OK / Risk / N/A) | Notes |
|-------|--------------------------|-------|
| Yield source identified (fees vs emissions) | | |
| Emissions decline or fee growth path | | |
| Sybil / multi-wallet farming mitigations | | |
| Whale concentration limits | | |
| Oracle / liquidity manipulation surface | | |
| Death spiral coupling (token price ↔ utility) | | |

---

## 6. Governance & upgrades

| Question | Answer |
|----------|--------|
| Who can change parameters? | |
| Timelock duration | |
| Emergency pause | |
| Guardian / multisig | |

---

## 7. Comparable protocols

| Protocol | Mechanism | Outcome lesson | Source tier |
|----------|-----------|----------------|-------------|
| | | | on-chain / report |

---

## 8. Metrics & kill switches

| Metric | Target | Review cadence | Action if miss |
|--------|--------|----------------|----------------|
| Real fee revenue | | | |
| Emission / fee ratio | | | |
| Retention (funded wallets) | | | |
| Gini / top-N holder share | | | |

Align with strategy memo kill conditions.

---

## 9. Product copy guardrails

Document forbidden claims for UI/marketing tied to this feature:

- [ ] No guaranteed APY or price
- [ ] Risks visible before first fund movement
- [ ] Emissions labeled as temporary if applicable

---

## Gate 2b exit

- [ ] All sections answered or `PENDING` with owner
- [ ] Top 3 economic risks listed with mitigations
- [ ] Engineering knows which parameters are admin-configurable vs immutable
