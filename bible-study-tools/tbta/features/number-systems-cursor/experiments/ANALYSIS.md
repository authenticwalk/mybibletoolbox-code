# Number-Systems Feature: Approach Analysis

**Feature**: number-systems  
**Training Set**: 494 verses across 6 values
**Goal**: Develop algorithm to predict Singular/Dual/Trial/Quadrial/Paucal/Plural with 95%+ accuracy

---

## Baseline Distribution (Training Set)

| Value | Count | Percentage | Context |
|-------|-------|------------|---------|
| **Trial** | 198 | 40.1% | Genesis 1:26, 1:27, 11:7 + others |
| **Dual** | 120 | 24.3% | Paired entities (eyes, hands, two disciples) |
| **Quadrial** | 74 | 15.0% | Four entities |
| **Plural** | 45 | 9.1% | Multiple entities (3+) |
| **Singular** | 37 | 7.5% | One entity |
| **Paucal** | 20 | 4.0% | A few entities (small group) |

**Observation**: Trial is most common in training set (40%), likely due to sampling strategy including Genesis contexts. This is NOT representative of overall Bible distribution (Trial is only 0.3% globally).

---

## Approach 1: Explicit Count Detection (Rule-Based)

**Strategy**: Look for explicit numbers in verse text or context

**Rules**:
1. If verse explicitly states "two" (δύο, שְׁנַיִם) → **Dual**
2. If verse explicitly states "three" (τρεῖς, שְׁלֹשָׁה) → **Trial**  
3. If verse explicitly states "four" (τέσσαρες, אַרְבָּעָה) → **Quadrial**
4. If verse states "a few" or "some" (small group context) → **Paucal**
5. If verse states large number or "many" → **Plural**
6. Default → **Singular**

**Pros**:
- ✅ High accuracy when count is explicit
- ✅ Simple to implement
- ✅ No theological interpretation needed

