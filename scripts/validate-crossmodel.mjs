#!/usr/bin/env node
// Cross-Model Hypothesis Validation Script
// Calls OpenAI (GPT-5.4 Pro) and Google Gemini (Deep Research Max) APIs in parallel
// for independent validation of MAGELLAN hypotheses.
//
// Tools enabled:
//   GPT-5.4 Pro: web_search_preview (high), code_interpreter
//   Gemini Deep Research Max: google_search, url_context, code_execution (SDK defaults for deep-research agents)
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

  // Helper: write partial output on error so 48 min of GPT work isn't lost
  const writePartial = (error) => {
    if (!text && !reasoningSummary) return; // nothing to save
    let partial = `> **PARTIAL OUTPUT** — GPT-5.4 Pro crashed after ${Math.round((Date.now() - start) / 1000)}s\n`;
    partial += `> Error: ${error}\n`;
    partial += `> Web searches: ${searchCount}, Code executions: ${codeRuns}\n\n---\n\n`;
    if (reasoningSummary) partial += `## GPT-5.4 Pro Reasoning Summary\n\n${reasoningSummary}\n\n---\n\n`;
    if (text) partial += text;
    if (codeOutputs.length > 0) {
      partial += '\n\n---\n\n## Code Execution Outputs (partial)\n\n';
      for (let i = 0; i < codeOutputs.length; i++) {
        partial += `### Execution ${i + 1}\n\`\`\`\n${codeOutputs[i]}\n\`\`\`\n\n`;
      }
    }
    writeFileSync(outputFile, partial);
    process.stderr.write(`[OpenAI] Partial output saved to ${outputFile} (${partial.length} chars)\n`);
  };

  try {
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
  } catch (streamError) {
    process.stderr.write(`[OpenAI] Error: ${streamError.message}\n`);
    writePartial(streamError.message);
    return {
      status: 'partial',
      model: 'gpt-5.4-pro',
      duration_s: Math.round((Date.now() - start) / 1000),
      error: streamError.message,
      web_searches: searchCount,
      code_executions: codeRuns,
      partial_output_saved: true,
    };
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
// Google Gemini — Deep Research Max (agentic: google_search + url_context + code_execution)
// Uses the Interactions API (background + streaming + reconnection).
// Runtime: 10-30 min typical, up to 60 min max per docs. We allow 90 min wall-clock.
// ---------------------------------------------------------------------------
const GEMINI_AGENT = 'deep-research-max-preview-04-2026';
const GEMINI_MAX_RUNTIME_MS = 90 * 60 * 1000;
const GEMINI_POLL_INTERVAL_MS = 15 * 1000;

async function callGemini(promptFile, outputFile) {
  const { GoogleGenAI } = await import('@google/genai');
  const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

  const prompt = readFileSync(promptFile, 'utf8');
  const start = Date.now();

  process.stderr.write(`[Gemini DR Max] Creating interaction (agent: ${GEMINI_AGENT})...\n`);

  let interactionId = null;
  let lastEventId = null;
  let isComplete = false;
  let errorMessage = null;
  let thoughts = '';
  let report = '';
  let images = [];
  let citations = [];
  const unknownDeltaTypes = new Set();
  const unknownOutputTypes = new Set();
  let firstAnnotationLogged = false;

  const elapsedS = () => Math.round((Date.now() - start) / 1000);
  const elapsedM = () => Math.round((Date.now() - start) / 60000);

  async function consume(stream) {
    for await (const chunk of stream) {
      if (Date.now() - start > GEMINI_MAX_RUNTIME_MS) {
        throw new Error(`[Gemini DR Max] wall-clock budget exceeded (${elapsedM()} min)`);
      }
      if (chunk.event_type === 'interaction.start') {
        interactionId = chunk.interaction?.id || interactionId;
        if (interactionId) {
          process.stderr.write(`[Gemini DR Max] Interaction: ${interactionId} (${elapsedS()}s)\n`);
        }
      }
      if (chunk.event_id) lastEventId = chunk.event_id;

      if (chunk.event_type === 'content.delta') {
        const d = chunk.delta || {};
        if (d.type === 'text') {
          if (!report) process.stderr.write(`[Gemini DR Max] Report streaming (${elapsedS()}s)...\n`);
          report += d.text || '';
        } else if (d.type === 'thought_summary') {
          const t = d.content?.text || d.text || '';
          thoughts += t;
          if (thoughts.length % 400 < t.length) process.stderr.write('.');
        } else if (d.type === 'image') {
          images.push(d);
          process.stderr.write(`[Gemini DR Max] Image chunk (${elapsedS()}s)\n`);
        } else if (d.type === 'text_annotation') {
          // Citation/annotation delta (empirically observed; not in official JS samples).
          // The schema isn't formally documented — probe multiple common field paths.
          // Dump the first one to stderr so we can refine the extraction on real data.
          if (!firstAnnotationLogged) {
            firstAnnotationLogged = true;
            try {
              process.stderr.write(`[Gemini DR Max] first text_annotation delta shape: ${JSON.stringify(chunk).slice(0, 600)}\n`);
            } catch (_) { /* ignore stringify issues */ }
          }
          const url = d.url || d.uri || d.web?.uri || d.web?.url || d.source?.url || d.source?.uri;
          const title = d.title || d.web?.title || d.source?.title || d.source_title;
          if (url) citations.push({ title: title || 'Source', uri: url });
        } else if (d.type) {
          unknownDeltaTypes.add(d.type);
        }
      } else if (chunk.event_type === 'interaction.complete') {
        isComplete = true;
        process.stderr.write(`\n[Gemini DR Max] interaction.complete (${elapsedM()} min)\n`);
      } else if (chunk.event_type === 'error') {
        errorMessage = chunk.error?.message || chunk.message || 'unknown stream error';
        isComplete = true;
        process.stderr.write(`\n[Gemini DR Max] error event: ${errorMessage}\n`);
      }
    }
  }

  function absorbOutputs(outputs) {
    for (const o of outputs || []) {
      const type = o.type;
      if (type === 'text' || (!type && typeof o.text === 'string')) {
        if (o.text && !report.includes(o.text)) report += (report ? '\n\n' : '') + o.text;
      } else if (type === 'image') {
        images.push(o);
      } else if (type === 'thought_summary' || type === 'thinking') {
        const t = o.content?.text || o.text || '';
        if (t && !thoughts.includes(t)) thoughts += (thoughts ? '\n\n' : '') + t;
      } else if (type) {
        unknownOutputTypes.add(type);
      }
      const annos = o.annotations || o.citations || [];
      for (const a of annos) {
        const url = a.url || a.uri || a.source?.url;
        if (url) citations.push({ title: a.title || a.source_title || 'Source', uri: url });
      }
    }
  }

  // 1. Open the streaming interaction
  // store: true is mandatory when background: true (per Python docs).
  // JS docs samples don't show it explicitly, but passing it is defensive and harmless.
  const initial = await client.interactions.create({
    input: prompt,
    agent: GEMINI_AGENT,
    background: true,
    store: true,
    stream: true,
    agent_config: {
      type: 'deep-research',
      thinking_summaries: 'auto',
      visualization: 'auto',
      collaborative_planning: false,
    },
  });

  try {
    await consume(initial);
  } catch (err) {
    process.stderr.write(`[Gemini DR Max] initial stream error: ${err.message}\n`);
  }

  // 2. Reconnect loop — the connection can drop at ~10 min per docs
  let reconnects = 0;
  while (!isComplete && interactionId) {
    if (Date.now() - start > GEMINI_MAX_RUNTIME_MS) {
      throw new Error(`[Gemini DR Max] wall-clock budget exceeded during reconnect (${elapsedM()} min)`);
    }
    let status;
    try {
      status = await client.interactions.get(interactionId);
    } catch (err) {
      process.stderr.write(`[Gemini DR Max] get() error (retrying in ${GEMINI_POLL_INTERVAL_MS / 1000}s): ${err.message}\n`);
      await new Promise(r => setTimeout(r, GEMINI_POLL_INTERVAL_MS));
      continue;
    }
    const statusStr = String(status.status || status.state || '').toLowerCase();
    process.stderr.write(`[Gemini DR Max] status=${statusStr || 'unknown'} (${elapsedM()} min, reconnects=${reconnects})\n`);

    if (statusStr === 'completed') {
      absorbOutputs(status.outputs);
      // Top-level citations field on the interaction if present
      for (const a of (status.citations || [])) {
        const url = a.url || a.uri;
        if (url) citations.push({ title: a.title || 'Source', uri: url });
      }
      isComplete = true;
      break;
    }
    if (statusStr === 'failed') {
      absorbOutputs(status.outputs);
      errorMessage = status.error || 'interaction failed without error message';
      throw new Error(`[Gemini DR Max] failed: ${errorMessage}`);
    }

    // Still in_progress — try to resume the stream from last event
    try {
      const resume = await client.interactions.get(interactionId, {
        stream: true,
        last_event_id: lastEventId,
      });
      reconnects += 1;
      await consume(resume);
    } catch (err) {
      process.stderr.write(`[Gemini DR Max] resume stream error (will poll): ${err.message}\n`);
      await new Promise(r => setTimeout(r, GEMINI_POLL_INTERVAL_MS));
    }
  }

  // 3. Final sweep — in case stream ended with complete but we haven't pulled outputs yet
  if (interactionId && !report) {
    try {
      const finalStatus = await client.interactions.get(interactionId);
      absorbOutputs(finalStatus.outputs);
    } catch (err) {
      process.stderr.write(`[Gemini DR Max] final get() failed: ${err.message}\n`);
    }
  }

  const duration = Math.round((Date.now() - start) / 1000);
  process.stderr.write(`[Gemini DR Max] Completed in ${Math.round(duration / 60)} min ${duration % 60}s\n`);

  if (unknownDeltaTypes.size) {
    process.stderr.write(`[Gemini DR Max] unknown delta types seen: ${[...unknownDeltaTypes].join(', ')}\n`);
  }
  if (unknownOutputTypes.size) {
    process.stderr.write(`[Gemini DR Max] unknown output types seen: ${[...unknownOutputTypes].join(', ')}\n`);
  }

  // Write full markdown
  let output = '';
  if (thoughts) {
    output += `## Gemini Deep Research Max — Thinking Process\n\n${thoughts}\n\n---\n\n`;
  }
  output += `## Report\n\n${report || '(no report text returned)'}`;

  if (images.length > 0) {
    output += '\n\n---\n\n## Visualizations\n\n';
    for (let i = 0; i < images.length; i++) {
      const img = images[i];
      const mime = img.mime_type || 'image/png';
      if (img.data) {
        output += `### Image ${i + 1}\n\n![visualization-${i + 1}](data:${mime};base64,${img.data.slice(0, 64)}...)\n\n_(truncated base64 preview; ${img.data.length} bytes total)_\n\n`;
      } else if (img.uri) {
        output += `### Image ${i + 1}\n\n![visualization-${i + 1}](${img.uri})\n\n`;
      }
    }
  }

  // Deduplicate citations by URI
  const seen = new Set();
  const uniqueCitations = citations.filter(c => {
    if (!c.uri || seen.has(c.uri)) return false;
    seen.add(c.uri);
    return true;
  });
  if (uniqueCitations.length > 0) {
    output += '\n\n---\n\n## Citations\n\n';
    for (const s of uniqueCitations) {
      output += `- [${s.title || 'Source'}](${s.uri})\n`;
    }
  }

  writeFileSync(outputFile, output);
  return {
    status: errorMessage ? 'partial' : 'completed',
    model: GEMINI_AGENT,
    agent: GEMINI_AGENT,
    duration_s: duration,
    has_thoughts: !!thoughts,
    grounding_sources: uniqueCitations.length,   // preserved key name for main() aggregator
    citations: uniqueCitations.length,
    code_executions: 0,                          // DR Max runs code internally; not exposed as discrete events
    visualizations: images.length,
    interaction_id: interactionId,
    error: errorMessage || undefined,
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
