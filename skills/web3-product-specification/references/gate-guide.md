# Gate guide — Web3 Product Specification

Load for the active gate only. Requires confirmed strategy memo.

---

## Gate 0: Ground truth audit

**Goal:** Establish what exists before designing deltas.

### Audit checklist

| Area | Capture |
|------|---------|
| Product surfaces | Web, mobile, mini-app, bot, API |
| Wallet flows | Connect, sign, batch, AA, paymaster |
| Chains | Chain IDs, testnets, bridge paths |
| Contracts | Proxies, upgradeability, pausability |
| Indexing | Subgraph, indexer lag, fallback |
| Roles | Admin, keeper, guardian, multisig |
| Metrics baseline | From memo or `PENDING` |

### Delta table (start)

| Capability | Current | Target | Change type (extend/new/deprecate) |
|------------|---------|--------|-------------------------------------|
| | | | |

### Output

- Audit summary (≤1 page)
- List of `PENDING` with owner
- Updated delta table

**Exit:** User confirms audit accuracy or accepts listed `PENDING` risk.

---

## Gate 1: Information architecture & flows

**Goal:** Structure before field-level requirements.

### Deliverables

1. Sitemap or surface map (bullets acceptable)
2. Primary user journeys (max 5 for Express)
3. Wallet touchpoints per journey (connect, approve, sign, submit)
4. Error / recovery paths at journey level

### Web3 flow annotations

For each journey step involving chain:

- Chain + network
- Who pays gas
- Required approvals (token, permit2, setApprovalForAll)
- Expected confirmation UX (pending, success, reverted)

**Exit:** IA confirmed; no Gate 2 until confirmed.

---

## Gate 2: Three-layer requirements

**Goal:** Engineering-ready stories per feature/epic.

### Per feature document

Use layers from main `SKILL.md`:

1. **Presentation & data**
2. **Interaction**
3. **Business & integration**

### User story format

```markdown
### [ID] [Title]

As a [persona], I want [goal], so that [outcome].

**Acceptance criteria**
- [ ] Given … When … Then …
- [ ] Wallet: …
- [ ] On revert: …

**Assumptions:** Assumes … If false → …

**Dependencies:** [contracts, APIs, other stories]
```

### Dual validation (P5)

For each story ask:

1. **Exists?** Already partially in product?
2. **Necessary?** Smaller story achieves 80% value?

### Scene-shift test

Change one variable (chain, wallet type, amount near limit, RPC slow) — does spec still hold? If not, add criteria.

**Trigger Gate 2b** if tokenomics touched — see [tokenomics-checklist.md](tokenomics-checklist.md).

**Exit:** Stories reviewed; PRD skeleton populated from [prd-template.md](prd-template.md).

---

## Gate 2b: Tokenomics (conditional)

Run when any: token launch, emissions, fee switch, points, ve-model, governance weight, liquidity mining.

Load [tokenomics-checklist.md](tokenomics-checklist.md). Attach completed checklist to PRD appendix.

**Exit:** Checklist complete or explicit `N/A` with reason signed by user.

---

## Gate 3: Compliance & abuse (conditional)

Run when: user funds move, yield marketing, geo-restricted users, KYC, securities-like promises, third-party custody.

Load [compliance-surface.md](compliance-surface.md). Output risk table—not legal advice.

**Exit:** Surface documented; counsel review flagged if high sensitivity.

---

## Gate 4: Iteration plan

**Goal:** Shippable slices with acceptance and observability.

### Iteration table

| Slice | Stories | Outcome | Metrics | Rollback |
|-------|---------|---------|---------|----------|
| MVP | | | | |
| +1 | | | | |

### Observability

| Event / metric | Tool | Alert threshold |
|----------------|------|-----------------|
| | | |

### Definition of done (release)

- [ ] Spec reviewed by engineering
- [ ] Testnet / staging checklist (if on-chain)
- [ ] Runbook for incident (pause, comms)
- [ ] Kill conditions from strategy memo wired to dashboards

**Exit:** Plan confirmed; PRD marked `Ready for engineering`.

---

## Parallel workstreams

When multiple streams (e.g. frontend + contracts):

- One checkpoint file per `WORKSTREAM-ID`
- Shared Gate 0 audit; fork at Gate 1 if surfaces differ
- Merge PRD sections with clear ownership tags
