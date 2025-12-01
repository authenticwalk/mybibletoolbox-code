# Hybrid Hints + LLM Methodology

## Task
Predict mood labels for 100 verses using:
1. Full verse data (text, constituent, translations)
2. Word-analysis hints (rule-based predictions and detected patterns)

## Approach

### Key Principle
**Hints are SUGGESTIONS, not ground truth.** Use linguistic judgment to override hints when semantic context demands it.

### Decision Logic

#### Priority 1: Conditionals = Potential
- Pattern: "If X, then Y"
- Reasoning: Describes hypothetical/potential scenarios
- Label: `'might' Potential`
- Examples: EXO 21:27 ("if a tooth...he knock out"), MRK 12:19 ("if any one's brother may die")

#### Priority 2: Explicit Modal "might"
- Pattern: Text contains modal "might"
- Label: `'might' Potential`
- Example: COL 4:8 ("that he might know")

#### Priority 3: Modal "may" - Context Dependent
- **Purpose clauses** ("that we may eat"): Usually `Indicative`
  - These express purpose/goal, not permission or hypothesis
  - Example: LUK 22:8 ("that we may eat")
- **Conditional "may"** ("if brother may die"): `'might' Potential`
  - Already handled by Priority 1
- **Permissive "may"** in legal context: `'may' (permissive)`
  - Rare in this dataset
- **Default**: `Indicative`

#### Priority 4: Negation (without conditional)
- Pattern: Negation detected but NO conditional
- Reasoning: "did not do X" is a statement of negative fact
- Label: `Indicative`
- Examples: "David did not turn aside" (1KI 15:5), "they did not listen" (EXO 6:9)

#### Priority 5: Book Genre Hints
- Hints like `legal_book` or `prophetic_book` do NOT automatically determine mood
- These books contain narrative, which is predominantly indicative
- Only relevant when combined with other features (e.g., legal + conditional)

#### Default: Indicative
- Biblical narrative is overwhelmingly indicative mood
- Statements of fact, past events, declarations

## When I Override Hints

### Override Case 1: Negation
**Hint says:** Indicative
**I predict:** Indicative
**Reasoning:** Negation doesn't change mood. "X did not happen" is still a factual statement (negative fact).

### Override Case 2: Purpose Clauses with "may"
**Hint detects:** `modal_may`
**Word prediction:** Might vary
**I predict:** Indicative (if purpose clause)
**Reasoning:** "that we may eat" expresses purpose, not permission or hypothesis. It's functionally indicative.

### Override Case 3: Book Genre Alone
**Hint says:** `legal_book` or `prophetic_book`
**I predict:** Still evaluate semantics
**Reasoning:** Legal/prophetic books contain narrative. Genre alone doesn't determine mood.

## Results

**Distribution:**
- Indicative: 91 (91%)
- 'might' Potential: 9 (9%)

This aligns with Biblical text being primarily narrative (indicative), with conditional/hypothetical scenarios appearing in legal codes and teachings.

## Confidence

High confidence in this approach because:
1. All 9 'might' Potential predictions are clear conditionals or hypotheticals
2. All negated facts correctly labeled as Indicative
3. Purpose clauses correctly distinguished from permissive "may"
4. Semantic analysis applied consistently across all 100 verses

## Code

See `refined_hybrid.py` for implementation.
