-- caseDB update: Oct 4, 2026 (NUCLEAR connections)
-- BETTISON = Police Chief AND DPSA charter school board secretary
-- Todd Perkins represented Operation Northern Hook targets + named with Banks in 2018 probe
-- Gloria McCastle: $20K+ across Banks/Gay-Dagnogo/Yancey/Knezek — network operative
-- Inner Link: Latisha Johnson (council) + Voices of Women to Win
-- Run: sqlite3 caseDB.sqlite < update_oct4_nuclear_connections.sql

--------------------------------------------------------------
-- CRITICAL: Todd Bettison — Police Chief ON charter school board
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Detroit Police Chief (permanent, appointed Feb 2025 by Duggan, confirmed by council). ALSO Secretary of Detroit Public Safety Academy (DPSA) board — a charter school. Uses official email bettisont239@detroitmi.gov for board business. Previously Deputy Mayor under Duggan (2022-2024). Previously 1st Assistant Chief under James White. 27-year DPD career starting 1994. Wayne State B.S. Criminal Justice. EMU Staff & Command graduate. Oakland University Six Sigma. DDP Board Member. THE POLICE CHIEF SITS ON A CHARTER SCHOOL BOARD. This is the structural bridge between police weaponization nexus and education fraud nexus. DPSA authorized by Eastern Michigan University (reappointed Oct 2023).'
WHERE id = 'bettison-todd';

--------------------------------------------------------------
-- CRITICAL: Todd Perkins — Operation Northern Hook + 2018 probe
--------------------------------------------------------------

UPDATE entities SET
    notes = 'P55623, Perkins Law Group, 615 Griswold Suite 400, Detroit 48226. Banks prior attorney. Ran for Detroit mayor 2025 (4th place, 4,603 votes, 5.35%). REPRESENTED Operation Northern Hook targets: Carol Banks (council staff) and Alonzo Jones (retired DPD officer, sentenced 15 months for cash bribes). ALSO represented Judge Vonda Evans in 2018 federal corruption investigation where Banks was ALSO NAMED as a subject. Fox 2: "others named included Wayne County Sheriff Benny Napoleon, City Councilman Gabe Leland, and former State Reps Brian Banks and Albera Tinsley-Talabi." Perkins represented Evans (co-named subject) and later became Banks''s attorney. Gasper Fiore (convicted bribery) donated $500 to his mayoral campaign. Gay-Dagnogo donated $750 to his campaign.'
WHERE id = 'perkins-todd';

--------------------------------------------------------------
-- CRITICAL: Gloria McCastle — network campaign operative
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('mccastle-gloria', 'Gloria McCastle', 'person',
    'Campaign operative/consultant. Total $20,410 from Banks network: Banks for Senate $9,450, Bank on Banks PAC $3,650, David Knezek State Senate $5,000, Yancey State Rep $1,310, Gay-Dagnogo Strong Women Lead PAC $1,000. Described in 2015 Detroit News profile as counselor at Detroit Recovery Project. Now a political money recipient across 5 committees in the Banks orbit. Bridges Banks campaign to Gay-Dagnogo PAC directly through shared operative.');

--------------------------------------------------------------
-- NEW: Carol Banks — Operation Northern Hook target
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('banks-carol', 'Carol Banks', 'person',
    'Former Detroit City Council staff member. Target of FBI Operation Northern Hook investigation. Represented by Todd Perkins. Relationship to Brian Banks TBD (shared surname — verify).');

--------------------------------------------------------------
-- NEW: Alonzo Jones — Operation Northern Hook convicted
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('jones-alonzo', 'Alonzo Jones', 'person',
    'Retired Detroit police officer. CONVICTED: Operation Northern Hook — cash bribes. Sentenced 15 months. Represented by Todd Perkins. DPD officer convicted of bribery in the same FBI probe nexus.');

