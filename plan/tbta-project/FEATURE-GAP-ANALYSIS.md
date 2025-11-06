# TBTA Feature Gap Analysis

**Purpose**: Comprehensive comparison of TBTA's actual features vs. what was documented in this project

---

## Summary

| Category | TBTA Has | We Documented | Coverage |
|----------|----------|---------------|----------|
| **Syntactic Categories** | 15 | 4 | 27% |
| **Noun Features** | 10 | 4 | 40% |
| **Verb Features** | 10 | 3 | 30% |
| **Adjective Features** | 2 | 1 | 50% |
| **Adverb Features** | 2 | 1 | 50% |
| **Other POS Features** | 5+ | 0 | 0% |
| **Structural Features** | 8+ | 0 | 0% |
| **Overall** | **52+ features** | **13 features** | **25%** |

---

## Part 1: Syntactic Categories

### TBTA Has (15 categories):
1. ✅ Noun (Category 1)
2. ✅ Verb (Category 2)
3. ✅ Adjective (Category 3)
4. ✅ Adverb (Category 4)
5. ❌ Adposition (Category 5)
6. ❌ Conjunction (Category 6)
7. ❌ Phrasal (Category 7)
8. ❌ Particle (Category 8)
9. ❌ Noun Phrase (Category 101)
10. ❌ Verb Phrase (Category 102)
11. ❌ Adjective Phrase (Category 103)
12. ❌ Adverb Phrase (Category 104)
13. ❌ Clause (Category 105)
14. ❌ Paragraph (Category 110)
15. ❌ Episode (Category 120)

**Coverage**: 4/15 = 27%

---

## Part 2: Noun Features (Category 1)

### TBTA Has:
1. ✅ **Number**: Singular, Dual, Trial, Quadrial, Paucal, Plural
   - Status: DOCUMENTED in features/number-systems/
   - Quality: Good (README + LEARNINGS + experiment)

2. ✅ **Participant Tracking**: 9 states
   - First Mention, Routine, Integration, Exiting, Restaging, Offstage, Generic, Interrogative, Frame Inferable
   - Status: DOCUMENTED in features/participant-tracking/
   - Quality: Good (README + LEARNINGS + experiment)

3. ✅ **Polarity**: Affirmative, Negative
   - Status: DOCUMENTED in features/polarity/
   - Quality: Partial (README + LEARNINGS, no experiment on nouns specifically)

4. ✅ **Proximity**: 10 values
   - Not Applicable, Near Speaker and Listener, Near Speaker, Near Listener
   - Remote within Sight, Remote out of Sight
   - Temporally Near, Temporally Remote
   - Contextually Near with Focus, Contextually Near
   - Status: DOCUMENTED in features/proximity/
   - Quality: Good (README + LEARNINGS, no experiment)

5. ❌ **Person**: First, Second, Third
   - First Inclusive, First Exclusive
   - First as Third, Second as Third
   - First Inclusive as Third, First Exclusive as Third
   - Status: NOT DOCUMENTED (agent terminated)
   - Impact: **Critical for Austronesian languages** (176 languages need clusivity)

6. ❌ **Surface Realization**: Noun, Always a Noun, PRO, Personal Pronoun
   - Status: NOT DOCUMENTED
   - Impact: Can't track pronoun vs. full noun discourse patterns

7. ❌ **Participant Status**: Not Applicable, Protagonist, Antagonist, Major Participant
   - Status: NOT DOCUMENTED
   - Impact: Can't identify narrative roles

8. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED
   - Impact: Can't stratify annotations by depth

9. ❌ **Lexical Sense**: A, B, C... (distinguishes multiple senses)
   - Status: NOT DOCUMENTED
   - Impact: Can't handle polysemy (same word, different meanings)

10. ❌ **Noun List Index**: 1-9, A-Z, a-z (coreference tracking)
    - Status: NOT DOCUMENTED
    - Impact: **Critical** - can't track pronoun antecedents across verses

**Coverage**: 4/10 = 40%

---

## Part 3: Verb Features (Category 2)

### TBTA Has:
1. ✅ **Time**: 23+ values
   - Present, Immediate Past, Earlier Today, Yesterday, 2 Days Ago, 3 Days Ago, Week Ago, Month Ago, Year Ago
   - During Speaker's Lifetime, Historic Past, Eternity Past, Unknown Past, Discourse
   - Immediate Future, Later Today, Tomorrow, 2 Days from Now, 3 Days from Now, Week from Now
   - Month from Now, Year from Now, Unknown Future, Timeless
   - Status: DOCUMENTED in features/verb-tam/
   - Quality: Good (README + LEARNINGS + experiment)

