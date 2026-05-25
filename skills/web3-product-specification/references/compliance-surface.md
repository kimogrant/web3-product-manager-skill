# Compliance & abuse surface (Gate 3)

Maps **product and go-to-market risk areas** for engineering and legal review. Outputs a risk table—not legal advice. Flag `COUNSEL REQUIRED` when sensitivity is high.

---

## When required

| Trigger | Run Gate 3 |
|---------|------------|
| Users deposit, swap, lend, or stake funds | Yes |
| Yield or return marketed | Yes |
| KYC / geo gating | Yes |
| Third-party custody or omnibus wallets | Yes |
| Token sale or airdrop with value | Yes |
| Read-only analytics, no fund movement | Often N/A |

---

## 1. Activity classification (product view)

Describe what the user can do in plain language:

| Activity | Enabled? | Notes |
|----------|----------|-------|
| Custody of user assets | | |
| Routing to third-party protocols | | |
| Issuance of instrument-like token | | |
| Gambling / prediction markets | | |
| Cross-border access | | |

**Sensitivity:** Low / Med / High (user-confirmed)

If High → mark all legal rows `COUNSEL REQUIRED`.

---

## 2. User geography & access

| Control | Implemented? | Spec requirement |
|---------|----------------|------------------|
| Geo IP block | | |
| Terms acceptance | | |
| Sanctions screening | | |
| Age gating | | |

Document **intended** markets; do not claim compliance without counsel sign-off.

---

## 3. Marketing & disclosures

| Surface | Requirement |
|---------|-------------|
| Landing page | Risk disclosures, no guaranteed returns |
| In-app first fund | Consent + risk summary |
| APY display | Methodology, gross vs net, period |
| Token descriptions | Utility vs investment framing (counsel) |

List copy that must **not** ship without review.

---

## 4. Abuse & fraud

| Vector | Mitigation in spec |
|--------|-------------------|
| Sybil airdrop | |
| Phishing (fake domains) | |
| Address poisoning | |
| Social engineering on support | |
| MEV on user txs | |
| Admin key compromise | |

---

## 5. Data & privacy

| Data | Collected? | Retention | User rights |
|------|------------|-----------|-------------|
| Wallet address | | | |
| Email / KYC | | | |
| IP / device | | | |

Note if on-chain data is public by design.

---

## 6. Third parties

| Vendor | Role | Failure impact |
|--------|------|----------------|
| RPC | | |
| Indexer | | |
| Fiat on-ramp | | |
| KYC provider | | |

---

## 7. Incident response (product requirements)

| Scenario | User-facing behavior | Internal runbook link |
|----------|----------------------|------------------------|
| Exploit | | |
| Pause | | |
| Oracle failure | | |
| Comm loss | | |

---

## Risk register output

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status |
|----|------|------------|--------|------------|-------|--------|
| R1 | | | | | | |

---

## Gate 3 exit

- [ ] Risk register attached to PRD §10
- [ ] `COUNSEL REQUIRED` items listed explicitly
- [ ] No shipping criteria that depend on unreviewed legal claims
- [ ] User acknowledges this is not legal advice
