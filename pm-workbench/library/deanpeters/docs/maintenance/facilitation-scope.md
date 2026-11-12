# Facilitation Scope Maintenance

## Why This Exists

Facilitation behavior is shared. If it breaks in one guided skill, it is usually broken everywhere that inherits the same protocol.

Use this file to quickly identify impacted skills and apply repo-wide fixes consistently.

## Canonical Source Of Truth

- `skills/workshop-facilitation/METHOD.md`

Core rule to preserve:
- Regular context/scoring questions should offer quick-select numbered options (include `Other (specify)` when useful).
- Numbered recommendations are for decision points only.

## How To Find Impacted Skills

Run:

```bash
rg -l "workshop-facilitation/METHOD.md" skills/*/METHOD.md | sort
```

This is the authoritative scope query. Do not rely only on static lists.

## Current Scope Snapshot (2026-02-11)

These files currently reference the facilitation source:

- `skills/acquisition-channel-advisor/METHOD.md`
- `skills/ai-shaped-readiness-advisor/METHOD.md`
- `skills/business-health-diagnostic/METHOD.md`
- `skills/context-engineering-advisor/METHOD.md`
- `skills/customer-journey-mapping-workshop/METHOD.md`
- `skills/discovery-interview-prep/METHOD.md`
- `skills/discovery-process/METHOD.md`
- `skills/epic-breakdown-advisor/METHOD.md`
- `skills/feature-investment-advisor/METHOD.md`
- `skills/finance-based-pricing-advisor/METHOD.md`
- `skills/lean-ux-canvas/METHOD.md`
- `skills/opportunity-solution-tree/METHOD.md`
- `skills/pol-probe-advisor/METHOD.md`
- `skills/positioning-workshop/METHOD.md`
- `skills/prd-development/METHOD.md`
- `skills/prioritization-advisor/METHOD.md`
- `skills/problem-framing-canvas/METHOD.md`
- `skills/product-strategy-session/METHOD.md`
- `skills/roadmap-planning/METHOD.md`
- `skills/skill-authoring-workflow/METHOD.md`
- `skills/tam-sam-som-calculator/METHOD.md`
- `skills/user-story-mapping-workshop/METHOD.md`

## Update Checklist

1. Edit `skills/workshop-facilitation/METHOD.md` first.
2. Run the scope query and patch affected skills when local wording may drift.
3. Sanity-check for contradictory language:

```bash
rg -n "numbered recommendations each turn|numbered recommendations at decision points" skills/*/METHOD.md
```

4. Run conformance checks on changed skills:

```bash
python3 scripts/check-skill-metadata.py <changed-skill-paths...>
```

