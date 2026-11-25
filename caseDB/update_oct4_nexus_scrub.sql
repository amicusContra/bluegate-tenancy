-- caseDB update: Oct 4, 2026 (nexus scrub — inverted graph)
-- Mayor Sheffield, Police Chief Bettison, Duggan bridge
-- Gay-Dagnogo campaign finance, Fleisher/Bedrock bridge
-- Bettison charter school board, Wayne State CJ alumni overlap
-- Run: sqlite3 caseDB.sqlite < update_oct4_nexus_scrub.sql

--------------------------------------------------------------
-- NEW ENTITIES: City Government — Power Tier
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('sheffield-mary', 'Mayor Mary Sheffield', 'person', NULL,
    '76th Mayor of Detroit. Assumed office Jan 1, 2026. First woman mayor of Detroit. Succeeded Duggan. Previously: City Council District 5 (2014-2022), Council President (2022-2026, youngest ever). Born [date of birth withheld]. Retained Bettison as police chief. $200K kickback allegation from Marvin Walker (denied). Gay-Dagnogo donated $1,000 to her mayoral campaign. Sheffield was Council President when Johnson was on Council.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('bettison-todd', 'Police Chief Todd Bettison', 'person', NULL,
    'Detroit Police Chief. Under OIG investigation (Sep 2026) + FBI referred "public corruption side." Appointed by Duggan as Deputy Mayor (May 2022), then Interim Chief, then permanent Chief (2024). Sheffield reappointed. Wayne State B.S. Criminal Justice (same program as Banks). EMU-authorized charter school board member: Detroit Public Safety Academy (reappointed Oct 2023). 27-year DPD career. Called activist Jahdante Smith to suppress Sheffield photos. Phone seized under separate warrant. BOPC voted to support him. Parallel to Banks: police weaponized for personal purposes.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('duggan-mike', 'Former Mayor Mike Duggan', 'person', NULL,
    'Mayor of Detroit 2014-2025. Did not seek reelection. Appointed Banks to Belle Isle PAC (Sep 2024, 3-year term). Appointed Bettison as Deputy Mayor (2022) then Police Chief. Bridge node: connects Banks network to Sheffield administration. Howard (Deputy Mayor) served under Duggan.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('walker-marvin', 'Marvin Walker', 'person', NULL,
    'Sheffield ex-boyfriend. Criminal convictions: forgery, identity theft. Claims Sheffield took $200K kickbacks on City Council real estate deals (denied). Photos posted by activist Smith. Criminal past parallel to Banks criminal past — both in orbit of political power.');

INSERT OR IGNORE INTO entities (id, name, type, email, notes)
VALUES ('smith-jahdante', 'Jahdante Smith', 'person', NULL,
    'Detroit activist. Posted Sheffield/Walker photos on social media. Bettison called asking removal. Phone seized by DPD Aug 19 under separate warrant. Handcuffed in front of 7-year-old son. Parallel to Kevin: civilian targeted by police action after exposing uncomfortable truths.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('dpsa', 'Detroit Public Safety Academy', 'org',
    'Charter school authorized by Eastern Michigan University. Bettison on board of directors (reappointed Oct 2023 by EMU Board of Regents). Police chief on charter school board = structural parallel to Miller (judge) on PCA board.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('bedrock', 'Bedrock (Dan Gilbert)', 'org',
    'Real estate/development company. Rock Holdings PAC gave Sheffield $23,000. Jared Fleisher (Bedrock) gave Johnson $500 AND was honored at Banks PCA inaugural gala alongside Crump-Gibson and DPSCD.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('fleisher-jared', 'Jared Fleisher', 'person',
    'Bedrock executive. Donated $500 to CM Johnson campaign. Honored at PCA inaugural gala (Banks LinkedIn post, May 2026) alongside Crump-Gibson and DPSCD. Bridge between corporate Detroit and Banks network.');

--------------------------------------------------------------
-- NEW ENTITIES: Wayne County Power Tier
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('saunders-tony', 'Tony Saunders', 'person',
    'Former Wayne County CFO. Serial domestic violence (3+ victims, Detroit/Troy/Fort Lauderdale). $300K/year part-time contractor (4x former full-time salary). $425K contract exceeded $100K cap without commission approval. Warren Evans gave contract. Assad Turfe sought leniency at sentencing ("intelligence, work ethic" = parallel to Meihn testimony for Banks). 36th District Court Judge Lynise Bryant sentenced first case.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('turfe-assad', 'Assad Turfe', 'person',
    'Deputy Wayne County Executive. Sought leniency for Saunders at sentencing. Character witness for serial domestic abuser = structural parallel to Meihn testifying Banks has "integrity." Wayne County executive office.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('evans-warren', 'Warren Evans', 'person',
    'Wayne County Executive. Gave Saunders the $425K contract that exceeded cap. Wayne County oversight of county operations.');

