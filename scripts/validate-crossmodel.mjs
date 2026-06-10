#!/usr/bin/env node
// Cross-Model Hypothesis Validation Script
// Calls OpenAI (GPT-5.5 Pro) and Google Gemini (Deep Research Max) APIs in parallel
// for independent validation of MAGELLAN hypotheses.
//
// Tools enabled:
//   GPT-5.5 Pro: web_search_preview (high), code_interpreter (server-side only;
//     no client-side `shell` tool — see OPENAI_TOOLS note below)
//   Gemini Deep Research Max: google_search, url_context, code_execution (SDK defaults for deep-research agents)
//
// API contracts:
//   OpenAI: Responses API. GPT-5.5 Pro does not support streaming; this script
//     uses background submit + poll. The response is stored remotely
//     (store: true), so we persist response.id to disk on submit and auto-resume
//     on retry, so long-running validations are never wasted.
//   Gemini: Interactions API, schema revision 2026-05-20 (v2). The v2 schema
//     rolled out 7 May 2026; v1 schema sunsets 8 June 2026. This script targets
//     v2 EXCLUSIVELY. Streaming events (per SDK 2.x InteractionSSEEvent union):
//     `interaction.created` / `step.delta` / `step.start` / `step.stop` /
//     `interaction.completed` / `interaction.status_update` / `error`. Outputs
//     are read via `interaction.steps[]` (Step union: model_output / thought /
//     user_input / *_call / *_result), with ModelOutputStep.content[] holding
//     TextContent | ImageContent etc., and ThoughtStep.summary[] holding the
//     thought trace. Requires `@google/genai >=2.0.0`.
//
// Usage:
//   node --env-file=.env.local scripts/validate-crossmodel.mjs \
//     --gpt-prompt <file> --gpt-out <file> \
//     --gemini-prompt <file> --gemini-out <file>
//
// Environment:
//   OPENAI_API_KEY  -- required for GPT validation
//   GEMINI_API_KEY  -- required for Gemini validation
//   At least one must be set.
//   Put keys in .env.local and use --env-file=.env.local flag.

import { readFileSync, writeFileSync, existsSync, unlinkSync, renameSync } from 'fs';

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
// Reasoning effort for GPT-5.5 Pro. Default 'xhigh' (deepest). 'high' is much
// faster and sufficient for validation (novelty + arithmetic checks) — pass
// `--effort high` when latency matters. Supported: 'medium' | 'high' | 'xhigh'.
const reasoningEffort = getArg('--effort') || 'xhigh';

// ---------------------------------------------------------------------------
// OpenAI: GPT-5.5 Pro, background submit + poll (streaming not supported).
//
// Reasoning effort: 'xhigh' (with single fallback to 'high'). Supported values
// on gpt-5.5-pro: 'medium', 'high', 'xhigh'.
//
// Tools: web_search_preview (high), code_interpreter (both server-side).
//
// Response shape notes:
//   - shell tool produces paired items: shell_call (the request) and
//     shell_call_output (with stdout/stderr/outcome.exit_code).
//   - code_interpreter_call.outputs is null in background mode; computed
//     values appear inline in the final message output_text. The 'code'
//     field is preserved in the call item.
//   - response.output_text is a convenience shortcut equivalent to
//     concatenated message output_text content.
//
// 4-hour wall-clock cap. On timeout the response is NOT cancelled:
// response.id is preserved on disk so the next run auto-resumes.
// ---------------------------------------------------------------------------
const OPENAI_WALL_CLOCK_MS = 4 * 60 * 60 * 1000; // 4 hours
const OPENAI_POLL_INTERVAL_MS = 30 * 1000;       // 30 s

