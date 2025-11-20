# TBTA Migration Plan - Complete TODO Resolution

**Created**: 2025-11-14
**Objective**: Systematically complete all 26 TODOs in bible-study-tools/tbta/
**Approach**: Dependency-aware, parallel-optimized, audit-ready execution

## Executive Summary

This plan resolves all 26 TODOs identified in the TBTA structure through 4 coordinated phases:
- **Phase 1**: Critical file updates (STAGES.md, README.md) - SEQUENTIAL, blocks all feature work
- **Phase 2**: Independent documentation creation - PARALLEL execution (8 files)
- **Phase 3**: Integration and cross-references - SEQUENTIAL, requires Phase 2 complete
- **Phase 4**: Feature migration and standardization - PARALLEL by tier (29 features)

**Total TODOs**: 26 identified + audit checklist items
**Estimated Time**: 6-8 hours focused work
**Success Criteria**: All checkboxes complete, audit passed, git committed

---

## Dependency Graph

```
PHASE 1 (CRITICAL PATH - BLOCKS ALL)
├─ STAGES.md update (500 lines methodology)
│  └─ Blocks: All feature work, template creation
└─ README.md coverage fix
   └─ Blocks: tbta-source/COVERAGE.md, documentation claims

PHASE 2 (PARALLEL EXECUTION)
├─ tbta-source/ population (8 files) [Independent]
├─ 3 key examples addition [Uses corrected README.md]
└─ OT/NT structure documentation [Independent research]

PHASE 3 (INTEGRATION)
├─ Cross-reference verification [Requires Phase 1+2]
├─ Progressive disclosure validation [Requires Phase 2]
└─ Template consolidation [Requires STAGES.md from Phase 1]

PHASE 4 (FEATURE MIGRATION)
└─ 29 features standardization [Requires STAGES.md, templates from Phase 3]
   ├─ Tier A features (19) - Priority 1
   ├─ Tier B features (20) - Priority 2
   └─ Tier C features (20) - Priority 3
```

---

## Memory Continuity Strategy

### Entry Point Document
**Primary**: `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/README.md`

All subagents MUST:
1. Load README.md first on initialization
2. Follow references to specific subdirectory READMEs
3. Load only files referenced in those READMEs
4. Store findings in hive memory with keys: `hive/{agent-type}/{topic}`

### Context Restoration Protocol
```bash
# Every subagent starts with:
1. Read bible-study-tools/tbta/README.md
2. Identify relevant section (tbta-source/, features/, languages/, learnings/)
3. Read subdirectory README.md
4. Load specific files as directed
5. Execute task
6. Store results in hive memory
```

---

## Phase 1: Critical File Updates (SEQUENTIAL)

**Duration**: 1-2 hours
**Blocks**: All subsequent phases
**Execution**: Must be done first, in order

### Task 1.1: Update STAGES.md with 500+ lines of methodology
**File**: `bible-study-tools/tbta/features/STAGES.md`
**Source**: `plan/tbta-rebuild-with-llm/features/STAGES.md`
**Changes**:
- Add Stage 4 dataset requirements (~220 lines)
  - Sample size minimums (100 verses)
  - Statistical power warnings
  - Balanced sampling (OT/NT, genres, difficulty)
  - Adversarial selection strategy
  - Enhanced YAML schema
- Add Stage 5 improvements (~180 lines)
  - Locked predictions protocol (git commit before testing)
  - 6-step error analysis process
  - External validation section
  - Iterative refinement guidance
- Add Stage 6 enhancements (~350 lines)
  - Structured subagent validation
  - 4 specialized peer reviewers (theological, linguistic, methodological, translation practitioner)
  - TBTA-REVIEW.md template
  - TRANSLATOR-IMPACT.md template
  - Production readiness checklist
- Remove resolved TODOs (lines 3, 7, 8, 13, 26, 28)
- Update cross-references

**Dependencies**: None
**Blocks**: All feature migration, template work
**Verification**: File size ~600 lines, all TODOs resolved, cross-references valid

### Task 1.2: Fix coverage claim in README.md
**File**: `bible-study-tools/tbta/README.md`
**Changes**:
- Line 5: Change "31,102 Bible verses" → "11,649 verses across 34 books (~37% of Bible)"
- Add note: "TBTA intentionally focuses on narrative and discourse-heavy books where cross-linguistic features matter most"
- Update tbta-source/COVERAGE.md reference to confirm it exists (will be created in Phase 2)
- Mark TODO complete: "[TODO: confirm this claim...]"

**Dependencies**: None
**Blocks**: tbta-source/COVERAGE.md creation
**Verification**: Accurate numbers, no false claims

### Task 1.3: Add 3 key examples to README.md
**File**: `bible-study-tools/tbta/README.md`
**Location**: After line 7
**Content**: 3 concrete examples showing why TBTA features matter:
- Example 1: Clusivity (Genesis 1:26 - trial number, affects 172 Austronesian languages)
- Example 2: Participant tracking (Genesis 4:8 - ambiguous referent, affects discourse clarity)
- Example 3: Time granularity (Genesis narratives - 20+ values, affects chronological understanding)

