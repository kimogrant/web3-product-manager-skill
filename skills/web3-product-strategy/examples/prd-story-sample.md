# Example: PRD user story (fictional)

Pattern for Gate 2 three-layer spec. Contract names marked `TBD` intentionally.

---

### US-014: First swap with sponsored gas

As a **new EOA user**, I want to complete my first swap without holding ETH for gas, so that I can experience core value in one session.

**Layers**

| Layer | Specification |
|-------|---------------|
| Presentation & data | Show swap pair, estimated output, sponsor badge “Gas covered for first swap”, pending/success/revert states |
| Interaction | Connect wallet → select pair → review → sign permit (if used) → sign swap → track tx hash → success CTA to portfolio |
| Business & integration | Paymaster policy: one sponsored tx per wallet per 30d; router `TBD`; fallback message if sponsor exhausted |

**Acceptance criteria**

- [ ] Given fresh EOA on Base, When user completes qualifying swap, Then gas is not debited from user for that tx
- [ ] Given wallet already sponsored in window, When user retries, Then UI explains limit and offers self-paid path
- [ ] Given tx reverted, When user returns, Then error shows explorer link and preserved form state
- [ ] Given wrong network, When connect, Then prompt switch to Base only

**Assumptions**

- Assumes paymaster relayer SLA 99.5%. If false → show self-paid path by default.

**Dependencies**

- US-002 wallet connect, paymaster service `TBD`, indexer events `SwapExecuted` `TBD`
