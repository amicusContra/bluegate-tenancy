-- caseDB update: Oct 4, 2026 (PACER dockets + case number registry)
-- Joseph Holland MDOC 443789 CONFIRMED: convicted drug dealer = Banks PAC treasurer
-- Jennifer Fiore = Gasper Fiore's DAUGHTER = Leland's ex-girlfriend ($2M contracts)
-- Sollars 71 months: Fiore wiretap LED to Taylor mayor investigation
-- Master federal case number registry for all connected cases
-- Run: sqlite3 caseDB.sqlite < update_oct4_pacer_dockets.sql

--------------------------------------------------------------
-- CRITICAL: Joseph Holland MDOC 443789 = Banks PAC treasurer
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Banks "longtime associate." Treasurer of Bank on Banks for Michigan PAC. MDOC #443789, SID 2321035P. DOB [date of birth withheld]. Black male. 5''11" 228lbs. Alias: Joseph Antione Williams. XXXX Grand Ave, Detroit 48238. TWO DRUG CONVICTIONS (Wayne County): (1) Controlled Substance Delivery/Manufacturing Narcotics/Cocaine <50g, offense Aug 2009, sentenced Apr 2010; (2) Controlled Substance Possession Narcotics/Cocaine <25g, offense Feb 2009, sentenced Apr 2009. Discharged May 8, 2024 — "Discharged Without Improvement." PAC shares Banks home address AND PO box with Banks Wayne County campaign. $14,500 unpaid fines, SOS referred to AG May 2022. A convicted drug dealer managing campaign finances for a 9-time convicted felon. SAME Holland referenced in trust/property documents? Tattoo: "Dylan" (son''s name), Linwood/Grand street sign, RIP.'
WHERE id = 'holland-joseph';

--------------------------------------------------------------
-- CRITICAL: Jennifer Fiore — Leland's girlfriend, Gasper's daughter
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('fiore-jennifer', 'Jennifer Fiore', 'person',
    'Gasper Fiore''s DAUGHTER. Was Gabe Leland''s girlfriend. Leland approved $2M+ in city contracts for companies connected to her. Fiore asked Banks on wiretap whether Jennifer would "stop pushing amendments to legislation if state officials gave Fiore the contract he wanted." She is the connection point between Fiore towing empire and Leland city council corruption. Police Chief James Craig contacted FBI after Leland asked Craig about the FBI towing investigation.');

--------------------------------------------------------------
-- CRITICAL: Rick Sollars — Taylor mayor, Fiore-connected
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('sollars-rick', 'Rick Sollars', 'person',
    'Former Mayor of Taylor, MI (2013-2021). CONVICTED: bribery conspiracy + wire fraud. Sentenced 71 months (Oct 2024). Case: United States v. Sollars, 19-cr-20836 (E.D. Mich.). Received $84,538 in bribes from Shady Awad (home renovations, appliances, cash). Stole $70,362 from reelection campaign (signed blank checks from treasurer). Fiore''s company paid for Sollars Las Vegas trip (Wynn Casino, $18K gambling one day) → followed by $114K concrete contract. FBI raided Taylor City Hall Feb 2019. Judge Mark Goldsmith sentenced. USAO Dawn Ison + FBI SAC Cheyvoryea Gibson announced. The Fiore wiretap INVESTIGATION LED to the Sollars case.');

--------------------------------------------------------------
-- NEW: Shady Awad — Sollars briber
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('awad-shady', 'Shady Awad', 'person',
    'Contractor/businessman. Realty Transition company. Bribed Taylor Mayor Sollars with $84,538 in home improvements, appliances, cash. Pled guilty 2021 to bribery conspiracy. Cooperated with FBI. Received city foreclosed properties through Right of First Refusal program in exchange.');

--------------------------------------------------------------
-- NEW: Elisa Grubbs — Leland campaign staffer
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('grubbs-elisa', 'Elisa Grubbs', 'person',
    'Leland campaign consultant/staffer. Charged with bribery conspiracy for picking up $7,500 cash payment from Robert Carmack on Leland''s behalf. Charged via information (= cooperating). Part of the Leland-Carmack-FBI recording chain.');

--------------------------------------------------------------
-- NEW: Robert Carmack — FBI informant who torpedoed Leland case
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('carmack-robert', 'Robert Carmack', 'person',
    'Detroit businessman. FBI informant in Leland investigation. Wore wire to record Leland demanding $15K payoff at Sting strip club. Delivered $7,500 FBI money to Grubbs. BUT his own subsequent criminal conduct TORPEDOED the federal case against Leland — prosecutors said his credibility was destroyed, forcing the state plea deal instead. The informant who was supposed to bring down Leland became the reason Leland got probation instead of prison.');

--------------------------------------------------------------
-- UPDATE: Leland — Jennifer Fiore connection
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Former Detroit City Councilman (District 7, west side). Named in 2018 federal wiretap investigation alongside Banks. CONVICTED: pled guilty to state felony misconduct in office (accepting $7,500 from Carmack). Resigned May 3, 2021. 2.5 years probation. Federal case dismissed because Carmack (FBI informant) conduct destroyed case. Leland''s EX-GIRLFRIEND was JENNIFER FIORE (Gasper Fiore''s daughter). Approved $2M+ in city contracts for Fiore-connected companies. Asked Police Chief Craig about FBI towing investigation — Craig then contacted FBI. Strip club meeting recorded by FBI wire.'
WHERE id = 'leland-gabe';

--------------------------------------------------------------
-- MASTER FEDERAL CASE NUMBER REGISTRY
--------------------------------------------------------------