--------------------------------------------------------------
-- NEW ENTITIES: Judicial Pipeline
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('mercier-daniel', 'Daniel Mercier', 'person',
    'P72620. Failed 2024 Wayne County Probate Court candidate (finished last). Hired as juvenile referee Jan 21 2026 ($102-140K). Fired Feb 20 2026 — same day Elrick called. 3 women accused DV. 2 states found unfit for bar. Disbarred then negotiated suspension. Tax liens. Malpractice suit. Chief Judge Ewell signed appointment. Nearly 2 dozen Wayne County judges endorsed his campaign. Credential fraud parallel to Banks.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('davis-kahlilia', 'Kahlilia Davis', 'person',
    'Former 36th District Court judge. Suspended 6 years (2023) by Michigan Supreme Court for "pervasive misconduct." Cannot serve until 2029. Tried to run in 2026 — SOS blocked, Court of Claims reversed, SOS blocked again. 36th District Court = same bench as Adam Sabree and Sean Perkins.');

--------------------------------------------------------------
-- RELATIONSHIPS: Sheffield Power Network
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('sheffield-mary', 'bettison-todd', 'appointment', 'Reappointed as Police Chief', 'BridgeDetroit Sep 2026',
    'Sheffield retained Bettison after succeeding Duggan. Both now under scrutiny — Sheffield for kickback allegations, Bettison for OIG investigation.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('sheffield-mary', 'duggan-mike', 'predecessor', 'Succeeded Duggan as Mayor Jan 1 2026', 'Wikipedia',
    'Inherited Duggan appointments including Banks on Belle Isle and Bettison as police chief.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('gay-dagnogo-sherry', 'sheffield-mary', 'campaign-finance', '$1,000 donation to Sheffield mayoral campaign', 'Michigan Chronicle, campaign finance records',
    'The woman who approved Banks charter and became Ombudsman directly funded the mayor. Quid pro quo chain extends upward.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('duggan-mike', 'banks-brian', 'appointment', 'Appointed Banks to Belle Isle PAC, Sep 2024, 3-year term', 'michigan.gov/dnr + thepurposegroupmichigan.com',
    'Mayor appointed a 9-time convicted felon to state parks committee. Bio lists JD without bar admission.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('duggan-mike', 'bettison-todd', 'appointment', 'Appointed Bettison as Deputy Mayor (2022) then Police Chief (2024)', 'detroitmi.gov press releases',
    'Duggan-to-Bettison pipeline: deputy mayor → interim chief → permanent chief.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('duggan-mike', 'howard-melia', 'employer', 'Howard served as Deputy Mayor under Duggan', 'michigan.gov/dnr',
    'Howard and Banks both on Belle Isle PAC — both Duggan appointees or retained.');

--------------------------------------------------------------
-- RELATIONSHIPS: Bettison — Charter + CJ + Police
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bettison-todd', 'dpsa', 'board-member', 'Board of Directors, Detroit Public Safety Academy (EMU charter)', 'EMU Board of Regents Oct 2023 reappointment',
    'Police chief on charter school board = structural parallel to Miller (judge) on PCA board. Both public officials lending authority to charter education.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bettison-todd', 'wayne-state-cj', 'alumnus', 'B.S. Criminal Justice, Wayne State University', 'detroitmi.gov bio',
    'Same CJ program as Banks (B.S. CJ 2004). Both Wayne State CJ alumni. Banks is advisory member of the same department.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('wayne-state-cj', 'Wayne State University Criminal Justice Department', 'org',
    'Department of Criminal Justice, College of Liberal Arts & Sciences. Both Banks (advisory member, alumnus) and Bettison (alumnus, police chief under investigation) are products of this program.');

--------------------------------------------------------------
-- RELATIONSHIPS: Fleisher/Bedrock Bridge
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fleisher-jared', 'johnson-latisha', 'campaign-finance', '$500 donation to Johnson City Council campaign', 'BridgeDetroit campaign finance',
    'Bedrock executive funds PCA board member.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fleisher-jared', 'banks-brian', 'gala-honoree', 'Honored at PCA inaugural gala (May 2026)', 'Banks LinkedIn post May 25 2026',
    'Gala honored: Fleisher (Bedrock), Crump-Gibson (GLLG), DPSCD. Corporate Detroit celebrating convicted felon school founder.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fleisher-jared', 'crump-gibson-jehan', 'gala-co-honoree', 'Both honored at PCA inaugural gala', 'Banks LinkedIn post May 25 2026',
    'Crump-Gibson honored at Banks gala BEFORE entering as defense counsel. Pre-existing relationship evidence multiplies.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('fleisher-jared', 'bedrock', 'employer', 'Bedrock executive', 'LinkedIn');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bedrock', 'sheffield-mary', 'campaign-finance', 'Rock Holdings PAC gave Sheffield $23,000', 'BridgeDetroit campaign finance',
    'Bedrock funds both Sheffield (mayor) and Johnson (PCA board) through PAC + individual. Corporate thread connecting political power to charter network.');

