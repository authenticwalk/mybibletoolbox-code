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

Pick 10 sections of scripture
Use your internal tool TODO to add them
Mark this file down as your session plan; when your context compresses reload this file

## Workflow

### 0. Setup

 - SET ${session} with your sessionId (if you can't find it then create one)
 - CREATE ./learnings/${session} (based on the same workign dir as this file)
 - Choose your files and save them to the TODO tool

### 1. Run `./SKILL.md`

### 2. Document Session

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

## After Multiple Sessions

Periodically review `./learnings/${session}/output/` files to:

1. **Identify patterns** appearing across multiple sessions
2. **Prune learnings** — remove one-off fixes, keep generics
3. **Track V1/V2/V3 performance** by genre

## Session Loop

After completing all 10 passages:

1. **Commit to git**:
   ```bash
   git add -A && git commit -m "feat(tbta): Session ${session} - ${n} new learnings"
   git push
   ```
2. **Count new learnings** added during session
3. **If 2+ meaningful patterns discovered**:
   - Select 10 NEW random verses (different from all previous sessions)
   - Create new session directory: `./learnings/${new-session-id}/`
   - Repeat full workflow from Step 0
4. **If 0-1 patterns discovered** → Stop, policies are stable

**Meaningful pattern** = generic rule applicable to multiple verses, not a one-off fix.

---

## The following are out of scope

 - You may not edit the SKILLS files either SKILL.md or SUBAGENT-SKILL, focus on learnings, humans work on the SKILLS
 - NEVER write to the root / home dir