2. ✅ **Aspect**: 9 values
   - Inceptive, Completive, Cessative, Continuative, Imperfective, Routinely, Habitual, Gnomic, Unmarked
   - Status: DOCUMENTED in features/verb-tam/
   - Quality: Good (README + LEARNINGS + experiment)

3. ✅ **Mood**: 12 values
   - Indicative
   - Definite Potential, Probable Potential, 'might' Potential, 'might not' Potential, Unlikely Potential, Impossible Potential
   - 'must' Obligation, 'should' Obligation, 'should not' Obligation, Forbidden Obligation
   - 'may' permissive
   - Status: DOCUMENTED in features/verb-tam/
   - Quality: Good (README + LEARNINGS + experiment)

4. ❌ **Reflexivity**: Not Applicable, Reciprocal, Reflexive
   - Status: NOT DOCUMENTED
   - Impact: Can't distinguish "they saw each other" vs "they saw themselves"

5. ✅ **Polarity**: Affirmative, Negative, Emphatic Affirmative, Emphatic Negative
   - Status: DOCUMENTED in features/polarity/
   - Quality: Partial (README + LEARNINGS, no verb-specific experiment)

6. ❌ **Adjective Degree** (on verbs): No Degree, Comparative, Superlative, Intensified, Extremely Intensified, 'too', 'less', 'least'
   - Status: NOT DOCUMENTED for verbs (only for adjectives)
   - Impact: Can't handle "run faster", "most blessed"

7. ❌ **Target Tense & Form**: Language-specific target tense encoding
   - Status: NOT DOCUMENTED
   - Impact: Can't provide language-specific translation guidance

8. ❌ **Target Aspect**: Language-specific target aspect encoding
   - Status: NOT DOCUMENTED
   - Impact: Can't map to target language aspect systems

9. ❌ **Target Mood**: Language-specific target mood encoding
   - Status: NOT DOCUMENTED
   - Impact: Can't map to target language mood systems

10. ❌ **Semantic Complexity Level**: 1-5 scale (same as nouns)
    - Status: NOT DOCUMENTED
    - Impact: Can't stratify verb annotations

**Coverage**: 3/10 = 30%

---

## Part 4: Adjective Features (Category 3)

### TBTA Has:
1. ✅ **Degree**: 11 values
   - No Degree, Comparative, Superlative
   - Intensified, Extremely Intensified, 'too'
   - 'less', 'least'
   - Equality, Intensified Comparative, Superlative of 2 items
   - Status: DOCUMENTED in features/degree/
   - Quality: Good (README + LEARNINGS, no experiment)

2. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED
   - Impact: Can't stratify adjective annotations

**Coverage**: 1/2 = 50%

---

## Part 5: Adverb Features (Category 4)

### TBTA Has:
1. ✅ **Degree**: 8 values
   - No Degree, Comparative, Superlative
   - Intensified, Extremely Intensified, 'too'
   - 'less', 'least'
   - Status: DOCUMENTED in features/degree/
   - Quality: Good (README + LEARNINGS, no experiment)

2. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED
   - Impact: Can't stratify adverb annotations

**Coverage**: 1/2 = 50%

---

## Part 6: Adposition Features (Category 5)

### TBTA Has:
1. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED

2. ❌ **Lexical Sense**: A, B, C... (multiple preposition senses)
   - Status: NOT DOCUMENTED

3. ❌ **Semantic Role Marking**: How adposition marks roles
   - Status: NOT DOCUMENTED
   - Impact: **Critical for case-marking languages**

4. ❌ **Polarity**: (if applicable)
   - Status: NOT DOCUMENTED

**Coverage**: 0/4 = 0%

**Impact**: **High** - Adpositions are critical for:
- Ergative languages (case marking)
- Languages without case inflection (like English)
- Semantic role assignment

---

## Part 7: Conjunction Features (Category 6)

### TBTA Has:
1. ❌ **Implicit**: Yes/No (whether conjunction is overt or inferred)
   - Status: MENTIONED in polarity research, NOT FULLY DOCUMENTED
   - Impact: Can't track coordination patterns

2. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED

3. ❌ **Lexical Sense**: A, B, C...
   - Status: NOT DOCUMENTED

4. ❌ **Conjunction Type**: Coordinating vs. Subordinating
   - Status: NOT DOCUMENTED

5. ❌ **Polarity**: (if applicable)
   - Status: NOT DOCUMENTED

**Coverage**: 0/5 = 0%

**Impact**: **Medium** - Affects clause chaining, coordination analysis

