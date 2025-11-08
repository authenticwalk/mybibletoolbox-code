#!/usr/bin/env python3
"""
Verse Parser Script with Claude Agent SDK

Processes Bible data (verses, chapters, books, or Strong's words) using Claude Agent SDK
with automated auditing and self-learning capabilities.

Usage:
    python verse_parser.py --dataset verse --markdown instructions.md --limit 100
    python verse_parser.py --dataset strongs --markdown analysis.md --continue
    python verse_parser.py --help
"""

import argparse
import json
import os
import random
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import yaml

# Import Anthropic SDK
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError

# Import project modules
from src.constants.bible import (
    BIBLE_STRUCTURE,
    format_verse_ref,
    get_all_verses,
    BOOK_NAMES
)


# ============================================================================
# Constants
# ============================================================================

PROGRESS_FILE = ".verse_parser_progress.json"
LEARNING_FILE = "verse_parser_learnings.md"

# Strong's number ranges
GREEK_STRONGS_MIN = 1
GREEK_STRONGS_MAX = 5624
HEBREW_STRONGS_MIN = 1
HEBREW_STRONGS_MAX = 8674


# ============================================================================
# Dataset Generators
# ============================================================================

def generate_verse_dataset(filter_pattern: Optional[str] = None) -> List[str]:
    """
    Generate list of all Bible verses.

    Args:
        filter_pattern: Optional filter (e.g., "MAT*" for Matthew only)

    Returns:
        List of verse references (e.g., ["GEN.001.001", "GEN.001.002", ...])
    """
    all_verses = get_all_verses()

    if filter_pattern:
        # Simple wildcard matching
        if filter_pattern.endswith("*"):
            prefix = filter_pattern[:-1]
            return [v for v in all_verses if v.startswith(prefix)]
        else:
            return [v for v in all_verses if v == filter_pattern]

    return all_verses


def generate_chapter_dataset(filter_pattern: Optional[str] = None) -> List[str]:
    """
    Generate list of all Bible chapters.

    Args:
        filter_pattern: Optional filter (e.g., "MAT*" for Matthew only)

    Returns:
        List of chapter references (e.g., ["GEN.001", "GEN.002", ...])
    """
    chapters = []

    books = BIBLE_STRUCTURE.keys()
    if filter_pattern:
        if filter_pattern.endswith("*"):
            prefix = filter_pattern[:-1]
            books = [b for b in books if b.startswith(prefix)]
        else:
            books = [filter_pattern] if filter_pattern in BIBLE_STRUCTURE else []

    for book in books:
        chapter_count = len(BIBLE_STRUCTURE[book])
        for chapter in range(1, chapter_count + 1):
            chapters.append(f"{book}.{chapter:03d}")

    return chapters


def generate_book_dataset(filter_pattern: Optional[str] = None) -> List[str]:
    """
    Generate list of all Bible books.

    Args:
        filter_pattern: Optional filter (e.g., "MAT" or "NT" for New Testament)

    Returns:
        List of book codes (e.g., ["GEN", "EXO", ...])
    """
    books = list(BIBLE_STRUCTURE.keys())

    if filter_pattern:
        if filter_pattern == "OT":
            # Old Testament (up to Malachi)
            return books[:39]
        elif filter_pattern == "NT":
            # New Testament (Matthew onwards)
            return books[39:]
        elif filter_pattern.endswith("*"):
            prefix = filter_pattern[:-1]
            return [b for b in books if b.startswith(prefix)]
        else:
            return [filter_pattern] if filter_pattern in books else []

    return books


def generate_strongs_dataset(filter_pattern: Optional[str] = None) -> List[str]:
    """
    Generate list of Strong's concordance numbers.

    Args:
        filter_pattern: Optional filter (e.g., "G*" for Greek only, "H*" for Hebrew)

    Returns:
        List of Strong's numbers (e.g., ["G0001", "G0002", ..., "H0001", ...])
    """
    strongs_numbers = []

    # Determine which to include
    include_greek = True
    include_hebrew = True

    if filter_pattern:
        if filter_pattern.startswith("G"):
            include_hebrew = False
        elif filter_pattern.startswith("H"):
            include_greek = False

    # Greek Strong's numbers (G0001-G5624)
    if include_greek:
        for num in range(GREEK_STRONGS_MIN, GREEK_STRONGS_MAX + 1):
            strongs_numbers.append(f"G{num:04d}")

    # Hebrew Strong's numbers (H0001-H8674)
    if include_hebrew:
        for num in range(HEBREW_STRONGS_MIN, HEBREW_STRONGS_MAX + 1):
            strongs_numbers.append(f"H{num:04d}")

    return strongs_numbers


