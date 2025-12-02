# {BOOK} {chapter}:{verse} — He1 Encoding

**Date**: {date}
**Version**: {V1|V2|V3}

---

## Step 1: Download NIV

```
text = "{NIV text}"
```

---

## Step 2: Fix Pronouns & Split Sentences

**Changes made:**
- {list what pronouns were resolved}
- {list sentences that were split}

```
text = "{updated text}"
```

---

## Step 3: Simplify Vocabulary

**Changes made:**
- {word} → {replacement} (reason: L2 pairing / explication / etc.)

```
text = "{updated text}"
```

---

## Step 4: Group Participants

**Changes made:**
- {repeated phrase} → {grouped form}

```
text = "{updated text}"
```

---

## Step 5: Fix Clauses

**Changes made:**
- {prepositional phrase} → {relative clause}
- {added brackets where}

```
text = "{updated text}"
```

---

## Step 6: Checklist Pass

| Check | Status |
|-------|--------|
| Quotes | {ok / speaker+verb added / first sentence bracketed} |
| Implicit | {ok / marked <<...>> or <...>} |
| Passives | {ok / added "by X"} |
| Commands | {ok / added (imp)} |
| Causality | {ok / "to"→"in order to"} |
| Connectors | {ok / fixed And/But/Then} |
| Forbidden | {ok / removed can/even/any/own} |

```
text = "{updated text}"
```

---

## Final He1

```
{final He1 encoding}
```

---

## Check Tool Results

**URL**: `editor.tabitha.bible/check?text={urlencoded}`

**Errors**: {list or "None"}

**Fixes applied**: {if any}

---

## Comparison with Reference

**Source**: `sources.tabitha.bible/Bible/{Book}/{ch}/{vs}`

**Reference He1**:
```
{phase_1_encoding from API}
```

**Differences**:
- {list differences or "Matches exactly"}

---

## Learnings

- {any new patterns discovered}
- {any mistakes made and how to avoid}

