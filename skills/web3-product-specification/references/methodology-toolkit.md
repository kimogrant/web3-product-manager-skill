# Methodology toolkit (on-demand)

Load **only when trigger signals match**. Do not run all methods by default.

| ID | Method | Layer | Typical trigger |
|----|--------|-------|-----------------|
| M1 | Opportunity Solution Tree (OST) | Strategy | Competing solution directions; skipping problem validation |
| M2 | Pioneers, Settlers, Outlaws (PoL) probe | Strategy | High-risk assumptions; technical path fork before Gate 0 |
| M3 | Epic hypothesis | Specification | Epic lacks measurable outcome |
| M4 | User story splitting | Specification | Story spans roles/scenarios; repeatedly deprioritized |

---

## M1: Opportunity Solution Tree (OST)

**When:** Team jumps to “how to build” before agreeing on the outcome.

**Steps:**

1. **Outcome** — One measurable product outcome (not a feature list).
2. **Opportunities** — 3–5 user needs / pain points that drive the outcome.
3. **Solutions** — 2–3 options per opportunity (include “do nothing”).
4. **Experiments** — Cheapest test per top solution (interview, prototype, on-chain pilot).

**Output (append to strategy memo or Phase 3):**

```markdown
## OST snapshot
Outcome: …
| Opportunity | Solutions considered | Preferred experiment |
|-------------|----------------------|----------------------|
```

**Exit:** User picks one solution branch to carry into specification.

---

## M2: PoL probe (assumption map)

**When:** Unresolved technical or market assumptions block Gate 0.

**Steps:**

1. List **assumptions** (max 8) as “We believe X.”
2. Classify: **Pioneers** (unknown, must learn first) | **Settlers** (known space, execute) | **Outlaws** (contrarian bet).
3. For each Pioneer: define **probe** (time-boxed, <1 week), success/fail signal.
4. Do not enter Gate 2 until Pioneer probes are **running** or explicitly accepted as risk.

**Output:**

| Assumption | Class | Probe | Signal |
|------------|-------|-------|--------|
| | P/S/O | | |

---

## M3: Epic hypothesis

**When:** Gate 2 epic has no verifiable success criteria.

**Template:**

```markdown
## Epic hypothesis: [name]
We believe that [change] for [persona] will result in [metric delta]
by [date]. We will know this when [measurement event].
```

**Checks:**

- [ ] Metric named in strategy memo or `PENDING` with owner
- [ ] Measurement is observable (on-chain or product analytics)
- [ ] Epic can be false — falsification stated

---

## M4: User story splitting

**When:** Story is too large, multi-role, or stuck in backlog.

**Split dimensions (pick 1–2):**

| Dimension | Example split |
|-----------|----------------|
| Workflow step | Connect vs approve vs submit |
| Role | LP vs borrower |
| Scenario | Happy path vs revert vs wrong chain |
| Data variant | First-time vs returning user |

**Rules:**

- Each child story ≤ 1 review session to specify
- Parent story ID retained (`US-014a`, `US-014b`)
- Do not split by “frontend vs backend” only — split by **user-visible progress**

**Output:** Updated story list in PRD §6 with traceability preserved.

---

## Invocation log (recommended)

| Method | Trigger seen? | Ran? | Artifact |
|--------|---------------|------|----------|
| M1 | Y/N | Y/N | link/section |
| M2 | Y/N | Y/N | |
| M3 | Y/N | Y/N | |
| M4 | Y/N | Y/N | |
