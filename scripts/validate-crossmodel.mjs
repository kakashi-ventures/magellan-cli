#!/usr/bin/env node
// Cross-Model Hypothesis Validation Script
// Calls OpenAI (GPT-5.4 Pro) and Google Gemini (3.1 Pro) APIs in parallel
// for independent validation of MAGELLAN hypotheses.
//
// Tools enabled:
//   GPT-5.4 Pro: web_search_preview (high), code_interpreter
//   Gemini 3.1 Pro: codeExecution, googleSearch
//
// Usage:
//   node --env-file=.env.local scripts/validate-crossmodel.mjs \
//     --gpt-prompt <file> --gpt-out <file> \
//     --gemini-prompt <file> --gemini-out <file>
//
// Environment:
//   OPENAI_API_KEY  — required for GPT validation
//   GEMINI_API_KEY  — required for Gemini validation
//   At least one must be set.
//   Put keys in .env.local and use --env-file=.env.local flag.

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
  const client = new OpenAI({ timeout: 45 * 60 * 1000 }); // 45 min timeout — GPT-5.4 Pro with all tools can take 30+ min

  const prompt = readFileSync(promptFile, 'utf8');
  const start = Date.now();

  process.stderr.write('[OpenAI] Calling gpt-5.4-pro (reasoning: high, streaming)...\n');

  // Use streaming to show progress in real-time
  const stream = await client.responses.create({
    model: 'gpt-5.4-pro',
    input: [
      {
        role: 'user',
        content: [{ type: 'input_text', text: prompt }],
      },
    ],
    reasoning: { effort: 'high', summary: 'auto' },
    tools: [
      { type: 'web_search_preview', search_context_size: 'high' },
      { type: 'code_interpreter', container: { type: 'auto' } },
    ],
    stream: true,
  });

  let text = '';
  let reasoningSummary = '';
  let annotations = [];
  let reasoningStarted = false;
  let outputStarted = false;
  let searchCount = 0;
  let codeRuns = 0;
  let codeOutputs = [];

  for await (const event of stream) {
    // Track reasoning phase
    if (event.type === 'response.reasoning_summary_part.added') {
      if (!reasoningStarted) {
        reasoningStarted = true;
        const elapsed = Math.round((Date.now() - start) / 1000);
        process.stderr.write(`[OpenAI] Reasoning started (${elapsed}s)...\n`);
      }
    }

    // Reasoning summary text deltas
    if (event.type === 'response.reasoning_summary_text.delta') {
      reasoningSummary += event.delta;
      // Print a dot every ~200 chars to show progress
      if (reasoningSummary.length % 200 < event.delta.length) {
        process.stderr.write('.');
      }
    }

    // Reasoning done, output starting
    if (event.type === 'response.reasoning_summary_text.done') {
      const elapsed = Math.round((Date.now() - start) / 1000);
      process.stderr.write(`\n[OpenAI] Reasoning complete (${elapsed}s), generating output...\n`);
    }

    // Output text deltas
    if (event.type === 'response.output_text.delta') {
      if (!outputStarted) {
        outputStarted = true;
        const elapsed = Math.round((Date.now() - start) / 1000);
        process.stderr.write(`[OpenAI] Output streaming started (${elapsed}s)...\n`);
      }
      text += event.delta;
    }

    // Web search progress
    if (event.type === 'response.web_search_call.in_progress') {
      searchCount++;
      process.stderr.write(`[OpenAI] Web search #${searchCount}...\n`);
    }
    if (event.type === 'response.web_search_call.searching') {
      process.stderr.write('s');
    }
    if (event.type === 'response.web_search_call.completed') {
      process.stderr.write(`\n[OpenAI] Search #${searchCount} completed\n`);
    }

    // Code interpreter progress
    if (event.type === 'response.code_interpreter_call.in_progress') {
      codeRuns++;
      process.stderr.write(`[OpenAI] Code execution #${codeRuns}...\n`);
    }
    if (event.type === 'response.code_interpreter_call.interpreting') {
      process.stderr.write('x');
    }
    if (event.type === 'response.code_interpreter_call.completed') {
      process.stderr.write(`\n[OpenAI] Code execution #${codeRuns} completed\n`);
    }

    // Completed — extract annotations and code outputs
    if (event.type === 'response.completed') {
      const response = event.response;
      for (const item of response?.output || []) {
        if (item.type === 'message') {
          annotations = item.content?.[0]?.annotations || [];
        }
        if (item.type === 'code_interpreter_call') {
          for (const out of item.outputs || []) {
            if (out.type === 'logs') codeOutputs.push(out.logs);
          }
        }
      }
    }
  }

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

  if (codeOutputs.length > 0) {
    output += '\n\n---\n\n## Code Execution Outputs\n\n';
    for (let i = 0; i < codeOutputs.length; i++) {
      output += `### Execution ${i + 1}\n\`\`\`\n${codeOutputs[i]}\n\`\`\`\n\n`;
    }
  }

  writeFileSync(outputFile, output);
  return {
    status: 'completed',
    model: 'gpt-5.4-pro',
    duration_s: duration,
    citations: annotations.length,
    has_reasoning: !!reasoningSummary,
    web_searches: searchCount,
    code_executions: codeRuns,
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

  process.stderr.write('[Gemini] Calling gemini-3.1-pro-preview (thinking: HIGH, streaming)...\n');

  // Use streaming to show thinking progress in real-time
  const stream = await ai.models.generateContentStream({
    model: 'gemini-3.1-pro-preview',
    contents: prompt,
    config: {
      tools: [
        { codeExecution: {} },
        { googleSearch: {} },
      ],
      thinkingConfig: {
        thinkingLevel: 'HIGH',
        includeThoughts: true,
      },
    },
  });

  let thoughts = '';
  let answer = '';
  let thinkingStarted = false;
  let answerStarted = false;
  let codeBlocks = [];
  let codeResults = [];
  let groundingSources = [];

  for await (const chunk of stream) {
    const parts = chunk.candidates?.[0]?.content?.parts || [];
    for (const part of parts) {
      // Thinking and answer text
      if (part.text) {
        if (part.thought) {
          if (!thinkingStarted) {
            thinkingStarted = true;
            const elapsed = Math.round((Date.now() - start) / 1000);
            process.stderr.write(`[Gemini] Thinking started (${elapsed}s)...\n`);
          }
          thoughts += part.text;
          if (thoughts.length % 200 < part.text.length) {
            process.stderr.write('.');
          }
        } else {
          if (!answerStarted) {
            answerStarted = true;
            const elapsed = Math.round((Date.now() - start) / 1000);
            process.stderr.write(`\n[Gemini] Thinking done, answer streaming (${elapsed}s)...\n`);
          }
          answer += part.text;
        }
      }

      // Code execution parts
      if (part.executableCode) {
        process.stderr.write(`[Gemini] Executing code...\n`);
        codeBlocks.push(part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        codeResults.push({
          outcome: part.codeExecutionResult.outcome,
          output: part.codeExecutionResult.output,
        });
        process.stderr.write(`[Gemini] Code result: ${part.codeExecutionResult.outcome}\n`);
      }
    }

    // Grounding metadata (at chunk level, not part level)
    const candidate = chunk.candidates?.[0];
    if (candidate?.groundingMetadata) {
      groundingSources = (candidate.groundingMetadata.groundingChunks || [])
        .filter(c => c.web)
        .map(c => ({ title: c.web.title, uri: c.web.uri }));
    }
  }

  const duration = Math.round((Date.now() - start) / 1000);
  process.stderr.write(`[Gemini] Completed in ${duration}s\n`);

  // Write full output
  let output = '';
  if (thoughts) {
    output += `## Gemini Thinking Process\n\n${thoughts}\n---\n\n`;
  }
  output += answer;

  if (codeBlocks.length > 0) {
    output += '\n\n---\n\n## Computational Verification\n\n';
    for (let i = 0; i < codeBlocks.length; i++) {
      output += `### Code Block ${i + 1}\n\`\`\`python\n${codeBlocks[i]}\n\`\`\`\n`;
      if (codeResults[i]) {
        output += `**Result** (${codeResults[i].outcome}):\n\`\`\`\n${codeResults[i].output || '(no output)'}\n\`\`\`\n\n`;
      }
    }
  }

  if (groundingSources.length > 0) {
    output += '\n\n---\n\n## Grounding Sources\n\n';
    for (const s of groundingSources) {
      output += `- [${s.title || 'Source'}](${s.uri})\n`;
    }
  }

  writeFileSync(outputFile, output);
  return {
    status: 'completed',
    model: 'gemini-3.1-pro-preview',
    duration_s: duration,
    has_thoughts: !!thoughts,
    code_executions: codeResults.length,
    grounding_sources: groundingSources.length,
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
