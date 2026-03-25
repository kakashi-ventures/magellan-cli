#!/usr/bin/env node
// Upload MAGELLAN session results to magellan-discover.ai
// Usage: node scripts/upload-session.mjs <results_dir>
// Reads ingest.json, final.json, quality-gate.json, and cross-model validation files.
// Prints result to stdout. Never throws — failures are reported as warnings.

import fs from 'fs';
import path from 'path';

const dir = process.argv[2];
if (!dir) {
  console.log('Usage: node scripts/upload-session.mjs <results_dir>');
  process.exit(1);
}

// Check contributor key
let contributorKey;
try {
  const config = JSON.parse(fs.readFileSync('.magellan/config.json', 'utf-8'));
  contributorKey = config.contributor_key || '';
} catch {
  contributorKey = '';
}

if (!contributorKey) {
  console.log('No contributor key configured. Tip: Run `/connect <key>` to publish discoveries.');
  process.exit(0);
}

// Read structured data
let ingest;
try {
  ingest = JSON.parse(fs.readFileSync(path.join(dir, 'ingest.json'), 'utf-8'));
} catch (e) {
  console.log('Upload skipped: could not read ingest.json — ' + e.message);
  process.exit(0);
}

let finalData = [];
try {
  const raw = JSON.parse(fs.readFileSync(path.join(dir, 'final.json'), 'utf-8'));
  finalData = raw.final_hypotheses || raw.hypotheses || raw;
} catch {}

// Convert groundedness string → integer (API requires number 0-10)
function groundednessToInt(g) {
  if (typeof g === 'number') return Math.min(10, Math.max(0, Math.round(g)));
  const map = { HIGH: 8, MEDIUM: 5, LOW: 2 };
  return map[String(g).toUpperCase()] ?? 5;
}

// Compose mechanism text from available fields (API requires ≥200 chars)
function composeMechanism(h) {
  if (h.mechanism && h.mechanism.length >= 200) return h.mechanism;
  const parts = [
    h.title,
    h.bridge && `Bridge concept: ${h.bridge}`,
    h.key_prediction && `Key prediction: ${h.key_prediction}`,
    h.key_numbers && `Key parameters: ${Object.entries(h.key_numbers).map(([k,v]) => `${k}=${v}`).join(', ')}`,
    h.quality_gate_notes && `Quality gate notes: ${h.quality_gate_notes}`,
  ].filter(Boolean);
  return parts.join('. ');
}

// Compose test protocol from key_prediction + quality_gate_notes (API requires ≥100 chars)
function composeTestProtocol(h) {
  if (h.test_protocol && h.test_protocol.length >= 100) return h.test_protocol;
  if (h.testProtocol && h.testProtocol.length >= 100) return h.testProtocol;
  const parts = [
    h.key_prediction && `Discriminating test: ${h.key_prediction}`,
    h.key_numbers && `Expected values: ${Object.entries(h.key_numbers).map(([k,v]) => `${k}=${v}`).join(', ')}`,
    h.quality_gate_notes,
  ].filter(Boolean);
  return parts.join('. ') || 'See full hypothesis card for test protocol details.';
}

// Build hypotheses from final.json
const hypotheses = (Array.isArray(finalData) ? finalData : []).map(h => ({
  id: h.id || h.title?.slice(0, 20) || 'unknown',
  title: h.title || '',
  mechanism: composeMechanism(h),
  supportingEvidence: h.supporting_evidence || h.supportingEvidence
    || h.quality_gate_notes || 'See full hypothesis card for supporting evidence.',
  counterEvidence: h.counter_evidence || h.counterEvidence || '',
  testProtocol: composeTestProtocol(h),
  bridgeSummary: h.bridge_summary || h.bridgeSummary || h.bridge || '',
  compositeScore: h.composite_score || h.compositeScore || 5,
  confidence: h.confidence || 5,
  groundedness: groundednessToInt(h.groundedness),
  qualityGate: h.verdict || h.quality_gate || h.qualityGate || 'CONDITIONAL_PASS',
  noveltyStatus: h.novelty_status || h.noveltyStatus || 'Unknown',
  cycle: h.cycle || 1,
  parentIds: h.parent_ids || h.parentIds || []
}));

// Read killed hypotheses — check final.json "excluded" first, then quality-gate.json
let killed = [];
try {
  // final.json may have "excluded" array with FAIL verdicts
  const raw = JSON.parse(fs.readFileSync(path.join(dir, 'final.json'), 'utf-8'));
  const excluded = raw.excluded || [];
  if (excluded.length > 0) {
    killed = excluded.map(h => ({
      id: h.id || 'unknown', title: h.title || '',
      mechanism: h.mechanism || '',
      killReason: h.kill_reason || h.killReason || h.reason || 'Failed quality gate',
      cycle: h.cycle || 1, confidence: h.confidence || 0,
      groundedness: groundednessToInt(h.groundedness),
      noveltyStatus: h.novelty_status || 'Unknown'
    }));
  }
} catch {}
// Fallback: read from quality-gate.json if no excluded in final.json
if (killed.length === 0) {
  try {
    const qg = JSON.parse(fs.readFileSync(path.join(dir, 'quality-gate.json'), 'utf-8'));
    const fails = (qg.hypotheses || qg.final_hypotheses || qg).filter(
      h => (h.verdict || h.quality_gate) === 'FAIL');
    killed = fails.map(h => ({
      id: h.id || 'unknown', title: h.title || '', mechanism: h.mechanism || '',
      killReason: h.kill_reason || h.killReason || h.reason || 'Failed quality gate',
      cycle: h.cycle || 1, confidence: h.confidence || 0,
      groundedness: groundednessToInt(h.groundedness),
      noveltyStatus: h.novelty_status || 'Unknown'
    }));
  } catch {}
}

// Read cross-model validation
let crossModel = {};
try { crossModel.gpt = fs.readFileSync(path.join(dir, 'validation-gpt.md'), 'utf-8').slice(0, 5000); } catch {}
try { crossModel.gemini = fs.readFileSync(path.join(dir, 'validation-gemini.md'), 'utf-8').slice(0, 5000); } catch {}

const payload = {
  session: {
    id: ingest.session_id,
    mode: ingest.mode,
    status: ingest.status,
    fieldA: ingest.field_a,
    fieldC: ingest.field_c,
    bridgeConcepts: ingest.bridge_concepts || [],
    strategy: ingest.strategy,
    disjointness: ingest.disjointness,
    pipelineStats: ingest.pipeline_stats,
    startedAt: ingest.started_at,
    completedAt: ingest.completed_at
  },
  hypotheses,
  killedHypotheses: killed,
  crossModelValidation: Object.keys(crossModel).length > 0 ? crossModel : undefined
};

try {
  const res = await fetch('https://www.magellan-discover.ai/api/sessions/upload', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + contributorKey, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const data = await res.json();

  if (res.status === 201) {
    console.log('Published to magellan-discover.ai: ' + (data.message || `${hypotheses.length} hypotheses`));
    ingest.uploaded = true;
    ingest.uploadedAt = new Date().toISOString();
    fs.writeFileSync(path.join(dir, 'ingest.json'), JSON.stringify(ingest, null, 2));
  } else {
    console.log('Upload warning (' + res.status + '): ' + (data.error || 'Unknown error'));
    ingest.uploaded = false;
    fs.writeFileSync(path.join(dir, 'ingest.json'), JSON.stringify(ingest, null, 2));
  }
} catch (e) {
  console.log('Upload skipped (offline or server error): ' + e.message);
}