# ============================================================================
# Progress Tracking
# ============================================================================

class ProgressTracker:
    """Manages progress state for resumable processing."""

    def __init__(self, progress_file: str = PROGRESS_FILE):
        self.progress_file = Path(progress_file)
        self.state = self._load_state()

    def _load_state(self) -> Dict:
        """Load progress state from file."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {}

    def save_state(self):
        """Save current state to file."""
        self.state["last_updated"] = datetime.utcnow().isoformat() + "Z"
        with open(self.progress_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def initialize(self, dataset_type: str, markdown_file: str, items: List[str]):
        """Initialize new progress tracking."""
        self.state = {
            "dataset_type": dataset_type,
            "markdown_file": markdown_file,
            "total_items": len(items),
            "completed_items": 0,
            "failed_items": 0,
            "items_list": items,
            "completed": [],
            "failed": [],
            "current_index": 0,
            "started_at": datetime.utcnow().isoformat() + "Z",
            "last_updated": datetime.utcnow().isoformat() + "Z"
        }
        self.save_state()

    def mark_completed(self, item: str):
        """Mark an item as completed."""
        if item not in self.state.get("completed", []):
            self.state.setdefault("completed", []).append(item)
            self.state["completed_items"] = len(self.state["completed"])
            self.state["current_index"] += 1
            self.save_state()

    def mark_failed(self, item: str, error: str):
        """Mark an item as failed."""
        if item not in self.state.get("failed", []):
            self.state.setdefault("failed", []).append({
                "item": item,
                "error": error,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
            self.state["failed_items"] = len(self.state["failed"])
            self.state["current_index"] += 1
            self.save_state()

    def get_remaining_items(self) -> List[str]:
        """Get list of items not yet processed."""
        completed = set(self.state.get("completed", []))
        failed_items = set(f["item"] for f in self.state.get("failed", []))
        processed = completed | failed_items

        return [item for item in self.state.get("items_list", [])
                if item not in processed]

    def can_continue(self) -> bool:
        """Check if there's a previous run that can be continued."""
        return bool(self.state and "items_list" in self.state)

    def print_status(self):
        """Print current progress status."""
        if not self.state:
            print("No progress data found.")
            return

        total = self.state.get("total_items", 0)
        completed = self.state.get("completed_items", 0)
        failed = self.state.get("failed_items", 0)
        remaining = total - completed - failed

        print(f"\nProgress Status:")
        print(f"  Dataset: {self.state.get('dataset_type', 'unknown')}")
        print(f"  Total items: {total}")
        print(f"  Completed: {completed} ({100*completed/total if total > 0 else 0:.1f}%)")
        print(f"  Failed: {failed}")
        print(f"  Remaining: {remaining}")
        print(f"  Started: {self.state.get('started_at', 'unknown')}")
        print()


# ============================================================================
# Data Management
# ============================================================================

