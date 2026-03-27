#!/usr/bin/env node
// One-shot GPT-5.4 validation script for MAGELLAN cross-model validation
// Uses gpt-5.4 (non-pro) with web_search_preview and code_interpreter
// Fallback from gpt-5.4-pro which returns "terminated" errors

import { readFileSync, writeFileSync } from 'fs';

const gptPromptFile = process.argv[2];
const gptOutFile    = process.argv[3];

if (!gptPromptFile || !gptOutFile) {
  console.error('Usage: node validate-gpt54.mjs <prompt-file> <output-file>');
  process.exit(1);
}

const { default: OpenAI } = await import('openai');
const client = new OpenAI({ timeout: 45 * 60 * 1000 }); // 45 min

const prompt = readFileSync(gptPromptFile, 'utf8');
const start = Date.now();

process.stderr.write('[OpenAI] Calling gpt-5.4 (reasoning: high, web_search + code_interpreter, streaming)...\n');

const stream = await client.responses.create({
  model: 'gpt-5.4',
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
  if (event.type === 'response.reasoning_summary_part.added') {
    if (!reasoningStarted) {
      reasoningStarted = true;
      const elapsed = Math.round((Date.now() - start) / 1000);
      process.stderr.write(`[OpenAI] Reasoning started (${elapsed}s)...\n`);
    }
  }

  if (event.type === 'response.reasoning_summary_text.delta') {
    reasoningSummary += event.delta;
    if (reasoningSummary.length % 200 < event.delta.length) {
      process.stderr.write('.');
    }
  }

  if (event.type === 'response.reasoning_summary_text.done') {
    const elapsed = Math.round((Date.now() - start) / 1000);
    process.stderr.write(`\n[OpenAI] Reasoning complete (${elapsed}s), generating output...\n`);
  }

  if (event.type === 'response.output_text.delta') {
    if (!outputStarted) {
      outputStarted = true;
      const elapsed = Math.round((Date.now() - start) / 1000);
      process.stderr.write(`[OpenAI] Output streaming started (${elapsed}s)...\n`);
    }
    text += event.delta;
  }

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

let output = `# GPT-5.4 Validation — EVT × Proteome Thermal Stability\n\n`;
output += `**Model**: gpt-5.4 (reasoning effort: high, web search: enabled, code interpreter: enabled)\n`;
output += `**Duration**: ${duration}s\n`;
output += `**Web searches performed**: ${searchCount}\n`;
output += `**Code executions**: ${codeRuns}\n\n---\n\n`;

if (reasoningSummary) {
  output += `## Reasoning Summary\n\n${reasoningSummary}\n\n---\n\n`;
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

writeFileSync(gptOutFile, output);
console.log(JSON.stringify({
  status: 'completed',
  model: 'gpt-5.4',
  duration_s: duration,
  citations: annotations.length,
  has_reasoning: !!reasoningSummary,
  web_searches: searchCount,
  code_executions: codeRuns,
}));
