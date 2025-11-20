# Feature Template Consolidation Analysis

**Date**: 2025-11-14
**Analyst**: Documentation Analyst Agent (TBTA Migration Hive Mind)
**Purpose**: Consolidate and standardize feature documentation templates

---

## Executive Summary

**Templates Found**: 5 different documentation templates with overlapping purposes
**Features to Migrate**: 29 subdirectories requiring standardization
**Primary Issue**: Progressive disclosure conflicts between TBTA-specific (500 lines) and general standards (200 lines)
**Recommendation**: Use STAGES.md as authoritative workflow, create consolidated features/TEMPLATE.md

---

## Templates Analyzed

### 1. GENERIC-FEATURE-TEMPLATE.md (542 lines)
**Location**: `/plan/tbta-rebuild-with-llm/GENERIC-FEATURE-TEMPLATE.md`

**Purpose**: LLM-based feature implementation methodology

**Structure**:
- Phase 1: Understand the Feature
- Phase 2: LLM Prediction Framework (with hierarchical prompts)
- Phase 3: Validation (blind prediction)
- Phase 4: Integration
- Phase 5: Prompt Refinement

**Best Practices**:
- ✅ Hierarchical prompt strategy (5 levels: Theological → Discourse → Grammar → Correlation → Baseline)
- ✅ Rarity principle (baseline = 80-90% accuracy immediately)
- ✅ Blind testing protocol (lock predictions before checking TBTA)
- ✅ Error categorization (5 types: Semantic Expansion, Theological Ambiguity, Cultural Knowledge, Rare Construction, Prompt Limitation)
- ✅ Multi-method validation (require agreement across prompts)
- ✅ Tiered automation by accuracy (95%+ = Tier 1, 85-94% = Tier 2, etc.)

**Issues**:
- ❌ Phase numbering conflicts with STAGES.md (5 phases vs 6 stages)
- ❌ Less comprehensive than STAGES.md (missing Stage 6 translation practitioner review)
- ❌ No balanced sampling requirements specified

---

### 2. FEATURE-AUDIT-TEMPLATE.md (189 lines)
**Location**: `/plan/tbta-rebuild-with-llm/features/FEATURE-AUDIT-TEMPLATE.md`

**Purpose**: Audit existing features against STAGES.md workflow

**Structure**:
- Stage 1-6 completion checklists (aligned with STAGES.md)
- Evidence documentation per stage
- Gap identification
- Overall assessment
- Recommendations (Priority 1-3)
- Historical context

**Best Practices**:
- ✅ Clear checklist format per stage
- ✅ Evidence-based assessment (files found, accuracy metrics)
- ✅ Gap identification structure
- ✅ Fully aligned with STAGES.md (6 stages)
- ✅ Preserves historical context while documenting deviations

**Issues**:
- ⚠️ Purpose is auditing, not creation (complementary to other templates)

---

### 3. PROGRESSIVE-DISCLOSURE.md (296 lines)
**Location**: `/plan/tbta-rebuild-with-llm/methodology/PROGRESSIVE-DISCLOSURE.md`

**Purpose**: Documentation structure standard for TBTA features

**Structure**:
- README.md Structure (≤500 lines)
  - Section 1: Purpose (50-100 lines)
  - Section 2: Methodology (200-300 lines) - INLINE essential content
  - Section 3: Output Schema (100-150 lines)
  - Section 4: Related Features (50 lines)
- Supplementary files (optional): METHOD.md, QUICK-REFERENCE.md, EXPERIMENT-REPORT.md