**Cons**:
- ❌ Requires actual verse text (not available without translation fetching)
- ❌ Misses implicit counts
- ❌ Fails on ambiguous cases (Genesis 1:26 doesn't say "three")

**Expected Accuracy**: 70-80% (many verses have explicit counts)

---

## Approach 2: Theological Context Analysis (Context-Aware)

**Strategy**: Use theological knowledge to infer number

**Rules by Context**:

### Trinity Contexts (→ Trial)
- Genesis 1:26-27 "Let us make" → **Trial** (Father, Son, Spirit)
- Genesis 11:7 "Let us go down" → **Trial** (Trinity in judgment)
- References to divine plural with Trinitarian interpretation

### Paired Biblical Entities (→ Dual)
- Two disciples (Luke 24:13, Acts 13:2)
- Two witnesses (Revelation 11)
- Paired body parts (eyes, hands, ears)
- Adam and Eve references
- Moses and Aaron pairs
- Peter and John combinations

### Small Group Worship (→ Paucal)
- Matthew 18:20 "two or three gather"
- Small house church gatherings
- Jesus + a few disciples (not all 12)

### Apostolic Council (→ Plural)
- Acts 15:25, 15:28 (multiple apostles/elders)
- Corporate church language

### Individual Reference (→ Singular)
- Single person named
- God (when singular emphasis)
- Individual prophets, kings

**Pros**:
- ✅ Works without translation texts (uses Bible knowledge)
- ✅ Handles theologically significant cases correctly
- ✅ Can leverage LLM's Biblical training data

**Cons**:
- ❌ Requires extensive Biblical knowledge
- ❌ May be inconsistent across verses
- ❌ Difficult to systematize

**Expected Accuracy**: 80-85% (good for theological contexts, weaker for ordinary narratives)

---

## Approach 3: Natural Pairs Detection (Pattern-Based)

**Strategy**: Identify naturally paired entities in Biblical contexts

**Natural Pairs** (→ Dual):
- **Body parts**: eyes (עֵינַיִם), ears (אָזְנַיִם), hands (יָדַיִם), feet
- **Parent pairs**: father and mother, Abraham and Sarah
- **Leader pairs**: Moses and Aaron, Peter and John, Barnabas and Saul
- **Created pairs**: Adam and Eve, male and female (Gen 1:27)
- **Symbolic pairs**: heaven and earth, day and night
- **Messenger pairs**: angels sent in pairs

**Quadrial Detection** (→ Quadrial):
- **Four corners of earth**
- **Four winds**
- **Four living creatures** (Ezekiel, Revelation)
- **Four rivers** (Genesis 2)

**Pros**:
- ✅ High accuracy for idiomatic Biblical expressions
- ✅ Culturally grounded in Hebrew/Greek usage
- ✅ Can be systematized with pattern list

**Cons**:
- ❌ Limited coverage (only ~25% of verses have natural pairs)
- ❌ Doesn't handle arbitrary counts well

**Expected Accuracy**: 90%+ on paired entities, but only ~25% coverage

---

## Approach 4: Grammatical Form Analysis (Morphological)

**Strategy**: Analyze source language morphology

**Hebrew Dual Form** (→ Dual):
- Dual ending: `יִם-` (-ayim)
- Example: עֵינַיִם (einayim, "eyes"), יָדַיִם (yadayim, "hands")
- Note: Hebrew dual is lexicalized for natural pairs, not productive

**Greek Number Marking**:
- δύο (duo) = "two" → Dual
- τρεῖς (treis) = "three" → Trial (if language has it)
- Plural forms → Plural or contextual interpretation

**Pros**:
- ✅ Objective (based on source text morphology)
- ✅ High accuracy when morphology is clear

**Cons**:
- ❌ Requires Greek/Hebrew text access
- ❌ Hebrew dual doesn't always map to grammatical dual in target language
- ❌ Greek doesn't have trial/quadrial/paucal, so doesn't help for those

**Expected Accuracy**: 85-90% for Dual, less useful for Trial/Quadrial/Paucal

---

## Approach 5: Verse Reference Pattern Matching (Heuristic)

**Strategy**: Match verse references to known patterns

**Observation from Training Data**:
- Genesis 1-11 (creation/early narratives) → High Trial concentration (Trinity contexts)
- Gospel parallel passages → Often Dual (two disciples sent)
- Apostolic letters → Often Plural (church/apostles)

**Heuristic Rules**:
1. Gen 1:26-27, Gen 11:7 → **Trial** (hardcode critical verses)
2. Luke 24:13, Acts 13:2 → **Dual** (known paired disciples)
3. Matthew 18:20 → **Paucal** (known small group context)
4. Revelation 4-5 (four living creatures) → **Quadrial**
5. Most epistles addressing "you" → **Plural** (church)

**Pros**:
- ✅ Can hardcode high-confidence cases
- ✅ Fast to implement
- ✅ No text analysis needed

**Cons**:
- ❌ Not generalizable
- ❌ Only covers known verses
- ❌ Brittle (fails on unseen verses)

**Expected Accuracy**: 95%+ on hardcoded verses, 0% on others (not viable as sole strategy)

---

## Approach 6: Hybrid: Theological + Pattern + Morphological

**Strategy**: Combine best elements from multiple approaches

**Decision Tree**:

```
1. Check for hardcoded critical verses (Gen 1:26, Luke 24:13, etc.)
   → If match: Return known value with HIGH confidence

2. Check for explicit count in context (if verse text available)
   → If found: Map count to number value with HIGH confidence

3. Check for natural pairs (body parts, parent pairs, disciple pairs)
   → If match: Return Dual with MEDIUM-HIGH confidence

4. Check for theological context
   a. Trinity context (Gen 1, Gen 11, creation language) → Trial
   b. Small group worship (Matt 18:20, house church) → Paucal
   c. Apostolic plural ("we" in Acts 15) → Plural

5. Check for symbolic/prophetic patterns
   → Four corners/winds/creatures → Quadrial
   
6. Default based on genre and book
   → Narrative: likely Dual or Plural (characters interacting)
   → Epistle: likely Plural (addressing churches)
   → Poetry: likely Singular or Plural (God or people)
```

**Pros**:
- ✅ Combines strengths of multiple approaches
- ✅ Handles various types of verses
- ✅ Can express confidence levels

**Cons**:
- ❌ Complex to implement
- ❌ May have conflicting signals

**Expected Accuracy**: 85-92%

---

## Approach 7-12: Additional Considerations

### 7. **Genre-Based Priors**
- Narrative → Likely Dual or Plural (characters)
- Epistle → Likely Plural (addressing churches)
- Poetry → Likely Singular (God) or Plural (people)
- Prophecy → Mixed (symbolic numbers common)

### 8. **Book-Specific Patterns**
- Genesis 1-11 → High Trial (creation contexts)
- Gospels → High Dual (disciple pairs)
- Acts → High Plural (church/apostles)
- Revelation → High Quadrial (four living creatures, four corners)

### 9. **Testament-Based Defaults**
- OT → More Dual (Hebrew dual forms for body parts)
- NT → More Plural (addressing churches)

### 10. **Participant Tracking Integration**
- If TBTA has participant tracking data → Count distinct participants
- Example: "they" referring to two people → Dual

### 11. **Corporate Solidarity Detection**
- Israel as collective → May be Singular (corporate) or Plural (individuals)
- Church as collective → Context-dependent

### 12. **Translation Consensus** (Ideal, but requires translation texts)
- Check 5 dual/trial-marking translations
- If 80%+ agree → High confidence
- If split → Flag as ambiguous

---

## Recommended Approach for PROMPT1

**Selected**: **Approach 6 (Hybrid)** with elements of Approach 2 (Theological) and Approach 3 (Natural Pairs)

**Rationale**:
1. We don't have translation texts yet (Approach 12 unavailable)
2. We can leverage LLM's Biblical knowledge (Approach 2)
3. We can systematize natural pairs (Approach 3)
4. We can hardcode critical verses (Approach 5)
5. Hybrid approach maximizes accuracy across verse types

**Implementation Plan**:
- Create PROMPT1.md with hierarchical decision tree
- Start with hardcoded critical verses
- Use theological context for Trinity/worship/apostolic contexts
- Use natural pairs for body parts and character pairs
- Default based on genre and testament

**Target Accuracy**: 85-90% on training set

---

## Next Steps

1. Create PROMPT1.md implementing hybrid approach
2. Test on training set (494 verses)
3. Analyze errors systematically (6-step process from STAGES.md)
4. Iterate with PROMPT2.md if accuracy < 90%
5. Lock predictions before checking test set

---

**Last Updated**: 2025-11-17  
**Status**: Analysis complete, ready for PROMPT1 development

