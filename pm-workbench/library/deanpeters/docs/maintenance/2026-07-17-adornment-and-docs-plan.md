# Adornment & Documentation Plan — Market Intelligence Suite (Jul 17, 2026)

Four plans, executed in order. Plan 1 adorns the 15 bare/incomplete skills from the
v0.83 release with `template.md` + `examples/`. Plan 2 surfaces the suite in the
README and docs, which currently do not mention it at all. Plan 3 gives every
adorned skill dual-domain examples (SaaS + industrial) and bakes the
template-plus-two-examples standard into the repo's own authoring instructions.
Plan 4 backfills the dual-domain standard across the eligible back catalog.

**Status legend:** `[ ]` pending · `[x]` done

---

## Findings that motivated this plan

- All 14 new v0.83 skills shipped with only `METHOD.md` — no `template.md`, no `examples/`.
- `company-intel/examples/` is an **empty directory** — effectively bare too.
- Library norms: workflows and components ship template + examples (see
  `roadmap-planning`, `discovery-process`, 19/24 components); recent interactives
  ship a conversation-flow example (`incoming-request-advisor`).
- README gaps: no v0.83 entry in "What's New" (stops at v0.82); the entire
  market-intelligence category is absent from "What You Can Get Done"; section
  header still reads "52 Skills, 3 Types" with tier counts 6/23/23 (actual
  19 workflow / 27 interactive / 24 component); no themed pack for the suite.

---

## Plan 1 — Adornment (15 skills, 4 waves) — ✅ COMPLETE (Jul 17, 2026)

**Organizing idea:** one shared fictional market runs through the whole suite so
the chained examples literally feed each other — the landscape-scan example
output is the input to the snapshot example, and so on down to the battle card.
That demonstrates the diffable-schema contract instead of just describing it.

**Fictional market (fresh surrogate universe, SaaS-flavored so pricing pages,
release notes, and PM job postings read naturally):** field service management
(FSM) software for mid-market trades.
- **Fieldlight** — "our" company, the perspective the examples are written from
- **Wrenchline** — legacy incumbent
- **DispatchCrow** — fast-moving startup
- **Vantiga FSM** — enterprise suite player

`company-intel` keeps the existing industrial surrogate universe (Helix Motion
Systems, Northfield Automation, Corvid Industrial, Brightwater Biologics).
All names are fictional per the customer-anonymization protocol. Never reuse a
real vendor name.

**Templates are extracted, not invented** — each `template.md` is the diffable
output schema already defined in the skill's Application section, with
Fact/Inference/Assumption label slots where the skill calls for them, plus a
"quality checks before you call it done" close.

