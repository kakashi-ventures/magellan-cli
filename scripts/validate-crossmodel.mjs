#!/usr/bin/env node
// Cross-Model Hypothesis Validation Script
// Calls OpenAI (GPT-5.4 Pro) and Google Gemini (3.1 Pro) APIs in parallel
// for independent validation of MAGELLAN hypotheses.
//
// Usage:
//   node scripts/validate-crossmodel.mjs \
//     --gpt-prompt <file> --gpt-out <file> \
//     --gemini-prompt <file> --gemini-out <file>
//
// Environment:
//   OPENAI_API_KEY  — required for GPT validation
//   GEMINI_API_KEY  — required for Gemini validation
//   At least one must be set.

import { readFileSync, writeFileSync } from 'fs';

// ---------------------------------------------------------------------------
// Argument parsing
// ---------------------------------------------------------------------------
const args = process.argv.slice(2);
const getArg = (flag) => {
  const idx = args.indexOf(flag);
  return idx >= 0 && idx + 1 < args.length ? args[idx + 1] : null;
};

const gptPromptFile   = getArg('--gpt-prompt');
const gptOutFile      = getArg('--gpt-out');
const geminiPromptFile = getArg('--gemini-prompt');
const geminiOutFile    = getArg('--gemini-out');

// ---------------------------------------------------------------------------
// OpenAI — GPT-5.4 Pro with reasoning effort high
// ---------------------------------------------------------------------------
async function callOpenAI(promptFile, outputFile) {
  const { default: OpenAI } = await import('openai');
  const client = new OpenAI(); // reads OPENAI_API_KEY from env

  const prompt = readFileSync(promptFile, 'utf8');
  const start = Date.now();

  process.stderr.write('[OpenAI] Calling gpt-5.4-pro (reasoning: high)...\n');

  const response = await client.responses.create({
    model: 'gpt-5.4-pro',
    input: [
      {
        role: 'user',
        content: [{ type: 'input_text', text: prompt }],
      },
    ],
    reasoning: { effort: 'high', summary: 'auto' },
  });

  // Extract text from output
  const messageItem = response.output.find(o => o.type === 'message');
  const text = messageItem?.content?.[0]?.text
    || JSON.stringify(response.output, null, 2);

  // Extract reasoning summary if available
  const reasoningItem = response.output.find(o => o.type === 'reasoning');
  let reasoningSummary = '';
  if (reasoningItem?.summary) {
    reasoningSummary = reasoningItem.summary
      .map(s => s.text)
      .join('\n');
  }

  // Extract annotations/citations if present
  const annotations = messageItem?.content?.[0]?.annotations || [];

  const duration = Math.round((Date.now() - start) / 1000);
  process.stderr.write(`[OpenAI] Completed in ${duration}s\n`);

  // Write full output
  let output = '';
  if (reasoningSummary) {
    output += `## GPT-5.4 Pro Reasoning Summary\n\n${reasoningSummary}\n\n---\n\n`;
  }
  output += text;
  if (annotations.length > 0) {
    output += '\n\n---\n\n## Citations\n\n';
    for (const a of annotations) {
      if (a.url) output += `- [${a.title || 'Source'}](${a.url})\n`;
    }
  }

  writeFileSync(outputFile, output);
  return {
    status: 'completed',
    model: 'gpt-5.4-pro',
    duration_s: duration,
    citations: annotations.length,
    has_reasoning: !!reasoningSummary,
  };
}

// ---------------------------------------------------------------------------
// Google Gemini — 3.1 Pro with thinking HIGH
// ---------------------------------------------------------------------------
async function callGemini(promptFile, outputFile) {
  const { GoogleGenAI } = await import('@google/genai');
  const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

  const prompt = readFileSync(promptFile, 'utf8');
  const start = Date.now();

  process.stderr.write('[Gemini] Calling gemini-3.1-pro (thinking: HIGH)...\n');

  const response = await ai.models.generateContent({
    model: 'gemini-3.1-pro',
    contents: prompt,
    config: {
      thinkingConfig: {
        thinkingLevel: 'HIGH',
        includeThoughts: true,
      },
    },
  });

  // Extract thoughts and answer from response parts
  let thoughts = '';
  let answer = '';

  const parts = response.candidates?.[0]?.content?.parts || [];
  for (const part of parts) {
    if (part.thought) {
      thoughts += part.text + '\n';
    } else if (part.text) {
      answer += part.text;
    }
  }

  // Fallback: use response.text if parts parsing yielded nothing
  if (!answer && response.text) {
    answer = response.text;
  }

  const duration = Math.round((Date.now() - start) / 1000);
  process.stderr.write(`[Gemini] Completed in ${duration}s\n`);

  // Write full output
  let output = '';
  if (thoughts) {
    output += `## Gemini Thinking Process\n\n${thoughts}\n---\n\n`;
  }
  output += answer;

  writeFileSync(outputFile, output);
  return {
    status: 'completed',
    model: 'gemini-3.1-pro',
    duration_s: duration,
    has_thoughts: !!thoughts,
  };
}

// ---------------------------------------------------------------------------
// Main — run both in parallel
// ---------------------------------------------------------------------------
async function main() {
  const results = {};
  const errors = {};
  const tasks = [];

  // OpenAI task
  if (gptPromptFile && gptOutFile) {
    if (process.env.OPENAI_API_KEY) {
      tasks.push(
        callOpenAI(gptPromptFile, gptOutFile)
          .then(r => { results.openai = r; })
          .catch(e => {
            process.stderr.write(`[OpenAI] Error: ${e.message}\n`);
            errors.openai = e.message;
          })
      );
    } else {
      errors.openai = 'OPENAI_API_KEY not set';
      process.stderr.write('[OpenAI] Skipped — OPENAI_API_KEY not set\n');
    }
  }

  // Gemini task
  if (geminiPromptFile && geminiOutFile) {
    if (process.env.GEMINI_API_KEY) {
      tasks.push(
        callGemini(geminiPromptFile, geminiOutFile)
          .then(r => { results.gemini = r; })
          .catch(e => {
            process.stderr.write(`[Gemini] Error: ${e.message}\n`);
            errors.gemini = e.message;
          })
      );
    } else {
      errors.gemini = 'GEMINI_API_KEY not set';
      process.stderr.write('[Gemini] Skipped — GEMINI_API_KEY not set\n');
    }
  }

  if (tasks.length === 0) {
    const report = { error: 'No API keys available — export files generated for manual validation', errors };
    console.log(JSON.stringify(report));
    process.exit(1);
  }

  await Promise.allSettled(tasks);
  console.log(JSON.stringify({ results, errors }, null, 2));
}

main().catch(e => {
  console.error(JSON.stringify({ error: e.message }));
  process.exit(1);
});
