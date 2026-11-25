-- caseDB update: Oct 4, 2026 (LARA DEEP PULL — Kevin's manual search)
-- RIGHT TURN PROJECT: Holland at 1968 SEVERN (Banks's home). Carlton Ross = Ross Catering.
-- PAC → charity → catering = money loop through treasurer's own company.
-- Save Detroit Jobs officers all at SAME ADDRESS 13560 E. McNichols.
-- Custom Promotions dissolved → reformed as LLC 3 months later (Gordon family).
-- Purpose Group LLC filed Nov 2024 at PCA school address.
-- Inner Link: Larry Thomas Jr (Southfield) vs Tessa R Marks (Lansing) — two entities.
-- Source: Michigan LARA Corporation Search (cofs.lara.state.mi.us), Oct 4 2026.
-- Run: sqlite3 caseDB.sqlite < update_oct4_lara_bombshell.sql

--------------------------------------------------------------
-- RIGHT TURN PROJECT — THE MONEY LOOP
--------------------------------------------------------------
-- Entity ID: 800936257
-- Filed: 05/07/2013
-- Status: DISSOLVED — Operation of Law
-- Inactive: 12/01/2021
-- Agent: JOSEPH HOLLAND JR — 1968 SEVERN, Grosse Pointe Woods MI 48236
-- President: JOSEPH HOLLAND — 1968 SEVERN (BANKS'S HOME ADDRESS)
-- Secretary: TERRENCE TARVER — 16500 North Park Drive, Southfield MI 48075
-- Treasurer: CARLTON ROSS — 16500 North Park Drive, Southfield MI 48075
-- Directors: Carlton Ross, Joseph Holland, Terrence Tarver
--
-- CRITICAL FINDINGS:
-- 1. Holland (MDOC 443789, convicted drug dealer) LIVES AT BANKS'S HOME
-- 2. Carlton Ross IS the owner of Ross Catering ($35K+ from Banks campaigns)
-- 3. The charity treasurer ran a catering company that billed the campaigns
--    that funded the charity he was treasurer of.
-- 4. PAC money → Right Turn Project ($24.7K) → Ross Catering ($15K+)
--    = money cycling through the charity treasurer's own business
-- 5. Charity registered at Banks's home. Never properly registered.
--    IRS dissolved it. $24.7K from MI Deserves Better PAC.
-- 6. Tarver and Ross share an address (16500 North Park Dr, Southfield)

UPDATE entities SET
    notes = 'Right Turn Project Inc. LARA Entity ID 800936257. Filed 05/07/2013. DISSOLVED — Operation of Law, inactive 12/01/2021. Registered at 1968 SEVERN, Grosse Pointe Woods MI 48236 = BANKS HOME ADDRESS. Agent: Joseph Holland Jr (MDOC 443789 convicted drug dealer = Banks PAC treasurer, LIVES WITH BANKS). President: Joseph Holland. Secretary: Terrence Tarver (16500 North Park Dr, Southfield 48075). Treasurer: CARLTON ROSS (16500 North Park Dr, Southfield 48075) = ROSS CATERING OWNER. Money loop: MI Deserves Better PAC gave $24,700 → Right Turn Project → Ross Catering got $35K+ from Banks campaigns → Ross is both charity treasurer AND campaign caterer. Never registered as charity. IRS dissolved. Last AR report 2018.'
WHERE id = 'right-turn-project';

--------------------------------------------------------------
-- NEW: Carlton Ross — Ross Catering owner = charity treasurer
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ross-carlton', 'Carlton Ross', 'person',
    'Owner of Ross Catering. Treasurer of Right Turn Project (Banks charity). Address: 16500 North Park Drive, Southfield MI 48075 (same as Terrence Tarver). MONEY LOOP: As charity treasurer, received PAC money into Right Turn Project ($24.7K). As catering owner, billed Banks campaigns $35K+. Ross Catering paid: Banks for Senate $8,431, Bank on Banks PAC $6,594, Bank on Wayne County $690, plus Bullock $1,800, others. LARA: Right Turn Project director. The man receiving campaign catering money IS the man managing charity money from the same political network.');

--------------------------------------------------------------
-- NEW: Terrence Tarver — charity secretary, shared address with Ross
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('tarver-terrence', 'Terrence Tarver', 'person',
    'Secretary of Right Turn Project (Banks charity). 16500 North Park Drive, Southfield MI 48075 — same address as Carlton Ross (Ross Catering owner/charity treasurer). LARA: Director. Relationship to Banks network beyond charity role TBD.');

--------------------------------------------------------------
-- UPDATE: Holland — LIVES AT BANKS HOME
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Right Turn Project President + Resident Agent. MDOC 443789 CONFIRMED convicted drug dealer (cocaine delivery/manufacture + possession). Banks for Senate PAC Treasurer. LIVES AT 1968 SEVERN, Grosse Pointe Woods MI 48236 = BANKS''S HOME ADDRESS. Both Banks Strategy & Consultants AND Right Turn Project registered at this address. Holland is Banks''s housemate AND political/charity officer. Convicted felon living with convicted felon, managing PAC and charity together. Felony record disqualifies bar admission — yet both claim professional credentials.'
WHERE id = 'holland-joseph';

--------------------------------------------------------------
-- UPDATE: Banks Strategy & Consultants
--------------------------------------------------------------

UPDATE entities SET
    notes = 'LARA Entity ID 802070120. Filed 02/25/2017. Active, Good (AR Due 02/15/2026 — OVERDUE). Domestic LLC. Agent: BRIAN R BANKS. Registered at 1968 SEVERN ROAD, Grosse Pointe Woods MI 48236 = Banks home. Same address as Right Turn Project (charity) and Holland (PAC treasurer). Campaign consulting entity: paid $15,750 by Yancey, $35,750 total across network. Banks ran strategy for the woman who became a judge. Mailing address uses "SEVERN ROAD" vs street address "SEVERN" — minor discrepancy.'
WHERE id = 'banks-strategy';

--------------------------------------------------------------
-- UPDATE: Purpose Group LLC
--------------------------------------------------------------

UPDATE entities SET
    notes = 'LARA Entity ID 803295082. Filed 11/14/2024. Active, Good. Domestic LLC. Agent: BRIAN BANKS. Registered at 10101 E. CANFIELD, DETROIT MI 48214 = Purpose Charter Academy school address. Management company registered AT the school it manages. Filed Nov 2024 — less than 1 year old. Manages PCA per school website footer: "Management by The Purpose Group | Authorized by Detroit Public Schools Community District." Banks is sole agent/member.'
WHERE id = 'purpose-group';

--------------------------------------------------------------
-- INNER LINK — TWO ENTITIES
--------------------------------------------------------------

-- THE INNER LINK LLC — LARA Entity ID 801470477
-- Filed 08/18/2008, Active, Good (AR Due 02/15/2026 — past due)
-- Agent: LARRY THOMAS JR
-- 17515 W 9 Mile Rd, Suite 100, Southfield MI 48075
-- Management Type: Member
--
-- INNER LINKS LLC — LARA Entity ID 803044192  
-- Filed 05/26/2023, Active, Good (AR Due 02/15/2027)
-- Agent: TESSA R MARKS
-- 2138 Marguerite Ave, Lansing MI 48912
-- Management Type: Member
--
-- TransparencyUSA payee name: "Inner Link Graphics"
-- The 2008 entity (Larry Thomas Jr, Southfield) is the likely match:
-- Southfield is the Detroit political ecosystem, $98K in political printing.
-- The 2023 entity (Tessa Marks, Lansing) may be successor or unrelated.

UPDATE entities SET
    notes = 'Print shop/vendor. $98,291 total from Banks orbit: Banks for Senate $39,315, Bank on Banks PAC $10,600, Bank on Wayne County $2,000, Yancey campaign $8,025, MI Deserves Better SuperPAC $37,151, CM Johnson $850. LARA: THE INNER LINK LLC (Entity ID 801470477, filed 08/18/2008, Active, AR overdue). Agent: LARRY THOMAS JR. Address: 17515 W 9 Mile Rd, Suite 100, Southfield MI 48075. Second entity: INNER LINKS LLC (Entity ID 803044192, filed 05/26/2023, Agent: Tessa R Marks, 2138 Marguerite Ave, Lansing MI 48912). Central printing vendor for entire Banks political network. Owner: LARRY THOMAS JR.'
WHERE id = 'inner-link';

--------------------------------------------------------------
-- NEW: Larry Thomas Jr — Inner Link owner
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('thomas-larry-jr', 'Larry Thomas Jr', 'person',
    'Owner/Agent of The Inner Link LLC (LARA Entity ID 801470477). 17515 W 9 Mile Rd, Suite 100, Southfield MI 48075. Print vendor that received $98,291 from Banks political network. Biggest single vendor in the network. Filed 08/18/2008.');

--------------------------------------------------------------
-- SAVE DETROIT JOBS / DETROIT LEADERS — SAME ADDRESS
--------------------------------------------------------------

-- LARA Entity ID: 802002459
-- Filed: 09/08/2016
-- Status: Active, Good
-- Type: Domestic Nonprofit Corporation
-- Agent: THE CORPORATION COMPANY (40600 Ann Arbor Rd E Ste 201, Plymouth 48170)
-- Mailing: 201 Townsend Street, Suite 900, Lansing MI 48933
-- Last Report: 2026
-- Matched Names: DETROIT LEADERS (confirmed rename)
--
-- ALL OFFICERS AT SAME ADDRESS: 13560 E. McNICHOLS, DETROIT MI 48205
-- President: KENNETH DANIELS
-- Secretary: ELISHA BROWN  
-- Treasurer: DAMIAN MITCHELL
-- Directors: Elisha Brown, Damian Mitchell, Kenneth Daniels
--
-- Previous reporting said: Knox (president), Mitchell (treasurer), Daniels.
-- LARA shows Daniels as President. Either Knox replaced or articles inaccurate.
-- The Corporation Company = professional registered agent service (Plymouth/Lansing)
-- 13560 E. McNichols — all three officers list this as their address.
-- Shell nonprofit: professional agent, shared address, dark money.

UPDATE entities SET
    notes = 'Dark money 501c4 nonprofit. LARA Entity ID 802002459. Filed 09/08/2016. Active. Assumed name: DETROIT LEADERS (confirmed). Agent: The Corporation Company (professional agent, Plymouth/Lansing). ALL THREE OFFICERS AT SAME ADDRESS: 13560 E. McNichols, Detroit MI 48205. President: Kenneth Daniels (former state rep, charged helping buy Mercedes for drug dealer). Secretary: Elisha Brown. Treasurer: Damian Mitchell (Board of Police Commissioners candidate). Last report 2026. Raised $100K+ in 2016 from BCBS, Moroun/Central Transport, Schostak PAC. Paid Carol Banks $18K+. Funded Latisha Johnson vs Elrick in District 4. Johnson won → now PCA board secretary.'
WHERE id = 'save-detroit-jobs';

--------------------------------------------------------------
-- NEW: Elisha Brown — Save Detroit Jobs secretary
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('brown-elisha', 'Elisha Brown', 'person',
    'Secretary + Director of Save Detroit Jobs / Detroit Leaders. 13560 E. McNichols, Detroit MI 48205 (same address as Kenneth Daniels and Damian Mitchell — all 3 officers). LARA filing. Dark money nonprofit.');

--------------------------------------------------------------
-- CUSTOM PROMOTIONS — FAMILY BUSINESS DISSOLVED + REFORMED
--------------------------------------------------------------

-- Custom Promotions, Inc. — LARA Entity ID 800545413
-- Filed 05/24/1989, DISSOLVED (Certificate of Dissolution)
-- Inactive 02/14/2022
-- Agent: ERIC M GORDON
-- 17520 W 12 Mile Rd #200, Southfield MI 48076
-- President: JASON GORDON
-- Secretary: ERIC GORDON  
-- Treasurer: SARA GORDON
-- Directors: Eric Gordon, Jason Gordon, Sara Gordon
-- Last Report: 2018
--
-- Custom Promotions, LLC — LARA Entity ID 802861635
-- Filed 05/25/2022, Active, Good (AR Due 02/15/2026)
-- Agent: JASON SAMUEL GORDON
-- 14326 East 9 Mile Road, Warren MI 48089
--
-- TIMELINE: Inc dissolved 02/14/2022 → LLC formed 05/25/2022 (3 months later)
-- Family business: Eric M Gordon (father), Jason Gordon (son/president), Sara Gordon
-- Investigated in UAW corruption probe (FBI/IRS/Labor)
-- Address moved: Southfield → Warren

UPDATE entities SET
    notes = 'Southfield/Warren MI promotional products company. TWO LARA ENTITIES: Custom Promotions Inc (Entity ID 800545413, filed 1989, DISSOLVED 02/14/2022, agent Eric M Gordon, 17520 W 12 Mile Rd #200 Southfield) AND Custom Promotions LLC (Entity ID 802861635, filed 05/25/2022, Active, agent Jason Samuel Gordon, 14326 E 9 Mile Rd Warren MI 48089). DISSOLVED AND REFORMED 3 MONTHS LATER. Gordon family business: Eric M Gordon (father/secretary), Jason Gordon (son/president), Sara Gordon (treasurer). Paid $10,500 by Banks for Senate. Also paid $662 by Committee to Elect Latisha Johnson. Gordon companies investigated by FBI/IRS/Labor in UAW corruption scandal ($3M+ from UAW since 2013). "Recurring focus" of investigation per Detroit News.'
WHERE id = 'custom-promotions';

--------------------------------------------------------------
-- 1968 SEVERN — THE ADDRESS
--------------------------------------------------------------
-- Three LARA entities registered at Banks's home:
-- 1. Banks Strategy & Consultants LLC (802070120) — Banks agent
-- 2. Right Turn Project Inc (800936257) — Holland agent (DISSOLVED)
-- 3. Purpose Group LLC registered at PCA school, but Banks himself lives at 1968 Severn
--
-- Holland (convicted drug dealer/PAC treasurer) is also at 1968 Severn.
-- This address is the nerve center of the entire political operation.

--------------------------------------------------------------
-- RELATIONSHIPS
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('ross-carlton', 'right-turn-project', 'treasurer', 'Treasurer of Right Turn Project (LARA)', 'LARA Entity ID 800936257',
    'Also owner of Ross Catering. PAC → charity → catering = money loop through same person.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('ross-carlton', 'ross-catering', 'owner', 'Owner of Ross Catering', 'LARA + TransparencyUSA',
    'Charity treasurer receiving PAC money AND catering vendor billing same campaigns. $35K+ in catering from Banks orbit.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('tarver-terrence', 'right-turn-project', 'secretary', 'Secretary of Right Turn Project (LARA)', 'LARA Entity ID 800936257',
    'Shares 16500 North Park Dr Southfield address with Carlton Ross.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('holland-joseph', 'banks-brian', 'housemate', 'Both at 1968 Severn, Grosse Pointe Woods MI 48236', 'LARA records',
    'Convicted drug dealer lives with convicted felon. Both manage political/charity entities from same home.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('thomas-larry-jr', 'inner-link', 'owner', 'Agent/Owner of The Inner Link LLC', 'LARA Entity ID 801470477',
    '$98K+ print vendor. Larry Thomas Jr is the person behind the biggest single vendor in Banks political network.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('brown-elisha', 'save-detroit-jobs', 'officer', 'Secretary + Director', 'LARA Entity ID 802002459',
    'Same address as Daniels and Mitchell: 13560 E. McNichols. Shell nonprofit.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('ross-carlton', 'right-turn-project', 'treasurer', 'record', 'Charity treasurer = catering owner = money loop', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('ross-carlton', 'ross-catering', 'owner', 'record', '$35K+ from Banks campaigns', 'LARA + TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('holland-joseph', 'banks-brian', 'housemate', 'record', '1968 Severn — both live there', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('thomas-larry-jr', 'inner-link', 'owner', 'record', 'Agent/Owner — $98K print vendor', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('tarver-terrence', 'right-turn-project', 'secretary', 'record', 'Same address as Ross (16500 North Park)', 'LARA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('ross-carlton', 'person', 'Carlton Ross (catering owner = charity treasurer)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('tarver-terrence', 'person', 'Terrence Tarver (Right Turn secretary)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('thomas-larry-jr', 'person', 'Larry Thomas Jr (Inner Link owner, $98K)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('brown-elisha', 'person', 'Elisha Brown (Save Detroit Jobs secretary)', 4);