**Source**: `plan/tbta-analysis.md` lines 146-375
**Dependencies**: None (can use existing research)
**Blocks**: None
**Verification**: Examples are concrete, show real translation impact

---

## Phase 2: Independent Documentation (PARALLEL)

**Duration**: 2-3 hours
**Blocks**: Phase 3 (integration)
**Execution**: Can run 8 tasks in parallel

### Task 2.1: Create tbta-source/COVERAGE.md
**Dependencies**: Task 1.2 (README.md coverage fix)
**Source**: `plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md`
**Content**:
- Actual coverage: 11,649 verses, 34 books, ~37%
- List of covered books (20 OT, 14 NT)
- Intentional focus explanation
- Link to data-coverage-analysis.md for details

**Verification**: Numbers match README.md, all books listed

### Task 2.2: Create tbta-source/TBTA-FEATURES.md
**Dependencies**: None (independent research)
**Source**: `plan/tbta-comprehensive-review.md` lines 40-250
**Content**:
- Confirm 59 features across 15 categories
- Three-tier structure (Tier A: 19, Tier B: 20, Tier C: 20)
- For each feature: name, values, languages affected, status (✅/🟨/⬜)
- Coverage percentages per tier

**Verification**: All 59 features enumerated, accurate status

### Task 2.3: Create tbta-source/TRANSLATION-EDGE-CASES.md
**Dependencies**: None
**Source**: `plan/tbta-analysis.md` lines 146-375
**Content**: 6 concrete examples with full analysis

**Verification**: Examples show real translation challenges

### Task 2.4: Create tbta-source/ACCURACY-RESULTS.md
**Dependencies**: None
**Source**: `plan/tbta-comprehensive-review.md` lines 326-333
**Content**: Validation results for tested features (80-100% accuracy)

**Verification**: Results are honest, methodology documented

### Task 2.5: Create tbta-source/DATA-ACCESS.md
**Dependencies**: None
**Source**: `plan/tbta-rebuild-with-llm/tbta-data/README.md`
**Content**: How to access TBTA data, file naming, parsing examples

**Verification**: Instructions are actionable

### Task 2.6: Create tbta-source/METHODOLOGY.md
**Dependencies**: None
**Source**: `plan/tbta-comprehensive-review.md` lines 497-520
**Content**: Breakthrough discoveries and methodology insights

**Verification**: Insights are specific and actionable

### Task 2.7: Create tbta-source/CRITIQUE.md
**Dependencies**: None
**Source**: `plan/tbta-rebuild-with-llm/combined/IMPROVEMENTS.md` (validate first)
**Content**: Constructive critiques of TBTA, validated and not made-up

**Verification**: Critiques are evidence-based, not speculation

### Task 2.8: Document OT/NT structural differences
**File**: To be determined (README.md or structure/README.md)
**Dependencies**: None (independent research)
**Content**: Explain how TBTA divides OT vs NT, how to align with myBibleToolbox verse-based structure

**Verification**: Clear explanation, actionable for implementation

---

## Phase 3: Integration and Cross-References (SEQUENTIAL)

**Duration**: 1 hour
**Dependencies**: Phases 1 and 2 complete
**Execution**: Must verify all links work

### Task 3.1: Verify all cross-references
**Action**: Audit all markdown links in TBTA directory
**Tools**: `grep -r "\[.*\](.*)" bible-study-tools/tbta/`
**Verification**: All links resolve, no broken references

### Task 3.2: Progressive disclosure validation
**Action**: Check all .md files against line limits
**Criteria**:
- READMEs: ≤500 lines (TBTA exception, document in features/README.md)
- Topic files: ≤400 lines
- Files >limits: Create subdirectory structure

**Verification**: All files compliant or exceptions documented

### Task 3.3: Create features/TEMPLATE.md
**Dependencies**: STAGES.md updated (Task 1.1)
**Content**: Consolidated best practices from:
- STAGES.md (authoritative)
- FEATURE-AUDIT-TEMPLATE.md (audit checklist)
- Progressive disclosure standards

**Verification**: Template is actionable, references STAGES.md

### Task 3.4: Update all README.md files with phase completions
**Files**:
- bible-study-tools/tbta/README.md (mark approach checklist items)
- bible-study-tools/tbta/tbta-source/README.md (link to new files)
- bible-study-tools/tbta/features/README.md (update with template info)
- bible-study-tools/tbta/languages/README.md (mark migration status)
- bible-study-tools/tbta/learnings/README.md (mark migration status)

**Verification**: All READMEs reflect current state

---

## Phase 4: Feature Migration (PARALLEL BY TIER)

**Duration**: 3-4 hours (can be split across sessions)
**Dependencies**: Phase 3 complete (STAGES.md, templates ready)
**Execution**: Parallel within tier, sequential across tiers