-- All connected federal cases in E.D. Michigan:
-- ═══════════════════════════════════════════════
-- United States v. Fiore, 16-cr-20732 (E.D. Mich.)
--   Master wiretap case. Banks named as "target subject."
--   FBI SA Bob Beeckman affidavit. Fiore pled guilty Aug 7, 2018.
--   Wiretap recorded Banks-Fiore conversations re: MDOT contract + police official.
--   Accidentally released document listed: Banks, Evans, Napoleon, Leland, Tinsley-Talabi.
--
-- United States v. Spivey, 2:21-cr-20490 (E.D. Mich.)
--   Operation Northern Hook. $35,900 bribes, 8 payments.
--   Sentenced 24 months. Judge Victoria Roberts → Stephen J. Murphy III.
--   Spivey warned targets, leaked source, failed polygraph.
--   AUSAs David Gardey + Frances Carlson.
--   Spivey introduced informant to OTHER unnamed council members.
--
-- United States v. Sollars, 19-cr-20836 (E.D. Mich.)
--   Taylor mayor. $84,538 bribes + $70K campaign theft.
--   Sentenced 71 months (Oct 2024). Judge Mark Goldsmith.
--   FBI raid Taylor City Hall Feb 2019.
--   Fiore wiretap investigation LED here.
--
-- Area Towing v. Sollars, 2:19-cv-10989 (E.D. Mich.)
--   Civil case. Judge Linda V. Parker, Mag. Elizabeth A. Stafford.
--   Obtained FBI wiretap files via subpoena (Mar 2025 order).
--   Forced Fiore deposition (completed Dec 2025, he pled Fifth).
--   Court ordered Fiore to answer by Mar 6, 2026.
--   These files contain the Banks wiretap conversations.
--
-- United States v. Johnson (Bert), E.D. Mich.
--   Ghost employee scheme. $23,133.
--   Judge Matthew Leitman. 90 days.
--   Cooperator Glynis Thornton (EAA school bribery).
--
-- Detroit Pension Fraud (multi-defendant)
--   38+ convictions including Kilpatrick.
--   Jeffrey Beasley: 11 years (trustee, $87M scheme).
--   George Stanton: probation (Tinsley-Talabi COS, wore wire).
--   Judge Nancy Edmunds. AUSA Barbara McQuade.
--
-- KEVIN'S CASES (Ingham County Circuit Court):
--   2026-4301-CZ (Mok v. Banks et al.)
--   2026-4349-CZ (Mok v. Banks et al.)
--   DaSean's custody: 26-108221-DC (Wayne County)

--------------------------------------------------------------
-- RELATIONSHIPS: Fiore family → Leland
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fiore-jennifer', 'leland-gabe', 'romantic', 'Leland''s ex-girlfriend', 'Fox 2 + Detroit News 2018',
    'Leland approved $2M+ in contracts for her connected companies while dating her. Her father was being wiretapped by FBI simultaneously.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('fiore-jennifer', 'fiore-gasper', 'daughter', 'Gasper Fiore''s daughter', 'M.L. Elrick Fox 2 + Detroit News',
    'Father running towing bribery scheme. Daughter dating councilman who approved her contracts. Father asked Banks on wiretap about Jennifer''s legislative amendments.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('leland-gabe', 'fiore-gasper', 'political-ally', 'Leland dated Fiore''s daughter + asked police chief about towing investigation', 'Detroit News Aug 2018',
    'Leland asked Police Chief Craig about FBI towing investigation → Craig contacted FBI. This connection exposed both of them.');

--------------------------------------------------------------
-- RELATIONSHIPS: Sollars → Fiore
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('sollars-rick', 'fiore-gasper', 'bribery', 'Fiore company paid for Sollars Las Vegas trip → $114K contract followed', 'Court filing 2:19-cv-10989 ECF 103',
    'Wynn Casino, $18K gambling in one day. Fiore wiretap investigation LED to Sollars case.');

--------------------------------------------------------------
-- RELATIONSHIPS: Carmack → Leland
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('carmack-robert', 'leland-gabe', 'informant', 'FBI informant, wore wire, recorded $15K demand at strip club', 'Free Press Aug 2020 FOIA recordings',
    'Delivered $7,500 FBI money via Grubbs. His subsequent conduct destroyed federal case → Leland got probation.');

--------------------------------------------------------------
-- UPDATE: Banks Strategy and Consultants
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Campaign consulting entity. Paid $15,750 by Yancey campaign. Paid $20,000 by Coalition to Regulate Marijuana Like Alcohol (2018 election). Total confirmed consulting income: $35,750. Banks was "leading opponent of auto insurance reform" and "formidable fundraiser who helped colleagues" per Free Press.'
WHERE id = 'banks-strategy';

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('holland-joseph', 'banks-brian', 'pac-treasurer', 'record', 'MDOC 443789 convicted drug dealer = PAC treasurer', 'OTIS + Free Press');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fiore-jennifer', 'leland-gabe', 'romantic', 'record', 'Ex-girlfriend — $2M+ contracts approved', 'Fox 2 + Detroit News');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('fiore-jennifer', 'fiore-gasper', 'daughter', 'record', 'Daughter of wiretap target', 'Court records');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('sollars-rick', 'fiore-gasper', 'bribery', 'record', 'Vegas trip → $114K contract', 'PACER 2:19-cv-10989');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('carmack-robert', 'leland-gabe', 'informant', 'record', 'FBI wire at strip club — $7.5K', 'Free Press FOIA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('fiore-jennifer', 'person', 'Jennifer Fiore (Gasper''s daughter, Leland''s ex)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('sollars-rick', 'person', 'Rick Sollars (Taylor mayor, 71 months)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('carmack-robert', 'person', 'Robert Carmack (FBI informant, unreliable)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('grubbs-elisa', 'person', 'Elisa Grubbs (Leland staffer, cooperating)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('awad-shady', 'person', 'Shady Awad ($84K bribery, cooperating)', 4);
