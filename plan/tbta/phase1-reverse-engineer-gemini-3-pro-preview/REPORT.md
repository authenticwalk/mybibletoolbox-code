# TBTA Reverse Engineering Report

## Objective
Analyze TBTA CSV exports for 15 Bible books to validate and refine the transformation rules for NIV → CNL (Controlled Natural Language).

## Methodology
1. **Data Acquisition**: Downloaded CSV exports from `AllTheWord/tbta_db_export`.
2. **Scope**: 15 Books (Genesis, Joshua, Ruth, 1-2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John).
3. **Analysis**: Developed a Python script (`analyze_tbta.py`) to scan for regex patterns corresponding to 12 hypothesized rules.
4. **Validation**: Categorized findings into "Supporting" and "Contradicting" evidence.

## Findings by Rule

### 1. Coreference Resolution
- **Rule**: Replace pronouns with explicit nouns.
- **Evidence**: Strong support in Genesis (e.g., Gen 1:4 "God... God... God").
- **Exceptions**: Found retained pronouns in 1 Samuel 1:1 ("He was in Zuph's clan") and Acts 3:26 ("he(God)"). This suggests some books or specific contexts (like "he" referring to God directly or in close proximity) may retain pronouns, or represent an earlier phase of translation.

### 2. Clause Segmentation
- **Rule**: One predicate per sentence.
- **Evidence**: High frequency of `.` and short sentences in Genesis 1.
- **Exceptions**: Some longer sentences remain, but often broken by `;` or new starts.

### 3. Explicit Relativization
- **Rule**: Appositives → `[who was...]`.
- **Evidence**: Consistent use in Genesis (Gen 7:1, 9:6) and 1 Samuel.
- **Exceptions**: Appositives like "X, the son of Y" sometimes remain (Gen 11:31 "Terah, the son of Terah"). Lists of animals/people (Gen 7:7) also retain comma separation without relativization.

### 4. Deixis Marking
- **Rule**: `I(Speaker)`, `you(Addressee)`.
- **Evidence**: Very consistent in direct speech (Gen 1:29, Gen 3:10).
- **Exceptions**: Occasional missing markers in Acts (Acts 15:7, 15:17) and Genesis 13:8 (formatting typo?).

### 6. Subordinate Bracketing
- **Rule**: Dependent clauses in `[...]`.
- **Evidence**: Ubiquitous. `[After God had created...]` (Gen 1:2).
- **Exceptions**: Few.

### 7. Quote Framing
- **Rule**: `Speaker said, ["..."]`.
- **Evidence**: Standard pattern.
- **Exceptions**: Variations in punctuation placement, e.g., `said, "[` (Gen 1:20, Titus 1:12). This might be a data entry inconsistency or an alternative standard.

### 8. Imperative Marking
- **Rule**: `(imp)`.
- **Evidence**: Clear usage in commands (Gen 1:22 "You(animals) (imp)...").

### 9. Hyphenated Verbs
- **Rule**: `run-away` (phrasal verbs).
- **Evidence**: `take-away` (Gen 14:12), `cut-off` (Gen 4:4).
- **Observation**: Also used for complex prepositions/conjunctions (`in-order-to`, `with-the-result-that`).

### 11. Demonym → Description
- **Rule**: "Moabite" → `[who was from Moab]`.
- **Evidence**: Ruth 2:2, Gen 28:8.
- **Exceptions**: "Canaanite", "Perizzite", "Jebusite" often retained in lists (Gen 10:16, Gen 13:7). This suggests lists of people groups might be exempt or treated as proper names (L4 LDV) rather than descriptions.

### 12. Gap-filling
- **Rule**: Implicit info marking.
- **Evidence**: `(implicit-subaction)`, `(footnote)` found in Genesis, Joshua.

## Conclusion
The hypothesized rules are largely confirmed by the data. Exceptions typically fall into:
1. **Lists/Genealogies**: Where strict relativization or segmentation would be cumbersome.
2. **Data Inconsistencies**: Typos or older versions of the data (e.g., punctuation variations).
3. **Complex Theological Concepts**: Where "he" referring to God might be retained for flow or reverence (Acts).

The updated `RULES.md` reflects these findings with specific references.

