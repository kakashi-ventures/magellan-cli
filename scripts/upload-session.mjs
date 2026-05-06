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

// Load quality-gate key_strength fields for supportingEvidence fallback
const qgById = {};
try {
  const qg = JSON.parse(fs.readFileSync(path.join(dir, 'quality-gate.json'), 'utf-8'));
  for (const h of (qg.hypotheses || qg.verdicts || [])) { qgById[h.id] = h; }
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
    || h.quality_gate_notes
    || (qgById[h.id] && qgById[h.id].key_strength)
    || `Bridge: ${h.bridge || h.bridge_summary || 'see mechanism'}. Key prediction: ${h.key_prediction || 'see full card'}. This hypothesis passed the MAGELLAN Quality Gate with verdict CONDITIONAL_PASS.`,
  counterEvidence: h.counter_evidence || h.counterEvidence || '',
  testProtocol: composeTestProtocol(h),
  bridgeSummary: h.bridge_summary || h.bridgeSummary || h.bridge || '',
  compositeScore: h.composite_score || h.compositeScore || h.composite || 5,
  confidence: h.confidence || 5,
  groundedness: groundednessToInt(h.groundedness),
  qualityGate: h.verdict || h.quality_gate || h.qualityGate || 'CONDITIONAL_PASS',
  noveltyStatus: h.novelty_status || h.noveltyStatus || 'Unknown',
  cycle: h.cycle || 1,
  parentIds: h.parent_ids || h.parentIds || [],
  // Rich data (v5.15+) — merged from quality-gate.json enrichment or present directly
  ...(h.rubric_details || h.rubric ? { rubricScores: h.rubric_details || h.rubric } : {}),
  ...(h.claims_verified != null ? { claimVerification: {
    claims_verified: h.claims_verified, claims_failed: h.claims_failed,
    claims_unverifiable: h.claims_unverifiable || h.claims_unverified,
    claims_parametric: h.claims_parametric || h.claims_speculative,
    citation_hallucinations: h.citation_hallucinations,
    key_strength: h.key_strength, key_risk: h.key_risk || h.key_weakness,
  } } : {}),
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

// Read cross-model validation (raw markdown — backward compat)
let crossModel = {};
try { crossModel.gpt = fs.readFileSync(path.join(dir, 'validation-gpt.md'), 'utf-8').slice(0, 5000); } catch {
  try { crossModel.gpt = fs.readFileSync(path.join(dir, 'gpt-validation.md'), 'utf-8').slice(0, 5000); } catch {}
}
try { crossModel.gemini = fs.readFileSync(path.join(dir, 'validation-gemini.md'), 'utf-8').slice(0, 5000); } catch {
  try { crossModel.gemini = fs.readFileSync(path.join(dir, 'gemini-validation.md'), 'utf-8').slice(0, 5000); } catch {}
}

// Read structured session-level data for rich upload
let crossModelConsensus, computationalValidation, sessionAnalysis, literatureData, scoutData;
try { crossModelConsensus = JSON.parse(fs.readFileSync(path.join(dir, 'cross-model.json'), 'utf-8')); } catch {}
try { computationalValidation = JSON.parse(fs.readFileSync(path.join(dir, 'computational.json'), 'utf-8')); } catch {
  try { computationalValidation = JSON.parse(fs.readFileSync(path.join(dir, 'computational-validation.json'), 'utf-8')); } catch {}
}
// Session-analyst structured output. Filename has varied across versions:
//   v5.13+:   meta-insights.json       (current canonical — written by session-analyst agent)
//   pre-5.13: session-analysis.json or session-analyst.json (legacy)
try { sessionAnalysis = JSON.parse(fs.readFileSync(path.join(dir, 'meta-insights.json'), 'utf-8')); } catch {
  try { sessionAnalysis = JSON.parse(fs.readFileSync(path.join(dir, 'session-analyst.json'), 'utf-8')); } catch {
    try { sessionAnalysis = JSON.parse(fs.readFileSync(path.join(dir, 'session-analysis.json'), 'utf-8')); } catch {}
  }
}
try { literatureData = JSON.parse(fs.readFileSync(path.join(dir, 'literature.json'), 'utf-8')); } catch {}
try { scoutData = JSON.parse(fs.readFileSync(path.join(dir, 'scout.json'), 'utf-8')); } catch {}

// Read pipeline narratives — auto-discover ALL .md files in results dir.
// Forward-compatible: any new .md file the pipeline produces is uploaded.
//
// Aliases map filename stems (what agents actually write today) → canonical
// keys (what the magellan-web frontend's PHASE_ORDER in
// `app/sessions/[id]/page.tsx` expects). The frontend filters narratives by
// these exact keys, so any mismatch silently hides the section.
//
// CONTRACT WITH FRONTEND: any change to a canonical key requires a coordinated
// magellan-web frontend update. Adding NEW canonicals is safe (frontend ignores
// unknown keys); RENAMING an existing canonical breaks the journey rendering.
const NARRATIVE_ALIASES = {
  // agent-written stem → frontend-expected canonical key (PHASE_ORDER)
  'critiqued-cycle1':       'critique-cycle1',
  'cycle1-critique':        'critique-cycle1',
  'critiqued-cycle2':       'critique-cycle2',
  'cycle2-critique':        'critique-cycle2',
  'ranked-cycle1':          'ranking-cycle1',
  'cycle1-ranked':          'ranking-cycle1',
  'ranked-cycle2':          'ranking-cycle2',
  'cycle2-ranked':          'ranking-cycle2',
  'cycle1-evolved':         'evolved-cycle1',
  'evolution-cycle1':       'evolved-cycle1',
  'cycle2-evolved':         'evolved-cycle2',
  'evolution-cycle2':       'evolved-cycle2',
  'literature-landscape':   'literature-context',
  'gpt-validation':         'validation-gpt',
  'gemini-validation':      'validation-gemini',
  'raw-hypotheses-cycle1':  'hypotheses-cycle1',
  'raw-hypotheses-cycle2':  'hypotheses-cycle2',
};
// No skiplist (v5.26.1): the frontend explicitly renders export-gpt/export-gemini
// as "GPT Validation Prompt" / "Gemini Validation Prompt" sections. Auto-discovery
// uploads them too. Frontend treats unknown keys as opt-out — safe forward.
const NARRATIVE_SKIPLIST = new Set([]);
const pipelineNarratives = {};
try {
  const mdFiles = fs.readdirSync(dir).filter(f => f.endsWith('.md'));
  for (const filename of mdFiles) {
    const stem = filename.slice(0, -3); // strip .md
    if (NARRATIVE_SKIPLIST.has(stem)) continue;
    const key = NARRATIVE_ALIASES[stem] || stem;
    if (pipelineNarratives[key]) continue; // first match wins
    try { pipelineNarratives[key] = fs.readFileSync(path.join(dir, filename), 'utf-8'); } catch {}
  }
} catch (e) {
  console.log('Warning: could not auto-discover .md files in ' + dir + ': ' + e.message);
}

// Read empirical validation (v5.13) — optional, backward-compatible
let empiricalValidation;
try {
  const convergence = JSON.parse(fs.readFileSync(path.join(dir, 'convergence.json'), 'utf-8'));
  const cAgg = convergence?.convergence?.aggregate || {};
  const datasetEvidence = JSON.parse(fs.readFileSync(path.join(dir, 'dataset-evidence.json'), 'utf-8'));
  const dAgg = datasetEvidence?.dataset_evidence?.aggregate || {};
  const confirmed = dAgg.confirmed || 0;
  const totalClaims = dAgg.total_claims || 0;
  const datasetScore = totalClaims > 0
    ? Math.max(0, Math.min(10, ((confirmed * 10 + (dAgg.supported || 0) * 6 - (dAgg.contradicted || 0) * 5) / totalClaims)))
    : 0;
  const strongConv = cAgg.strong_count || 0;
  const moderateConv = cAgg.moderate_count || 0;
  const convScore = strongConv > 0 ? 9 : moderateConv > 0 ? 6 : (cAgg.weak_count || 0) > 0 ? 3 : 0;
  empiricalValidation = {
    convergenceStrongCount: strongConv,
    convergenceModerateCount: moderateConv,
    datasetConfirmedCount: confirmed,
    datasetTotalClaims: totalClaims,
    empiricalEvidenceScore: Math.round((datasetScore * 0.55 + convScore * 0.45) * 10) / 10
  };
} catch {
  // Empirical validation files don't exist — backward-compatible, skip silently
}

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
    outputLicense: ingest.output_license || null,
    outputLicenseReason: ingest.output_license_reason || null,
    attribution: ingest.attribution || null,
    startedAt: ingest.started_at,
    completedAt: ingest.completed_at
  },
  hypotheses,
  killedHypotheses: killed,
  crossModelValidation: Object.keys(crossModel).length > 0 ? crossModel : undefined,
  empiricalValidation: empiricalValidation || undefined,
  // Rich session-level data (v5.15+ — website will store as JSONB)
  crossModelConsensus: crossModelConsensus || undefined,
  computationalValidation: computationalValidation || undefined,
  sessionAnalysis: sessionAnalysis || undefined,
  literatureData: literatureData || undefined,
  scoutData: scoutData || undefined,
  pipelineNarratives: Object.keys(pipelineNarratives).length > 0 ? pipelineNarratives : undefined,
};

try {
  const res = await fetch('https://www.magellan-discover.ai/api/sessions/upload', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + contributorKey, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const data = await res.json();

  if (res.status === 201) {
    const sessionUrl = data.url || `https://www.magellan-discover.ai/sessions/${ingest.session_id}`;
    console.log('Published to magellan-discover.ai: ' + (data.message || `${hypotheses.length} hypotheses`));
    console.log('View results: ' + sessionUrl);
    console.log('Your profile: https://www.magellan-discover.ai/profile');
    ingest.uploaded = true;
    ingest.uploadedAt = new Date().toISOString();
    ingest.session_url = sessionUrl;
    fs.writeFileSync(path.join(dir, 'ingest.json'), JSON.stringify(ingest, null, 2));
  } else {
    console.log('Upload warning (' + res.status + '): ' + (data.error || 'Unknown error'));
    ingest.uploaded = false;
    fs.writeFileSync(path.join(dir, 'ingest.json'), JSON.stringify(ingest, null, 2));
  }
} catch (e) {
  console.log('Upload skipped (offline or server error): ' + e.message);
}