---

## Part 8: Phrasal Features (Category 7)

### TBTA Has:
1. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED

2. ❌ **Lexical Sense**: A, B, C... (for multi-word idioms)
   - Status: NOT DOCUMENTED

3. ❌ **Phrasal Type**: What kind of multi-word unit
   - Status: NOT DOCUMENTED

4. ❌ **Polarity**: (if applicable)
   - Status: NOT DOCUMENTED

**Coverage**: 0/4 = 0%

**Impact**: **High for some languages** - Serial verb constructions in Niger-Congo, Austronesian

---

## Part 9: Particle Features (Category 8)

### TBTA Has:
1. ❌ **Particle Type**: QuoteBegin, QuoteEnd, Discourse markers
   - Status: NOT DOCUMENTED
   - Impact: **High** - Can't track quotation boundaries

2. ❌ **Semantic Complexity Level**: 1-5 scale
   - Status: NOT DOCUMENTED

3. ❌ **Lexical Sense**: A, B, C...
   - Status: NOT DOCUMENTED

4. ❌ **Polarity**: (if applicable)
   - Status: NOT DOCUMENTED

**Coverage**: 0/4 = 0%

**Impact**: **High** - Quotation marking is critical for:
- Direct vs. indirect speech
- Discourse structure
- Translation of "he said" constructions

---

## Part 10: Phrase-Level Features (Categories 101-104)

### TBTA Has (for NP, VP, AdjP, AdvP):
1. ❌ **Implicit**: Whether phrase is overt or inferred
   - Status: NOT DOCUMENTED

2. ❌ **Sequence**: Not in a Sequence, First Coordinate, Last Coordinate, Middle Coordinate
   - Status: NOT DOCUMENTED
   - Impact: Can't track coordination structure

3. ❌ **Semantic Role**: Most Agent-like, Most Patient-like, Source, Destination, Instrument, Beneficiary, etc.
   - Status: NOT DOCUMENTED
   - Impact: **Critical for ergative languages**

4. ❌ **Thing-Thing Relationship**: Genitive, Possessive, Part-Whole, etc.
   - Status: NOT DOCUMENTED

5. ❌ **Relativized**: Yes/No (whether phrase contains relative clause)
   - Status: NOT DOCUMENTED

**Coverage**: 0/5 = 0%

**Impact**: **Very High** - These are core syntactic features for understanding:
- Argument structure
- Coordination
- Possession
- Relative clauses

---

## Part 11: Clause-Level Features (Category 105)

### TBTA Has:
1. ❌ **Illocutionary Force**: Statement, Question, Command, Exclamation
   - Status: NOT DOCUMENTED
   - Impact: **High** - Can't distinguish sentence types

2. ❌ **Clause Type**: Main, Subordinate, Relative, Complement
   - Status: NOT DOCUMENTED
   - Impact: **High** - Can't track clause structure

3. ❌ **Speaker**: Who is speaking in this clause
   - Status: NOT DOCUMENTED
   - Impact: **High** - Critical for quotations

4. ❌ **Listener**: Who is being addressed
   - Status: NOT DOCUMENTED
   - Impact: **High** - Critical for quotations

5. ❌ **Rhetorical Question**: Yes/No
   - Status: NOT DOCUMENTED

6. ❌ **Discourse Genre**: Narrative, Direct Speech, Prayer, etc.
   - Status: NOT DOCUMENTED
   - Impact: **Very High** - Affects interpretation

7. ❌ **Salience Band**: Pivotal, Primary, Secondary, Backgrounded
   - Status: NOT DOCUMENTED
   - Impact: **High** - Narrative prominence tracking

8. ❌ **Sequence**: Coordination tracking at clause level
   - Status: NOT DOCUMENTED

**Coverage**: 0/8 = 0%

**Impact**: **Very High** - These are critical discourse-level features

---

## Part 12: Paragraph & Episode Features (Categories 110, 120)

### TBTA Has:
1. ❌ **Paragraph boundaries**: Discourse segmentation
   - Status: NOT DOCUMENTED
   - Impact: **High** - Affects translation unit decisions

2. ❌ **Episode boundaries**: Narrative structure
   - Status: NOT DOCUMENTED
   - Impact: **High** - Major discourse units

3. ❌ **Episode Type**: Scene, Summary, Background, etc.
   - Status: NOT DOCUMENTED

**Coverage**: 0/3 = 0%

**Impact**: **High** - Macro-level discourse structure

---

## Part 13: Cross-Cutting Features

