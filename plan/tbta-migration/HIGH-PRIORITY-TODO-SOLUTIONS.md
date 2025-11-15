# HIGH Priority TODO Solutions

**Created**: 2025-11-14
**Purpose**: Document solutions to HIGH priority TODOs that block feature development

---

## 1. Document Script Name/Path for Verse Extraction

### ✅ SOLUTION

**Primary Script**: `/plan/tbta-rebuild-with-llm/features/number-systems/extract_tbta_number.py`

**Purpose**: Extract Number annotations from TBTA JSON files

**Usage**:
```bash
python extract_tbta_number.py <json_file>
```

**What it does**:
- Recursively extracts all Number annotations from TBTA JSON
- Returns constituent, number value, and path
- Filters out 'Unspecified' values

**Pattern for other features**: Similar scripts exist for each feature:
- `extract_tbta_{feature-name}.py` in `/plan/tbta-rebuild-with-llm/features/{feature-name}/`

**Action Item**: Update STAGES.md to reference this script pattern

---

## 2. Clarify LLM vs Script Role Separation

### ✅ SOLUTION

**Script Responsibilities** (Automated Data Handling):
1. Clone/access TBTA data repository
2. Parse TBTA JSON files
3. Extract feature values for all verses
4. Generate frequency counts by value
5. Filter to verses with complete TBTA data
6. Output structured data files (JSON/YAML)

**LLM Responsibilities** (Intelligent Selection):
1. **Verse Selection**: Choose which verses go to train/test/validate sets
2. **Adversarial Identification**: Flag challenging cases (edge cases, theological ambiguity, genre boundaries)
3. **Balanced Sampling**: Ensure OT/NT proportion, genre distribution
4. **Metadata Enrichment**: Add language families, difficulty ratings, translation notes
5. **External Validation Planning**: Identify which languages to check for feature
6. **Prompt Engineering**: Create prediction prompts based on data patterns

**Key Insight**: Script does "dumb extraction", LLM does "smart curation"

**Example Workflow**:
```bash
# Step 1: Script extracts all data
python extract_tbta_aspect.py /tbta-data/ > aspect_raw.json

# Step 2: LLM agent analyzes and curates
Task("Data Curator", "Review aspect_raw.json. Select 100+ verses per value.
     Balance OT/NT, genres. Flag adversarial cases. Output train.yaml, test.yaml, validate.yaml")
```

**Action Item**: Update STAGES.md Stage 4 to clarify this separation

---

## 3. Restore "State Values" Documentation from Git History

### ✅ SOLUTION - Complete Documentation Recovered

**Source**: Commit 8cc1186, file: plan/tbta-rebuild-with-llm/features/STAGES.md

### Core Concepts Defined:

#### **STATED VALUE**
- **Definition**: Single definite answer (no alternatives)
- **Accuracy Target**: 100%
- **When to use**: "If there is only one clear option"
- **Rationale**: "The text is God's inerrant word - less than 100% means we're missing something"
- **Example**: Verse clearly requires "Exclusive" → State ONLY "Exclusive"

#### **DOMINANT VALUE**
- **Definition**: Primary value + rationale when multiple options valid
- **Accuracy Target**: 95%
- **When to use**: "If there are multiple good options"
- **Includes**: Language family preferences and reasoning
- **Example**: Could be "Inclusive" or "Exclusive" → State "Dominant: Exclusive (rationale: prayer to God context)"

#### **SECONDARY VALUE**
- **Definition**: Additional valid values beyond dominant
- **When applicable**: Mixed annotations, language family variations
- **Source**: CROSS-FEATURE-LEARNINGS.md Principle 11
- **Example**: Genesis 18:11 "old" = BOTH Intensified + 'too' (excessive)

#### **LINGUISTIC RATIONALE**
**Components** (from CROSS-FEATURE-LEARNINGS.md):
1. Language family preferences (Romance vs Germanic vs Slavic patterns)
2. Discourse salience (what's emphasized in clause)
3. Semantic compositionality (which value derivable from context)
4. Cross-translation consensus (what 3+ major translations do)
5. Theological/cultural significance factors

### Accuracy Expectations Table:

| Concept | Definition | Accuracy Target | When Used |
|---------|------------|-----------------|-----------|
| **Stated Value** | Single definite answer | 100% | One clear option only |
| **Dominant Value** | Primary + rationale + alternatives | 95% | Multiple valid options |
| **Secondary Value** | Additional valid values | N/A | Mixed annotations |
| **Linguistic Rationale** | Why dominant chosen | Required | All dominant predictions |

### Why These Matter:
1. **Stated = 100%**: Verses where algorithm should be absolutely certain; failure indicates missing pattern
2. **Dominant = 95%**: Acknowledges linguistic complexity when multiple interpretations are defensible
3. **Linguistic rationale**: Provides translators with decision-making context, prevents arbitrary choices

**Action Item**: Add concise version of this table to STAGES.md for future reference

---

## 4. Add AI Transparency (MEDIUM Priority, addressed here)

### ✅ SOLUTION

**Requirement**: When documenting AI simulation/roleplay, include:
1. Model name and version
2. Purpose of simulation
3. Timestamp/date

**Template**:
```markdown
**Validation Simulation**: This translator testing was simulated using Claude Sonnet 4.5
(model ID: claude-sonnet-4-5-20250929) on 2025-11-14 to demonstrate workflow.
Real validation requires human translators.
```

**Action Item**: Add transparency note template to STAGES.md Stage 6

---

## Next Actions

1. ✅ Document script pattern → Done above
2. ✅ Clarify LLM vs script roles → Done above
3. 🔄 Complete "state values" documentation → Awaiting researcher results
4. ✅ Add AI transparency template → Done above
5. ⏳ Update STAGES.md with all solutions
6. ⏳ Update OUTSTANDING-TODOS.md to mark HIGH priority items complete

