-- caseDB update: Oct 4, 2026 (campaign finance deep dive)
-- Stallworth family operation, Banks-Yancey paid consulting, Inner Link $97K loop
-- Federal bribery convictions (Bert Johnson, Andre Spivey) in endorsement chain
-- Rebecca Fadel on Yancey payroll, Nicole=Thomas wife confirmed
-- Run: sqlite3 caseDB.sqlite < update_oct4_campaign_finance.sql

--------------------------------------------------------------
-- UPDATE: Wells Stallworth — marriage to Thomas III confirmed
--------------------------------------------------------------

UPDATE entities SET
    notes = 'MacDowell Board Chair since 2012 (11 years). MARRIED TO Thomas Stallworth III (former State Rep who defended Banks at 2016 felony rally). Together donated $1,250 to Banks 2022 campaign. Former CEO Children''s Center (Jul 2023 — stepped down 2024 personal reasons). Former VP Planned Parenthood Advocates of Michigan. Founding co-chair MI Reproductive Freedom for All (Prop 3 2022). MAPSA Charter Hero. Refused to discuss Banks with Elrick Aug 2023. Email nwells@childrensctr.net BOUNCED Oct 4 — left org. She IS the institutional bridge between Banks criminal past and educational career.'
WHERE id = 'wells-stallworth-nicole';

--------------------------------------------------------------
-- UPDATE: Thomas Stallworth III — marriage + rally
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('stallworth-thomas', 'Thomas Stallworth III', 'person',
    'Former MI State Rep (2011-2015). Married to Nicole Wells Stallworth (MacDowell Board Chair). Defended Banks at 2016 felony rally: "I think it''s a miscarriage of justice." MSU Board candidate 2024. Govt relations consultant (clients: governor office, DHHS, Quicken Loans, DMC). Detroit Board of Education 1980s. Mother and brother also served in MI House — political dynasty. Endorsed alongside Banks for Duggan 2025. Campaign finance noncompliant (AG referral Oct 2025).');

--------------------------------------------------------------
-- UPDATE: Keith Stallworth
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('stallworth-keith', 'Keith B. Stallworth', 'person',
    'Former MI State Rep. Endorsed Duggan alongside Banks at Michigan Central Station Aug 2025. Donated to Duggan. Part of the Stallworth political family (separate branch from Thomas III). Banks network orbit.');

--------------------------------------------------------------
-- NEW: Banks Strategy and Consultants
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('banks-strategy', 'Banks Strategy and Consultants', 'org',
    'Campaign consulting entity. Banks was PAID $15,750 by Yancey campaign through this entity. Banks ran strategy for the woman who became a judge. Return on investment: Yancey attends his school events, endorses publicly. TransparencyUSA payee records.');

--------------------------------------------------------------
-- NEW: Inner Link Graphics — expanded
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('inner-link', 'Inner Link Graphics', 'org',
    'Print shop/vendor. $97,091 total from Banks orbit: Banks for Senate $39,315, Bank on Banks PAC $10,600, Bank on Wayne County $2,000, Yancey campaign $8,025, MI Deserves Better SuperPAC $37,151. Central printing vendor for entire political network. Owner TBD.');

--------------------------------------------------------------
-- NEW: Convicted endorsers
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('johnson-bert', 'Senator Bert Johnson', 'person',
    'Former MI State Senator. Endorsed Banks 2016 Senate campaign. CONVICTED: federal bribery — sentenced to 7 years. Took bribes while in office. One of two Banks endorsers later convicted of federal corruption.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('spivey-andre', 'Andre Spivey', 'person',
    'Former Detroit City Councilman. Endorsed Banks 2016 Senate campaign. CONVICTED: federal bribery — sentenced to 9 months. Took $35,900 in bribes from towing company owner. Second Banks endorser convicted of federal corruption.');

--------------------------------------------------------------
-- RELATIONSHIPS: Stallworth family operation
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('stallworth-thomas', 'wells-stallworth-nicole', 'spouse', 'Married', 'MLive Oct 2024 + Elrick Aug 2023',
    'The family that credential-washed Banks: Thomas defended at felony rally, Nicole hired him at MacDowell. Both donated $1,250 to his campaign.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('stallworth-thomas', 'banks-brian', 'political-ally', 'Defended Banks at 2016 felony rally + co-endorsed Duggan 2025', 'Detroit News Jul 2016 + Lansing City Pulse Aug 2025',
    '"I think it''s a miscarriage of justice" — said at rally for man with 8 felony charges. Ten years later, still endorsing alongside him.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('stallworth-thomas', 'duggan-mike', 'endorser', 'Endorsed Duggan for Governor Aug 2025 alongside Banks', 'Lansing City Pulse',
    'Michigan Central Station event. 200+ endorsers including Banks, both Stallworths, Marshall Bullock.');