--------------------------------------------------------------
-- RELATIONSHIPS: Wayne County Patronage
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('evans-warren', 'saunders-tony', 'contract', '$425K contract — exceeded $100K cap without commission approval', 'Elrick Free Press Feb 2026');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('turfe-assad', 'saunders-tony', 'character-witness', 'Sought leniency at DV sentencing', 'Elrick Free Press Feb 2026',
    'Character witness for serial abuser = parallel to Meihn testifying Banks has integrity at TCR 22-12. Same pattern: institutional insiders vouching for bad actors.');

--------------------------------------------------------------
-- RELATIONSHIPS: Judicial Pipeline
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('ewell-edward', 'mercier-daniel', 'appointment', 'Chief Judge signed Mercier juvenile referee appointment', 'Elrick Free Press Feb-Mar 2026 + 3rdcc.org SCAO rescission',
    'Ewell signed appointment of man with 3 DV accusations, disbarment, tax liens. Fired same day Elrick called. Pattern: Ewell signs problematic appointments (Mercier AND Miller Canon 4C).');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('davis-kahlilia', 'sabree-adam', 'same-court', '36th District Court — Davis suspended, Sabree sits', 'Court records');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source)
VALUES ('davis-kahlilia', 'perkins-sean', 'same-court', '36th District Court — Davis suspended, Perkins sits', 'Court records');

--------------------------------------------------------------
-- GRAPH EDGES: Power Tier
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sheffield-mary', 'bettison-todd', 'appointment', 'record', 'Reappointed police chief', 'BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sheffield-mary', 'duggan-mike', 'predecessor', 'record', 'Succeeded as mayor Jan 2026', 'Wikipedia');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('gay-dagnogo-sherry', 'sheffield-mary', 'campaign-finance', 'record', '$1,000 donation', 'Michigan Chronicle');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('duggan-mike', 'banks-brian', 'appointment', 'record', 'Belle Isle PAC Sep 2024', 'michigan.gov/dnr');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('duggan-mike', 'bettison-todd', 'appointment', 'record', 'Deputy Mayor 2022 → Chief 2024', 'detroitmi.gov');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('duggan-mike', 'howard-melia', 'appointment', 'record', 'Deputy Mayor under Duggan', 'detroitmi.gov');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bettison-todd', 'dpsa', 'board-member', 'record', 'Charter school board (EMU)', 'EMU Board of Regents Oct 2023');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bettison-todd', 'wayne-state-cj', 'alumnus', 'record', 'B.S. Criminal Justice', 'detroitmi.gov bio');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'wayne-state-cj', 'advisory-member', 'record', 'Advisory Member CJ Dept', 'PowerVoter + MDE records');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fleisher-jared', 'johnson-latisha', 'campaign-finance', 'record', '$500 donation', 'BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fleisher-jared', 'banks-brian', 'gala-honoree', 'record', 'Honored at PCA gala May 2026', 'Banks LinkedIn');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fleisher-jared', 'crump-gibson-jehan', 'gala-co-honoree', 'record', 'Both honored at PCA gala', 'Banks LinkedIn');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bedrock', 'sheffield-mary', 'campaign-finance', 'record', 'Rock Holdings PAC $23,000', 'BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('ewell-edward', 'mercier-daniel', 'appointment', 'record', 'Signed referee appointment — fired same day Elrick called', 'Elrick Free Press + 3rdcc.org SCAO');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('turfe-assad', 'saunders-tony', 'character-witness', 'record', 'Sought leniency at DV sentencing', 'Elrick Free Press');

--------------------------------------------------------------
-- GRAPH NODES: Power Tier
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('sheffield-mary', 'person', 'Mayor Mary Sheffield', 1);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('bettison-todd', 'person', 'Police Chief Todd Bettison', 1);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('duggan-mike', 'person', 'Fmr Mayor Mike Duggan', 1);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('walker-marvin', 'person', 'Marvin Walker', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('smith-jahdante', 'person', 'Jahdante Smith (activist)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('dpsa', 'entity', 'Detroit Public Safety Academy (EMU charter)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('bedrock', 'entity', 'Bedrock (Dan Gilbert)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('fleisher-jared', 'person', 'Jared Fleisher (Bedrock)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('saunders-tony', 'person', 'Tony Saunders (fmr WC CFO)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('turfe-assad', 'person', 'Assad Turfe (Dep WC Exec)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('evans-warren', 'person', 'Warren Evans (WC Executive)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('mercier-daniel', 'person', 'Daniel Mercier P72620', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('davis-kahlilia', 'person', 'Kahlilia Davis (suspended judge)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('wayne-state-cj', 'entity', 'Wayne State CJ Department', 3);