--------------------------------------------------------------
-- NEW: Vonda Evans — 2018 federal probe co-named
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('evans-vonda', 'Judge Vonda Evans', 'person',
    'Wayne County Circuit Court judge. Named in 2018 federal corruption investigation alongside Banks, Benny Napoleon, Gabe Leland, Tinsley-Talabi. Represented by Todd Perkins. USAO confirmed she was not a target or suspect. But she was NAMED in same probe as Banks — and Perkins represented her then later became Banks''s attorney.');

--------------------------------------------------------------
-- NEW: Gabe Leland — 2018 federal probe
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('leland-gabe', 'Gabe Leland', 'person',
    'Former Detroit City Councilman. Named in 2018 federal corruption investigation alongside Banks. Later CONVICTED: pled guilty to misconduct in office (accepting $7,500 illegal campaign contribution from Robert Carmack). Resigned from council.');

--------------------------------------------------------------
-- NEW: Benny Napoleon — 2018 federal probe
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('napoleon-benny', 'Benny Napoleon', 'person',
    'Former Wayne County Sheriff. Named in 2018 federal corruption investigation alongside Banks. Died Dec 2020 (COVID). Was a 2013 Detroit mayoral candidate vs Duggan. Perkins backed Napoleon for mayor in 2013.');

--------------------------------------------------------------
-- NEW: David Knezek — McCastle bridge
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('knezek-david', 'David Knezek', 'person',
    'Former MI State Senator (D-Dearborn Heights, 2015-2018). McCastle received $5,000 from his campaign. Same campaign operative pool as Banks network. RESIGNED from Senate 2018 after sexual harassment allegations. Replaced by Adam Hollier who lost to Banks in subsequent redistricting.');

--------------------------------------------------------------
-- UPDATE: Inner Link — Latisha Johnson + Voices of Women
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Print shop/vendor. $98,291 total confirmed (TransparencyUSA): Banks for Senate $39,315, MI Deserves Better SuperPAC $37,151.33, Bank on Banks PAC $10,600, Yancey campaign $8,025, Bank on Wayne County $2,000, Committee to Elect Latisha Johnson $850, Voices of Women to Win $350. Central printing vendor for Banks political network. Latisha Johnson is sitting City Council District 4 member.'
WHERE id = 'inner-link';

--------------------------------------------------------------
-- DPSA Board members — full roster
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('cheeks-kamal', 'Kamal Cheeks', 'person',
    'President, DPSA Board of Directors since Apr 2013 (13+ years). MBC Real Estate. kcheeks@mbcrealestate.com. Real estate professional overseeing a charter school for 13 years.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('simms-charles', 'Charles Simms', 'person',
    'Member, DPSA Board of Directors. Uses city email simmsc@detroitmi.gov. Another city employee sitting on a charter school board.');

--------------------------------------------------------------
-- RELATIONSHIPS: Bettison dual role
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bettison-todd', 'dpsa', 'board-member', 'Secretary, DPSA Board of Directors', 'detroitpsa.com/board-of-directors',
    'The police chief sits on a charter school board. Uses official city email. EMU reappointed Oct 2023. This is the structural bridge: police weaponization nexus ↔ education fraud nexus.');

--------------------------------------------------------------
-- RELATIONSHIPS: Perkins 2018 federal probe
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('perkins-todd', 'evans-vonda', 'attorney', 'Represented Evans in 2018 federal corruption investigation', 'Fox 2 Detroit Jan 2018',
    'Evans was co-named with Banks in same probe. Perkins represented her, then later became Banks''s attorney.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('perkins-todd', 'jones-alonzo', 'attorney', 'Represented Jones in Operation Northern Hook', 'BridgeDetroit Jan 2025',
    'Jones was retired DPD officer convicted of taking cash bribes. Perkins represented Northern Hook targets.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('perkins-todd', 'banks-carol', 'attorney', 'Represented Carol Banks in Operation Northern Hook', 'BridgeDetroit Jan 2025',
    'Council staff member. Relationship to Brian Banks TBD.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-brian', 'evans-vonda', 'co-named', 'Both named in 2018 federal corruption investigation', 'Fox 2 Detroit Jan 2018',
    'Same probe also named Napoleon and Leland and Tinsley-Talabi. Banks''s later attorney (Perkins) represented a co-named subject.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-brian', 'napoleon-benny', 'co-named', 'Both named in 2018 federal corruption investigation', 'Fox 2 Detroit Jan 2018',
    'Wayne County Sheriff + convicted felon state rep named in same federal probe.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-brian', 'leland-gabe', 'co-named', 'Both named in 2018 federal corruption investigation', 'Fox 2 Detroit Jan 2018',
    'Leland later convicted of misconduct in office — accepting $7,500 illegal campaign contribution.');

