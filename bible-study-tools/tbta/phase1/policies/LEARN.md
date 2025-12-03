# TBTA Learning Session — Random Verse Encoding

> **Goal**: Encode random scripture passages to discover new patterns and improve V1/V2/V3 policies.

## Quick Start

```
Read: ./SKILL.md (orchestrator workflow)
Pick: Random passage from corpus below
Run: Full V1/V2/V3 parallel encoding
Update: Learnings files with discoveries
```

---

## Passage Selection

**Pick ONE randomly** — vary genre, testament, and complexity each session.

### Corpus (by genre)

| Genre | Books | Characteristics |
|-------|-------|-----------------|
| Narrative (OT) | Genesis, Joshua, Ruth, 1 Samuel, 2 Samuel, Nehemiah, Esther | Dialogue, action, genealogies |
| Prophetic | Daniel, Jonah, Nahum | Visions, oracles, judgment |
| Gospel | Matthew, Mark | Parables, miracles, discourse |
| Acts | Acts | Speeches, travel, church history |
| Epistle | Titus, Philemon, 2 John | Greetings, theology, commands |

### Selection Method

1. **Roll for genre**: Pick random genre from table above
2. **Roll for book**: Pick random book from that genre
3. **Roll for chapter**: Pick valid chapter number
4. **Pick verse range**: 5-10 verses (avoid splitting paragraphs)

**Or use this shortcut**:
```python
import random
books = ["GEN", "JOS", "RUT", "1SA", "2SA", "NEH", "EST", "DAN", "JON", "NAH", "MAT", "MRK", "ACT", "TIT", "PHM", "2JN"]
book = random.choice(books)
# Then pick chapter/verses manually based on book length
```

### Suggested Starting Points (if random feels overwhelming)

| Book | Passage | Why |
|------|---------|-----|
| Genesis 22:1-10 | Abraham/Isaac sacrifice — dialogue, commands, theology |
| Joshua 2:1-10 | Rahab and spies — dialogue, deception, promise |
| Ruth 3:1-10 | Threshing floor — cultural context, dialogue |
| 1 Samuel 17:40-50 | David vs Goliath — action, direct speech |
| 2 Samuel 12:1-10 | Nathan's parable — nested story, confrontation |
| Nehemiah 1:1-10 | Prayer — first person, confession, request |
| Esther 4:10-17 | Mordecai/Esther exchange — dialogue, decision |
| Daniel 3:13-23 | Fiery furnace — threat, defiance, action |
| Jonah 1:1-10 | Call and flight — commands, storm narrative |
| Nahum 1:1-8 | Oracle against Nineveh — poetic, theophany |
| Matthew 8:1-10 | Healings — dialogue, faith statements |
| Mark 4:35-41 | Storm stilling — action, questions, amazement |
| Acts 9:1-10 | Saul's conversion — vision, dialogue, transformation |
| Titus 2:1-10 | Instructions — commands, qualifications |
| Philemon 8-18 | Appeal for Onesimus — persuasion, relationship |
| 2 John 7-13 | Warning about deceivers — doctrine, commands |

---

## Workflow

### 1. Fetch Passage

```bash
# Single verse
python src/tools/fetch_verse.py "{BOOK} {ch}:{vs}"

# Or fetch chapter and extract
curl "https://www.biblestudytools.com/niv/{book}/{chapter}.html"
```

### 2. Launch Parallel Subagents

Run V1, V2, V3 **simultaneously** with this prompt for each:

```
Read: ./SUBAGENT-SKILL{-V2|-V3}.md + learnings-v{1|2|3}.md
Input: "{verse_ref}: {niv_text}"
Return: He1 encoding (linter-validated), issues
NOTE: Run linter until clean (max 12 iterations) BEFORE returning
```

### 3. Fetch Reference Encoding

```bash
curl -H "Accept: application/json" "https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}"
```

Compare each agent's output against `phase_1_encoding` field.

### 4. Score Results

| Agent | Matches Reference? | Linter Errors | Notes |
|-------|-------------------|---------------|-------|
| V1 | ✅/❌ | count | issues |
| V2 | ✅/❌ | count | issues |
| V3 | ✅/❌ | count | issues |

### 5. Update Learnings

**Critical**: Update the WRONG agent's learnings, not the winner's.

| Scenario | Action |
|----------|--------|
| All match | No update needed |
| Some wrong | Update wrong version's `learnings-v{n}.md` |
| All wrong same way | Update ALL learnings files |
| New pattern discovered | Add to appropriate learnings + consider SUBAGENT-SKILL update |

### 6. Document Session

Create: `./output/{date}-{book}-{ch}-{vs}.md`

```markdown
# {Book} {ch}:{vs-vs} — Learning Session

## Passage
{NIV text}

## Results
| Agent | Match | Errors | Iterations |
|-------|-------|--------|------------|
| V1 | | | |
| V2 | | | |
| V3 | | | |

## Winner
{V1/V2/V3} — {why}

## Patterns Discovered
- {pattern} → `{solution}` (added to learnings-v{n}.md)

## Issues Unresolved
- {description}
```

---

## Learnings Format Reminder

**Headers = Generic categories** — NOT verse-specific:
```markdown
## Title Positioning
- "[Title] [Name]" → "[Name] the [title]" (Mt 2:1, 1Sa 17:4)
```

**Verse refs = Suffix** — evidence, not scope:
```markdown
- "Magi" → "wise men" (Mt 2:1)
```

**No metadata** — no "(V1 Winner)", error counts, iterations

---

## Session Goals

Each session should aim to:

1. **Validate** — existing rules work on new passages
2. **Discover** — new patterns not yet documented
3. **Differentiate** — identify V1 vs V2 vs V3 strengths
4. **Aggregate** — merge similar patterns into generic rules

### Target Metrics (per 10 sessions)

- 3+ new patterns discovered
- 1+ rule generalization (specific → generic)
- V1/V2/V3 comparison data for different genres

---

## Genre-Specific Challenges to Watch For

| Genre | Common Challenges |
|-------|-------------------|
| Narrative | Pronouns, dialogue attribution, temporal sequences |
| Prophetic | Metaphor, personification, judgment oracles |
| Gospel | Parables (nested stories), miracles, crowds |
| Acts | Speeches (long quotes), travel, names |
| Epistle | Greetings, theology vocabulary, commands |

---

## After Multiple Sessions

Periodically review `./output/` files to:

1. **Identify patterns** appearing across multiple sessions
2. **Update SUBAGENT-SKILL files** with validated rules
3. **Prune learnings** — remove one-off fixes, keep generics
4. **Track V1/V2/V3 performance** by genre