**Best Practices**:
- ✅ Inline essential content (don't reference SCHEMA.md, STANDARDIZATION.md externally)
- ✅ 500-line limit for complex technical features
- ✅ Progressive disclosure to supplementary files for deep details
- ✅ Anti-pattern list (what NOT to do)
- ✅ Migration guide for existing docs

**Issues**:
- ⚠️ File says it should be renamed (not "progressive-disclosure")
- ⚠️ Conflicts with general progressive-disclosure SKILL (500 vs 200 lines)

---

### 4. progressive-disclosure SKILL (357 lines)
**Location**: `/.claude/skills/progressive-disclosure/SKILL.md`

**Purpose**: General markdown documentation standard (project-wide)

**Structure**:
- README.md: ≤200 lines (self-contained overview)
- Topic files: ≤400 lines (detailed content on ONE topic)
- Anti-spam rule (update existing before creating new)
- Link format rule (use `[text](file.md)`, not aliases)

**Best Practices**:
- ✅ Plan ahead - estimate size before creating files
- ✅ README is self-contained (not just index/TOC)
- ✅ Topic sections with key findings + links (not generic "Subfiles:" lists)
- ✅ Decision tree for file creation
- ✅ Common patterns (simple, nested, experiments, tools)

**Issues**:
- ⚠️ 200-line limit conflicts with TBTA feature complexity (need 500 lines)

---

### 5. STAGES.md (552 lines)
**Location**: `/plan/tbta-rebuild-with-llm/features/STAGES.md`

**Purpose**: Authoritative 6-stage workflow for building TBTA features

**Structure**:
- Stage 1: Research TBTA Documentation
- Stage 2: Language Study
- Stage 3: Scholarly and Internet Research
- Stage 4: Generate Proper Test Set (100 verses per value, 40/30/30 split)
- Stage 5: Propose Hypothesis and First Prompt (12 approaches, iterative refinement, 100% accuracy target, 6-step error analysis)
- Stage 6: Test Against Validate Set & Peer Review (4 subagents: theological, linguistic, methodological, translation practitioner)

**Best Practices**:
- ✅ Most comprehensive and up-to-date workflow
- ✅ Balanced sampling requirements (100 verses per value minimum)
- ✅ Adversarial selection strategy for test set
- ✅ External validation methodology (check against real translations)
- ✅ 6-step systematic error analysis
- ✅ **NEW**: Stage 6 translation practitioner review (real-world testing)
- ✅ Production readiness checklist

**Issues**:
- None - this is the authoritative standard

---

## Progressive Disclosure Conflict Resolution

### The Conflict

**Two different line limits**:
- TBTA features: README ≤500 lines (PROGRESSIVE-DISCLOSURE.md)
- General standard: README ≤200 lines (progressive-disclosure SKILL)

### Root Cause

TBTA features are **complex technical documentation** that must:
- Inline methodology (not reference external standards docs)
- Include code examples (10-30 lines each)
- Show 3-5 real verse examples with analysis
- Document hierarchical decision trees
- Provide validation requirements

This cannot fit in 200 lines while remaining self-contained.

### Resolution

**Recommendation**: Clarify in `features/README.md` that:

1. **General project READMEs**: ≤200 lines (follows progressive-disclosure SKILL)
   - Directory overviews
   - Project summaries
   - Navigation guides

2. **TBTA Feature READMEs**: ≤500 lines (TBTA-specific complexity)
   - Technical implementation docs
   - Inline methodology (essential content, not references)
   - Code examples and verse analysis
   - Must be self-contained per PROGRESSIVE-DISCLOSURE.md

3. **All supplementary files**: ≤400 lines (follows progressive-disclosure SKILL)
   - METHOD.md, LEARNINGS.md, etc.

**Update Required**: PROGRESSIVE-DISCLOSURE.md should:
- Reference `/.claude/skills/progressive-disclosure/SKILL.md` for general principles
- Clarify that 500-line limit is TBTA feature exception
- Document when to use which standard

---

## Template Consolidation Recommendations

### Primary Template: STAGES.md

**Status**: ✅ Authoritative workflow for feature development

**Action**: No changes needed - this is the standard to follow

---

### Supporting Templates

#### Keep: FEATURE-AUDIT-TEMPLATE.md

**Purpose**: Audit existing features against STAGES.md
**Status**: ✅ Complementary tool (different purpose)
**Action**: No changes needed

---

#### Archive: GENERIC-FEATURE-TEMPLATE.md

**Issues**:
- Outdated phase numbering (5 vs 6)
- Missing Stage 6 translation practitioner review
- Superseded by STAGES.md

**Action**:
1. Add deprecation notice at top: "⚠️ DEPRECATED: Use STAGES.md instead"
2. Preserve valuable content:
   - Hierarchical prompt strategy → Reference in features/TEMPLATE.md
   - Error categorization → Already in STAGES.md
   - Rarity principle → Already in CROSS-FEATURE-LEARNINGS.md
3. Consider moving to archive/

---

#### Update: PROGRESSIVE-DISCLOSURE.md

**Issues**:
- Naming confusion with progressive-disclosure SKILL
- Conflicts in line limits not explained

**Action**:
1. Rename to avoid confusion: `features/DOCUMENTATION-STANDARD.md`
2. Add section clarifying relationship with progressive-disclosure SKILL
3. Document 500-line exception for TBTA features
4. Reference authoritative SKILL for general principles

---

#### Create: features/TEMPLATE.md

**Purpose**: Consolidated best practices for feature documentation

**Content** (≤400 lines):
```markdown
# TBTA Feature Documentation Template

Quick reference combining STAGES.md workflow with documentation best practices.

## Overview
- Authoritative workflow: [STAGES.md](STAGES.md)
- Documentation standard: [DOCUMENTATION-STANDARD.md](DOCUMENTATION-STANDARD.md)
- Audit tool: [FEATURE-AUDIT-TEMPLATE.md](FEATURE-AUDIT-TEMPLATE.md)

## Quick Start Checklist

### Stage 1: Research TBTA Documentation
- [ ] Read TBTA official docs for feature
- [ ] Review CROSS-FEATURE-LEARNINGS.md
- [ ] Create README.md with stage checklist

### Stage 2-6: [See STAGES.md for complete workflow]

## File Structure Standard

features/{feature-name}/
├── README.md (≤500 lines, self-contained)
│   ├── Purpose (50-100 lines)
│   ├── Methodology (200-300 lines, INLINE)
│   ├── Output Schema (100-150 lines)
│   └── Related Features (50 lines)
├── experiments/
│   ├── train.yaml (40% sample, 100+ verses per value)
│   ├── test.yaml (30% sample)
│   ├── validate.yaml (30% sample)
│   ├── ANALYSIS.md (up to 12 approaches)
│   ├── PROMPT1.md, PROMPT2.md, ... (iterations)
│   ├── LEARNINGS.md (error analysis)
│   ├── VALIDATION-RESULTS.md (accuracy metrics)
│   └── EXTERNAL-VALIDATION.md (if applicable)
└── archive/ (legacy files if migrated)

## Documentation Best Practices

[Reference key insights from STAGES.md, PROGRESSIVE-DISCLOSURE.md, and GENERIC-FEATURE-TEMPLATE.md]
```

---

## Feature Migration Checklist

**Total Features**: 29 subdirectories in `/plan/tbta-rebuild-with-llm/features/`

### Current Structure Patterns

**Inconsistencies Found**:

1. **Directory structure**:
   - ✅ person-systems/: Has experiments/ subdirectory
   - ❌ degree/: Files directly in root
   - Mixed: Various approaches

2. **File naming**:
   - ✅ person-systems/: PROMPT1.md, PROMPT2.md
   - ❌ Others: experiment-001.md
   - Standardize on: PROMPT{N}.md (clearer iteration tracking)

3. **Test set format**:
   - ✅ person-systems/: YAML format (train.yaml, test.yaml)
   - ❌ Others: Markdown or mixed
   - Standardize on: YAML (easier parsing, metadata support)

4. **Archive location**:
   - ✅ person-systems/: archive-10-phase/
   - ❌ Others: Various or none
   - Standardize on: archive/ (simpler naming)

### Migration Checklist (Per Feature)

For each of 29 features, verify:

#### File Structure
- [ ] Has README.md with stage checklist
- [ ] README is ≤500 lines
- [ ] README inlines methodology (no external references to SCHEMA.md, STANDARDIZATION.md)
- [ ] Has experiments/ subdirectory
- [ ] Legacy files moved to archive/ (if applicable)

#### Test Sets (Stage 4 Requirements)
- [ ] Has experiments/train.yaml (40% sample)
- [ ] Has experiments/test.yaml (30% sample)
- [ ] Has experiments/validate.yaml (30% sample)
- [ ] Each set has 100+ verses per value (if feature has multiple values)
- [ ] Balanced sampling: OT/NT proportional, multiple genres
- [ ] Includes adversarial cases in test set

#### Methodology Documentation (Stage 5)
- [ ] Has experiments/ANALYSIS.md (approaches documented)
- [ ] Has experiments/PROMPT{N}.md (iterations tracked)
- [ ] Has experiments/LEARNINGS.md (error analysis with 6-step process)
- [ ] Predictions locked with git commits before validation

#### Validation (Stage 6)
- [ ] Has experiments/VALIDATION-RESULTS.md (accuracy metrics)
- [ ] Subagent validation performed (blind testing)
- [ ] Has experiments/EXTERNAL-VALIDATION.md (if feature has observable translations)
- [ ] Peer review complete (4 reviewers: theological, linguistic, methodological, translation practitioner)
- [ ] Has experiments/TRANSLATOR-IMPACT.md (real-world testing)

#### Production Readiness
- [ ] Accuracy ≥95% on validate set
- [ ] All peer reviews passed
- [ ] Net benefit positive (mistakes avoided > mistakes introduced)
- [ ] README documents production status

---

## Standardization Rules Summary

### Directory Structure
```
features/{feature-name}/
├── README.md
├── experiments/
│   ├── train.yaml
│   ├── test.yaml
│   ├── validate.yaml
│   ├── ANALYSIS.md
│   ├── PROMPT1.md
│   ├── PROMPT2.md
│   ├── LEARNINGS.md
│   ├── VALIDATION-RESULTS.md
│   ├── EXTERNAL-VALIDATION.md (optional)
│   └── TRANSLATOR-IMPACT.md (Stage 6)
├── archive/ (if migrated from old structure)
└── [optional supplementary files]
    ├── METHOD.md (≤400 lines)
    ├── QUICK-REFERENCE.md (≤400 lines)
    └── [other topic files]
```

### File Naming Conventions
- Test sets: `train.yaml`, `test.yaml`, `validate.yaml`
- Iterations: `PROMPT1.md`, `PROMPT2.md`, `PROMPT3.md`, ...
- Analysis: `ANALYSIS.md`, `LEARNINGS.md`, `VALIDATION-RESULTS.md`
- External: `EXTERNAL-VALIDATION.md`, `TRANSLATOR-IMPACT.md`
- Archive: `archive/` (simple, not `archive-{methodology-name}/`)

### README Structure (≤500 lines)
1. **Purpose** (50-100 lines)
   - What/Why/Who
   - Translation impact
   - Language families affected

2. **Methodology** (200-300 lines)
   - INLINE extraction/prediction code (10-30 lines)
   - Hierarchical decision tree
   - Validation requirements
   - NO external references to SCHEMA.md, etc.

3. **Output Schema** (100-150 lines)
   - Filename format
   - YAML structure with complete example
   - 3-5 real verse examples

4. **Related Features** (50 lines)
   - Cross-feature correlations
   - Integration with Macula
   - Translation workflow integration

### Progressive Disclosure
- README ≤500 lines (TBTA features only)
- Supplementary files ≤400 lines each
- Inline essentials, link to details
- Self-contained (don't force clicking to understand basics)

---

## Recommended Next Steps

1. **Create consolidated template** (Priority 1)
   - [ ] Create `features/TEMPLATE.md` with best practices
   - [ ] Deprecate GENERIC-FEATURE-TEMPLATE.md
   - [ ] Update PROGRESSIVE-DISCLOSURE.md → DOCUMENTATION-STANDARD.md

2. **Standardize existing features** (Priority 2)
   - [ ] Audit all 29 features using FEATURE-AUDIT-TEMPLATE.md
   - [ ] Identify features missing Stage 4-6 requirements
   - [ ] Prioritize by tier (A → B → C)

3. **Update documentation references** (Priority 3)
   - [ ] Update features/README.md to reference new TEMPLATE.md
   - [ ] Add progressive disclosure clarification
   - [ ] Link to STAGES.md as authoritative workflow

---

## Appendix: Feature List by Current Status

### Well-Structured (Reference Examples)
- person-systems/ - Has experiments/, YAML test sets, stage checklist

### Needs Migration (29 total)
1. 02-verbs/
2. 07-phrasal-elements/
3. 101-noun-phrases/
4. 105-clauses/
5. degree/
6. discourse-genre/
7. ergative-absolutive/
8. evidentiality/
9. honorifics-register/
10. illocutionary-force/
11. locative-systems/
12. noun-classes/
13. number-systems/
14. numeral-classifiers/
15. participant-tracking/
16. polarity/
17. possessive-classification/
18. potential-errors/
19. proximity/
20. serial-verb-constructions/
21. surface-realization/
22. switch-reference/
23. time-granularity/
24. topic-np/
25. verb-extensions/
26. verb-tam/
27. voice-systems/

**Next Action**: Run FEATURE-AUDIT-TEMPLATE.md against each feature to assess completion status and gaps.

---

**Analysis Complete**: 2025-11-14
**Stored in Memory**: hive/analyst/feature-templates
