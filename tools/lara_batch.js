// LARA MiBusiness Registry Batch Search v2
// Runs inside browser console on mibusinessregistry.lara.state.mi.us
// Paste this entire script into the browser DevTools console (F12 → Console)
// after navigating to the search page so Cloudflare cookies are active.
//
// Usage: After pasting, call:
//   await laraBatch(['inner link', 'banks strategy', 'purpose group'])
//   await laraDetail('801470477')
//
// Rate limiting: LARA enforces ~10 searches per window before HTTP 429.
// This script now auto-backs off and retries on 429.
// Use laraBatchSlow() for 3s delay between searches (safer for large batches).

const SEARCH_EP = '/api/businessEntitySearch/webSearch';
const DETAIL_EP = '/api/BusinessRecordDetails/GetRecordDetails';

async function laraSearch(term, retries = 3) {
  const encoded = encodeURIComponent(term);
  const url = `${SEARCH_EP}?SEARCH_VALUE=${encoded}&SearchByOption=-1&QueryTypeId=1&BusinessRecordTypeId=0&BusinessStatusTypeId=0`;
  for (let attempt = 0; attempt <= retries; attempt++) {
    const r = await fetch(url);
    if (r.ok) return await r.json();
    if (r.status === 429 && attempt < retries) {
      const wait = (attempt + 1) * 15000;
      console.warn(`  ⏳ Rate limited (429). Waiting ${wait/1000}s before retry ${attempt+1}/${retries}...`);
      await new Promise(r => setTimeout(r, wait));
      continue;
    }
    throw new Error(`Search failed: HTTP ${r.status}`);
  }
}

async function laraDetail(entityId) {
  const url = `${DETAIL_EP}/${entityId}`;
  const r = await fetch(url);
  if (!r.ok) throw new Error(`Detail failed: HTTP ${r.status}`);
  return await r.json();
}

async function laraBatch(terms) {
  const results = {};
  for (let i = 0; i < terms.length; i++) {
    const term = terms[i];
    console.log(`[${i+1}/${terms.length}] Searching: ${term}`);
    try {
      const searchData = await laraSearch(term);
      const rows = searchData.rows || {};
      const entities = Object.values(rows);
      console.log(`  Found ${entities.length} results`);
      
      // Get details for each result
      for (const entity of entities) {
        const eid = entity.RECORD_NUM || entity.EntityId;
        const internalId = entity.ID;
        console.log(`  → Detail: ${entity.TITLE?.[0] || 'unknown'} (${eid})`);
        try {
          const detail = await laraDetail(eid);
          results[eid] = {
            search_term: term,
            name: detail.Name,
            entityId: detail.FileNum,
            status: detail.Status?.Name,
            type: detail.RecordType?.Name,
            agent: detail.RegisteredAgentName,
            agentAddress: detail.RegisteredAgentAddress,
            mailingAddress: detail.RegisteredAgentMailingAddress,
            filingDate: detail.InitialFilingDate,
            inactiveDate: detail.InactiveDate,
            arDue: detail.AnnualReportDueDate,
            arStanding: detail.StandingAROverride,
            email: detail.Email,
            purpose: detail.Purpose,
            management: detail.ManagementTypeId,
            assumedNames: detail.AssumedNames?.map(a => a.AssumedName) || [],
            parties: detail.Parties?.map(p => ({
              name: p.Name || p.PartyName,
              title: p.Title || p.PartyType,
              address: p.Address || p.PartyAddress
            })) || [],
            act: detail.ActFormedUnder
          };
          await new Promise(r => setTimeout(r, 500)); // rate limit
        } catch (e) {
          console.warn(`  ⚠ Detail failed for ${eid}: ${e.message}`);
          results[eid] = { search_term: term, name: entity.TITLE?.[0], error: e.message };
        }
      }
    } catch (e) {
      console.error(`  ✗ Search failed: ${e.message}`);
      results[`error_${term}`] = { search_term: term, error: e.message };
    }
    await new Promise(r => setTimeout(r, 1000)); // rate limit between searches
  }
  
  // Output as downloadable JSON
  const blob = new Blob([JSON.stringify(results, null, 2)], {type: 'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `lara_batch_${new Date().toISOString().slice(0,10)}.json`;
  a.click();
  
  console.log(`\n✅ Done! ${Object.keys(results).length} entities saved.`);
  console.table(Object.entries(results).map(([id, r]) => ({
    ID: id,
    Name: r.name,
    Agent: r.agent,
    Status: r.status,
    Email: r.email
  })));
  
  return results;
}

// Slow batch — 3s between searches, safer for large batches
async function laraBatchSlow(terms) {
  const results = {};
  for (let i = 0; i < terms.length; i++) {
    const term = terms[i];
    console.log(`[${i+1}/${terms.length}] Searching: ${term}`);
    try {
      const searchData = await laraSearch(term);
      const rows = searchData.rows || {};
      const entities = Object.values(rows);
      console.log(`  Found ${entities.length} results`);
      
      for (const entity of entities) {
        const eid = entity.RECORD_NUM || entity.EntityId;
        console.log(`  → Detail: ${entity.TITLE?.[0] || 'unknown'} (${eid})`);
        try {
          const detail = await laraDetail(eid);
          results[eid] = {
            search_term: term,
            name: detail.Name,
            entityId: detail.FileNum,
            status: detail.Status?.Name,
            type: detail.RecordType?.Name,
            agent: detail.RegisteredAgentName,
            agentAddress: detail.RegisteredAgentAddress,
            mailingAddress: detail.RegisteredAgentMailingAddress,
            filingDate: detail.InitialFilingDate,
            inactiveDate: detail.InactiveDate,
            arDue: detail.AnnualReportDueDate,
            arStanding: detail.StandingAROverride,
            email: detail.Email,
            purpose: detail.Purpose,
            management: detail.ManagementTypeId,
            assumedNames: detail.AssumedNames?.map(a => a.AssumedName) || [],
            parties: detail.Parties?.map(p => ({
              name: p.Name || p.PartyName,
              title: p.Title || p.PartyType,
              address: p.Address || p.PartyAddress
            })) || [],
            act: detail.ActFormedUnder
          };
          await new Promise(r => setTimeout(r, 1000));
        } catch (e) {
          console.warn(`  ⚠ Detail failed for ${eid}: ${e.message}`);
          results[eid] = { search_term: term, name: entity.TITLE?.[0], error: e.message };
        }
      }
    } catch (e) {
      console.error(`  ✗ Search failed: ${e.message}`);
      results[`error_${term}`] = { search_term: term, error: e.message };
    }
    await new Promise(r => setTimeout(r, 3000));
  }
  
  const blob = new Blob([JSON.stringify(results, null, 2)], {type: 'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `lara_batch_slow_${new Date().toISOString().slice(0,10)}.json`;
  a.click();
  
  console.log(`\n✅ Done! ${Object.keys(results).length} entities saved.`);
  return results;
}

// Make available globally
window.laraSearch = laraSearch;
window.laraDetail = laraDetail;
window.laraBatch = laraBatch;
window.laraBatchSlow = laraBatchSlow;

console.log('🔧 LARA tools v2 loaded. Usage:');
console.log('  await laraBatch(["inner link", "banks strategy"])     // 1s delay');
console.log('  await laraBatchSlow(["inner link", "banks strategy"]) // 3s delay (safer)');
console.log('  await laraDetail("801470477")');
console.log('  await laraSearch("carlton ross")');
console.log('  Rate limit: auto-backoff on HTTP 429 (15s/30s/45s retries)');
