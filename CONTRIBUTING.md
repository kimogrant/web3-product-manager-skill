# Contributing

Thank you for improving Web3 Product Manager Skills.

## What to contribute

- Clearer phase or gate instructions in `references/`
- Additional **examples** (redacted real patterns preferred)
- Tokenomics, compliance, or chain-specific checklists (keep factual; cite sources)
- Install / agent compatibility notes in `docs/`

## Skill authoring rules

1. **One folder per skill** under `skills/<name>/` with `SKILL.md` at the root of that folder.
2. **`name` in frontmatter** must match the folder name (lowercase, hyphens).
3. **`description`** — third person, includes WHAT and WHEN (trigger phrases).
4. Keep main `SKILL.md` under **500 lines**; move detail to `references/`.
5. Do not embed secrets, API keys, or wallet addresses in examples.
6. English only for skill canon unless adding a separate localized mirror is explicitly requested.

## Pull request checklist

- [ ] Both skills still install via `./skill.sh install` to a temp directory
- [ ] `python tests/test_layout.py` passes
- [ ] New reference files linked from the parent `SKILL.md`
- [ ] `VERSION` bumped for user-facing behavior changes (semver)

## Local checks

```bash
python tests/test_layout.py
python tests/test_quality.py
./skill.sh list
```

## Scope we avoid

- Legal advice presented as definitive jurisdiction guidance
- Guaranteed token price or yield claims
- Copy-paste of proprietary third-party playbooks without permission