// NOTE: do NOT add the `shell` tool here. Two empirically-verified reasons (2026-06-09):
//  1. Bare `{ type: 'shell' }` defaults to a CLIENT-SIDE local shell
//     (`environment.type: 'local''`): the model emits shell_call items and the
//     integrator must execute them and submit shell_call_output back in a follow-up
//     turn. This background submit+poll flow never services those calls, so the
//     response stalls in `in_progress` forever (no error, no required_action) past
//     the wall-clock cap. (A real latent bug, removed -- but NOT the cause of the
//     S032 hang; that was TPM-rate saturation from heavy tool use. See CHANGELOG v5.30.)
//  2. The only background-safe shell is HOSTED (`environment.type: 'container_auto'`),
//     but the API rejects code_interpreter + hosted shell together:
//     "code_interpreter and shell with an OpenAI-managed container cannot be used
//     together at the same time" (mutually_exclusive_parameters). So keeping shell
//     would force DROPPING code_interpreter.
// For validation (arithmetic/statistics verification + novelty), code_interpreter's
// Python sandbox is the more valuable managed-container tool; web_search_preview
// covers novelty. If a future validation genuinely needs data-fetching/CLI tools,
// switch to hosted-shell-ALONE (drop code_interpreter) and update the extraction
// logic below to read shell_call_output items.
const OPENAI_TOOLS = [
  // 'medium' (not 'high') search context: a high-context web search pulls a large
  // amount of content into the token stream; with ~30 searches per validation that
  // saturates the org TPM tier (S032: gpt-5.5-pro xhigh hit the 1,000,000 tokens/min
  // limit, hanging/failing the response). 'medium' cuts per-search token intake.
  { type: 'web_search_preview', search_context_size: 'medium' },
  { type: 'code_interpreter', container: { type: 'auto' } },
];
// Bound the tool-calling loop so the response always terminates. Uncapped, the
// 2-hypothesis validation ran 4-7h without finishing (S032). A full report needs
// ~30 calls; 40 leaves headroom while preventing a runaway loop.
const OPENAI_MAX_TOOL_CALLS = 40;

async function submitOpenAI(client, prompt, effort) {
  return client.responses.create({
    model: 'gpt-5.5-pro',
    input: [{ role: 'user', content: [{ type: 'input_text', text: prompt }] }],
    reasoning: { effort, summary: 'auto' },
    tools: OPENAI_TOOLS,
    max_tool_calls: OPENAI_MAX_TOOL_CALLS,
    background: true,
    store: true,
  });
}

