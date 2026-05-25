# Phase guide — Web3 Product Strategy

Load this file when executing Phases 1–5 of `web3-product-strategy`.

## Source traceability

1. In Phase 1, register inputs as `SRC-1`, `SRC-2`, … in a running **Source index** table.
2. In Phases 2–4, tag every material claim: `(Source: SRC-2, tier: on-chain, as-of: YYYY-MM-DD)`.
3. Synthesized conclusions list **all** contributing SRC IDs.
4. If no input supports a claim, tag `Implicit` and list in open questions—do not present as verified fact.
5. Attach the Source index to the memo handoff for `web3-product-specification`.

---

## Phase 1: Frame & reframe

**Outputs:** Decision brief (1 page max)

1. Restate the user’s ask in one decision sentence.
2. List 2–3 alternative framings (“Are we deciding X or Y?”).
3. Identify decision type: new product | major feature | optimization | response to competitor.
4. Confirm mode (Full / Express / Pulse) and time budget.
5. Capture constraints and regulatory sensitivity (low / med / high).
6. Open **Source index** — assign `SRC-1` to user brief; reserve `SRC-2+` for artifacts.

**Reframe check (S7):** If the team is debating implementation before validating the problem, pause and document the problem hypothesis separately.

**Checkpoint:**

```markdown
Phase 1 complete | Mode: [Full|Express|Pulse]
Decision: [one sentence]
Reframe options: [bullets]
Open questions: [max 5]
Proceed to Phase 2? (await user)
```

---

## Phase 2: Parallel evidence

Run **Track A (build case)** and **Track B (challenge case)** independently.

### Track A — Opportunity

| Area | Questions | Evidence tier |
|------|-----------|---------------|
| Problem | Who hurts today? How often? | First-party / on-chain |
| Market | TAM/SAM credible range | Reports + on-chain |
| Timing | Why now? Catalysts? | Time-boxed (S4) |
| Solution fit | Why us vs alternatives? | Product + competitive |
| Economics | Revenue or value capture path | Model + comparables |

### Track B — Challenge

| Area | Questions |
|------|-----------|
| Demand | Is pain acute or narrative-only? |
| Competition | Incumbent response? Commoditization? |
| Execution | Team, audit, liquidity, distribution gaps? |
| Regulation | What kills launch in target geos? |
| Incentives | Mercenary capital, farm-and-dump risk? |

Use [data-sources.md](data-sources.md) for source priority.

**Domain lenses (optional, Phase 2):** If the decision is clearly DeFi, L2, or Consumer, load the matching specialist reference from the specification skill for benchmark and risk prompts:

| Domain | File (sibling skill — install both) |
|--------|-------------------------------------|
| DeFi | `.cursor/skills/web3-product-specification/references/defi-product-surface.md` |
| L2 | `.cursor/skills/web3-product-specification/references/l2-product-surface.md` |
| Consumer | `.cursor/skills/web3-product-specification/references/consumer-product-surface.md` |

**Rules:**

- No shared draft conclusions between tracks until Phase 3.
- Every quantitative claim: `value + source + as-of date`.
- Unknown → `PENDING`, not estimates presented as facts.

**Checkpoint:** Summarize A and B in separate sections; list top 5 conflicts between tracks.

---

## Phase 3: Synthesis

### 3.1 Confrontation matrix

| Dimension | Track A | Track B | Resolution |
|-----------|---------|---------|------------|
| Demand | | | |
| Timing | | | |
| Moat | | | |
| Risk | | | |

### 3.2 Pre-mortem (12 months forward, project failed)

List 6–10 failure causes including uncomfortable ones (team, legal, liquidity, oracle, bridge, key person).

For each: likelihood (L/M/H), leading indicator, mitigation.

### 3.3 Kill conditions (S6)

Each kill condition must be:

- Observable on-chain or in product analytics when possible
- Time-bound or threshold-based
- Owned (who monitors)

Example pattern: “If 90d retained funded wallets < X after launch, pause emissions review.”

### 3.4 Recommendation draft

Choose one: **Build** | **Pilot** | **Defer** | **Kill**

Include opportunity cost (S5): what stops if this proceeds.

**Checkpoint:** Present recommendation + kill conditions; await user pushback before Phase 4.

**Methodology triggers (Phase 2–3):**

| Signal | Load |
|--------|------|
| Competing solution directions | `methodology-toolkit.md` **M1** (sibling specification skill path) |
| High-risk assumptions before build | **M2** |

Path: `.cursor/skills/web3-product-specification/references/methodology-toolkit.md`

---

## Phase 4: Strategy memo

Produce using [strategy-memo-template.md](strategy-memo-template.md).

**Quality bar:**

- Executive summary ≤ 200 words
- Self-contained for a reader without prior chat context
- Assumptions table with falsification signals
- Explicit Pilot scope if not full Build

**Human gate:** Ask: “Confirm memo to proceed to specification?”  
Only continue to `web3-product-specification` after explicit confirmation.

---

## Phase 5: Track & retrospective (post-ship)

Optional; run after launch or pilot end.

| Item | Action |
|------|--------|
| Kill conditions | Status vs thresholds |
| Assumptions | Confirmed / falsified |
| Memo accuracy | What was wrong; update playbook |
| Next decision | Iterate, scale, or sunset |

Document learnings in 5–10 bullets; do not rewrite history of the original memo silently.

---

## Pulse mode shortcut

| Phase | Pulse behavior |
|-------|----------------|
| 1 | Required (compressed) |
| 2 | 3 bullets A, 3 bullets B; on-chain only if decision is chain-native |
| 3 | Top 3 risks + recommendation |
| 4 | Half-page memo |
| 5 | Skip unless user asks |
