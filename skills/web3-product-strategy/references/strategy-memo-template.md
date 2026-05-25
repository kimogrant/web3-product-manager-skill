# Strategy memo template

Copy into the workspace or deliver as the Phase 4 artifact. Replace bracketed placeholders.

---

```markdown
# Strategy memo: [Decision title]

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Mode | Full / Express / Pulse |
| Recommendation | Build / Pilot / Defer / Kill |
| Owner | [PM name or role] |
| Reviewers | [names or teams] |

## Executive summary

[≤200 words: recommendation first, why now, key risk, opportunity cost]

## Decision statement

[One sentence describing what was decided]

## Context

- Target user / wallet persona:
- Chain(s) / environment:
- Product surface:
- Regulatory sensitivity: Low / Med / High

## Problem & opportunity (Track A summary)

[Bullets with source tags: (on-chain | report | first-party | sentiment)]

## Challenge summary (Track B summary)

[Strongest reasons not to build]

## Synthesis

### Confrontation highlights

[Where A and B disagreed; how resolved]

### Pre-mortem (top failures)

| Failure mode | Likelihood | Leading indicator | Mitigation |
|--------------|------------|-------------------|------------|
| | | | |

## Recommendation detail

### If Build or Pilot

- Scope in:
- Scope out:
- Pilot exit criteria (if Pilot):
- Success metrics (90d):

| Metric | Target | Source |
|--------|--------|--------|
| | | |

### Opportunity cost

[What pauses or deprioritizes if this proceeds]

## Assumptions & falsification

| ID | Assumption | Falsification signal | Monitor |
|----|------------|----------------------|---------|
| A1 | | | |

## Kill conditions

| ID | Condition | Threshold | Review date |
|----|-----------|-----------|-------------|
| K1 | | | |

## Open questions

| ID | Question | Owner | Due |
|----|----------|-------|-----|
| Q1 | | | |

## Handoff to specification

- [ ] Memo confirmed by: [name/date]
- Next skill: `web3-product-specification`
- Attach: [links to research, dashboards, competitor refs]
```

---

## Memo quality checklist

- [ ] Recommendation in first paragraph (S1)
- [ ] At least one on-chain or first-party anchor for chain-native products (S3)
- [ ] Trends include time window (S4)
- [ ] Opportunity cost stated (S5)
- [ ] ≥3 falsifiable assumptions (S6)
- [ ] Kill conditions measurable (S6)
- [ ] No fabricated statistics