async function callOpenAI(promptFile, outputFile) {
  const { default: OpenAI } = await import('openai');
  // SDK request timeout slightly above our wall-clock so it never trips first.
  const client = new OpenAI({ timeout: OPENAI_WALL_CLOCK_MS + 5 * 60 * 1000 });

  const prompt = readFileSync(promptFile, 'utf8');
  const start = Date.now();
  const responseIdFile = `${outputFile}.response-id`;
  let responseId = null;

  // Auto-resume from a previous run that left a response-id file behind.
  if (existsSync(responseIdFile)) {
    responseId = readFileSync(responseIdFile, 'utf8').trim();
    process.stderr.write(`[OpenAI] Resuming response ${responseId} from ${responseIdFile}\n`);
  } else {
    process.stderr.write(`[OpenAI] Submitting gpt-5.5-pro (reasoning: ${reasoningEffort}, background, web_search + code_interpreter)...\n`);
    let submitted;
    try {
      submitted = await submitOpenAI(client, prompt, reasoningEffort);
    } catch (err) {
      const msg = err?.message || String(err);
      if (/reasoning|effort|xhigh/i.test(msg) && reasoningEffort !== 'high') {
        process.stderr.write(`[OpenAI] ${reasoningEffort} rejected, retrying with high: ${msg}\n`);
        submitted = await submitOpenAI(client, prompt, 'high');
      } else {
        throw err;
      }
    }
    responseId = submitted.id;
    writeFileSync(responseIdFile, responseId);
    process.stderr.write(`[OpenAI] Submitted ${responseId} (saved to ${responseIdFile})\n`);
  }

  // Poll until terminal status, but never cancel mid-flight on timeout.
  // Terminal states: completed (full output), incomplete (partial output, e.g.
  // hit max_output_tokens), failed / cancelled (no recoverable output).
  let response;
  let terminalStatus = null;
  while (true) {
    if (Date.now() - start > OPENAI_WALL_CLOCK_MS) {
      const minutes = Math.round((Date.now() - start) / 60000);
      process.stderr.write(
        `[OpenAI] Wall-clock budget exceeded (${minutes} min). Response ${responseId} preserved at ${responseIdFile}.\n` +
        `         Re-run this script to auto-resume polling, or call client.responses.retrieve('${responseId}') manually.\n`
      );
      return {
        status: 'partial',
        model: 'gpt-5.5-pro',
        duration_s: Math.round((Date.now() - start) / 1000),
        recovery_id: responseId,
        recovery_file: responseIdFile,
        error: `wall-clock ${minutes}min exceeded; response preserved on OpenAI side`,
      };
    }
    await new Promise(r => setTimeout(r, OPENAI_POLL_INTERVAL_MS));
    try {
      response = await client.responses.retrieve(responseId);
    } catch (err) {
      process.stderr.write(`[OpenAI] retrieve() error (will retry in ${OPENAI_POLL_INTERVAL_MS / 1000}s): ${err.message}\n`);
      continue;
    }
    const elapsed = Math.round((Date.now() - start) / 1000);
    process.stderr.write(`[OpenAI] status=${response.status} (${elapsed}s)\n`);
    if (response.status === 'completed') {
      terminalStatus = 'completed';
      break;
    }
    if (response.status === 'incomplete') {
      // The response stopped early but response.output[] still contains whatever
      // was generated before the cutoff. Save it as partial rather than throw.
      const reason = response.incomplete_details?.reason || 'unknown';
      process.stderr.write(`[OpenAI] status=incomplete (reason=${reason}). Salvaging partial output.\n`);
      terminalStatus = 'incomplete';
      try { renameSync(responseIdFile, `${responseIdFile}.incomplete`); } catch (_) { /* ignore */ }
      break;
    }
    if (response.status === 'failed') {
      // A heavy validation can hit the org TPM rate limit AFTER generating its full
      // report (S032: ~990k/1M tokens-per-min). If a message with text exists, salvage
      // it as partial rather than discard a complete report; only throw if truly empty.
      const hasText = (response.output || []).some(
        it => it.type === 'message' && (it.content || []).some(c => c.type === 'output_text' && c.text)
      );
      try { renameSync(responseIdFile, `${responseIdFile}.failed`); } catch (_) { /* ignore */ }
      if (hasText) {
        process.stderr.write(`[OpenAI] status=failed (${response.error?.message || 'no message'}) but report present. Salvaging.\n`);
        terminalStatus = 'failed_salvaged';
        break;
      }
      throw new Error(`OpenAI failed (no recoverable output): ${response.error?.message || 'no error message'}`);
    }
    if (response.status === 'cancelled') {
      try { renameSync(responseIdFile, `${responseIdFile}.cancelled`); } catch (_) { /* ignore */ }
      throw new Error(`OpenAI cancelled: ${response.error?.message || 'no error message'}`);
    }
  }

  // Extract from response.output[]. Works for both completed and incomplete.
  // Item types:
  //   - message: { content: [{ type: 'output_text', text, annotations }] }
  //   - reasoning: { summary: [{ type: 'summary_text', text }] }
  //   - web_search_call / code_interpreter_call / shell_call: tool invocations
  //   - shell_call_output: paired output with stdout/stderr/outcome.exit_code
  let text = '';
  let reasoningSummary = '';
  let annotations = [];
  let codeOutputs = [];
  let shellOutputs = [];
  let searchCount = 0;
  let codeRuns = 0;
  let shellRuns = 0;
  const unknownItemTypes = new Set();
  for (const item of response.output || []) {
    if (item.type === 'message') {
      for (const c of item.content || []) {
        if (c.type === 'output_text') {
          text += c.text || '';
          if (Array.isArray(c.annotations)) annotations = annotations.concat(c.annotations);
        }
      }
    } else if (item.type === 'reasoning') {
      for (const s of item.summary || []) {
        if (s.type === 'summary_text') reasoningSummary += s.text || '';
      }
    } else if (item.type === 'web_search_call') {
      searchCount++;
    } else if (item.type === 'code_interpreter_call') {
      codeRuns++;
      // outputs is null in background mode but we keep the loop for forward-compat.
      for (const out of item.outputs || []) {
        if (out.type === 'logs') codeOutputs.push(out.logs);
      }
    } else if (item.type === 'shell_call') {
      shellRuns++;
    } else if (item.type === 'shell_call_output') {
      // Per OpenAI shell tool docs: paired with shell_call, contains stdout/stderr/outcome.
      const stdout = item.stdout || '';
      const stderr = item.stderr || '';
      const exitCode = item.outcome?.exit_code;
      shellOutputs.push({ stdout, stderr, exit_code: exitCode });
    } else if (item.type !== undefined) {
      unknownItemTypes.add(item.type);
    }
  }
  if (unknownItemTypes.size > 0) {
    process.stderr.write(`[OpenAI] Unrecognized response.output[] item types: ${[...unknownItemTypes].join(', ')}\n`);
  }

  if (terminalStatus === 'completed') {
    // Success: clean up the response-id file.
    try { unlinkSync(responseIdFile); } catch (_) { /* ignore */ }
  }

  const duration = Math.round((Date.now() - start) / 1000);
  process.stderr.write(`[OpenAI] ${terminalStatus} in ${duration}s (web_searches=${searchCount}, code_runs=${codeRuns}, shell_runs=${shellRuns})\n`);

  let output = '';
  if (terminalStatus === 'incomplete') {
    const reason = response.incomplete_details?.reason || 'unknown';
    output += `> **PARTIAL OUTPUT** (status=incomplete, reason=${reason}, after ${duration}s).\n`;
    output += `> Response id ${responseId} preserved at ${responseIdFile}.incomplete for forensics.\n\n---\n\n`;
  } else if (terminalStatus === 'failed_salvaged') {
    output += `> **SALVAGED REPORT** (status=failed: ${response.error?.message || 'terminal error'}, after ${duration}s).\n`;
    output += `> The model produced this report before the terminal error (typically the org TPM rate limit); content recovered. Response id ${responseId} preserved at ${responseIdFile}.failed.\n\n---\n\n`;
  }
  // Report first: the verdicts are the deliverable and the upload excerpt is the head.
  // (The reasoning summary, appended at the end, is supplementary and can be verbose.)
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
  if (shellOutputs.length > 0) {
    output += '\n\n---\n\n## Shell Execution Outputs\n\n';
    for (let i = 0; i < shellOutputs.length; i++) {
      const s = shellOutputs[i];
      output += `### Command ${i + 1}` + (s.exit_code !== undefined ? ` (exit=${s.exit_code})` : '') + '\n';
      if (s.stdout) output += `stdout:\n\`\`\`\n${s.stdout}\n\`\`\`\n`;
      if (s.stderr) output += `stderr:\n\`\`\`\n${s.stderr}\n\`\`\`\n`;
      output += '\n';
    }
  }

  if (reasoningSummary) {
    output += `\n\n---\n\n## GPT-5.5 Pro Reasoning Summary (supplementary)\n\n${reasoningSummary}\n`;
  }

  writeFileSync(outputFile, output);
  return {
    status: terminalStatus === 'completed' ? 'completed' : 'partial',
    model: 'gpt-5.5-pro',
    duration_s: duration,
    citations: annotations.length,
    has_reasoning: !!reasoningSummary,
    web_searches: searchCount,
    code_executions: codeRuns,
    shell_executions: shellRuns,
    response_id: responseId,
    incomplete_reason: terminalStatus === 'incomplete' ? (response.incomplete_details?.reason || 'unknown') : undefined,
  };
}

