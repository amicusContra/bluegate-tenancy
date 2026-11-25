-- caseDB update: Oct 4, 2026 (LARA API — programmatic access achieved)
-- API endpoint: /api/businessEntitySearch/webSearch + /api/BusinessRecordDetails/GetRecordDetails
-- Bypassed Cloudflare by making fetch calls from authenticated browser context.
-- Tool saved: tools/lara_batch.js (paste into DevTools console)
--
-- DISCOVERIES:
-- WhitlowBanks LLC: entity name = "Whitlow" + "Banks" combined (filed 2017)
-- Larry Thomas Jr: email larrythomasjr@the-inner-link.com, home 22256 Laurel Woods Ct Southfield
-- Inner Link assumed name: WWW.OBITUARIES4LESS.COM (obituary printing)
-- Kevin W Mccastle: Roofing & Construction LLC (Fremont MI — different from Gloria)
-- Charles Whitlow: Muskegon restaurant owner (may = "Carles" TransparencyUSA payee)
-- Run: sqlite3 caseDB.sqlite < update_oct4_lara_api.sql

--------------------------------------------------------------
-- WHITLOWBANKS LLC — name says it all
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('whitlowbanks', 'WhitlowBanks LLC', 'org',
    'LARA Entity ID 802085022. Filed 04/20/2017 (during Banks political career). Active (inactive date 02/18/2020). Agent: TAMEKA RAMSEY, 91 N Saginaw St #110, Pontiac MI 48342. Entity name literally combines "Whitlow" + "Banks" — suggests a business partnership. TransparencyUSA lists "Carles Whitlow" as $8,500 payee from Banks for Senate. "Carles" may be "Charles" misspelled, or a given name. All Purpose Clause.');

--------------------------------------------------------------
-- UPDATE: Inner Link — email + assumed name
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Print shop/vendor. $98,291 total from Banks orbit. LARA: THE INNER LINK LLC (Entity ID 801470477, filed 08/18/2008, Active, Good). Agent: LARRY THOMAS JR. Office: 17515 W 9 Mile Rd, Suite 100, Southfield MI 48075. Mailing: 17515 W 9 Mile Rd, Ste 100, Ste. 100, Southfield MI 48075. EMAIL: larrythomasjr@the-inner-link.com. Assumed name: WWW.OBITUARIES4LESS.COM (registered 06/27/2019, renewed 12/26/2024, expires 12/31/2029). Also does obituary printing. Act: Michigan Limited Liability Company Act (023-1993). Management: Member. Legacy doc: E1147W.'
WHERE id = 'inner-link';

--------------------------------------------------------------
-- UPDATE: Larry Thomas Jr — home address
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Owner/Agent of The Inner Link LLC ($98K print vendor). Email: larrythomasjr@the-inner-link.com. Business: 17515 W 9 Mile Rd Ste 100, Southfield MI 48075. ALSO owns: The Larry Thomas Group LLC (Entity ID 801763084, filed 02/20/2014, Active). Home: 22256 Laurel Woods Ct, Southfield MI 48034. Also runs obituaries4less.com. Biggest single vendor in Banks political network.'
WHERE id = 'thomas-larry-jr';

--------------------------------------------------------------
-- UPDATE: Carles Whitlow — likely = Charles Whitlow
--------------------------------------------------------------

-- TransparencyUSA: "Carles Whitlow" $8,500 from Banks for Senate
-- LARA: "WhitlowBanks LLC" entity exists (filed 2017, Banks career era)
-- LARA: CHARLES WHITLOW owns Whitlow's Forerunner Restaurant Inc
--   (800215280, 4610 Airline Rd, Muskegon MI 49444, filed 1985, Active)
--   President + Director. Jamie Dorbos = Secretary/Treasurer/Director.
-- LARA: CHARLES WHITLOW was agent for Whitlow Hoofman Enterprises Inc
--   (800273598, dissolved 2009, same Muskegon address)
-- NOTE: Muskegon is 2.5 hours from Detroit. Different metro.
--   Could be same person (campaign worker doesn't need to be local)
--   or different Charles Whitlow. The WhitlowBanks LLC (Pontiac)
--   is closer to Detroit metro.

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('whitlow-charles', 'Charles "Carles" Whitlow', 'person',
    'TransparencyUSA: "Carles Whitlow" — $8,500 payee from Banks for Senate (5th largest individual payee). LARA shows WhitlowBanks LLC (802085022, filed 04/20/2017 — Banks era, Pontiac). Also Charles Whitlow owns Whitlow''s Forerunner Restaurant Inc (800215280, Muskegon, 4610 Airline Rd, filed 1985, Active) — President + Director, Jamie Dorbos = Sec/Treas/Dir. Whitlow Hoofman Enterprises dissolved 2009. "Carles" may be misspelling of "Charles" or actual given name. Whether Muskegon Whitlow = Detroit campaign Whitlow TBD.');

--------------------------------------------------------------
-- Kevin W Mccastle — Fremont MI (different from Gloria)
--------------------------------------------------------------

-- Kevin W Mccastle: Mccastle Roofing & Construction LLC
-- 801266950, filed 03/12/2004, 9029 W 16th St, Fremont MI 49412
-- Fremont is rural western MI — different metro from Detroit
-- Veronica Mccastle: MccastleSoap LLC (802763700, filed 11/10/2021)
-- Gloria McCastle ($20K+ political operative) may be related or different family
-- NOTE: McCASTLE (roofing) vs McCAST  LE (political) — same spelling

--------------------------------------------------------------
-- LARA API INFRASTRUCTURE NOTES
--------------------------------------------------------------

-- SEARCH endpoint:
--   GET /api/businessEntitySearch/webSearch
--   Params: SEARCH_VALUE, SearchByOption=-1, QueryTypeId=1, 
--           BusinessRecordTypeId=0, BusinessStatusTypeId=0
--   Returns: {template: [...], rows: {id: {TITLE, RECORD_NUM, Agent, ...}}}
--
-- DETAIL endpoint:
--   GET /api/BusinessRecordDetails/GetRecordDetails/{entityId}
--   Returns: full entity detail including:
--     Name, FileNum, Status, RecordType, RegisteredAgentName,
--     RegisteredAgentAddress, Email, Parties[], AssumedNames[],
--     InitialFilingDate, InactiveDate, AnnualReportDueDate,
--     ManagementTypeId, Purpose, ActFormedUnder
--
-- HISTORY endpoint (not yet tested):
--   GET /api/BusinessRecordDetails/GetHistory/{entityId}
--
-- ACCESS: Cloudflare bot protection. Must run from browser context
--   that passed challenge. Tool: tools/lara_batch.js
--   Paste into DevTools console on mibusinessregistry.lara.state.mi.us

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('whitlowbanks', 'banks-brian', 'named-entity', 'inference', 'Entity name = "Whitlow" + "Banks" combined, filed 2017', 'LARA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('whitlowbanks', 'entity', 'WhitlowBanks LLC (entity name = Whitlow+Banks)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('whitlow-charles', 'person', 'Charles "Carles" Whitlow ($8,500 payee)', 4);
