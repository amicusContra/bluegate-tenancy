-- caseDB update: Oct 4, 2026 (WIDE SCRAPE — associates, case numbers, contamination tracing)
-- Hutchings = CO-CHAIR of MI Deserves Better PAC → now Purpose Charter Treasurer
-- Full wiretap target list: 8 named targets, 23+ total convictions in probe
-- Marrocco CONVICTED attempted extortion (Sep 2022), 23+ convictions in his probe
-- Turfe = Evans chief of staff, wiretap target subject, NOT charged
-- Cheeks = Detroit Assn of Realtors president, worked with Sabree on property sales
-- Reynolds = 17 years (longest sentence in Fiore investigation)
-- Rizzo = 66 months, wore wire, $4M forfeiture, key cooperator
-- Run: sqlite3 caseDB.sqlite < update_oct4_wide_scrape.sql

--------------------------------------------------------------
-- CRITICAL: Hutchings = MI Deserves Better PAC CO-CHAIR
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Founder, DH Strategies (now DB Strategies LLC). PURPOSE CHARTER ACADEMY BOARD TREASURER. CO-CHAIRMAN of Michigan Deserves Better SuperPAC — the SAME PAC that paid Inner Link Graphics $37,151 and gave Banks''s Right Turn Project charity $24,700. MBIPC (MI Brain Injury Provider Council) government affairs liaison for Washtenaw and Wayne county. Congressional Black Caucus Champion of Change Awardee 2019. NFL Player Care Foundation partnership. MBA, CBIS. The PAC co-chair became the school''s treasurer. Money in through the PAC, money out through the school, same person managing both.'
WHERE id = 'hutchings-devin';

--------------------------------------------------------------
-- UPDATE: Cheeks — Realtors + Sabree property pipeline
--------------------------------------------------------------

UPDATE entities SET
    notes = 'President, DPSA Board since Apr 2013 (13+ years). Principal Broker & Co-Founder, MBC Real Estate Company. Former President, Detroit Association of Realtors (2016). Detroit Realtor of the Year 2012 & 2016. 14th District Director, Michigan Realtors. Detroit Brownfield Redevelopment Authority Community Advisory Committee. Grand Canyon University MBA (Finance), Ferris State BBA. CRITICAL: Created pilot program allowing Realtors to schedule showings on Wayne County Treasurer (Sabree) owned properties PRIOR TO AUCTION. Sold 52 properties generating $793,789 for Sabree''s office. Real estate broker connecting the property/foreclosure pipeline to charter school governance. Reappointed by EMU Board of Regents Oct 2025.'
WHERE id = 'cheeks-kamal';

--------------------------------------------------------------
-- FULL WIRETAP TARGET LIST (from WJR Dec 27, 2017 + Detroit News Dec 26, 2017)
--------------------------------------------------------------

-- The accidentally unsealed FBI wiretap document named these target subjects:
--
-- 1. Anthony Marrocco — Macomb PW Commissioner — CONVICTED (attempted extortion, Sep 2022)
-- 2. Benny Napoleon — Wayne County Sheriff — DECEASED (COVID Dec 2020)
-- 3. Vonda Evans — Wayne County Judge — CLEARED by USAO
-- 4. Gabe Leland — Detroit Councilman — CONVICTED (state misconduct, May 2021)
-- 5. Brian Banks — State Rep — NOT CHARGED (left office before probe concluded)
-- 6. William Wild — Westland Mayor — CLEARED by USAO
-- 7. Assad Turfe — Chief Assistant to Wayne County Exec Evans — NOT CHARGED
-- 8. Alberta Tinsley-Talabi — State Rep — NOT CHARGED (under investigation via Stanton)
-- + Gasper Fiore — Towing — CONVICTED (bribery conspiracy, Aug 2018)
-- + "Casab" — mentioned in Beeckman affidavit alongside Tinsley-Talabi and Napoleon
--
-- FBI SA Beeckman: "Evidence has been gathered showing that crimes involving
-- corruption have been committed by some of the target subjects, including
-- Tinsley-Talabi, Napoleon and Casab. However, those investigations have been
-- pending for months or years and the evidence so far has not been sufficient
-- to bring federal charges."
--
-- TOTAL CONVICTIONS in broader Macomb+Detroit corruption probe: 23+
-- Including: Rizzo, Fiore, Reynolds, Bucci, Marrocco, Spivey, Leland, Sollars, Johnson