class DataManager:
    """Manages git sparse-checkout and data loading."""

    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            # Import here to avoid early initialization
            from src.config import DATA_DIR
            data_dir = DATA_DIR
        self.data_dir = data_dir
        self.commentary_dir = data_dir / "commentary"
        self.strongs_dir = data_dir / "strongs"

    def checkout_verse_data(self, verse_ref: str):
        """
        Checkout data for a specific verse using git sparse-checkout.

        Args:
            verse_ref: Verse reference (e.g., "MAT.005.003")
        """
        book, chapter, verse = verse_ref.split(".")
        pattern = f"commentary/{book}/{chapter}/{verse}"

        self._add_sparse_pattern(pattern)

    def checkout_chapter_data(self, chapter_ref: str):
        """
        Checkout data for a specific chapter.

        Args:
            chapter_ref: Chapter reference (e.g., "MAT.005")
        """
        book, chapter = chapter_ref.split(".")
        pattern = f"commentary/{book}/{chapter}"

        self._add_sparse_pattern(pattern)

    def checkout_book_data(self, book_code: str):
        """
        Checkout data for a specific book.

        Args:
            book_code: Book code (e.g., "MAT")
        """
        pattern = f"commentary/{book_code}"

        self._add_sparse_pattern(pattern)

    def checkout_strongs_data(self, strongs_num: str):
        """
        Checkout data for a Strong's number.

        Args:
            strongs_num: Strong's number (e.g., "G0026")
        """
        pattern = f"strongs/{strongs_num}"

        self._add_sparse_pattern(pattern)

    def _add_sparse_pattern(self, pattern: str):
        """Add a pattern to git sparse-checkout."""
        try:
            subprocess.run(
                ["git", "sparse-checkout", "add", pattern],
                cwd=self.data_dir,
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to checkout {pattern}: {e.stderr.decode()}")

    def load_verse_data(self, verse_ref: str) -> Dict:
        """
        Load all YAML data for a verse.

        Args:
            verse_ref: Verse reference (e.g., "MAT.005.003")

        Returns:
            Dictionary with all verse data combined
        """
        book, chapter, verse = verse_ref.split(".")
        verse_dir = self.commentary_dir / book / chapter / verse

        if not verse_dir.exists():
            return {"verse": verse_ref, "data": {}, "note": "No data files found"}

        combined_data = {"verse": verse_ref, "files": {}}

        # Load all YAML files in the verse directory
        for yaml_file in verse_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                    combined_data["files"][yaml_file.name] = data
            except Exception as e:
                print(f"Warning: Failed to load {yaml_file}: {e}")

        return combined_data

    def load_chapter_data(self, chapter_ref: str) -> Dict:
        """Load all YAML data for a chapter."""
        book, chapter = chapter_ref.split(".")
        chapter_dir = self.commentary_dir / book / chapter

        if not chapter_dir.exists():
            return {"chapter": chapter_ref, "data": {}, "note": "No data files found"}

        combined_data = {"chapter": chapter_ref, "verses": {}}

        # Load all verses in the chapter
        for verse_dir in sorted(chapter_dir.iterdir()):
            if verse_dir.is_dir():
                verse_ref = f"{book}.{chapter}.{verse_dir.name}"
                combined_data["verses"][verse_dir.name] = self.load_verse_data(verse_ref)

        return combined_data

    def load_book_data(self, book_code: str) -> Dict:
        """Load all YAML data for a book."""
        book_dir = self.commentary_dir / book_code

        if not book_dir.exists():
            return {"book": book_code, "data": {}, "note": "No data files found"}

        combined_data = {"book": book_code, "chapters": {}}

        # Load all chapters in the book
        for chapter_dir in sorted(book_dir.iterdir()):
            if chapter_dir.is_dir():
                chapter_ref = f"{book_code}.{chapter_dir.name}"
                combined_data["chapters"][chapter_dir.name] = self.load_chapter_data(chapter_ref)

        return combined_data

    def load_strongs_data(self, strongs_num: str) -> Dict:
        """Load all YAML data for a Strong's number."""
        strongs_dir = self.strongs_dir / strongs_num

        if not strongs_dir.exists():
            return {"strongs": strongs_num, "data": {}, "note": "No data files found"}

        combined_data = {"strongs": strongs_num, "files": {}}

        # Load all YAML files for this Strong's number
        for yaml_file in strongs_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                    combined_data["files"][yaml_file.name] = data
            except Exception as e:
                print(f"Warning: Failed to load {yaml_file}: {e}")

        return combined_data


# ============================================================================
# Claude SDK Integration
# ============================================================================

class ClaudeAgentRunner:
    """Manages Claude API sessions for processing and auditing."""

    def __init__(self, markdown_file: Path, model: str = "claude-sonnet-4-5-20250929"):
        self.markdown_file = markdown_file
        self.instructions = self._load_instructions()
        self.model = model
        self.max_tokens = 4096

        # Initialize Anthropic client
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is required. "
                "Set it with: export ANTHROPIC_API_KEY=your_key_here"
            )
        self.client = Anthropic(api_key=api_key)

    def _load_instructions(self) -> str:
        """Load instructions from markdown file."""
        if not self.markdown_file.exists():
            raise FileNotFoundError(f"Markdown file not found: {self.markdown_file}")

        with open(self.markdown_file, 'r') as f:
            return f.read()

    def run_processing_session(self, item: str, context_data: Dict) -> Tuple[bool, str, Optional[str]]:
        """
        Run a processing session for an item using Claude API.

        Args:
            item: Item reference (verse, chapter, book, or Strong's number)
            context_data: Data loaded for this item

        Returns:
            Tuple of (success, output, error_message)
        """
        try:
            print(f"  [Processing] {item}")
            print(f"    Instructions: {len(self.instructions)} chars")
            print(f"    Context data: {len(str(context_data))} chars")

            # Build the user message with instructions + context
            context_str = json.dumps(context_data, indent=2, ensure_ascii=False)
            user_message = f"""{self.instructions}

# Context Data

The following data has been loaded for {item}:

```json
{context_str}
```

Please process this data according to the instructions above.
"""

            # Call Claude API
            print(f"    Calling Claude API (model: {self.model})...")
            message = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            # Extract text response
            output = ""
            for block in message.content:
                if hasattr(block, 'text'):
                    output += block.text

            print(f"    ✓ Received response ({message.usage.input_tokens} in, {message.usage.output_tokens} out)")

            return True, output, None

        except RateLimitError as e:
            error_msg = f"Rate limit exceeded: {str(e)}"
            print(f"    ✗ {error_msg}")
            return False, "", error_msg

        except APIConnectionError as e:
            error_msg = f"API connection error: {str(e)}"
            print(f"    ✗ {error_msg}")
            return False, "", error_msg

        except APIError as e:
            error_msg = f"API error: {str(e)}"
            print(f"    ✗ {error_msg}")
            return False, "", error_msg

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"    ✗ {error_msg}")
            return False, "", error_msg

    def run_audit_session(self, item: str, output: str, context_data: Dict) -> Tuple[bool, str]:
        """
        Run an audit session to validate completed work using Claude API.

        Args:
            item: Item reference
            output: Output from processing session
            context_data: Original context data

        Returns:
            Tuple of (passed, feedback)
        """
        try:
            print(f"  [Auditing] {item}")

            # Build audit prompt
            context_str = json.dumps(context_data, indent=2, ensure_ascii=False)
            audit_prompt = f"""You are an expert reviewer validating work against specific instructions.

# Original Instructions

{self.instructions}

# Context Data

```json
{context_str}
```

# Completed Work

```
{output}
```

# Your Task

Review the completed work carefully and check if it:
1. Follows all instructions from the original task
2. Uses the provided context data appropriately
3. Adheres to cited standards (STANDARDIZATION.md, SCHEMA.md, etc.)
4. Includes proper source citations
5. Avoids fabrication or hallucination
6. Produces the expected output format

Respond with:
- "PASS" if the work meets all requirements
- "FAIL" followed by specific issues if there are problems

Be thorough but concise in identifying issues.
"""

            # Call Claude API for audit
            print(f"    Calling Claude API for audit...")
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                messages=[
                    {
                        "role": "user",
                        "content": audit_prompt
                    }
                ]
            )

            # Extract audit response
            feedback = ""
            for block in message.content:
                if hasattr(block, 'text'):
                    feedback += block.text

            # Determine if passed
            passed = feedback.strip().upper().startswith("PASS")

            if passed:
                print(f"    ✓ Audit passed")
            else:
                print(f"    ✗ Audit failed")

            return passed, feedback

        except Exception as e:
            error_msg = f"Audit error: {str(e)}"
            print(f"    ✗ {error_msg}")
            return False, error_msg