### TBTA Has (applies to multiple categories):
1. ✅ **Polarity**: Affirmative, Negative, Emphatic variants
   - Status: DOCUMENTED in features/polarity/
   - Quality: Good for nouns/verbs, not tested on other categories

2. ❌ **Semantic Complexity Level**: 1-5 scale (all word-level categories)
   - Status: NOT DOCUMENTED
   - Impact: Can't stratify by annotation depth

3. ❌ **Lexical Sense**: A, B, C... (all word-level categories)
   - Status: NOT DOCUMENTED
   - Impact: **Very High** - Can't disambiguate polysemy

**Coverage**: 1/3 = 33%

---

## Overall Feature Count

### Total TBTA Features: 52+

| Category | Count |
|----------|-------|
| Noun-specific | 10 |
| Verb-specific | 10 |
| Adjective-specific | 2 |
| Adverb-specific | 2 |
| Adposition-specific | 4 |
| Conjunction-specific | 5 |
| Phrasal-specific | 4 |
| Particle-specific | 4 |
| Phrase-level | 5 |
| Clause-level | 8 |
| Paragraph/Episode | 3 |
| **Total** | **57** |

### Features We Documented: 13

| Feature | Status |
|---------|--------|
| Number | ✅ Full |
| Participant Tracking | ✅ Full |
| Verb Time | ✅ Full |
| Verb Aspect | ✅ Full |
| Verb Mood | ✅ Full |
| Polarity | ✅ Partial |
| Proximity | ✅ Partial |
| Degree (Adj/Adv) | ✅ Partial |
| Person | ❌ Failed (agent terminated) |
| Reflexivity | ❌ Not attempted |
| Surface Realization | ❌ Not attempted |
| Participant Status | ❌ Not attempted |
| Semantic Complexity | ❌ Not attempted |

**Actual Coverage**: 13/57 = **23%**

---

## Priority Ranking of Missing Features

### **Critical Priority** (Must have for basic TBTA reproduction):
1. **Person** (especially Inclusive/Exclusive) - 176 Austronesian languages need this
2. **Lexical Sense** - Disambiguation is fundamental
3. **Semantic Role** - Critical for ergative languages
4. **Illocutionary Force** - Can't distinguish questions/commands
5. **Speaker/Listener** - Critical for quotation tracking
6. **Noun List Index** - Coreference resolution is essential
7. **Particle features** (QuoteBegin/QuoteEnd) - Quotation boundaries

### **High Priority** (Important for comprehensive reproduction):
8. **Reflexivity** - Common grammatical category
9. **Surface Realization** - Discourse tracking
10. **Participant Status** - Narrative analysis
11. **Semantic Complexity Level** - Stratification
12. **Clause Type** - Syntactic structure
13. **Salience Band** - Discourse prominence
14. **Sequence** (coordination) - Syntactic structure
15. **Target Tense/Aspect/Mood** - Language-specific guidance

### **Medium Priority** (Useful but not essential):
16. Adposition features
17. Conjunction features (beyond Implicit)
18. Phrasal features
19. Discourse Genre
20. Paragraph/Episode boundaries

### **Lower Priority** (Nice to have):
21. Thing-Thing Relationship
22. Relativized
23. Rhetorical Question

---

## Recommendations

### For Immediate Correction:
1. Add **prominent disclaimer** to all documents:
   - "This project covers 13 of 57 TBTA features (23%)"
   - "Missing critical features: Person, Lexical Sense, Semantic Role, Coreference"
   - "Cannot claim complete TBTA reproduction"

2. Rename project to:
   - "TBTA Partial Reproduction - Phase 1"
   - "TBTA Core Features Study"
   - NOT "TBTA Reproduction" (implies completeness)

3. Update accuracy claims:
   - "91-97% accuracy on 6 features tested on Genesis 1 narrative"
   - NOT "97.8% TBTA reproduction accuracy"

### For Future Work:
1. Complete **Critical Priority features** (7 features) - 2-3 weeks
2. Add **High Priority features** (8 features) - 2-3 weeks
3. Add **Medium Priority features** (4 features) - 1-2 weeks
4. Add **Lower Priority features** (4 features) - 1 week
5. **Total**: 6-9 weeks for comprehensive coverage

### For Validation:
1. Test each feature across **8 genres** (not just Genesis narrative)
2. Minimum **50-100 verses per feature** for validation
3. Calculate **genre-specific accuracy**
4. Identify **failure modes** and edge cases

---

**Document Status**: Critical Analysis - Feature Gap Inventory
**Conclusion**: Current project covers ~23% of TBTA features, cannot claim comprehensive reproduction
**Action Required**: Update all documentation with honest limitations