--------------------------------------------------------------
-- NEW: Marrocco — CONVICTED
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('marrocco-anthony', 'Anthony Marrocco', 'person',
    'Former Macomb County Public Works Commissioner (1993-2016). CONVICTED: attempted extortion (pled guilty Sep 2022). Case before Judge Robert Cleland. Plea deal: drops 3 charges, max 16 months. FBI investigated 6+ years. Named in same wiretap as Banks. Part of 23+ conviction probe that included Rizzo, Fiore, Reynolds, Bucci. Charged May 2020 with 4 counts. Teamed with underling (Bucci) to extort contractors. Hired Steve Fishman as defense attorney.');

--------------------------------------------------------------
-- NEW: Turfe — Evans chief of staff, wiretap target
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('turfe-assad', 'Assad Turfe', 'person',
    'Wayne County Executive Warren Evans chief of staff (promoted Jun 2018, previously chief assistant). Named as wiretap "target subject" in accidentally unsealed 2017 FBI document. NOT charged. Started career as jail deputy, became lieutenant. Crain''s Detroit "50 Names to Know in Government" 2021. Gave update on Wayne County corruption case at Commission meeting May 2022. Evans''s right hand man was on the FBI''s target list while Evans was endorsing Banks.');

--------------------------------------------------------------
-- NEW: Wild — Westland Mayor, cleared
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('wild-william', 'William Wild', 'person',
    'Westland Mayor (2007-present, 3+ terms). Named as wiretap "target subject" in 2017 FBI document. CLEARED by USAO — received assurance he was not a target. Ran for Wayne County Executive 2014 (lost to Evans). Attorney: Eric Stempien.');

--------------------------------------------------------------
-- NEW: Reynolds — 17 years
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('reynolds-dean', 'Dean Reynolds', 'person',
    'Former Clinton Township Trustee. CONVICTED: 14 counts bribery and conspiracy. Sentenced 17 YEARS (reduced by 16 months in 2024). Longest corruption sentence in Metro Detroit since Kilpatrick. Took $150K+ in bribes from Rizzo, Fiore, and others for garbage, towing, and engineering contracts. Only person who went to trial. Judge Robert Cleland. Offered 10-year plea, rejected it. Jury convicted in ~1 hour (Jun 2018).');

--------------------------------------------------------------
-- NEW: Rizzo — trash mogul, key cooperator
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('rizzo-chuck', 'Chuck Rizzo Jr.', 'person',
    'Former CEO, Rizzo Environmental Services (Sterling Heights). CONVICTED: bribery + wire fraud. Sentenced 66 months + $4M forfeiture. Key FBI cooperator — wore wire for months, taped bribe payments. But later became uncooperative and "participated in criminal activity during purported cooperation." Denied early release. Embezzled $900K from his own company/investors. Bribes to officials in 4+ Macomb communities. Judge Robert Cleland.');

--------------------------------------------------------------
-- NEW: Bucci — Marrocco's right hand
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('bucci-dino', 'Dino Bucci', 'person',
    'Former Macomb Township Trustee. CONVICTED. Marrocco''s right-hand-man. Cooperated with FBI. FBI had 4 wiretaps on Bucci including his burner phone. Pled guilty to public corruption charges. His cooperation led to Marrocco indictment.');

--------------------------------------------------------------
-- NEW: Eric Smith — Macomb County Prosecutor
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('smith-eric-macomb', 'Eric Smith', 'person',
    'Former Macomb County Prosecutor. CONVICTED in same corruption investigation. The elected county prosecutor convicted alongside contractors and officials in his own jurisdiction. Part of the 23+ conviction count.');

--------------------------------------------------------------
-- NEW: Alan C. Young & Associates
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('alan-young-assoc', 'Alan C. Young & Associates, P.C.', 'org',
    '7310 Woodward Ave Suite 740, Detroit 48202. (313) 873-7500. Minority-owned CPA firm. 40+ years, 35+ professionals. Auditor for MacDowell Preparatory Academy for 9 consecutive years (FY2017-FY2025). Also audits: Quest Charter, Detroit Merit Charter, Grand River Academy, Burton Glen Charter, Oakside Prep, Regent Park Scholars, South Canton Scholars, Warrendale Charter, Laurus Academy, Dearborn Academy, Northridge Academy, Plymouth Educational Center. Alan C. Young: founder/CEO, former Deloitte, appointed by 2 Governors to MI State Board of Accountancy, First Independence Bank board, MSU Black Alumni Board, Kappa Alpha Psi National Auditor. Concurring review partner on ALL engagements.');