# ============================================================================
# Learning System
# ============================================================================

class LearningLogger:
    """Logs failures and learnings for continuous improvement."""

    def __init__(self, learning_file: str = LEARNING_FILE):
        self.learning_file = Path(learning_file)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create learning file if it doesn't exist."""
        if not self.learning_file.exists():
            with open(self.learning_file, 'w') as f:
                f.write("# Verse Parser Learnings\n\n")
                f.write("Auto-generated log of failures and learnings.\n\n")

    def log_failure(self, item: str, error: str, context: Dict):
        """
        Log a processing failure.

        Args:
            item: Item that failed
            error: Error message
            context: Additional context about the failure
        """
        timestamp = datetime.utcnow().isoformat() + "Z"

        with open(self.learning_file, 'a') as f:
            f.write(f"\n## Failure: {item}\n\n")
            f.write(f"**Timestamp**: {timestamp}\n\n")
            f.write(f"**Error**: {error}\n\n")

            if context:
                f.write("**Context**:\n")
                f.write(f"```json\n{json.dumps(context, indent=2)}\n```\n\n")

            f.write("---\n")

    def log_audit_failure(self, item: str, feedback: str, output: str):
        """
        Log an audit failure.

        Args:
            item: Item that failed audit
            feedback: Audit feedback
            output: Original output that failed
        """
        timestamp = datetime.utcnow().isoformat() + "Z"

        with open(self.learning_file, 'a') as f:
            f.write(f"\n## Audit Failure: {item}\n\n")
            f.write(f"**Timestamp**: {timestamp}\n\n")
            f.write(f"**Audit Feedback**: {feedback}\n\n")
            f.write(f"**Output**:\n```\n{output[:500]}...\n```\n\n")
            f.write("---\n")


