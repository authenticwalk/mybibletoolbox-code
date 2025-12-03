# Ruth 4 SKILL Comparison Test

## Objective
Compare 3 TBTA encoding approaches on Ruth 4 verses.

## Test Verses
- Ruth 4:1 - Narrative with dialogue, cultural setting (gate, elders)
- Ruth 4:5 - Legal/cultural complexity (levirate marriage)
- Ruth 4:13 - Narrative conclusion (marriage, birth)

## Agents
| Agent | Approach | Output File |
|-------|----------|-------------|
| A | V1-examples | ./agent-v1-examples.md |
| B | V2-rules | ./agent-v2-rules.md |
| C | V3-progressive | ./agent-v3-progressive.md |

## Rules
1. NO looking at sources.tabitha.bible until ALL predictions complete
2. Show step-by-step work with text at each step
3. After predictions, compare to reference
4. Document differences

## Status
- [x] Agent A (V1) - completed
- [x] Agent B (V2) - completed
- [x] Agent C (V3) - completed
- [x] Comparison analysis v1 (NIV source)
- [x] Comparison analysis v2 (Unchurched Adults source)

## Key Finding
**V2 Rules-First is most maintainable** - § references make errors traceable and fixable.

## Output Files
- `agent-v1-examples.md` - NIV test
- `agent-v2-rules.md` - NIV test
- `agent-v3-progressive.md` - NIV test
- `v2-agent-v1-examples.md` - Unchurched Adults test
- `v2-agent-v2-rules.md` - Unchurched Adults test
- `v2-agent-v3-progressive.md` - Unchurched Adults test
- `COMPARISON.md` - NIV analysis
- `COMPARISON-v2.md` - Unchurched Adults + maintainability analysis