--------------------------------------------------------------
-- EXPANDED MACOMB FEDERAL CASE REGISTRY
--------------------------------------------------------------

-- United States v. Marrocco (E.D. Mich., Port Huron) — attempted extortion
--   Pled guilty Sep 2022. Judge Robert Cleland. Max 16 months.
--
-- United States v. Reynolds (E.D. Mich., Port Huron) — 14 counts bribery/conspiracy
--   Convicted Jun 2018 (jury, ~1 hour). 17 years. Judge Robert Cleland.
--   Reduced by 16 months (retroactive guidelines, Mar 2024).
--
-- United States v. Rizzo (E.D. Mich., Port Huron) — bribery + wire fraud
--   Pled guilty. 66 months + $4M. Judge Robert Cleland. Key cooperator.
--
-- United States v. Bucci (E.D. Mich.) — public corruption
--   Pled guilty. Cooperated. 4 wiretaps on his phones.
--
-- All before Judge Robert Cleland in Port Huron.
-- Macomb cases tried in Port Huron (Eastern Division).
-- Detroit cases (Spivey, Sollars) in Detroit (Southern Division).

--------------------------------------------------------------
-- RELATIONSHIPS
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('hutchings-devin', 'mi-deserves-better', 'co-chairman', 'Co-Chair of Michigan Deserves Better SuperPAC', 'LinkedIn profile',
    'PAC co-chair → school treasurer. Same person managed the PAC that gave Banks''s charity $24,700 AND now manages the school''s finances.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('cheeks-kamal', 'sabree-eric', 'business', 'Created pilot program selling Sabree-owned properties through Realtors', 'LinkedIn + Detroit Assn of Realtors records',
    '$793,789 in property sales through Sabree''s office. Real estate broker connected to county treasurer connected to charter school governance.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('turfe-assad', 'evans-warren', 'chief-of-staff', 'Chief of Staff to Wayne County Executive', 'Arab American News Jun 2018 + Crain''s 2021',
    'Evans''s right hand man was FBI wiretap target subject. Evans endorsed Banks. Turfe not charged.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('marrocco-anthony', 'fiore-gasper', 'co-investigation', 'Same FBI wiretap investigation, both convicted', 'Detroit News + DOJ',
    'Macomb County Public Works ↔ Towing empire. 23+ convictions in combined probe.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('reynolds-dean', 'fiore-gasper', 'bribery', 'Reynolds took bribes from Fiore for towing contracts', 'DOJ + Detroit News',
    'Reynolds got 17 years. Fiore got 21 months. Reynolds went to trial; Fiore cooperated.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('rizzo-chuck', 'reynolds-dean', 'co-conspirator', 'Rizzo bribed Reynolds for trash contracts', 'DOJ + WXYZ',
    'Key cooperator taped Reynolds. Jury convicted in ~1 hour based on recordings.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('hutchings-devin', 'mi-deserves-better', 'co-chairman', 'record', 'PAC co-chair → school treasurer pipeline', 'LinkedIn');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('cheeks-kamal', 'sabree-eric', 'business', 'record', 'Property sales pilot with Wayne Co Treasurer', 'Detroit Assn Realtors');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('turfe-assad', 'evans-warren', 'chief-of-staff', 'record', 'COS — wiretap target, not charged', 'Arab American News');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('marrocco-anthony', 'fiore-gasper', 'co-investigation', 'record', 'Both convicted in Macomb probe', 'DOJ');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('marrocco-anthony', 'person', 'Marrocco (convicted extortion)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('turfe-assad', 'person', 'Assad Turfe (Evans COS, wiretap target)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('wild-william', 'person', 'William Wild (Westland Mayor, cleared)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('reynolds-dean', 'person', 'Dean Reynolds (17 years)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('rizzo-chuck', 'person', 'Chuck Rizzo Jr. (66mo, key cooperator)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('bucci-dino', 'person', 'Dino Bucci (cooperator, 4 wiretaps)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('smith-eric-macomb', 'person', 'Eric Smith (Macomb Prosecutor, convicted)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('alan-young-assoc', 'entity', 'Alan C. Young & Associates (auditor 9yr)', 3);