// ---------------------------------------------------------------------------
// Google Gemini -- Deep Research Max (agentic: google_search + url_context + code_execution)
// Uses the Interactions API at schema revision 2026-05-20 (v2). Background
// streaming with reconnection on the ~10-min connection drop documented by Google.
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
      const eventType = chunk.event_type;

      if (eventType === 'interaction.created') {
        interactionId = chunk.interaction?.id || interactionId;
        if (interactionId) {
          process.stderr.write(`[Gemini DR Max] Interaction: ${interactionId} (${elapsedS()}s)\n`);
        }
      }
      if (chunk.event_id) lastEventId = chunk.event_id;

      if (eventType === 'step.delta') {
        // step.delta payload: chunk.delta is a StepDelta.* variant per SDK 2.x.
        // Known type discriminators: text | image | audio | document | video |
        // thought_summary | thought_signature | text_annotation_delta |
        // arguments_delta | {google_search,url_context,code_execution,
        // file_search,mcp_server_tool,google_maps}_call|_result.
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
        } else if (d.type === 'text_annotation_delta') {
          // SDK 2.x: d.annotations is Array<URLCitation | FileCitation | PlaceCitation>.
          // URLCitation has {url, title}; FileCitation has {document_uri, title}.
          if (!firstAnnotationLogged) {
            firstAnnotationLogged = true;
            try {
              process.stderr.write(`[Gemini DR Max] first annotation delta shape: ${JSON.stringify(chunk).slice(0, 600)}\n`);
            } catch (_) { /* ignore stringify issues */ }
          }
          for (const a of (d.annotations || [])) {
            const url = a.url || a.document_uri || a.uri;
            if (url) citations.push({ title: a.title || 'Source', uri: url });
          }
        } else if (
          // Known StepDelta variants with no user-visible payload: silently drop.
          // Tool deltas fire during DR Max's autonomous loop; the resulting evidence
          // ends up attached to text content via text_annotation_delta + step.content
          // annotations, so we don't need to surface the raw call/result chunks.
          d.type === 'thought_signature' ||
          d.type === 'arguments_delta' ||
          d.type === 'audio' || d.type === 'document' || d.type === 'video' ||
          d.type === 'code_execution_call' || d.type === 'code_execution_result' ||
          d.type === 'url_context_call'    || d.type === 'url_context_result' ||
          d.type === 'google_search_call'  || d.type === 'google_search_result' ||
          d.type === 'file_search_call'    || d.type === 'file_search_result' ||
          d.type === 'mcp_server_tool_call' || d.type === 'mcp_server_tool_result' ||
          d.type === 'google_maps_call'    || d.type === 'google_maps_result'
        ) {
          // expected, no-op
        } else if (d.type) {
          unknownDeltaTypes.add(d.type);
        }
      } else if (eventType === 'interaction.completed') {
        isComplete = true;
        process.stderr.write(`\n[Gemini DR Max] interaction.completed (${elapsedM()} min)\n`);
      } else if (eventType === 'error') {
        errorMessage = chunk.error?.message || chunk.message || 'unknown stream error';
        isComplete = true;
        process.stderr.write(`\n[Gemini DR Max] error event: ${errorMessage}\n`);
      }
      // Other v2 events not affecting our state machine:
      //   step.start / step.stop -- step boundaries; we accumulate via step.delta
      //   interaction.in_progress -- periodic tick (replaces v1 interaction.status_update)
      //   interaction.requires_action -- tool approval (DR Max is autonomous; not expected)
    }
  }

  // v2 schema: interaction.steps[] is a Step union per SDK 2.x. Type discriminators:
  //   user_input | model_output | thought |
  //   {function,code_execution,url_context,google_search,file_search,mcp_server_tool,google_maps}_call|_result
  // ModelOutputStep.content[] is Array<Content_2>: TextContent | ImageContent |
  //   AudioContent | DocumentContent | VideoContent. TextContent carries `annotations`.
  // ThoughtStep has .summary[] (Array<TextContent | ImageContent>) -- NOT .content[].
  // All *_call / *_result step types carry no user-visible text; citations attach
  // to model_output.content[i].annotations.
  function absorbSteps(steps) {
    for (const o of steps || []) {
      const type = o.type;

      if (
        type === 'user_input' ||
        type === 'function_call' || type === 'function_result' ||
        type === 'code_execution_call' || type === 'code_execution_result' ||
        type === 'url_context_call'    || type === 'url_context_result' ||
        type === 'google_search_call'  || type === 'google_search_result' ||
        type === 'file_search_call'    || type === 'file_search_result' ||
        type === 'mcp_server_tool_call' || type === 'mcp_server_tool_result' ||
        type === 'google_maps_call'    || type === 'google_maps_result'
      ) {
        // Defensive: drain any citations that happen to ride on these steps.
        const skipAnnos = o.annotations || o.citations || [];
        for (const a of skipAnnos) {
          const url = a.url || a.document_uri || a.uri;
          if (url) citations.push({ title: a.title || 'Source', uri: url });
        }
        continue;
      }

      const textParts = [];
      const thoughtParts = [];

      // model_output: content[] is Content_2 union; TextContent has annotations[].
      if (type === 'model_output' && Array.isArray(o.content)) {
        for (const c of o.content) {
          if (c.type === 'text' && typeof c.text === 'string') {
            textParts.push(c.text);
          } else if (c.type === 'image') {
            images.push(c);
          }
          for (const a of (c.annotations || [])) {
            const url = a.url || a.document_uri || a.uri;
            if (url) citations.push({ title: a.title || 'Source', uri: url });
          }
        }
      }

      // thought: summary[] is Array<TextContent | ImageContent>, NOT content[].
      if (type === 'thought' && Array.isArray(o.summary)) {
        for (const c of o.summary) {
          if (c.type === 'text' && typeof c.text === 'string') {
            thoughtParts.push(c.text);
          } else if (c.type === 'image') {
            images.push(c);
          }
        }
      }

      // Merge into running buffers with dedupe.
      const textBlock = textParts.join('');
      const thoughtBlock = thoughtParts.join('');
      if (textBlock && !report.includes(textBlock)) {
        report += (report ? '\n\n' : '') + textBlock;
      }
      if (thoughtBlock && !thoughts.includes(thoughtBlock)) {
        thoughts += (thoughts ? '\n\n' : '') + thoughtBlock;
      }

      // Track unrecognized step types for forensics.
      if (type && type !== 'model_output' && type !== 'thought') {
        unknownOutputTypes.add(type);
      }

      // Top-level annotations (defensive; not in SDK type defs but cheap to drain).
      const annos = o.annotations || o.citations || [];
      for (const a of annos) {
        const url = a.url || a.document_uri || a.uri;
        if (url) citations.push({ title: a.title || 'Source', uri: url });
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
      absorbSteps(status.steps);
      // Top-level citations field on the interaction if present
      for (const a of (status.citations || [])) {
        const url = a.url || a.uri;
        if (url) citations.push({ title: a.title || 'Source', uri: url });
      }
      isComplete = true;
      break;
    }
    if (statusStr === 'failed') {
      absorbSteps(status.steps);
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
      absorbSteps(finalStatus.steps);
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
// Per-hypothesis split (TPM cure). A single GPT-5.5 Pro call validating BOTH
// hypotheses runs ~30 high-context tool calls and pushes the org to ~1M
// tokens/min, saturating the TPM tier (S032). Validating ONE hypothesis per
// call roughly halves the per-minute token rate so each call stays under the
// limit and completes cleanly. Calls are SEQUENTIAL (never concurrent;
// concurrency re-creates the contention). Each sub-call reuses callOpenAI, so
// it inherits medium search context, max_tool_calls, salvage-on-failed and
// response-id resume. Falls back to a single call if <2 hypotheses are present.
// Gemini is NOT split: it is one model and does not consume the OpenAI TPM pool.
// ---------------------------------------------------------------------------
function splitGptPrompt(prompt) {
  const lines = prompt.split('\n');
  const heads = [];
  lines.forEach((l, i) => { if (/^##\s+HYPOTHESIS\b/i.test(l)) heads.push(i); });
  if (heads.length < 2) return null; // single hypothesis or unrecognized format: no split
  const preamble = lines.slice(0, heads[0]).join('\n');
  return heads.map((startAt, k) => {
    const endAt = k + 1 < heads.length ? heads[k + 1] : lines.length;
    const section = lines.slice(startAt, endAt).join('\n');
    return `${preamble}\n\n${section}\n\n---\n` +
      `NOTE: Validate ONLY the single hypothesis above. It is sent on its own ` +
      `(hypothesis ${k + 1} of ${heads.length}) so each response stays within API ` +
      `rate limits; do not reference or wait for the others.\n`;
  });
}

async function callOpenAISplit(promptFile, outputFile) {
  const subs = splitGptPrompt(readFileSync(promptFile, 'utf8'));
  if (!subs) return callOpenAI(promptFile, outputFile); // single-hypothesis path unchanged
  process.stderr.write(`[OpenAI] Per-hypothesis split: ${subs.length} sequential calls (TPM-safe).\n`);
  const parts = [];
  const statuses = [];
  for (let k = 0; k < subs.length; k++) {
    const subPromptFile = `${promptFile}.h${k + 1}`;
    const subOutFile = `${outputFile}.h${k + 1}`;
    // Resume guard: a hypothesis already validated in a prior run leaves its
    // output file with no lingering response-id; reuse it instead of re-billing.
    if (existsSync(subOutFile) && !existsSync(`${subOutFile}.response-id`)) {
      process.stderr.write(`[OpenAI] Hypothesis ${k + 1}/${subs.length} already validated; reusing.\n`);
      statuses.push('completed');
    } else {
      writeFileSync(subPromptFile, subs[k]);
      process.stderr.write(`[OpenAI] Validating hypothesis ${k + 1}/${subs.length}...\n`);
      try {
        const r = await callOpenAI(subPromptFile, subOutFile);
        statuses.push(r.status || 'completed');
      } catch (e) {
        process.stderr.write(`[OpenAI] Hypothesis ${k + 1} failed: ${e.message}\n`);
        statuses.push('failed');
      }
    }
    let partText = '';
    try { partText = readFileSync(subOutFile, 'utf8'); } catch (_) { /* ignore */ }
    parts.push(`# Validation: Hypothesis ${k + 1} of ${subs.length}\n\n${partText || '_(no output recovered)_'}`);
  }
  writeFileSync(outputFile, parts.join('\n\n---\n\n'));
  const status = statuses.every(s => s === 'completed') ? 'completed'
    : statuses.some(s => s === 'completed' || s === 'partial') ? 'partial' : 'failed';
  return { status, model: 'gpt-5.5-pro', mode: 'per-hypothesis-split', hypotheses: subs.length, statuses };
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
        callOpenAISplit(gptPromptFile, gptOutFile)
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
