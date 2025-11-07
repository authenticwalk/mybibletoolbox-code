# Feature Documentation Improvement Plan

**Date**: 2025-11-07
**Goal**: Improve all TBTA features to production-ready documentation standards
**Approach**: Systematic improvement using parallel agents, progressive disclosure

## Scope

Improve all 19 TIER A features to have:
- ✅ TIER 1 elements (must-have): Translation Impact, Value Enumeration, Baseline, Quick Test, Examples
- ✅ TIER 2 elements (high-value): Prompt Template, Gateway Features, Common Errors, Validation approach
- ✅ Progressive disclosure: README ≤200 lines, split into topic files if needed
- ❌ NOT doing experiments yet - documentation only

## Feature Groups

### Group 1: Verb TAM (3 features)
- Aspect (verb-tam/aspect-*)
- Mood (verb-tam/mood-*)
- Reflexivity (verb-tam/reflexivity-*)

### Group 2: Person System (1 feature)
- Person/Clusivity (person-systems/*)

### Group 3: Number System (1 feature)
- Number Systems (number-systems/*)

### Group 4: Participant Tracking (1 feature)
- Participant Tracking (participant-tracking/*)

### Group 5: Proximity/Degree/Polarity (3 features)
- Proximity (proximity/*)
- Degree (degree/*)
- Polarity (polarity/*)

### Group 6: Discourse (2 features)
- Discourse Genre (discourse-genre/*)
- Illocutionary Force (illocutionary-force/*)

### Group 7: Phrasal/Surface (2 features)
- Phrasal Elements (07-phrasal-elements/*)
- Surface Realization (surface-realization/*)

### Group 8: Time Granularity (1 feature)
- Time Granularity (time-granularity/*)

### Group 9: Speaker Demographics (6 features)
- Speaker, Listener, Attitude, Age, Age Relationship, Speech Style (honorifics-register/*)

### Group 10: Missing Features (3 features)
- Semantic Role (needs creation)
- Salience Band (needs creation)
- Topic NP (needs validation)

## Documentation Standards

Each feature README must include:

### TIER 1 (Must-Have)
1. **Translation Impact** (top of file, 2-3 sentences + star ratings)
2. **Value Enumeration** (complete table)
3. **Baseline Statistics** ("XX% are value Y")
4. **Quick Test** (3-5 yes/no questions for translators)
5. **Examples** (3-5 verses with reasoning)

### TIER 2 (High-Value)
6. **Prompt Template** (hierarchical 5-level approach)
7. **Gateway Features** (what to check first, correlations)
8. **Common Errors** (3-5 patterns with solutions)
9. **Validation Approach** (how to test, expected accuracy)

### Progressive Disclosure
- README.md ≤200 lines (self-contained overview)
- Topic files ≤400 lines each
- Split into subdirectories if complex:
  - README.md (overview)
  - METHODOLOGY.md (prediction approach)
  - VALIDATION.md (testing approach)
  - LEARNINGS.md (insights from experiments)
  - language-typology.md (cross-linguistic patterns)

## Work Approach

1. **Parallel Processing**: Launch 8 agents working on different feature groups
2. **No Experiments**: Documentation only, no validation experiments
3. **Progressive Disclosure**: Use /progressive-disclosure skill for all .md files
4. **Consistency**: Follow same structure across all features
5. **Quality**: Solid, production-ready documentation ready for researchers

## Success Criteria

- [ ] All 19 TIER A features have complete TIER 1 elements
- [ ] All 19 TIER A features have complete TIER 2 elements
- [ ] All READMEs ≤200 lines (split if needed)
- [ ] All topic files ≤400 lines
- [ ] Consistent structure across features
- [ ] Ready for researchers to use for predictions

## Status Tracking

See individual group status files:
- group-01-verb-tam-status.md
- group-02-person-status.md
- group-03-number-status.md
- group-04-participant-status.md
- group-05-proximity-degree-polarity-status.md
- group-06-discourse-status.md
- group-07-phrasal-surface-status.md
- group-08-time-status.md
- group-09-speaker-demographics-status.md
- group-10-missing-features-status.md
