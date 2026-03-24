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
  finalData = raw.hypotheses || raw;
} catch {}

// Build hypotheses from final.json
const hypotheses = (Array.isArray(finalData) ? finalData : []).map(h => ({
  id: h.id || h.title?.slice(0, 20) || 'unknown',
  title: h.title || '',
  mechanism: h.mechanism || '',
  supportingEvidence: h.supporting_evidence || h.supportingEvidence || '',
  counterEvidence: h.counter_evidence || h.counterEvidence || '',
  testProtocol: h.test_protocol || h.testProtocol || '',
  bridgeSummary: h.bridge_summary || h.bridgeSummary || '',
  compositeScore: h.composite_score || h.compositeScore || 5,
  confidence: h.confidence || 5,
  groundedness: h.groundedness || 5,
  qualityGate: h.verdict || h.quality_gate || h.qualityGate || 'CONDITIONAL_PASS',
  noveltyStatus: h.novelty_status || h.noveltyStatus || 'Unknown',
  cycle: h.cycle || 1,
  parentIds: h.parent_ids || h.parentIds || []
}));

// Read killed hypotheses
let killed = [];
try {
  const qg = JSON.parse(fs.readFileSync(path.join(dir, 'quality-gate.json'), 'utf-8'));
  const fails = (qg.hypotheses || qg).filter(h => (h.verdict || h.quality_gate) === 'FAIL');
  killed = fails.map(h => ({
    id: h.id || 'unknown', title: h.title || '', mechanism: h.mechanism || '',
    killReason: h.kill_reason || h.killReason || h.reason || 'Failed quality gate',
    cycle: h.cycle || 1, confidence: h.confidence || 0, groundedness: h.groundedness || 0,
    noveltyStatus: h.novelty_status || 'Unknown'
  }));
} catch {}

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
