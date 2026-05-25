# PRD template — Web3 products

Use at Gate 2 onward. Link to confirmed strategy memo at top.

---

```markdown
# PRD: [Feature / initiative name]

| Field | Value |
|-------|-------|
| Version | 0.1 |
| Status | Draft / In review / Ready for engineering |
| Author | |
| Strategy memo | [link or filename] |
| Chains | |
| Target release | |

## 1. Summary

[Problem, solution, success metrics — from memo]

## 2. Goals & non-goals

### Goals

-

### Non-goals

-

## 3. Users & personas

| Persona | Needs | Wallet context |
|---------|-------|----------------|
| | | |

## 4. Context & ground truth (Gate 0)

[Audit summary; link screenshots/docs]

### Delta table

| Capability | Current | Target | Change |
|------------|---------|--------|--------|
| | | | |

## 5. Information architecture (Gate 1)

[Surface map, journeys]

## 6. Requirements (Gate 2)

### Epic: [name]

#### Story [ID]: [title]

**Layers**

| Layer | Specification |
|-------|---------------|
| Presentation & data | |
| Interaction | |
| Business & integration | |

**Acceptance criteria**

-

**Assumptions**

-

**Out of scope**

-

---

[Repeat per story]

## 7. Wallet & chain requirements

| Requirement | Detail |
|-------------|--------|
| Supported chains | |
| Wallet types | EOA / smart account / WC / embedded |
| Gas sponsorship | |
| Approvals | |
| Indexing / events | |

## 8. Failure & edge cases

| Scenario | Expected UX | Backend behavior |
|----------|-------------|------------------|
| Tx reverted | | |
| RPC timeout | | |
| Wrong network | | |
| Insufficient gas | | |
| Stale price / oracle | | |

## 9. Tokenomics appendix (Gate 2b)

[Link checklist or N/A]

## 10. Compliance & abuse surface (Gate 3)

[Link risk table or N/A]

## 11. Metrics & instrumentation

| Metric | Definition | Source | Owner |
|--------|------------|--------|-------|
| | | | |

## 12. Iteration plan (Gate 4)

| Slice | Scope | Exit criteria |
|-------|-------|---------------|
| | | |

## 13. Open questions

| ID | Question | Owner | Due |
|----|----------|-------|-----|
| | | | |

## 14. Approvals

| Role | Name | Date |
|------|------|------|
| PM | | |
| Engineering | | |
| Security (if on-chain) | | |
```

---

## PRD review checklist

- [ ] Traceable to strategy memo recommendation
- [ ] Non-goals prevent scope creep
- [ ] Each story has testable acceptance criteria
- [ ] No fabricated contract addresses or event names
- [ ] Tokenomics and compliance sections filled or N/A with reason
- [ ] Kill conditions from memo reflected in metrics section
