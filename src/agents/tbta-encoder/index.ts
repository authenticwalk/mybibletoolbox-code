#!/usr/bin/env node
/**
 * TBTA Encoder Agent
 * 
 * Encodes NIV Bible verses to He1 format using Claude Agent SDK.
 * 
 * Usage:
 *   npx ts-node index.ts "MAT 2:1-10"           # Text reference
 *   cat verses.jsonl | npx ts-node index.ts    # Stdin JSONL
 *   cat labeled.jsonl | npx ts-node index.ts --diagnose  # Diagnostic mode
 */

import { query, type SDKMessage, type SDKResultMessage } from '@anthropic-ai/claude-agent-sdk';
import { readFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { createInterface } from 'readline';

import {
  type VerseInput,
  type LabeledInput,
  type EncodingOutput,
  type DiagnosticOutput,
  parseInputLine,
  isLabeledInput,
  formatOutput,
} from './interfaces/index.js';

/**
 * Log to stderr (doesn't pollute JSONL output on stdout)
 */
function log(message: string): void {
  console.error(`[tbta-encoder] ${message}`);
}

// Get the directory of this script
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Path to SKILL.md relative to this script
const SKILL_MD_PATH = join(__dirname, '../../../bible-study-tools/tbta/phase1/policies/SKILL.md');

/**
 * Load SKILL.md content as the orchestrator prompt
 */
function loadSkillPrompt(): string {
  log(`Loading SKILL.md from ${SKILL_MD_PATH}`);
  try {
    const content = readFileSync(SKILL_MD_PATH, 'utf-8');
    log(`Loaded SKILL.md (${content.length} chars)`);
    return content;
  } catch (error) {
    log(`ERROR: Failed to load SKILL.md: ${error}`);
    process.exit(1);
  }
}

/**
 * Build the prompt for the agent
 */
function buildPrompt(skillContent: string, input: VerseInput | LabeledInput, diagnoseMode: boolean): string {
  let prompt = skillContent + '\n\n---\n\n# Current Task\n\n';

  if (isLabeledInput(input)) {
    // Diagnostic mode with human labels
    prompt += `## Mode: Diagnostic Analysis\n\n`;
    prompt += `**Reference**: ${input.reference}\n`;
    if (input.verse) {
      prompt += `**Verse Text**: ${input.verse}\n`;
    }
    prompt += `**Draft Encoding**: ${input.draft_phase_1_encoding}\n`;
    prompt += `**Correct Encoding**: ${input.phase_1_encoding}\n`;
    if (input.explanation) {
      prompt += `**Explanation**: ${input.explanation}\n`;
    }
    prompt += `\n**Task**: Analyze why the draft differs from the correct encoding. `;
    prompt += `Focus on step-by-step diagnosis. Identify which subagent approach(es) would have produced the wrong result. `;
    prompt += `Suggest specific learnings updates.\n`;
  } else if (diagnoseMode) {
    // Regular input but in diagnose mode
    prompt += `## Mode: Diagnostic (Verbose)\n\n`;
    prompt += `**Reference**: ${input.reference}\n`;
    if (input.verse) {
      prompt += `**Verse Text**: ${input.verse}\n`;
    }
    prompt += `\n**Task**: Encode this verse to He1 with detailed step-by-step output. `;
    prompt += `Show reasoning for each transformation.\n`;
  } else {
    // Standard encoding mode
    prompt += `## Mode: Standard Encoding\n\n`;
    prompt += `**Reference**: ${input.reference}\n`;
    if (input.verse) {
      prompt += `**Verse Text**: ${input.verse}\n`;
    }
    prompt += `\n**Task**: Encode this verse to He1. Return the best encoding.\n`;
  }

  return prompt;
}

/**
 * Extract the result from the SDK message stream
 */
function extractResult(resultMessage: SDKResultMessage): { encoding?: string; error?: string } {
  if (resultMessage.subtype === 'success') {
    // Try to extract the encoding from the result text
    const result = resultMessage.result;
    
    // Look for "Final He1" or similar patterns in the result
    const finalMatch = result.match(/(?:Final He1|draft_phase_1_encoding)[:\s]*["']?([^"'\n]+)["']?/i);
    if (finalMatch) {
      return { encoding: finalMatch[1].trim() };
    }
    
    // If no specific pattern found, return the whole result
    return { encoding: result };
  } else {
    // Error case
    return { error: resultMessage.errors?.join('; ') || 'Unknown error' };
  }
}

/**
 * Process a single input and return the output
 */
async function processInput(
  input: VerseInput | LabeledInput,
  skillPrompt: string,
  diagnoseMode: boolean
): Promise<EncodingOutput | DiagnosticOutput> {
  const mode = isLabeledInput(input) ? 'diagnostic-labeled' : diagnoseMode ? 'diagnostic-verbose' : 'standard';
  log(`Processing ${input.reference} (mode: ${mode})`);
  
  const prompt = buildPrompt(skillPrompt, input, diagnoseMode);
  log(`Built prompt (${prompt.length} chars)`);

  try {
    log(`Starting agent query...`);
    const stream = query({
      prompt,
      options: {
        permissionMode: 'bypassPermissions', // Allow agent to use tools without prompting
      },
    });

    let resultMessage: SDKResultMessage | null = null;
    let messageCount = 0;

    // Iterate through the message stream
    for await (const message of stream) {
      messageCount++;
      
      // Log progress for different message types
      if (message.type === 'system' && 'subtype' in message && message.subtype === 'init') {
        log(`Agent initialized (model: ${(message as any).model || 'unknown'})`);
      } else if (message.type === 'assistant') {
        log(`Received assistant message`);
      } else if (message.type === 'result') {
        resultMessage = message as SDKResultMessage;
        log(`Received result (subtype: ${resultMessage.subtype})`);
      }
    }

    log(`Stream complete (${messageCount} messages)`);

    if (!resultMessage) {
      log(`ERROR: No result message received`);
      return {
        reference: input.reference,
        verse: input.verse,
        draft_phase_1_encoding: '',
        error: 'No result received from agent',
      };
    }

    const { encoding, error } = extractResult(resultMessage);

    if (error) {
      log(`Agent returned error: ${error}`);
    } else {
      log(`Got encoding (${encoding?.length || 0} chars)`);
    }

    if (isLabeledInput(input)) {
      // Diagnostic output
      const output: DiagnosticOutput = {
        reference: input.reference,
        verse: input.verse,
        draft_phase_1_encoding: encoding || input.draft_phase_1_encoding,
        phase_1_encoding: input.phase_1_encoding,
        matches: encoding === input.phase_1_encoding,
        error,
      };
      return output;
    } else {
      // Standard output
      const output: EncodingOutput = {
        reference: input.reference,
        verse: input.verse,
        draft_phase_1_encoding: encoding || '',
        error,
      };
      return output;
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    log(`ERROR: ${errorMessage}`);
    return {
      reference: input.reference,
      verse: input.verse,
      draft_phase_1_encoding: '',
      error: errorMessage,
    };
  }
}

/**
 * Read input from stdin
 */
async function readStdin(): Promise<string[]> {
  return new Promise((resolve) => {
    const lines: string[] = [];
    const rl = createInterface({
      input: process.stdin,
      terminal: false,
    });

    rl.on('line', (line) => {
      if (line.trim()) {
        lines.push(line);
      }
    });

    rl.on('close', () => {
      resolve(lines);
    });

    // If stdin is a TTY (interactive), resolve immediately with empty array
    if (process.stdin.isTTY) {
      resolve([]);
    }
  });
}

/**
 * Main entry point
 */
async function main(): Promise<void> {
  log(`Starting tbta-encoder`);
  
  const args = process.argv.slice(2);
  const diagnoseMode = args.includes('--diagnose') || args.includes('-d');
  const filteredArgs = args.filter((arg) => arg !== '--diagnose' && arg !== '-d');

  if (diagnoseMode) {
    log(`Diagnostic mode enabled`);
  }

  // Load the skill prompt
  const skillPrompt = loadSkillPrompt();

  // Collect inputs
  const inputs: (VerseInput | LabeledInput)[] = [];

  // Check for CLI argument input
  if (filteredArgs.length > 0) {
    // CLI argument: treat as text reference
    const reference = filteredArgs.join(' ');
    log(`Input from CLI: "${reference}"`);
    inputs.push({ reference });
  } else {
    // Read from stdin
    log(`Reading from stdin...`);
    const stdinLines = await readStdin();
    log(`Read ${stdinLines.length} lines from stdin`);
    for (const line of stdinLines) {
      try {
        inputs.push(parseInputLine(line));
      } catch (error) {
        log(`Error parsing line: ${line}`);
      }
    }
  }

  if (inputs.length === 0) {
    console.error('Usage:');
    console.error('  npx tsx index.ts "MAT 2:1-10"           # Text reference');
    console.error('  cat verses.jsonl | npx tsx index.ts    # Stdin JSONL');
    console.error('  cat labeled.jsonl | npx tsx index.ts --diagnose  # Diagnostic mode');
    process.exit(1);
  }

  log(`Processing ${inputs.length} input(s)`);

  // Process each input
  for (let i = 0; i < inputs.length; i++) {
    const input = inputs[i];
    log(`\n--- Input ${i + 1}/${inputs.length} ---`);
    const output = await processInput(input, skillPrompt, diagnoseMode);
    console.log(formatOutput(output));
  }

  log(`\nComplete!`);
}

// Run main
main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});

