# Verse Parser Script

Automated Bible data processing using Claude Agent SDK with built-in auditing and self-learning.

## Overview

The `verse_parser.py` script processes Bible data (verses, chapters, books, or Strong's words) by:

1. **Loading data** from the mybibletoolbox-data repository
2. **Processing** each item using Claude Agent SDK with custom instructions
3. **Auditing** completed work in a separate session
4. **Learning** from failures to improve over time
5. **Tracking progress** so runs can be resumed

## Quick Start

### Installation

```bash
# Install dependencies (including Anthropic SDK)
pip install -r requirements.txt

# Setup minimal Bible data
./setup-minimal-data.sh

# Set your Anthropic API key (required!)
export ANTHROPIC_API_KEY=your_key_here
```

**Note**: The script requires an Anthropic API key to function. Get one at https://console.anthropic.com/

### Basic Usage

```bash
# Process 100 random verses
python verse_parser.py \
  --dataset verse \
  --markdown examples/sample_verse_instructions.md \
  --limit 100

# Process with different model
python verse_parser.py \
  --dataset verse \
  --markdown examples/sample_verse_instructions.md \
  --model claude-opus-4-20250514 \
  --limit 50

# Skip audit phase for faster processing
python verse_parser.py \
  --dataset verse \
  --markdown examples/sample_verse_instructions.md \
  --no-audit \
  --limit 100

# Check status
python verse_parser.py --status

# Continue interrupted run
python verse_parser.py --continue

# Process all Matthew chapters
python verse_parser.py \
  --dataset chapter \
  --markdown chapter_summary.md \
  --filter "MAT*"
```

## Command-Line Options

### Required (for new runs)

- `--dataset {verse|chapter|book|strongs}` - Type of data to process
- `--markdown PATH` - Path to markdown instruction file

### Optional

- `--limit N` - Number of items to process (default: 100, use -1 for all)
- `--filter PATTERN` - Filter items (e.g., "MAT*" for Matthew, "G*" for Greek)
- `--model MODEL` - Claude model to use (default: claude-sonnet-4-5-20250929)
- `--max-tokens N` - Maximum tokens for responses (default: 4096)
- `--no-audit` - Skip audit phase (faster but less validated)
- `--continue` - Continue from previous run
- `--redo-all` - Start fresh, ignore previous progress
- `--status` - Show current progress and exit

### Available Models

- `claude-sonnet-4-5-20250929` (default) - Latest Sonnet, best balance
- `claude-opus-4-20250514` - Most capable, slower and more expensive
- `claude-haiku-4-20250430` - Fastest and cheapest, good for simple tasks

## Dataset Types

### Verse Mode

Process individual verses.

```bash
python verse_parser.py --dataset verse --markdown verse_analysis.md --limit 100
```

- **Total items**: ~31,000 verses
- **Example item**: `MAT.005.003`
- **Data loaded**: All YAML files in `.data/commentary/MAT/005/003/`

### Chapter Mode

Process entire chapters.

```bash
python verse_parser.py --dataset chapter --markdown chapter_summary.md --filter "MAT*"
```

- **Total items**: ~1,189 chapters
- **Example item**: `MAT.005`
- **Data loaded**: All verses in Matthew chapter 5

### Book Mode

Process entire books.

```bash
python verse_parser.py --dataset book --markdown book_overview.md --limit 10
```

- **Total items**: 66 books
- **Example item**: `MAT`
- **Data loaded**: All chapters and verses in Matthew

### Strongs Mode

Process Strong's concordance entries.

```bash
python verse_parser.py --dataset strongs --markdown word_study.md --filter "G*" --limit 50
```

- **Total items**: ~8,674 (5,624 Hebrew + 3,050 Greek)
- **Example item**: `G0026` (agapē - love)
- **Data loaded**: All YAML files in `.data/strongs/G0026/`

## Filter Patterns

Use filters to limit processing to specific subsets:

```bash
# Only Matthew verses
--dataset verse --filter "MAT*"

# Only New Testament books
--dataset book --filter "NT"

# Only Old Testament books
--dataset book --filter "OT"

# Only Greek Strong's numbers
--dataset strongs --filter "G*"

# Only Hebrew Strong's numbers
--dataset strongs --filter "H*"

# Specific book
--dataset chapter --filter "ROM"
```

## Instruction Files

Create markdown files that define the task for Claude. See `examples/sample_verse_instructions.md` for a template.

### Key Elements

1. **Task Description**: What to analyze
2. **Output Format**: Expected structure (usually YAML)
3. **Guidelines**: Rules to follow (citations, standards, etc.)
4. **Examples**: Sample output for reference

### Example Structure

```markdown
# Verse Analysis Instructions

## Task
Analyze the verse and provide:
- Source language analysis
- Translation comparison
- Theological themes

## Output Format
\```yaml
verse: {REF}
analysis:
  ...
\```

## Guidelines
- Always cite sources
- Follow STANDARDIZATION.md
- Never fabricate data
```

## Progress Tracking

Progress is automatically saved to `.verse_parser_progress.json`:

```json
{
  "dataset_type": "verse",
  "total_items": 100,
  "completed_items": 45,
  "failed_items": 3,
  "items_list": ["MAT.005.003", ...],
  "completed": ["MAT.005.003", ...],
  "failed": [{"item": "JHN.001.001", "error": "..."}],
  "current_index": 48
}
```

### Resume Interrupted Runs

```bash
# Check current status
python verse_parser.py --status

# Continue from where it left off
python verse_parser.py --continue

# Start completely fresh
python verse_parser.py --dataset verse --markdown new.md --redo-all
```

## Learning System

Failures are logged to `verse_parser_learnings.md` for review:

```markdown
## Failure: MAT.005.003

**Timestamp**: 2025-11-08T10:30:00Z

**Error**: Processing timeout

**Context**:
\```json
{
  "dataset_type": "verse",
  "item": "MAT.005.003"
}
\```

---

## Audit Failure: JHN.003.016

**Timestamp**: 2025-11-08T10:35:00Z

**Audit Feedback**: Missing source citations

**Output**:
\```
verse: JHN.003.016
...
\```
```

Review this file periodically to:
- Identify common failure patterns
- Improve instruction files
- Debug processing issues

## Data Management

The script automatically manages data checkout using git sparse-checkout:

```python
# For verses
git sparse-checkout add commentary/MAT/005/003

# For chapters
git sparse-checkout add commentary/MAT/005

# For books
git sparse-checkout add commentary/MAT

# For Strong's
git sparse-checkout add strongs/G0026
```

Data is loaded and provided to Claude as context automatically.

## Claude SDK Integration

### Current Status

✅ **FULLY IMPLEMENTED** - The script now uses the official Anthropic Python SDK!

The `ClaudeAgentRunner` class:
- Initializes the Anthropic client with API key from environment
- Implements `run_processing_session()` with full API integration
- Implements `run_audit_session()` for validation
- Handles errors (rate limits, API errors, connection issues)
- Supports multiple Claude models
- Reports token usage for monitoring

### How It Works

**Processing Phase** (verse_parser.py:453-525):
```python
message = self.client.messages.create(
    model=self.model,
    max_tokens=self.max_tokens,
    messages=[{
        "role": "user",
        "content": f"{instructions}\n\n{context_data}"
    }]
)
```

**Audit Phase** (verse_parser.py:527-611):
```python
audit_prompt = """Review work against instructions...
- Check if follows all requirements
- Verify source citations
- Validate output format
"""

message = self.client.messages.create(
    model=self.model,
    max_tokens=2048,
    messages=[{"role": "user", "content": audit_prompt}]
)

# Passes if response starts with "PASS"
passed = feedback.strip().upper().startswith("PASS")
```

### Configuration

**Model Selection**:
```bash
# Use Opus for complex analysis (slower, more accurate)
python verse_parser.py --model claude-opus-4-20250514 --dataset verse --markdown analysis.md

# Use Haiku for simple tasks (faster, cheaper)
python verse_parser.py --model claude-haiku-4-20250430 --dataset verse --markdown simple.md

# Use Sonnet (default, balanced)
python verse_parser.py --dataset verse --markdown analysis.md
```

**Token Limits**:
```bash
# Increase for longer outputs
python verse_parser.py --max-tokens 8192 --dataset chapter --markdown detailed.md

# Decrease for shorter outputs
python verse_parser.py --max-tokens 2048 --dataset verse --markdown brief.md
```

### Error Handling

The implementation includes comprehensive error handling:
- **RateLimitError**: Logged and processing continues with next item
- **APIConnectionError**: Network issues are caught and logged
- **APIError**: General API errors are handled gracefully
- All errors are logged to the learning file for analysis

## Examples

### Example 1: Analyze First 10 Beatitudes

```bash
python verse_parser.py \
  --dataset verse \
  --markdown verse_analysis.md \
  --filter "MAT.005*" \
  --limit 10
```

### Example 2: Generate Chapter Summaries for Romans

```bash
python verse_parser.py \
  --dataset chapter \
  --markdown chapter_summary.md \
  --filter "ROM*"
```

### Example 3: Study Greek Words for Love

```bash
python verse_parser.py \
  --dataset strongs \
  --markdown love_word_study.md \
  --filter "G0025*"  # agapē family
```

### Example 4: Process All Gospels

```bash
# Matthew
python verse_parser.py --dataset book --markdown gospel_themes.md --filter "MAT"

# Mark (continue from previous)
python verse_parser.py --continue
# ... update filter to MRK in instruction file or run separately
```

## Troubleshooting

### Data Directory Not Found

```bash
# Run setup script
./setup-minimal-data.sh

# Or set custom location
export MYBIBLE_DATA_DIR=/path/to/data
```

### API Key Issues

```bash
# Set API key
export ANTHROPIC_API_KEY=your_key_here

# Or add to .env file
echo "ANTHROPIC_API_KEY=your_key_here" >> .env
```

### Sparse Checkout Errors

```bash
# Check current checkout
cd .data
git sparse-checkout list

# Reset if needed
git sparse-checkout disable
git sparse-checkout init --cone
git sparse-checkout set strongs commentary/MAT
```

## Advanced Usage

### Custom Data Processing

You can extend the script by:

1. Adding new dataset generators in `generate_*_dataset()` functions
2. Customizing data loading in `DataManager.load_*_data()` methods
3. Adding custom validation in `run_audit_session()`

### Batch Processing

Process multiple instruction files sequentially:

```bash
for instructions in instructions/*.md; do
  echo "Processing with $instructions"
  python verse_parser.py --dataset verse --markdown "$instructions" --limit 50
done
```

### Parallel Processing

Run multiple instances with different filters:

```bash
# Terminal 1: Process Old Testament
python verse_parser.py --dataset verse --markdown analysis.md --filter "GEN*"

# Terminal 2: Process New Testament
python verse_parser.py --dataset verse --markdown analysis.md --filter "MAT*"
```

## See Also

- `plan/verse-parser-script/README.md` - Detailed implementation plan
- `examples/sample_verse_instructions.md` - Sample instruction file
- `STANDARDIZATION.md` - Data format standards
- `SCHEMA.md` - YAML schema requirements