# ============================================================================
# Main Processing Logic
# ============================================================================

def process_items(
    dataset_type: str,
    items: List[str],
    markdown_file: Path,
    progress_tracker: ProgressTracker,
    data_manager: DataManager,
    agent_runner: ClaudeAgentRunner,
    learning_logger: LearningLogger,
    skip_audit: bool = False
):
    """
    Main processing loop for items.

    Args:
        dataset_type: Type of dataset (verse, chapter, book, strongs)
        items: List of items to process
        markdown_file: Path to markdown instruction file
        progress_tracker: Progress tracking instance
        data_manager: Data management instance
        agent_runner: Claude agent runner instance
        learning_logger: Learning logger instance
    """
    total = len(items)

    for idx, item in enumerate(items, 1):
        print(f"\n[{idx}/{total}] Processing: {item}")

        try:
            # 1. Checkout data
            if dataset_type == "verse":
                data_manager.checkout_verse_data(item)
                context_data = data_manager.load_verse_data(item)
            elif dataset_type == "chapter":
                data_manager.checkout_chapter_data(item)
                context_data = data_manager.load_chapter_data(item)
            elif dataset_type == "book":
                data_manager.checkout_book_data(item)
                context_data = data_manager.load_book_data(item)
            elif dataset_type == "strongs":
                data_manager.checkout_strongs_data(item)
                context_data = data_manager.load_strongs_data(item)
            else:
                raise ValueError(f"Unknown dataset type: {dataset_type}")

            # 2. Run processing session
            success, output, error = agent_runner.run_processing_session(item, context_data)

            if not success:
                print(f"  ❌ Processing failed: {error}")
                progress_tracker.mark_failed(item, error)
                learning_logger.log_failure(item, error, {"dataset_type": dataset_type})
                continue

            # 3. Run audit session (if not skipped)
            if not skip_audit:
                passed, feedback = agent_runner.run_audit_session(item, output, context_data)

                if not passed:
                    print(f"  ❌ Audit failed: {feedback}")
                    progress_tracker.mark_failed(item, f"Audit failed: {feedback}")
                    learning_logger.log_audit_failure(item, feedback, output)
                    continue
            else:
                print(f"  ⚠️  Skipping audit (--no-audit enabled)")

            # 4. Mark as completed
            print(f"  ✅ Completed successfully")
            progress_tracker.mark_completed(item)

        except Exception as e:
            print(f"  ❌ Unexpected error: {e}")
            progress_tracker.mark_failed(item, str(e))
            learning_logger.log_failure(item, str(e), {"dataset_type": dataset_type})

    # Print final summary
    progress_tracker.print_status()