### Wave 1 — The chain (schemas lock first)
- [x] `market-landscape-scan` — template.md + examples/sample.md
- [x] `competitive-research-snapshot` — template.md + examples/sample.md (consumes the scan example)
- [x] `competitive-intel-watch` — template.md + examples/sample.md (diffs the snapshot example; confirms one of its Assumptions)
- [x] `battle-card-builder` — template.md + examples/sample.md (rebuilt from the watch example's update flags)

### Wave 2 — Standalone investigation workflows
- [x] `swot-analysis` — template.md + examples/sample.md (Wrenchline, synthesized from session evidence)
- [x] `porters-five-forces` — template.md + examples/sample.md (FSM industry structure)
- [x] `ansoff-matrix` — template.md + examples/sample.md (honestly empty diversification quadrant)
- [x] `pestel-delta-monitor` — template.md + examples/sample.md (two broken assumptions traced to baseline entries)
- [x] `voice-of-customer-miner` — template.md + examples/sample.md (frequency honesty caps a theme at low confidence)
- [x] `pricing-packaging-tracker` — template.md + examples/sample.md (both material moves structural, no price change)

### Wave 3 — Protocol, umbrella, disciplines
- [x] `competitive-analysis-process` — template.md (seven-step engagement tracker) + examples/sample.md (orchestration transcript linking into the delegated skills' examples). **Bonus fix:** Step 3's stale "voice-of-customer-miner lands in a future wave" note replaced with the real delegation + References entry.
- [x] `autonomous-investigation` — template.md (investigation brief: the contract's 7 clauses as fill-in decisions) + examples/protocol-in-action.md (gate revision, gaps list, unattended rerun)
- [x] `intelligence-collection-disciplines` — template.md (collection-plan worksheet) + examples/sample.md (4 disciplines run, 3 consciously skipped, fusion verdict)

### Wave 4 — Interactive + cleanup
- [x] `intel-discipline-advisor` — examples/conversation-flow.md + template.md (one-page triage card)
- [x] `company-intel` — examples/executive-signal-refresh.md fills the empty examples/ dir (Then/Now, Dropped Language, quiet graded)

### Wave closes
- [x] `scripts/test-a-skill.sh --smoke` — all 15 pass, 0 warnings
- [x] `scripts/test-library.sh` — all green (1 pre-existing warning on incoming-request-advisor, unrelated); catalogs regenerated
- [x] Anonymization sweep — all example content fictional; no real vendor names
- [x] METHOD.md cross-links added: each skill's schema section points to its template.md, each Examples section points to its examples file (the `incoming-request-advisor` precedent)

### After Plan 2 (deferred deliberately)
- [x] Rerun `scripts/build-dist.sh` — done at the end of Plan 2 (Jul 17); ZIPs carry the new templates/examples and `dist/packages/` includes `06-market-intel-pack.zip`.

---

## Plan 2 — Documentation surfacing — ✅ COMPLETE (Jul 17, 2026)

1. [x] **README "What You Can Get Done"** — add a "Market & competitive
   intelligence" block. Flagship links: `competitive-analysis-process` (umbrella),
   the four-skill chain on one line, `intel-discipline-advisor` (entry point),
   `tam-sam-som-calculator` (autonomous-research mode). Highest-leverage fix —
   the suite is invisible in the primary nav today.
2. [x] **README "What's New"** — write the missing v0.83 entry: 14 skills +
   2 upgrades, Fact/Inference/Assumption vocabulary, link to
   `docs/announcements/2026-07-17-v0-83-market-intelligence-suite.md`.
3. [x] **README staleness** — "52 Skills, 3 Types" → 70; tier diagram counts →
   19/27/24. (Badge, banner, and dist/README already say 70 — header + diagram only.)
4. [x] **`docs/Market Intelligence Suite Summary.md`** — new doc mirroring the
   `Finance Suite Summary.md` precedent: chain diagram, eight disciplines,
   when-to-use-which triage, how the two upgrades fit. Link from README Docs section.
5. [x] **Themed pack** — market-intel pack in `scripts/build-claude-desktop-packs.sh`,
   row in README packs table, note in `docs/RELEASE-PACKAGING.md`.
6. [x] **Sweep secondary docs** — `Using PM Skills 101.md`,
   `PM Skills Rule-of-Thumb Guide.md`, `docs/CHANGELOG.md` for category
   enumerations that predate the suite.
7. [x] **Regenerate `dist/`** — the single deferred `build-dist.sh` run from Plan 1.

**Sequencing rationale:** adorn first, document second — the suite summary can
then link to templates/examples that exist, and `dist/` regenerates exactly once.

---

## Plan 3 — Dual-domain examples + authoring standard — ✅ COMPLETE (Jul 17, 2026)

**Why:** a skill demonstrated only in a SaaS market quietly teaches "this is a SaaS
technique," and vice versa. PMs in industrial, hardware, and regulated businesses are
exactly the readers the ladder should reach — the disciplines compendium already
teaches MASINT/customs/facility signals that only shine outside SaaS. Two worked
examples from different domains prove the framework generalizes and double the
chance a reader sees their own business on the page.

### 3a. Add the missing domain example per adorned skill

The Plan 1 examples used one fictional universe each. Add the complementary domain:

**SaaS-only today (Fieldlight/Wrenchline FSM universe) → add an industrial example**
(reuse the established industrial surrogates — Helix Motion Systems, Northfield
Automation, Corvid Industrial, Brightwater Biologics — so the two universes stay
consistent repo-wide):
- [x] `market-landscape-scan`
- [x] `competitive-research-snapshot`
- [x] `competitive-intel-watch`
- [x] `battle-card-builder`
- [x] `swot-analysis`
- [x] `porters-five-forces`
- [x] `ansoff-matrix`
- [x] `pestel-delta-monitor`
- [x] `voice-of-customer-miner`
- [x] `pricing-packaging-tracker`
- [x] `competitive-analysis-process`
- [x] `autonomous-investigation`
- [x] `intelligence-collection-disciplines` (the industrial example is where MASINT/customs/facility chains finally get to star)
- [x] `intel-discipline-advisor` (second conversation flow, industrial situation)

**Perspective company (DECIDED):** industrial chain examples are written from **Northfield
Automation**'s seat, investigating Helix Motion Systems, Corvid Industrial, and Meridian Freight
Systems (already fictional in the disciplines compendium) in the retrofit-automation market; the
industrial watch example reads the same Helix "Foresight" event the `company-intel` refresh
documents — the universes interlock.

**Industrial-only today → add a SaaS example:**
- [x] `company-intel` (second refresh example on a fictional SaaS company — new SaaS surrogate or one of the Fieldlight-universe vendors)

Conventions (DECIDED): existing example files keep their names; added domain examples get a
domain suffix (`sample-industrial.md`, `executive-signal-refresh-saas.md`); every file
keeps the "all fictional" declaration and the closing "Why this example works"
teaching block; chain examples in the industrial universe should chain too, mirroring
the FSM set.

### 3b. Bake the standard into the repo's own instructions

New skills should **optimally** ship: `template.md` + a SaaS-domain example + an
industrial/non-SaaS-domain example. Frame as the quality bar, not a hard gate
(interactive advisors may substitute a conversation-flow example per domain).

- [x] `CLAUDE.md` — add to Skill Anatomy notes + Quality Checklist ("Does the skill
  ship a template and examples from two business domains?")
- [x] `CONTRIBUTING.md` — same standard in the contributor checklist, with the why
  (single-domain examples quietly narrow who the skill teaches)
- [x] `docs/Building PM Skills.md` — authoring guide section
- [x] `skills/skill-authoring-workflow/METHOD.md` and `skills/pm-skill-creator/METHOD.md` —
  the meta-skills that generate new skills must prompt for both domains
- [x] `scripts/build-a-skill.sh` / `scripts/add-a-skill.sh` — check whether the wizards'
  example steps should prompt for a second domain (doc-level nudge at minimum)
- [x] Smoke-check candidate — DECIDED: no validator rule. The standard has judgment-based
  exemptions (definitionally-SaaS, career skills) a script can't adjudicate; it lives in the
  CLAUDE.md/CONTRIBUTING checklists instead

### Close
- [x] Smoke tests + anonymization sweep on all touched skills
- [x] Regenerate `dist/` once — done Jul 17; industrial examples ship in all 70 ZIPs

---

## Plan 4 — Library-wide dual-domain backfill (execute after Plan 3)

**Why:** a keyword scan (Jul 17) of the ~36 back-catalog skills with examples found
essentially the entire set SaaS-flavored or domain-neutral — only `proto-persona`
shows any industrial vocabulary. The "single-domain examples quietly narrow who the
skill teaches" problem applies to most of the library, not just the intel suite.
Plan 4 brings the back catalog up to the standard Plan 3b writes down.

**Carve-outs (do NOT retrofit — and say why in commit messages so a future session
doesn't "fix" them):**
- **Definitionally SaaS:** `saas-revenue-growth-metrics`, `saas-economics-efficiency-metrics`,
  and the finance advisors built on SaaS metrics (`feature-investment-advisor`,
  `finance-based-pricing-advisor`, `acquisition-channel-advisor`, `business-health-diagnostic`,
  `finance-metrics-quickref`) — an industrial example would be forced. Judgment call per
  skill: some finance concepts (payback, margin) do generalize; add only where honest.
- **Domain-agnostic career/leadership:** `altitude-horizon-framework`,
  `director-readiness-advisor`, `vp-cpo-readiness-advisor`, `executive-onboarding-playbook`,
  `product-sense-interview-answer` — examples are about role transitions, not markets.

**In scope (~28-30 skills):** the craft/framework skills where an industrial example
proves generality — `roadmap-planning`, `discovery-process`, `prd-development`,
`product-strategy-session`, `jobs-to-be-done`, `positioning-statement`,
`problem-statement`, `problem-framing-canvas`, `user-story` (+ mapping/splitting),
`epic-hypothesis`, `opportunity-solution-tree`, `lean-ux-canvas`, `customer-journey-map`,
`proto-persona`, `storyboard`, `press-release`, `eol-message`, `pol-probe`,
`pestel-analysis`, `tam-sam-som-calculator`, `company-research`, `organic-growth-advisor`,
`recommendation-canvas`, `incoming-request-advisor`, `discovery-interview-prep` (currently
bare — gets full adornment), the stakeholder trio, and remaining bare interactives as
judged per skill.

**Conventions:** reuse the two established fictional universes (Fieldlight FSM = SaaS,
Helix/Northfield/Corvid/Brightwater = industrial); follow whatever file-naming decision
Plan 3 makes; every example keeps the fictional declaration and a "Why this example
works" close.

- [ ] Batch the work by theme (delivery, discovery, strategy, stakeholder) — one PR-sized
  commit per batch, smoke-tested
- [ ] Final `dist/` regen + catalog rebuild after the last batch
