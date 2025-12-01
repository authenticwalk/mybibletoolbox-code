# Vocabulary (Checklist §1-2)

## Semantic Complexity Levels

| Level | Color | Action | Example |
|-------|-------|--------|---------|
| 0 | Blue | Use directly | "go", "man", "food" |
| 1 | Cream | Use directly | Most Longman Defining Vocabulary |
| 2 | Magenta | Pair with simple | "son/descendant", "serve/worship" |
| 3 | Green | Use alternates | "(complex) glory (simple) greatness" |
| 4 | Brown | Use directly | Proper nouns: "Jerusalem", "Paul" |

## Level 2: Pairings
Format: `simple/complex`

**Common pairings** (from practice):
- `serve/worship`
- `promise/swear`
- `gather/harvest`
- `grain/barley`
- `kneel/bow`
- `servants/workers`
- `family/clan`
- `friends/brothers-D`

**Explications** (when pairing won't work):
- `daughter-in-law` → `son's wife`
- `mother-in-law` → `husband's mother`
- `helmet` → `hard hat`

## Level 3: Alternates
Format: `(complex) ... (simple) ...`

```
(complex) Mary had faith in God.
(simple) Mary trusted in God.
```

## Null Pairing
Use `null/X` when no simple substitute is acceptable:
- `friends/brothers-D <<and null/sisters-D>>`
- If "sisters" unavailable, nothing is generated

## Word Senses
Mark sense when ambiguous: `know-C`, `thing-B`
- TBTA picks lowest letter matching argument structure
- Only mark if computer might get it wrong

## Hyphenated Words
- Write as in ontology: `stand-up`, `pick-up`, `take-away`
- **Never inflect**: `stand-up` not `stood-up`
- Default tense is discourse
- For other tenses: `stand-up _present`, `stand-up _future`

## Numbers
- ✅ Use numerals: `2 sons`, `10 years`
- ❌ Not words: `two sons`, `ten years`
- Number words not recognized as adjectives in ontology

## Capitalization
- Don't capitalize unless first word of sentence
- ✅ `king Herod`
- ❌ `King Herod`

## New Words
- Most Longman Defining Vocabulary (LDV) words can be added
- Mark with `_inLDV` if you want to use one not in ontology
- Complex words need 20+ Bible occurrences and easy pairing

## Common Mistakes

| Wrong | Right | Why |
|-------|-------|-----|
| "worship" alone | "serve/worship" | L2 needs pairing |
| "two sons" | "2 sons" | Numbers as digits |
| "picked-up" | "pick-up" | No inflection on hyphenated |
| "King David" | "king David" | No mid-sentence capitals |

