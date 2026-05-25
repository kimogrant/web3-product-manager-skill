# Example: PRD user story (fictional)

Shows **three-layer spec**, `(Source: SRC-n)` tags, and `TBD` for unknown chain facts.

**Context:** Follows [strategy-memo-sample.md](strategy-memo-sample.md). In a real PRD, SRC-2 = approved strategy memo.

---

## Source index (excerpt)

| ID | Description |
|----|-------------|
| SRC-2 | Approved strategy memo (Pilot, Base first swap) |
| SRC-7 | Paymaster vendor API draft (described) |
| SRC-8 | Competitor: Rabby first-tx sponsor UX screenshot (described) |

---

### US-014: First swap with sponsored gas

As a **new EOA user**, I want to complete my first swap without holding ETH for gas, so that I can experience core value in one session.

**Traceability:** `(Source: SRC-2, decision: Pilot scope)` `(Source: SRC-8, tier: first-party)` for sponsor badge pattern.

**Layers**

| Layer | Specification |
|-------|---------------|
| Presentation & data | Swap pair, estimated output, sponsor badge, pending/success/revert `(Source: SRC-8)` |
| Interaction | Connect → review → sign → track hash → success CTA |
| Business & integration | Paymaster: 1 sponsored tx / wallet / 30d `(Source: SRC-7)`; router `TBD` |

**Acceptance criteria**

- [ ] Given fresh EOA on Base, When qualifying swap completes, Then user gas not debited `(Source: SRC-2, metric K1)`
- [ ] Given sponsor exhausted for wallet, When retry, Then self-paid path with clear copy `(Source: SRC-7)`
- [ ] Given tx reverted, When user returns, Then explorer link + form state preserved
- [ ] Given wrong network, When connect, Then switch-to-Base prompt only

**Assumptions**

- Assumes paymaster SLA 99.5% `(Source: SRC-7)`. If false → default self-paid `(Source: SRC-2, A1)`.

**Dependencies**

- US-002 wallet connect; events `SwapExecuted` `TBD` (register SRC-9 when ABI confirmed)