### Task 4.1: Audit 29 features using FEATURE-AUDIT-TEMPLATE.md
**Action**: Systematically audit each feature subdirectory
**Output**: Migration checklist with priorities

### Task 4.2: Migrate Tier A features (19 features)
**Priority**: HIGH (68% complete, high value)
**Method**: Standardize directory structure per STAGES.md
**Verification**: Each feature has:
- README.md (≤500 lines)
- experiments/train.yaml (100+ verses per value)
- experiments/test.yaml
- experiments/validate.yaml
- experiments/LEARNINGS.md (6-step error analysis)
- experiments/VALIDATION-RESULTS.md

### Task 4.3: Migrate Tier B features (20 features)
**Priority**: MEDIUM (15% complete)
**Method**: Same as Tier A
**Note**: May be incomplete, document status

### Task 4.4: Migrate Tier C features (20 features)
**Priority**: LOW (0-70% documented)
**Method**: Create scaffolding only
**Note**: Mark as "not started" in documentation

---

## Audit Checklist

### Pre-Execution Audit
- [ ] All dependencies identified correctly
- [ ] Parallel tasks are truly independent
- [ ] Memory continuity strategy documented
- [ ] Peer review plan in place

### Post-Phase 1 Audit
- [ ] STAGES.md has all 500+ lines integrated
- [ ] No TODOs remain in STAGES.md
- [ ] README.md has correct coverage numbers (11,649 verses)
- [ ] 3 key examples added to README.md
- [ ] All changes committed to git

### Post-Phase 2 Audit
- [ ] 8 tbta-source/ files created
- [ ] All files have inline citations
- [ ] No fabricated data (all sourced from plan files)
- [ ] Cross-references use correct paths
- [ ] All changes committed to git

### Post-Phase 3 Audit
- [ ] All markdown links verified (no 404s)
- [ ] Progressive disclosure compliance checked
- [ ] features/TEMPLATE.md created and actionable
- [ ] All READMEs updated with current status
- [ ] All changes committed to git

### Post-Phase 4 Audit
- [ ] 29 features audited with status documented
- [ ] Tier A features standardized (19 features)
- [ ] Tier B features migrated or status documented
- [ ] Tier C features scaffolded
- [ ] All changes committed to git

### Final Audit (Before Completion)
- [ ] All 26 original TODOs resolved
- [ ] No new TODOs introduced without justification
- [ ] All files follow STANDARDIZATION.md conventions
- [ ] All files follow SCHEMA.md conventions
- [ ] Git history is clean (meaningful commits)
- [ ] README.md checklist updated
- [ ] Migration plan marked complete

---

## Peer Review Plan

Before execution, this plan will be reviewed by 3 specialized agents:

### Reviewer 1: Dependency Analyst
**Focus**: Verify dependency graph is correct
**Questions**:
- Are all blocking dependencies identified?
- Can parallel tasks truly run independently?
- Are there hidden dependencies we missed?

### Reviewer 2: Memory Continuity Specialist
**Focus**: Verify subagents can restore context
**Questions**:
- Is README.md sufficient as entry point?
- Can a new agent pick up mid-phase?
- Are memory keys well-structured?

### Reviewer 3: Audit Specialist
**Focus**: Verify audit checklist is comprehensive
**Questions**:
- Can we verify completion objectively?
- Are success criteria measurable?
- What could slip through the cracks?

---

## Execution Protocol

### Before Starting
```bash
git checkout -b tbta-migration-complete
git push -u origin tbta-migration-complete
```

### After Each Phase
```bash
git add bible-study-tools/tbta/
git commit -m "feat(tbta): complete Phase {N} - {description}"
git push
```

### If Interrupted
1. Check last completed phase in git log
2. Read `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/README.md`
3. Check migration plan for next incomplete task
4. Restore hive memory: `npx claude-flow@alpha hooks session-restore --session-id "swarm-1763149850808-ovswmjk2f"`
5. Continue from next task

---

## Success Metrics

**Quantitative**:
- 26 TODOs resolved ✅
- 0 new unjustified TODOs ✅
- 100% of Tier A features standardized ✅
- 8 tbta-source/ files created ✅
- All audit checklist items passed ✅

**Qualitative**:
- Documentation is clear and actionable
- Subagents can navigate using READMEs
- Migration is repeatable (documented process)
- No information loss from plan files
- Ready for production feature work

---

## Risk Mitigation

**Risk**: Memory loss mid-execution
**Mitigation**: README.md entry point, git commits per phase, hive memory backup

**Risk**: Parallel tasks create conflicts
**Mitigation**: Careful dependency analysis, independent file targets

**Risk**: Scope creep (new TODOs discovered)
**Mitigation**: Document new TODOs for future work, stay focused on 26 original

**Risk**: Quality degradation under time pressure
**Mitigation**: Audit checklist enforced, peer review before execution

---

**Status**: ⏳ AWAITING PEER REVIEW
**Next Step**: Launch 3 reviewer agents for plan validation