--------------------------------------------------------------
-- RELATIONSHIPS: Banks-Yancey money pipeline
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-brian', 'yancey-tenisha', 'paid-consultant', '$15,750 via Banks Strategy and Consultants', 'TransparencyUSA payee records',
    'Banks was PAID to get Yancey elected as judge. She then attended his school events. This is not friendship — it is return on investment.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-strategy', 'yancey-tenisha', 'campaign-vendor', '$15,750 campaign consulting', 'TransparencyUSA',
    'Banks ran her campaign strategy through his consulting entity.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fadel-rebecca', 'yancey-tenisha', 'campaign-payee', '$5,384.93 from Yancey campaign', 'TransparencyUSA',
    'Legislative staff under Banks ALSO on Yancey payroll. Bar complaint already filed. Cross-pollination between Banks legislative office and Yancey campaign.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('inner-link', 'yancey-tenisha', 'campaign-vendor', '$8,025 printing for Yancey campaign', 'TransparencyUSA');

--------------------------------------------------------------
-- RELATIONSHIPS: Inner Link $97K loop
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('inner-link', 'banks-brian', 'campaign-vendor', '$51,915 total: Senate $39,315, BoB PAC $10,600, Wayne $2,000', 'TransparencyUSA',
    'Banks is Inner Link''s biggest political client. $51,915 directly from Banks entities. Plus $8,025 from Yancey (Banks client). Total orbit: $97,091.');

--------------------------------------------------------------
-- RELATIONSHIPS: Convicted endorsers
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('johnson-bert', 'banks-brian', 'endorser', 'Endorsed Banks 2016 Senate campaign', 'Ballotpedia',
    'Later convicted of federal bribery (7 years). Banks endorsed by convicted federal criminal.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('spivey-andre', 'banks-brian', 'endorser', 'Endorsed Banks 2016 Senate campaign', 'Ballotpedia',
    'Later convicted of federal bribery (9 months, $35,900). Second Banks endorser convicted of federal corruption.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('duggan-mike', 'banks-brian', 'endorser', 'Endorsed Banks 2016 Senate campaign', 'Ballotpedia',
    'Later appointed Banks to Belle Isle PAC. Endorser-to-appointer pipeline.');

--------------------------------------------------------------
-- RELATIONSHIPS: PCA gala honorees (Crump-Gibson pre-existing)
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('crump-gibson-jehan', 'banks-brian', 'gala-honoree', 'Honored at PCA inaugural gala May 2026', 'Banks LinkedIn post May 25 2026',
    'Crump-Gibson honored at Banks school gala 4 months BEFORE entering as defense counsel Sep 30. Pre-existing relationship evidence compounds: LARA attorney-in-fact + gala honoree.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-thomas', 'wells-stallworth-nicole', 'spouse', 'record', 'Married — family credential-washing operation', 'MLive + Elrick');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-thomas', 'banks-brian', 'political-ally', 'record', '2016 felony rally defense + 2025 co-endorsement', 'Detroit News + Lansing City Pulse');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'yancey-tenisha', 'paid-consultant', 'record', '$15,750 via Banks Strategy and Consultants', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fadel-rebecca', 'yancey-tenisha', 'campaign-payee', 'record', '$5,384.93 from campaign', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('inner-link', 'banks-brian', 'vendor', 'record', '$51,915 from Banks entities', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('inner-link', 'yancey-tenisha', 'vendor', 'record', '$8,025 printing', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('johnson-bert', 'banks-brian', 'endorser', 'record', 'Endorsed 2016 — later convicted federal bribery 7yr', 'Ballotpedia + DOJ');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('spivey-andre', 'banks-brian', 'endorser', 'record', 'Endorsed 2016 — later convicted federal bribery 9mo', 'Ballotpedia + DOJ');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('crump-gibson-jehan', 'banks-brian', 'gala-honoree', 'record', 'Honored at PCA gala May 2026 — 4mo before entering as counsel', 'Banks LinkedIn');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('stallworth-keith', 'banks-brian', 'co-endorser', 'record', 'Both endorsed Duggan Aug 2025 + donated', 'Lansing City Pulse');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('stallworth-thomas', 'person', 'Thomas Stallworth III (Nicole''s husband)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('stallworth-keith', 'person', 'Keith B. Stallworth', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('banks-strategy', 'entity', 'Banks Strategy & Consultants', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('inner-link', 'entity', 'Inner Link Graphics ($97K)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('johnson-bert', 'person', 'Sen. Bert Johnson (convicted bribery)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('spivey-andre', 'person', 'Andre Spivey (convicted bribery)', 3);
