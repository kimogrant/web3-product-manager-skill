# Gate 3.5: Prototype validation (conditional)

Load after **Gate 3** (or in parallel if no compliance trigger) and **before Gate 4**, when the team needs to **validate flows** before engineering lock-in.

**Not for:** pixel-perfect brand design or production frontend implementation.

---

## When required

| Trigger | Run Gate 3.5 |
|---------|----------------|
| New user journey or major IA change | Yes |
| Wallet / tx flow changed | Yes |
| Stakeholder needs “clickable” review | Yes |
| Pure backend / config change, no UX | N/A |

---

## Grounding (same as Gate 0)

- [ ] PRD §6 stories for in-scope flows are draft-complete
- [ ] Reference UI exists: Figma link, screenshots, or competitor walkthrough `(Source: SRC-n)`
- [ ] No invented field names or event types in prototype spec

---

## Prototype modes (pick one)

| Mode | Best for | Deliverable |
|------|----------|-------------|
| **Figma** | Design review, copy, layout | Linked frames + flow prototype |
| **HTML vibe** | Fast eng/PM test, wallet mocks | Static or local HTML in repo path |
| **Staging** | Existing app branch | URL + feature flag name |

Document chosen mode in PRD §7 (Prototype).

---

## Scope checklist

For each in-scope journey from Gate 1:

- [ ] Happy path clickable end-to-end (can be mocked chain)
- [ ] Error state represented (revert, wrong network, sponsor exhausted)
- [ ] Loading / pending state shown
- [ ] Copy matches PRD (no new promises)
- [ ] Wallet prompts labeled (connect, sign, approve)

---

## Review session

| Role | Question |
|------|----------|
| PM | Does this match PRD acceptance criteria? |
| Eng | Any impossible contract/API call shown? |
| Design (if any) | IA only — defer pixel specs |

Capture **delta list**: PRD change vs prototype change (prototype wrong → fix prototype; PRD wrong → update PRD before Gate 4).

---

## Output (PRD §7)

```markdown
## Prototype validation
- Mode: Figma | HTML | Staging
- Link / path: …
- Review date: …
- Outcome: Approved | Approved with PRD edits | Revisit Gate 1/2

### Deltas applied to PRD
- [ ] …
```

---

## Exit

- [ ] Prototype approved or PRD updated from deltas
- [ ] Checkpoint shows Gate 3.5 ✅ or N/A with reason
- [ ] Then proceed to Gate 4 iteration plan