# ============================================================================
# CLI Entry Point
# ============================================================================

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Process Bible data using Claude Agent SDK with automated auditing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process 100 random verses
  python verse_parser.py --dataset verse --markdown instructions.md --limit 100

  # Process all Strong's Greek words
  python verse_parser.py --dataset strongs --markdown analysis.md --filter "G*"

  # Continue interrupted run
  python verse_parser.py --continue

  # Start fresh
  python verse_parser.py --dataset verse --markdown new.md --redo-all
        """
    )

    parser.add_argument(
        "--dataset",
        choices=["verse", "chapter", "book", "strongs"],
        help="Type of dataset to process"
    )

    parser.add_argument(
        "--markdown",
        type=Path,
        help="Path to markdown instruction file"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Number of items to process (default: 100, -1 for all)"
    )

    parser.add_argument(
        "--filter",
        type=str,
        help="Filter pattern (e.g., 'MAT*' for Matthew, 'G*' for Greek)"
    )

    parser.add_argument(
        "--continue",
        dest="continue_run",
        action="store_true",
        help="Continue from previous run"
    )

    parser.add_argument(
        "--redo-all",
        dest="redo_all",
        action="store_true",
        help="Start fresh, ignoring previous progress"
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Show current progress status and exit"
    )

    parser.add_argument(
        "--model",
        type=str,
        default="claude-sonnet-4-5-20250929",
        help="Claude model to use (default: claude-sonnet-4-5-20250929)"
    )

    parser.add_argument(
        "--no-audit",
        dest="skip_audit",
        action="store_true",
        help="Skip the audit phase (faster but less validated)"
    )

    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        help="Maximum tokens for Claude responses (default: 4096)"
    )

    args = parser.parse_args()

    # Initialize progress tracker
    progress_tracker = ProgressTracker()

    # Show status if requested
    if args.status:
        progress_tracker.print_status()
        return

    # Handle continue mode
    if args.continue_run:
        if not progress_tracker.can_continue():
            print("Error: No previous run found to continue.")
            sys.exit(1)

        print("Continuing previous run...")
        progress_tracker.print_status()

        # Get configuration from previous run
        dataset_type = progress_tracker.state["dataset_type"]
        markdown_file = Path(progress_tracker.state["markdown_file"])
        items = progress_tracker.get_remaining_items()

        if not items:
            print("No remaining items to process.")
            return

    else:
        # New run - validate arguments
        if not args.dataset or not args.markdown:
            parser.error("--dataset and --markdown are required for new runs")

        dataset_type = args.dataset
        markdown_file = args.markdown

        # Validate markdown file exists
        if not markdown_file.exists():
            print(f"Error: Markdown file not found: {markdown_file}")
            sys.exit(1)

        # Generate dataset
        print(f"Generating {dataset_type} dataset...")

        if dataset_type == "verse":
            all_items = generate_verse_dataset(args.filter)
        elif dataset_type == "chapter":
            all_items = generate_chapter_dataset(args.filter)
        elif dataset_type == "book":
            all_items = generate_book_dataset(args.filter)
        elif dataset_type == "strongs":
            all_items = generate_strongs_dataset(args.filter)

        print(f"  Total items in dataset: {len(all_items)}")

        # Shuffle for random order
        random.shuffle(all_items)

        # Apply limit
        if args.limit > 0:
            items = all_items[:args.limit]
            print(f"  Limited to: {len(items)} items")
        else:
            items = all_items

        # Initialize progress tracking (unless redo-all with existing progress)
        if args.redo_all or not progress_tracker.can_continue():
            progress_tracker.initialize(dataset_type, str(markdown_file), items)
        else:
            # Ask user if they want to continue or start fresh
            response = input("Previous run found. Continue? (y/n): ").lower()
            if response == 'y':
                items = progress_tracker.get_remaining_items()
                if not items:
                    print("No remaining items to process.")
                    return
            else:
                progress_tracker.initialize(dataset_type, str(markdown_file), items)

    # Initialize components
    data_manager = DataManager()
    agent_runner = ClaudeAgentRunner(
        markdown_file,
        model=args.model if hasattr(args, 'model') else "claude-sonnet-4-5-20250929"
    )

    # Update max_tokens if specified
    if hasattr(args, 'max_tokens'):
        agent_runner.max_tokens = args.max_tokens

    learning_logger = LearningLogger()

    # Store skip_audit setting
    skip_audit = args.skip_audit if hasattr(args, 'skip_audit') else False

    # Process items
    print(f"\nStarting processing of {len(items)} items...\n")
    print("=" * 60)

    try:
        process_items(
            dataset_type,
            items,
            markdown_file,
            progress_tracker,
            data_manager,
            agent_runner,
            learning_logger,
            skip_audit
        )
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        print("Progress has been saved. Use --continue to resume.")
        sys.exit(0)

    print("\n" + "=" * 60)
    print("Processing complete!")
    print(f"\nLearnings logged to: {LEARNING_FILE}")
    print(f"Progress saved to: {PROGRESS_FILE}")


if __name__ == "__main__":
    main()
