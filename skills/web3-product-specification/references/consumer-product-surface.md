# Consumer Web3 product surface — specialist reference

Load for **retail-facing** products: wallets, onboarding, social, gaming, NFT marketplaces, lifestyle apps, Telegram/mini-apps, and **agent-assisted** consumer flows. Use at **Gate 0–2**; lighter tokenomics unless points, membership, or tradable rewards exist.

Pair with [compliance-surface.md](compliance-surface.md) when users buy, sell, or earn value.

---

## 1. Product archetype

| Archetype | North-star metric | Spec focus |
|-----------|-------------------|------------|
| Wallet / super-app | Funded wallets, DAU/WAU | Connect, send, dApp browser, security |
| Onboarding funnel | Time-to-first-value | Gasless first action, education, drop-off |
| Social / creator | Retention, posts per user | Identity, moderation, tipping |
| Gaming / world | Session length, payer % | Assets, marketplace, anti-cheat |
| NFT marketplace | GMV, listings | Mint, royalty, creator fees |
| Lifestyle / rewards | Habit retention | Points, streaks, partner rewards |
| AI agent consumer | Task completion rate | Delegation limits, disclosure, revoke |

---

## 2. Gate 0 — Consumer ground truth audit

| Area | Capture |
|------|---------|
| Platforms | Web, iOS, Android, TWA, Telegram, Discord |
| Auth | Email, social, passkey, wallet-only |
| Wallet model | EOA, embedded, smart account, session keys |
| Fiat rails | On-ramp vendor, geo, KYC point |
| Chains exposed | User-visible vs backend-only |
| Asset types | FT, NFT, points (off-chain), SBT |
| Notification | Push, email, bot messages |
| Support | In-app, ticket, community |
| Moderation | UGC, reports, ban flow |

**Funnel baseline (from memo or `PENDING`):**

| Stage | Rate / count |
|-------|--------------|
| Install / land | |
| Wallet connect | |
| First funded | |
| First core action | |
| D7 / D30 return | |

---

## 3. Gate 1 — Consumer journeys

### Onboarding (mandatory spec)

| Step | Consumer detail |
|------|-----------------|
| Value prop | One-screen outcome, not jargon |
| Wallet create/import | Seedless path, recovery, social login risks |
| First action | Gasless, sponsored, or < $1 equivalent |
| Education | Skip vs expand; never block on whitepaper length |
| Failure | Drop-off recovery (email remind, deep link) |

### Wallet & security journeys

- [ ] Connect external wallet (WC, injected)
- [ ] Wrong network / unsupported asset
- [ ] Sign message vs sign transaction — plain language
- [ ] Session expiry and re-auth
- [ ] Lost device / account recovery (embedded wallet)

### Social & UGC (if applicable)

- [ ] Create / edit / delete content
- [ ] Report and block
- [ ] Minor safety / illegal content escalation path

### Gaming / NFT (if applicable)

- [ ] Buy, sell, transfer asset
- [ ] Cooldowns, inventory, repair (economy loops)
- [ ] Secondary royalty display

---

## 4. Gate 2 — Consumer requirement extensions

| Topic | Spec detail |
|-------|-------------|
| Language | Plain English; define “gas”, “network”, “approve” inline |
| Tx status | Human states: preparing → confirm in wallet → processing → done / failed |
| Errors | Actionable copy + support link; no raw revert hex to user |
| Limits | Per-day spend, withdrawal, sponsored tx caps |
| Privacy | What is public on-chain vs private in app |
| Accessibility | Mobile tap targets, screen reader for critical flows |
| Performance | Target time-to-interactive; skeleton states |

**Notification matrix**

| Event | Channel | User control (opt-out?) |
|-------|---------|-------------------------|
| Tx confirmed | | |
| Price alert | | |
| Social mention | | |
| Marketing | | |

---

## 5. Growth & economy (consumer)

| Mechanic | PM checks |
|----------|-----------|
| Referral | Sybil resistance, cap, disclosure |
| Points | Off-chain vs on-chain; redemption rules |
| Streaks / boosts | Repair, inflation, partner liability |
| Airdrop eligibility | Snapshot transparency, farming abuse |
| Paid ads claim | No guaranteed returns |

If tradable token or NFT reward → run [tokenomics-checklist.md](tokenomics-checklist.md).

---

## 6. Agent-assisted consumer (if applicable)

| Requirement | Detail |
|-------------|--------|
| Disclosure | User knows agent can sign within policy |
| Scope | Allowlisted contracts, max spend, time box |
| Revoke | One-tap disable agent / session key |
| Audit | Activity feed human-readable |
| Failure | Agent stops; user manual fallback |

Do not spec “full autonomous trading” without explicit risk review and compliance gate.

---

## 7. Compliance & trust (consumer)

| Surface | Requirement |
|---------|-------------|
| Custody | Who holds keys; insurance claims accurate |
| Minors | Age gate if rewards or purchases |
| Gambling-like loops | Loot box odds if regulated markets |
| Marketing | Influencer/KOL claims review |
| Data | Wallet linked to PII — privacy policy alignment |

---

## 8. Metrics (consumer)

| Metric | Definition |
|--------|------------|
| WAU / MAU | App open, not only on-chain tx |
| Funded wallets | First inbound value threshold |
| Activation | First core action within 24h |
| Retention | D1/D7/D30 cohort |
| Support rate | Tickets per 1k WAU |
| NPS / CSAT | Survey cadence |

Separate **app analytics** from **on-chain**; reconcile in strategy memo.

---

## 9. Pre-ship consumer checklist

- [ ] Onboarding tested on fresh device + fresh wallet
- [ ] Error copy reviewed without jargon
- [ ] Sponsored gas budget exhaustion path
- [ ] Push/email opt-in compliant with platform rules
- [ ] UGC moderation path if applicable
- [ ] Kill conditions wired (retention, cost per activated user)

---

## Out of scope

- App Store / Play policy full legal review
- Game economy Monte Carlo simulation
- Brand / visual design system
