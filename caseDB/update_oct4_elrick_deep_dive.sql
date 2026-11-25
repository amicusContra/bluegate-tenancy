-- caseDB update: Oct 4, 2026 (Elrick deep dive + Bettison OIG probe)
-- Bettison UNDER ACTIVE OIG INVESTIGATION (Sep 16 2026) for Sheffield photo suppression
-- Banks on FBI wiretap with Fiore discussing bribes + police official advocacy
-- Banks endorsed by Sabree, Sheffield, Duggan, Chang, Warren Evans — ALL on record
-- Right Turn Project charity fraud ($24K from PAC, no IRS filings, dissolved 2019)
-- Pugh-Cotton-Banks sexual harassment + felony pipeline
-- Run: sqlite3 caseDB.sqlite < update_oct4_elrick_deep_dive.sql

--------------------------------------------------------------
-- CRITICAL: Bettison ACTIVELY under OIG investigation Sep 2026
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Detroit Police Chief (permanent, appointed Feb 2025 by Duggan). Secretary of DPSA charter school board (bettisont239@detroitmi.gov). UNDER ACTIVE OIG INVESTIGATION as of Sep 16, 2026: pressured activist Jahdante Smith to remove social media photos of Mayor Sheffield with ex-boyfriend Marvin Walker. Police then DETAINED Smith and SEIZED his phone. FBI now handling investigation per Free Press sources. DDP Board Member. Previously Deputy Mayor under Duggan (2022-2024). 27-year DPD career. Wayne State B.S. Criminal Justice. The police chief used police power to protect the mayor''s personal reputation, then sits on a charter school board run by the education fraud nexus. Police↔Education↔Political nexus bridge.'
WHERE id = 'bettison-todd';

--------------------------------------------------------------
-- UPDATE: Banks — FBI wiretap + full endorsement list
--------------------------------------------------------------

-- Add wiretap details and endorsement chain
-- FBI Special Agent Bob Beeckman affidavit includes Banks-Fiore wiretap transcripts
-- Banks discussed getting Fiore MDOT contract + advocating with "high-ranking police official"
-- FBI agent believed "paperwork" = cash bribe payment

--------------------------------------------------------------
-- NEW: Jahdante Smith — activist, Bettison target
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('smith-jahdante', 'Jahdante Smith', 'person',
    'Detroit activist. Posted photos of Mayor Sheffield with ex-boyfriend Marvin Walker on social media. Police Chief Bettison personally called him Aug 5 2026 asking to remove photos. City community relations director also called. Sheffield''s father confronted him on social media. Then police DETAINED Smith and SEIZED his phone under warrant related to separate complaint (alleged threats). Bettison denies connection. OIG investigating. FBI now handling case per Free Press. 24-minute recorded phone call with Bettison obtained by CBS Detroit.');

--------------------------------------------------------------
-- NEW: Marvin Walker — Sheffield ex, businessman
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('walker-marvin', 'Marvin Walker', 'person',
    'Detroit businessman and activist with criminal past. Former romantic partner of Mayor Sheffield (when she was on council). Photos of them together posted on social media triggered Bettison''s intervention. Bettison spoke with Walker on Jul 11 2026 about human trafficking complaint. DPD investigation into Walker handed off to outside agency (FBI).');

--------------------------------------------------------------
-- NEW: The Right Turn Project — Banks charity fraud
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('right-turn-project', 'The Right Turn Project', 'org',
    'Banks charity incorporated 2013. Stated purpose: "promoting social welfare of the local community." Received $24,700 from MI Deserves Better PAC ($20K 2015, $2.7K 2016, $2K 2018). $1K from Operating Engineers 324 PAC (2019). NEVER registered with MI AG as required. Stopped filing IRS annual reports in 2015 but kept raising money. IRS dissolved 2019. Campaign T-shirts at charity health expo (May 2016) = IRS political activity violation. Charity Navigator expert Kevin Scally: multiple red flags. Banks claims he is "not a registered agent of any charities." FRAUD.');

--------------------------------------------------------------
-- NEW: Joseph Holland — Banks PAC treasurer
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('holland-joseph', 'Joseph Holland', 'person',
    'Treasurer, Bank on Banks for Michigan PAC. Banks "longtime associate." PAC shares mailing address with Banks home AND shares PO box with Banks Wayne County commissioner campaign account. PAC owes $14,500 in fines for failing to file campaign finance reports. SOS referred to AG May 12, 2022. Name matches MDOC prisoner ID 443789? VERIFY Holland connection to trust/property documents.');

--------------------------------------------------------------
-- NEW: Charles Pugh — sex crimes pipeline
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('pugh-charles', 'Charles Pugh', 'person',
    'Former Detroit City Council President. CONVICTED: sex crimes against a minor (CSC with 14-year-old). Sentenced 5.5-15 years. REFERRED Tramaine Cotton to Banks for a job, saying he "needed a job that didn''t require much work but provided benefits." Cotton then sued Banks for sexual harassment. Pugh→Banks referral pipeline: convicted sex offender referred aide who alleged sexual harassment by Banks.');