--------------------------------------------------------------
-- RELATIONSHIPS: McCastle bridges
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('mccastle-gloria', 'banks-brian', 'campaign-payee', '$13,100 total from Banks entities (Senate $9,450 + BoB PAC $3,650)', 'TransparencyUSA',
    'Single largest individual payee from Banks Senate campaign.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('mccastle-gloria', 'gay-dagnogo-sherry', 'campaign-payee', '$1,000 from Gay-Dagnogo Strong Women Lead PAC', 'TransparencyUSA',
    'Same operative paid by both Banks AND Gay-Dagnogo. Direct bridge.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('mccastle-gloria', 'yancey-tenisha', 'campaign-payee', '$1,310 from Yancey campaign', 'TransparencyUSA',
    'Three-way bridge: McCastle paid by Banks + Gay-Dagnogo + Yancey.');

--------------------------------------------------------------
-- RELATIONSHIPS: Operation Northern Hook
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('jones-alonzo', 'operation-northern-hook', 'convicted', 'Retired DPD officer, sentenced 15 months, cash bribes', 'BridgeDetroit',
    'Represented by Todd Perkins (Banks''s attorney).');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('banks-carol', 'operation-northern-hook', 'target', 'Council staff member, investigation target', 'BridgeDetroit',
    'Represented by Todd Perkins (Banks''s attorney).');

--------------------------------------------------------------
-- RELATIONSHIPS: Inner Link → Latisha Johnson
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('inner-link', 'johnson-latisha', 'campaign-vendor', '$850 printing for Committee to Elect Latisha Johnson', 'TransparencyUSA',
    'Sitting City Council District 4 member. Founder MECCA Development Corporation.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bettison-todd', 'dpsa', 'board-member', 'record', 'Police Chief = DPSA board secretary. Official city email.', 'detroitpsa.com');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('perkins-todd', 'evans-vonda', 'attorney', 'record', 'Represented Evans — co-named with Banks in 2018 probe', 'Fox 2');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('perkins-todd', 'jones-alonzo', 'attorney', 'record', 'Represented Northern Hook target (convicted 15mo)', 'BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'evans-vonda', 'co-named', 'record', 'Both named in 2018 federal corruption investigation', 'Fox 2');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'leland-gabe', 'co-named', 'record', 'Both named in 2018 federal probe — Leland later convicted', 'Fox 2');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('mccastle-gloria', 'banks-brian', 'campaign-payee', 'record', '$13,100 from Banks entities', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('mccastle-gloria', 'gay-dagnogo-sherry', 'campaign-payee', 'record', '$1,000 from Strong Women Lead PAC', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('inner-link', 'johnson-latisha', 'vendor', 'record', '$850 printing', 'TransparencyUSA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('mccastle-gloria', 'person', 'Gloria McCastle ($20K+ network operative)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('banks-carol', 'person', 'Carol Banks (Northern Hook target)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('jones-alonzo', 'person', 'Alonzo Jones (DPD, convicted bribery)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('evans-vonda', 'person', 'Judge Vonda Evans (2018 probe co-named)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('leland-gabe', 'person', 'Gabe Leland (convicted, 2018 probe)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('napoleon-benny', 'person', 'Benny Napoleon (deceased, 2018 probe)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('knezek-david', 'person', 'David Knezek (resigned harassment)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('cheeks-kamal', 'person', 'Kamal Cheeks (DPSA President 13yr)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('simms-charles', 'person', 'Charles Simms (DPSA, detroitmi.gov)', 4);
