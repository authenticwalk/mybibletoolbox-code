/**
 * Output interfaces for TBTA encoder
 */

import type { VerseInput } from './input.js';

/**
 * Standard encoding output
 * Extends VerseInput with the generated encoding
 */
export interface EncodingOutput extends VerseInput {
  /** The He1 encoding produced by the agent */
  draft_phase_1_encoding: string;
  /** Error message if encoding failed */
  error?: string;
}

/**
 * Diagnostic output for human-labeled comparison mode
 */
export interface DiagnosticOutput extends EncodingOutput {
  /** The correct/reference encoding from human labeler */
  phase_1_encoding: string;
  /** Whether the draft matches the reference */
  matches: boolean;
  /** Diagnostic analysis from the agent */
  diagnosis?: string;
  /** Suggested learnings updates */
  suggested_learnings?: string;
}

/**
 * Format output as JSONL line
 */
export function formatOutput(output: EncodingOutput | DiagnosticOutput): string {
  return JSON.stringify(output);
}

