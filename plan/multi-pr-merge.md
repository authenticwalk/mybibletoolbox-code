# Multi-PR Merge Plan

## Objective
Merge three PR branches into current branch `claude/multi-pr-approach-testing-011CUqn8zohDxen2yuNGQ6zH`:
1. `claude/nested-docs-skill-process-011CUqK3iWNttjXJWW9jroPY` (main source of truth)
2. `claude/tbta-local-analysis-flow-011CUpJTkaCVzLZmAfvThGqX`
3. `claude/reproduce-tbta-results-011CUoxCL1qFLSfiB9pKBCv1`

## Key Deliverables
- Progressive disclosure skill integrated
- Local analysis method and examples merged
- Consolidated plan/tbta-rebuild-with-llm directory (from tbta-project + tbta-project-local)
- All markdown following progressive disclosure format
- Python work removed
- Experiments verified for methodology

## Progress

### Branch 1: nested-docs-skill-process
Status: Not started
- [ ] Fetch and explore branch
- [ ] Understand progressive disclosure skill format
- [ ] Merge content

### Branch 2: tbta-local-analysis-flow
Status: Not started
- [ ] Fetch and explore branch
- [ ] Review LOCAL-ANALYSIS-*.md files
- [ ] Review features/person-systems example
- [ ] Merge content

### Branch 3: reproduce-tbta-results
Status: Not started
- [ ] Fetch and explore branch
- [ ] Identify what to keep/remove
- [ ] Verify experiments methodology

### Consolidation
Status: ✅ COMPLETED
- [x] Created plan/tbta-rebuild-with-llm
- [x] Merged tbta-project + tbta-project-local (all content consolidated)
- [x] Applied progressive disclosure format to all READMEs
- [x] Removed Python code (5 files: 4 validators + 1 analyzer)
- [x] Cleaned up redundant progress reports
- [x] Preserved important methodology files (CORRECTED-PLAN.md, LOCAL-ANALYSIS-WORKFLOW.md)
- [x] Removed old directories (plan/tbta-project, plan/tbta-project-local)

## Learnings

### Experiments Methodology Verified
The Python scripts in experiments are **validation tools**, not fabrication:
- Load actual TBTA YAML files from .data/commentary
- Extract and analyze existing annotations
- Generate pattern reports and test cases
- The experiment markdown files show LLM-based prediction methodology

**Decision**: Remove Python scripts (per user requirement to focus on LLM prompts), but keep the experiment markdown files as they document legitimate LLM-based analysis methodology.

### Directory Structure
Final consolidated structure in plan/tbta-rebuild-with-llm/:
```
tbta-rebuild-with-llm/
├── README.md (197 lines - project overview with inline findings)
├── LEARNINGS.md (397 lines - detailed methodology insights)
├── CORRECTED-PLAN.md (from tbta-project - future roadmap)
├── LOCAL-ANALYSIS-WORKFLOW.md (from tbta-project-local - validation method)
├── features/ (13 features consolidated)
│   ├── README.md (200 lines - follows progressive disclosure)
│   ├── person-systems/ (with clusivity verse examples)
│   ├── degree/, polarity/, proximity/, number-systems/
│   ├── participant-tracking/, verb-tam/, discourse-genre/
│   └── ... (+ 6 more features)
├── languages/families/ (8 language families, 600+ languages)
│   ├── README.md (190 lines - follows progressive disclosure)
│   ├── austronesian.md, indo-european.md, niger-congo.md
│   ├── trans-new-guinea.md, mayan.md, otomanguean.md
│   └── other-families.md (70+ additional families)
├── experiments/ (8 feature validation experiments)
│   ├── README.md (189 lines - follows progressive disclosure)
│   └── aspect/, mood/, person-systems/, participant-tracking/
│       noun-index/, number-systems/, proximity/, time/
├── combined/ (production-ready system)
│   ├── README.md (180 lines - follows progressive disclosure)
│   ├── TBTA-MASTER-PROMPT.md (9-step annotation process)
│   ├── tbta-predictor-skill.md (LLM skill specification)
│   ├── reproduction-prompt.md, language-adaptation-guide.md
│   └── integration-test.md, worked-example-genesis-1-4.md
└── tbta-data/ (schema and samples)
    ├── README.md, SCHEMA.md, examples.md
    └── samples/ (14 Genesis + other sample verses)
```

### Progressive Disclosure Applied
All main READMEs now follow the progressive-disclosure skill format:
- ≤200 lines (self-contained overviews)
- Topic sections with inline key findings (not just links)
- Clear navigation to detail files
- No redundant "Subfiles:" lists
- Actual insights in the overview, not forcing clicks

### Key Statistics
- **Total files**: ~150+ markdown files + 14 JSON samples
- **Python removed**: 5 files (all validation/analysis scripts)
- **Features**: 13 documented with varying completeness
- **Languages**: 600+ across 76+ language families
- **Experiments**: 8 features validated (80-100% accuracy)
- **Combined system**: Production-ready prompts for 6 features
