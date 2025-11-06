# Progressive Disclosure Documentation Standard for TBTA Features

**Last Updated:** 2025-11-05
**Source:** Learned from bible-study-tools pattern (e.g., strongs-word-research)

---

## Core Principle

**Token Efficiency:** Main README target ≤500 lines. Inline only what's relevant to THIS feature.

Progressive disclosure means readers get the essential information first, with details available as they need them - but not requiring external file navigation for the basics.

---

## README.md Structure (≤500 lines)

### Section 1: Purpose (50-100 lines)

**What it is:**
- Feature name and category (Noun/Verb/Clause/Phrase)
- One-sentence description
- Problem it solves for translators

**Why it matters:**
- Translation impact (concrete examples)
- Which language families need this feature
- Error types prevented

**Who needs it:**
- Target audiences: translators, pastors, students, AI systems
- Primary use case (specific scenario)
- When NOT to use this feature

**Template:**
```markdown
# {Feature Name} ({TBTA Category N})

{One-sentence description of what this feature encodes}

**Target Audience:** {Bible translators, pastors, students} working with {specific language families}

**Primary Use Case:** When translating {specific situation}, users need {this feature} because {concrete reason}. Without it, {specific error occurs}.
```

### Section 2: Methodology (200-300 lines)

**Inline the essential how-to**, don't reference external docs.

**Phase 1: Data Extraction/Identification**
- Where is this feature in TBTA YAML? (exact path)
- Is it explicit (read directly) or implicit (must predict)?
- What context is needed? (verse-level vs discourse-level)
- Extraction code example (10-20 lines)

**Phase 2: Prediction/Analysis** (if not explicit)
- Hierarchical decision tree (Level 1 → Level 2 → Baseline)
- Key correlations (Mood → Aspect, Semantics → Number, etc.)
- Confidence tiers (95% automate, 85% review, <85% flag)
- Prediction code example (20-30 lines)

**Phase 3: Validation and Verification**
- Critical validation rules (from REVIEW-GUIDELINES.md)
- Feature-specific validation (value ranges, consistency checks)
- Error categorization (semantic gap, ambiguity, rare construction)
- Test results summary (accuracy percentage)

**Template:**
```markdown
## Methodology

### Phase 1: Data Extraction

**Location in TBTA Data:**
```python
# Found at: clauses[i]['children'][j]['FeatureName']
def extract_feature(verse_yaml):
    # ...code...
```

**Context Required:** {Verse-level | Chapter-level | Book-level}

### Phase 2: Prediction Method (if not explicit)

**Decision Tree:**
1. **Level 1: Theological/Semantic Analysis** (95%+ confidence)
   - If {condition}: return {value}
2. **Level 2: Grammatical Cues** (85%+ confidence)
   - If {condition}: return {value}
3. **Baseline: Default Value** (baseline_accuracy% confidence)
   - return {most_common_value}

**Key Correlations:**
- Mood={value} → Feature={predicted} (85% confidence)
- Semantics={type} → Feature={predicted} (80% confidence)

### Phase 3: Validation

**Accuracy:** {X}% on {N} test verses

**Critical Rules:**
- [ ] All values from official TBTA enumeration
- [ ] Cross-feature consistency (check related features)
- [ ] Theological soundness (check divine speaker cases)
```

### Section 3: Output Schema (100-150 lines)

**Filename format:**
```
./bible/commentaries/{BOOK}/{CHAPTER}/{VERSE}/{BOOK}-{CHAPTER}-{VERSE}-{feature}.yaml
```

**YAML structure** (show complete example):
```yaml
verse: BOOK.chapter.verse
feature_name:
  value: {extracted_value}
  confidence: {0.0-1.0}
  method: {explicit|predicted}
  context: {any additional context}
metadata:
  source: tbta
  version: 1.0.0
```

**Examples** (3-5 actual verses):
- Simple case (most common value)
- Complex case (rare value with explanation)
- Edge case (ambiguous, multiple interpretations)

### Section 4: Related Features (50 lines)

**Integration with other TBTA features:**
- Which features correlate? (Mood → Aspect, Person → Number)
- Which features conflict? (check consistency)
- Recommended processing order

**Integration with Macula data:**
- How does this complement Macula? (pragmatics vs morphology)
- Can Macula data help predict this feature?

**Translation workflow integration:**
- When to consult this feature (translation workflow step)
- How to present to translators (format, simplification)

---

## Supplementary Files (Optional)

