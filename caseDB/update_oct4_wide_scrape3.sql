-- caseDB update: Oct 4, 2026 (WIDE SCRAPE batch 3 — campaign payees + contributor analysis)
-- Gay-Dagnogo Strong Women Lead PAC → Banks for Senate $9,750 DIRECT
-- Venus Coleman: Banks payee $7,350 + federal case 2:91-cr-80936 (convicted)
-- Latania Lewis: shared payee Banks $6,675 + Yancey $1,900
-- Banks top contributor analysis: same labor PACs fund Banks AND Sheffield
-- Rafeal Camper: unidentified, $1,000 "Prayers to you and your fam"
-- Run: sqlite3 caseDB.sqlite < update_oct4_wide_scrape3.sql

--------------------------------------------------------------
-- CRITICAL: Gay-Dagnogo PAC → Banks DIRECT $9,750
--------------------------------------------------------------

-- TransparencyUSA: Banks for Senate Top Contributors:
-- Strong Women Lead PAC: $9,750
-- This IS Gay-Dagnogo's PAC.
--
-- So Gay-Dagnogo:
-- 1. Funded Banks's Senate campaign ($9,750 from her PAC)
-- 2. Sat on DPSCD board that authorized his charter schools
-- 3. Announced Purpose Charter Academy development team
-- 4. Moved from DPSCD board to City Ombudsman (quid pro quo)
-- 5. Paid McCastle $1,000 from same PAC (shared Banks operative)
-- 6. Donated $750 to Todd Perkins (Banks's attorney) mayoral campaign
-- 7. Donated $1,000 to Mary Sheffield mayoral campaign
--
-- She is the single most connected node between political and education nexus.

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('gay-dagnogo-sherry', 'banks-brian', 'pac-funder', '$9,750 from Strong Women Lead PAC to Banks for Senate', 'TransparencyUSA',
    'Gay-Dagnogo PAC DIRECTLY funded Banks campaign. Then she sat on board authorizing his schools. Then she moved to Ombudsman. Then she announced his second school. Full circle.');

--------------------------------------------------------------
-- Banks for Senate Top Contributors (full list for reference)
--------------------------------------------------------------

-- $37,500 — Brian Banks (self)
-- $13,000 — Michigan Association of Health Plans PAC
-- $11,500 — Michigan Association for Justice Justice PAC
--           (same PAC gave $50K to MI Deserves Better SuperPAC)
-- $10,000 — Michigan State Carpenters Council PAC
--           (same Carpenters gave Sheffield $20-30K)
-- $10,000 — Operating Engineers Local 324 St of MI PAC
--           (same Engineers gave Right Turn Project $1K)
-- $9,750  — Strong Women Lead PAC (Gay-Dagnogo!)
-- $2,500  — Erin Gust
-- $2,000  — Artesia McNeal Washington
-- $2,000  — Brandi Neal
-- $2,000  — Deborah Watts
--
-- PATTERN: Same labor PACs fund Banks AND Sheffield AND MI Deserves Better.
-- Carpenters: Banks $10K, Sheffield $20-30K
-- Operating Engineers: Banks $10K, Right Turn $1K, Bank on Banks $2.5K
-- MI Assn for Justice: Banks $11.5K, MI Deserves Better $50K

--------------------------------------------------------------
-- NEW: Venus Coleman — Banks payee + federal case
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('coleman-venus', 'Venus Coleman', 'person',
    'Banks for Senate payee: $7,350. Detroit resident. FEDERAL CASE: United States v. Coleman et al, 2:91-cr-80936 (E.D. Mich.), multi-defendant criminal case. Filed Coram Nobis motions 2005 and 2008, both denied by Judge Patrick J. Duggan. A campaign operative/payee with federal criminal history working for a convicted felon''s political campaign.');

--------------------------------------------------------------
-- NEW: Latania Lewis — shared Banks/Yancey payee
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('lewis-latania', 'Latania Lewis', 'person',
    'Paid by BOTH Banks for Senate ($6,675) AND Yancey campaign ($1,900). Total $8,575 from Banks orbit. Administrative Support Secretary at Central City Health (nonprofit, Detroit). Another shared operative across Banks and Yancey campaigns, like McCastle, Inner Link, and Fadel.');

--------------------------------------------------------------
-- NEW: Rafeal Camper — unidentified payment recipient
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('camper-rafeal', 'Rafeal Camper', 'person',
    'Received $1,000 from MacDowell Preparatory Academy (check register Jan 24, 2024). Memo: "Prayers to you and your fam." No public record found identifying this person or connection to the school. Clutch Justice also found no connection. Payment unexplained — direct question for MacDowell.');

--------------------------------------------------------------
-- Banks for Senate full payee registry (top 10)
--------------------------------------------------------------

-- $39,315 — Inner Link Graphics (print vendor)
-- $24,240 — Mass Mailing LLC
-- $10,500 — Custom Promotions
-- $9,450  — Gloria McCastle (individual — also paid by Gay-Dagnogo PAC, Yancey, Knezek)
-- $8,500  — Carles Whitlow (individual — TBD identity)
-- $8,431  — Ross Catering (also paid $6,594 by Bank on Banks PAC = $15,025 total)
-- $8,000  — Brian Banks (self-paid from campaign)
-- $7,350  — Venus Coleman (individual — federal case 2:91-cr-80936)
-- $6,875  — Outfront Media (billboards — later sued Banks for $17K+ unpaid)
-- $6,675  — Latania Lewis (individual — also paid $1,900 by Yancey)
--
-- Total top 10 payees: $129,346 of $171,044 total expenditures (75.6%)
-- Individual payees: McCastle $9,450 + Whitlow $8,500 + Banks $8,000
--                    + Coleman $7,350 + Lewis $6,675 = $39,975 (23.4%)

--------------------------------------------------------------
-- RELATIONSHIPS: Shared payees across campaigns
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('lewis-latania', 'banks-brian', 'campaign-payee', '$6,675 from Banks for Senate', 'TransparencyUSA',
    'Shared with Yancey campaign. Central City Health employee.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('lewis-latania', 'yancey-tenisha', 'campaign-payee', '$1,900 from Yancey campaign', 'TransparencyUSA',
    'Fourth shared Banks-Yancey payee (after Banks Strategy, Inner Link, McCastle, Fadel).');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('coleman-venus', 'banks-brian', 'campaign-payee', '$7,350 from Banks for Senate', 'TransparencyUSA',
    'Federal criminal record (2:91-cr-80936). Convicted person working for convicted felon campaign.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('gay-dagnogo-sherry', 'banks-brian', 'pac-funder', 'record', '$9,750 Strong Women Lead PAC → Banks for Senate', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('coleman-venus', 'banks-brian', 'campaign-payee', 'record', '$7,350 + federal case 2:91-cr-80936', 'TransparencyUSA + PACER');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('lewis-latania', 'banks-brian', 'campaign-payee', 'record', '$6,675 (shared with Yancey)', 'TransparencyUSA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('coleman-venus', 'person', 'Venus Coleman ($7,350 + federal case)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('lewis-latania', 'person', 'Latania Lewis (shared Banks/Yancey $8,575)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('camper-rafeal', 'person', 'Rafeal Camper ($1K "Prayers", unidentified)', 4);