--------------------------------------------------------------
-- NEW: Tramaine Cotton — sexual harassment plaintiff
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('cotton-tramaine', 'Tramaine Cotton', 'person',
    'Former Banks legislative aide. Referred by Charles Pugh. Hosted strip shows in clubs. Banks sent him to cash campaign check at grocery store (campaign finance violation). Got $6K raise after 90 days. Sued Banks alleging sexual harassment — pressured to engage in sex acts. Lost cellphone with Banks''s alleged salacious texts. State of Michigan paid ~$12K settlement. Taxpayers paid $85K in legal fees defending Banks. Then-House Speaker Kevin Cotter agreed to settle.');

--------------------------------------------------------------
-- NEW: Gasper Fiore — FBI wiretap connection
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Towing consultant/businessman. CONVICTED: bribery of public official (Clinton Township Trustee Dean Reynolds). Sentenced 21 months (2018). FBI wiretap on his phone recorded conversations with Banks (2016) — Banks discussed getting Fiore MDOT contract + advocating with "high-ranking police official." FBI agent believed "paperwork" in conversation = cash bribe payment. Wiretap affidavit by FBI SA Bob Beeckman listed Banks as "target subject." Donated $500 to Todd Perkins mayoral campaign. Same wiretap affidavit accidentally released naming Banks, Evans, Napoleon, Leland, Tinsley-Talabi.'
WHERE id = 'fiore-gasper';

--------------------------------------------------------------
-- UPDATE: Sabree — CONFIRMED endorses Banks
--------------------------------------------------------------

-- M.L. Elrick Free Press Jul 2022: "Banks enjoys the support of
-- Wayne County Executive Warren Evans, Wayne County Treasurer Eric Sabree,
-- Detroit City Council President Mary Sheffield, state Sen. Stephanie Chang
-- and Detroit Mayor Mike Duggan."
-- Sabree also had family buying foreclosed Harper Woods properties
-- while he ran the auction. Harper Woods = Banks's legislative district.

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('sabree-eric', 'Eric Sabree', 'person',
    'Wayne County Treasurer. ENDORSED Banks for Wayne County Commissioner 2022 (per M.L. Elrick Free Press). Family purchased foreclosed Harper Woods properties through wife''s company U.S. Development Services while Sabree was deputy treasurer running the auction. Ethics complaint dismissed 5-1. At least 10 properties owned by Sabree family. Harper Woods = Banks''s former legislative district. AG investigated his office''s auction practices.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('chang-stephanie', 'Stephanie Chang', 'person',
    'MI State Senator (D-Detroit). ENDORSED Banks for Wayne County Commissioner 2022 per M.L. Elrick Free Press. Sitting state senator endorsing a 9-time convicted felon.');

--------------------------------------------------------------
-- RELATIONSHIPS: Bettison-Sheffield protection
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bettison-todd', 'sheffield-mary', 'protector', 'Called activist to remove photos of Sheffield, police then seized phone', 'CBS Detroit + BridgeDetroit + Metro Times Sep 2026',
    'Police chief used authority to protect mayor''s personal reputation. OIG investigating. FBI now handling. Police weaponization for political protection — identical pattern to Banks case.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('bettison-todd', 'smith-jahdante', 'suppression', 'Called Smith Aug 5 requesting photo removal, police later detained and seized phone', 'CBS Detroit Sep 16 2026',
    '24-minute recorded call. Smith detained, phone seized under warrant. Chief denies connection. OIG probe open.');

--------------------------------------------------------------
-- RELATIONSHIPS: Banks endorsement chain (all confirmed)
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('sabree-eric', 'banks-brian', 'endorser', 'Endorsed Banks for Wayne County Commissioner 2022', 'M.L. Elrick Free Press Jul 2022',
    'Wayne County Treasurer endorsing convicted felon. Sabree family bought foreclosed Harper Woods properties — Banks''s district.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('sheffield-mary', 'banks-brian', 'endorser', 'Endorsed Banks for Wayne County Commissioner 2022', 'M.L. Elrick Free Press Jul 2022',
    'City Council President → now Mayor. Endorsed same felon now under her protection via Bettison.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('chang-stephanie', 'banks-brian', 'endorser', 'Endorsed Banks for Wayne County Commissioner 2022', 'M.L. Elrick Free Press Jul 2022',
    'Sitting state senator endorsing 9-time convicted felon.');