### METHOD.md (Detailed Implementation)

**When to create:**
- Algorithm is complex (>100 lines)
- Multiple approaches exist (compare trade-offs)
- Deep technical detail needed (developers only)

**Contents:**
- Complete code implementation
- Full decision tree with all branches
- Correlation matrices and statistics
- Edge case handling strategies
- Performance optimization notes

### QUICK-REFERENCE.md (Lookup Table)

**When to create:**
- Feature has many values (10+)
- Translators need fast lookup
- Examples for each value helpful

**Contents:**
- Table of all feature values
- One-sentence explanation per value
- 1-2 verse examples per value
- Language family recommendations

### EXPERIMENT-REPORT.md (Research Details)

**When to create:**
- Experiments were run (test data exists)
- Accuracy metrics available
- Error analysis completed
- Future improvements identified

**Contents:**
- Test methodology
- Full accuracy breakdown by category
- Error categorization and examples
- Lessons learned
- Next steps for improvement

---

## Anti-Patterns to Avoid

❌ **Don't:**
- Reference SCHEMA.md, STANDARDIZATION.md, REVIEW-GUIDELINES.md
  - Inline the relevant rules instead (3-5 bullet points)
- Write "See X.md for details"
  - Inline essential details, link to supplementary file if exists
- Make README >500 lines
  - Move details to METHOD.md or QUICK-REFERENCE.md
- Use jargon without definition
  - Define on first use: "morphological analysis (grammatical forms)"
- Assume Greek/Hebrew knowledge
  - Explain in plain language, provide transliteration

✅ **Do:**
- Start with user problem (translation scenario)
- Inline extraction/prediction code (10-30 lines)
- Show 3-5 real verse examples
- Define success clearly (accuracy percentage)
- Be honest about limitations
- Make it scannable (headers, bold, lists)

---

## Example: Applying to "Proximity" Feature

**Main README.md (≤500 lines):**

1. **Purpose** (75 lines)
   - Proximity encodes demonstrative distinctions (this/that)
   - Critical for Japanese (これ/それ/あれ), Korean, Spanish
   - Prevents using wrong demonstrative in translation

2. **Methodology** (250 lines)
   - **Phase 1:** Extract from `noun['Proximity']` field
   - **Phase 2:** If missing, predict from:
     - Demonstrative article present? → Check discourse distance
     - Spatial context? → Near Speaker/Listener/Remote
     - Temporal context? → Temporally Near/Remote
   - **Phase 3:** Validate against 9 official proximity values

3. **Output Schema** (125 lines)
   - Filename: `BOOK-CHAPTER-VERSE-proximity.yaml`
   - YAML structure with example
   - 5 verse examples (near, remote, temporal, contextual, ambiguous)

4. **Related Features** (50 lines)
   - Correlates with: Participant Tracking (contextual proximity)
   - Integration with: Demonstrative articles in Macula
   - Translation workflow: Check before translating demonstratives

**Supplementary:**
- `METHOD.md` - Complete decision tree, correlation matrix
- `QUICK-REFERENCE.md` - 9-value lookup table with examples

---

## Migration Guide for Existing Docs

**If you have old-style docs with many external references:**

1. **Identify the 20% that matters 80%** (Pareto principle)
   - What do translators MUST know?
   - What are the most common cases?

2. **Inline that 20% into README**
   - Copy-paste critical rules from SCHEMA.md
   - Inline common patterns from METHOD.md
   - Embed key examples from EXPERIMENT-REPORT.md

3. **Link to supplementary for the 80%**
   - Move detailed algorithms to METHOD.md
   - Move full value lists to QUICK-REFERENCE.md
   - Move test data to EXPERIMENT-REPORT.md

4. **Verify ≤500 line target**
   - If over 500: What can move to supplementary?
   - If under 300: What essential details are missing?

---

## Quality Checklist

Before finalizing any TBTA feature documentation:

- [ ] README.md is ≤500 lines
- [ ] Purpose section answers: What/Why/Who in <100 lines
- [ ] Methodology section shows extraction/prediction code inline
- [ ] Output schema includes 3-5 real verse examples
- [ ] No references to external standards docs (inline key rules instead)
- [ ] Technical terms defined on first use
- [ ] Limitations documented honestly
- [ ] Success metrics stated clearly (accuracy percentage)
- [ ] Related features identified
- [ ] Supplementary files justified (not created by default)

---

**This standard applies to ALL new TBTA feature documentation going forward.**
