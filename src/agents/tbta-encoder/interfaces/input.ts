/**
 * Input interfaces for TBTA encoder
 */

/**
 * Basic verse input for encoding
 * @property reference - USFM format reference (e.g., MAT.002.001 or "MAT 2:1")
 * @property verse - NIV text (optional - agent will fetch if missing)
 */
export interface VerseInput {
  reference: string;
  verse?: string;
}

/**
 * Human-labeled input for diagnostic mode
 * Extends VerseInput with encoding comparison fields
 */
export interface LabeledInput extends VerseInput {
  /** The draft encoding produced by the agent */
  draft_phase_1_encoding: string;
  /** The correct/reference encoding from human labeler */
  phase_1_encoding: string;
  /** Optional explanation of differences or issues */
  explanation?: string;
}

/**
 * Parse a line of JSONL input into VerseInput or LabeledInput
 */
export function parseInputLine(line: string): VerseInput | LabeledInput {
  const trimmed = line.trim();
  if (!trimmed) {
    throw new Error('Empty input line');
  }

  try {
    const parsed = JSON.parse(trimmed);
    if (!parsed.reference || typeof parsed.reference !== 'string') {
      throw new Error('Missing or invalid "reference" field');
    }
    return parsed as VerseInput | LabeledInput;
  } catch (e) {
    // Not JSON - treat as plain text reference (e.g., "MAT 2:1-10")
    return { reference: trimmed };
  }
}

/**
 * Check if input is a LabeledInput (has phase_1_encoding field)
 */
export function isLabeledInput(input: VerseInput | LabeledInput): input is LabeledInput {
  return 'phase_1_encoding' in input && typeof (input as LabeledInput).phase_1_encoding === 'string';
}