--------------------------------------------------------------
-- RELATIONSHIPS: FBI wiretap web
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fiore-gasper', 'banks-brian', 'wiretap', 'FBI wiretap recorded conversations 2016 — MDOT contract + police official advocacy', 'M.L. Elrick Free Press Jul 2022 + Fox 2 Jan 2018',
    'FBI SA Beeckman affidavit. Banks = "target subject." Fiore offered mobile billboard. "Paperwork" = believed to be cash bribe. Banks advocated for Fiore with "high-ranking police official" — police weaponization nexus ON TAPE.');

--------------------------------------------------------------
-- RELATIONSHIPS: Charity fraud
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('right-turn-project', 'banks-brian', 'charity', 'Banks founded 2013, IRS dissolved 2019', 'M.L. Elrick Free Press Jul 2022',
    'Never registered with AG. Stopped IRS filings 2015. Kept raising money. Campaign T-shirts at charity event. $24,700 from PAC. Banks: "not a registered agent."');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('mi-deserves-better', 'right-turn-project', 'funder', '$24,700 total: $20K (2015) + $2.7K (2016) + $2K (2018)', 'Free Press + TransparencyUSA',
    'PAC funded by rehab centers → Banks''s unregistered charity. Laundering political money through fake charity.');

--------------------------------------------------------------
-- RELATIONSHIPS: Pugh-Cotton-Banks pipeline
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('pugh-charles', 'banks-brian', 'referral', 'Pugh referred Cotton to Banks for no-work job', 'M.L. Elrick Free Press Jul 2022',
    'Convicted sex offender council president referred aide who would allege sexual harassment by Banks. Both predators in the same pipeline.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('cotton-tramaine', 'banks-brian', 'plaintiff', 'Sued Banks for sexual harassment — $12K settlement + $85K taxpayer legal fees', 'M.L. Elrick Free Press Jul 2022',
    'Cotton alleged Banks pressured sex acts. Lost phone with evidence. State paid to settle and defend.');

--------------------------------------------------------------
-- RELATIONSHIPS: Holland PAC
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('holland-joseph', 'banks-brian', 'associate', 'PAC treasurer, "longtime associate," shared mailing address and PO box', 'M.L. Elrick Free Press Jul 2022',
    'BoB PAC treasurer. Shares home address AND PO box with Banks campaigns. $14,500 fines. SOS→AG referral. VERIFY: same Holland as MDOC 443789?');

--------------------------------------------------------------
-- NEW: MI Deserves Better entity
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('mi-deserves-better', 'Michigan Deserves Better Auto Insurance (SuperPAC)', 'org',
    'Political action committee funded by rehabilitation centers opposing no-fault auto insurance reform. Major contributors: Special Tree Ltd $70K, Eisenhower Center $57.5K, MI Assn for Justice $50K, Quality Home Medical $30K, Rainbow Rehabilitation $22.5K. Paid Inner Link $37,151. Gave Banks charity Right Turn Project $24,700. Banks was "leading opponent of auto insurance reform" and "formidable fundraiser who helped colleagues." PAC→Banks charity = political money laundering through unregistered charity.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('bettison-todd', 'sheffield-mary', 'protector', 'record', 'OIG probe Sep 2026: photo suppression + phone seizure', 'CBS Detroit + BridgeDetroit');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fiore-gasper', 'banks-brian', 'wiretap', 'record', 'FBI wiretap 2016: MDOT contract + police official advocacy', 'Free Press + Fox 2');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sabree-eric', 'banks-brian', 'endorser', 'record', 'Endorsed Wayne County Commissioner 2022', 'Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sheffield-mary', 'banks-brian', 'endorser', 'record', 'Endorsed Wayne County Commissioner 2022 as Council President', 'Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('mi-deserves-better', 'right-turn-project', 'funder', 'record', '$24,700 PAC→unregistered charity', 'Free Press + TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('mi-deserves-better', 'inner-link', 'vendor', 'record', '$37,151 printing', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('pugh-charles', 'banks-brian', 'referral', 'record', 'Sex offender referred aide who alleged harassment', 'Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('holland-joseph', 'banks-brian', 'associate', 'record', 'PAC treasurer, shared address, $14.5K fines', 'Free Press');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('smith-jahdante', 'person', 'Jahdante Smith (activist, phone seized)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('walker-marvin', 'person', 'Marvin Walker (Sheffield ex)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('right-turn-project', 'entity', 'Right Turn Project (IRS dissolved)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('holland-joseph', 'person', 'Joseph Holland (PAC treasurer)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('sabree-eric', 'person', 'Eric Sabree (Wayne Co Treasurer)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('pugh-charles', 'person', 'Charles Pugh (convicted sex crimes)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('cotton-tramaine', 'person', 'Tramaine Cotton (harassment plaintiff)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('mi-deserves-better', 'entity', 'MI Deserves Better PAC ($24.7K→Banks charity)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('chang-stephanie', 'person', 'Sen. Stephanie Chang (Banks endorser)', 3);
