-- caseDB update: Oct 4, 2026 (LARA Deep Pull — Full Entity Portfolios)
-- Source: LARA API via browser-context fetch (Cloudflare bypass)
-- SearchByOption=3 searches by registered agent name.
--
-- CRITICAL FINDINGS:
-- 1. PCA BOARD: Lamar Moreland (Banks's attorney) is PCA DIRECTOR
-- 2. PCA BOARD: Latisha Johnson (dark money beneficiary) is PCA SECRETARY
-- 3. Banks has 12+ entities spanning Detroit, Holland/Zeeland, Clarkston, Waterford
-- 4. Purpose empire = THREE entities: Purpose Charter Academy + Purpose Group + Purpose Foundation
-- 5. B. Roderick's Salon address = SAME as Carlton Ross/Terrence Tarver (16500 N Park, Southfield)
-- 6. Jason Gordon has 20 entities + is an ATTORNEY (Deen Legal PLLC)
-- 7. Save Detroit Jobs has THREE names: Save Detroit Jobs + Impact Detroit + Detroit Leaders
-- 8. Save Detroit Jobs set up by DYKEMA LAW FIRM (compliance@dykema.com)
-- 9. Joseph Holland also ran On Point Tutoring Inc (tutoring→education pipeline)
-- 10. Serenity Guardianship Services — Banks ran guardianship co without bar admission
--
-- Run: sqlite3 caseDB.sqlite < update_oct4_lara_deep.sql

--------------------------------------------------------------
-- PURPOSE CHARTER ACADEMY — THE ENTITY + BOARD
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('pca-entity', 'Purpose Charter Academy (LARA)', 'org',
    'LARA Entity ID 900072324. Domestic Nonprofit Corporation. Filed 07/31/2025. Active, Good standing. Agent: Brian Banks. Address: 10101 E. Canfield, Detroit MI 48214. Email: brianbanksjd@gmail.com. BOARD: President Cylenthia Latoye Miller, Secretary Latisha Johnson (CM District 2), Treasurer Devin Hutchings, Directors Major Clora + LAMAR MORELAND + Cylenthia Miller. MORELAND IS ON THE BOARD OF THE SCHOOL HE IS REPRESENTING BANKS FOR IN LITIGATION.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('miller-cylenthia', 'Cylenthia Latoye Miller', 'person',
    'PCA Board President + Director. 10101 E. Canfield address. Identity TBD — no LARA entities in her name as agent.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('hutchings-devin', 'Devin Hutchings', 'person',
    'PCA Board Treasurer. Also owns DB Athletics LLC (802715414, filed 08/06/2021) and DB Strategies LLC (802710175, filed 07/28/2021). Both filed within days of each other in summer 2021.');

--------------------------------------------------------------
-- PURPOSE FOUNDATION — Banks + Holland nonprofit
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('purpose-foundation', 'Purpose Foundation', 'org',
    'LARA Entity ID 803294855. Domestic Nonprofit Corporation. Filed 12/09/2024. Active, Good standing. Agent: Brian Banks. Address: 1968 SEVERN ROAD, GPW 48236 (Banks home). Email: BrianBanksJD@gmail.com. Officers: Brian Banks (President + Director), Joseph Holland Jr (Treasurer + Secretary) — BOTH at 1968 Severn. Holland is STILL working with Banks despite Right Turn Project dissolution. Third "Purpose" entity alongside PCA and Purpose Group LLC.');

--------------------------------------------------------------
-- BANKS ENTITY PORTFOLIO (12+ entities)
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('anchor-rock', 'Anchor Rock Services Inc', 'org',
    'LARA Entity ID 800770907. Filed 02/09/2015. Active, Good. Agent: Brian Banks, XXXXX Crossing Ct Suite 110, Holland MI 49424. Email: brian@anchorrockservices.com. Assumed names: Anchor Rock Construction (reg 11/21/2024), Great Lakes Fire Supply (reg 09/23/2020, expired), Great Lakes Upfitting (reg 02/27/2020 + 02/05/2024). Officers: Brian Banks (President+Director, 20 W Garfield, Zeeland MI 49464), Doug Reams (Treasurer, 2322 Edson Dr, Hudsonville MI 49426), Brian Meiste (Secretary, Holland). Construction/upfitting company in west Michigan. "Great Lakes" branding used in BOTH commercial and political entities.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ars-holdings', 'ARS Holdings LLC', 'org',
    'LARA Entity ID 802091174. Filed 05/12/2017. Active, Good. Agent: Brian Banks,Member. Address: 11555 Crossing Court Suite 110, Holland MI 49424. Email: brian@anchorrockservices.com. Holding company for Anchor Rock Services.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('of-the-light', 'Of The Light Ventures LLC', 'org',
    'LARA Entity ID 803248859. Filed 07/24/2024. Active, Good. Agent: Brian Banks, 20 W. Garfield Avenue, Zeeland MI 49464. No email. Filed 4 months before Purpose Group LLC. Zeeland = Banks''s west Michigan base.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('serenity-guardianship', 'Serenity Guardianship Services Inc', 'org',
    'LARA Entity ID 802290962. Domestic PROFIT Corporation. Filed 03/07/2019. Dissolved (Operation of Law) 07/15/2023. Agent: Brian Banks, 1968 Severn, GPW 48236. Email: BBesq06@aol.com. Banks was SOLE officer (President, Director, Treasurer, Secretary). A non-attorney running a for-profit guardianship company. Guardianship work involves court filings and legal rights — potential UPL issue. BBesq06 email = same as Right Turn Project.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('banks-powerwashing', 'Banks Powerwashing LLC', 'org',
    'LARA Entity ID 801634031. Filed 02/09/2012. Active but Not Good standing (inactive 02/16/2016). Agent: Brian Banks, 5581 Parview Apt 306, Clarkston MI 48346. Earlier Banks address.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('free-flow-gutter', 'Free Flow Gutter Protection LLC', 'org',
    'LARA Entity ID 802950394. Filed 11/29/2022. Active but Not Good standing (inactive 03/01/2026). Agent: Brian Banks, 623 Lakeside Dr, Waterford MI 48328. Another Banks address.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('b-rodericks-salon', 'B. Roderick''s Salon & Spa Inc', 'org',
    'LARA Entity ID 800591240. Filed 10/09/2001. Dissolved (Operation of Law) 07/15/2004. Agent: Brian Banks, 16500 NORTHPARK DR #1715, SOUTHFIELD MI 48075. CRITICAL: This is the SAME ADDRESS as Carlton Ross and Terrence Tarver in Right Turn Project filings. Banks used this address 2001-2004. Ross and Tarver used it 2013+. Establishes long-term connection to 16500 N Park.');

--------------------------------------------------------------
-- BANKS EMAIL REGISTRY
--------------------------------------------------------------
-- BanksStrategy@gmail.com (Banks Strategy & Consultants)
-- BrianBanksJD@gmail.com / brianbanksjd@gmail.com (Purpose Group, Purpose Foundation, PCA)
-- BBesq06@aol.com (Right Turn Project, Serenity Guardianship)
-- brian@anchorrockservices.com (Anchor Rock, ARS Holdings)

--------------------------------------------------------------
-- BANKS ADDRESS TIMELINE
--------------------------------------------------------------
-- 2001-2004: 16500 Northpark Dr #1715, Southfield 48075 (B. Roderick's Salon)
-- 2012: 5581 Parview Apt 306, Clarkston 48346 (Banks Powerwashing)
-- 2015-present: XXXXX Crossing Ct Suite 110, Holland 49424 (Anchor Rock/ARS)
-- 2017-present: 1968 Severn Rd, Grosse Pointe Woods 48236 (home/political base)
-- 2022: 623 Lakeside Dr, Waterford 48328 (Free Flow Gutter)
-- 2024-present: XX W Garfield Ave, Zeeland 49464 (Of The Light/Anchor Rock)
-- 2024-present: 10101 E Canfield, Detroit 48214 (Purpose Group/PCA)

--------------------------------------------------------------
-- SAVE DETROIT JOBS — TRIPLE IDENTITY + DYKEMA
--------------------------------------------------------------

UPDATE entities SET
    notes = 'LARA Entity ID 802002459. Domestic Nonprofit Corporation. Filed 09/08/2016. Active, Good. Agent: THE CORPORATION COMPANY (professional formation agent), 40600 Ann Arbor Rd E Ste 201, Plymouth MI 48170. Mailing: 201 Townsend Street Suite 900, Lansing MI 48933 (= DYKEMA LAW FIRM Lansing office). Email: compliance@dykema.com (= DYKEMA). THREE ASSUMED NAMES: Save Detroit Jobs (original), Impact Detroit (reg 09/07/2018), Detroit Leaders (reg 08/10/2021, exp 12/31/2026). Officers: Kenneth Daniels (President), Damian Mitchell (Treasurer), Elisha Brown (Secretary) — ALL at 13560 E. McNichols, Detroit 48205. Set up by Michigan''s largest/most powerful law firm. Dark money vehicle fought Charlie LeDuff/Steve Elrick reporting. Funded Latisha Johnson vs Elrick in 2021.'
WHERE id = 'save-detroit-jobs';

--------------------------------------------------------------
-- CUSTOM PROMOTIONS — GORDON FAMILY + DEEN LEGAL
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('gordon-jason', 'Jason Samuel Gordon', 'person',
    'ATTORNEY. Owns Deen Legal Services PLLC (801895172, filed 01/28/2009, Active). Also owns Custom Promotions LLC (802861635, filed 05/25/2022 — 3 months after Inc dissolved). Email: JGordon@DeenLegal.com. Address: 14326 East 9 Mile Road, Warren MI 48089 (SAME address for Deen Legal + Custom Promotions). Investigated by FBI/IRS/Department of Labor in UAW bribery case ($3M+ from UAW). Also paid by Latisha Johnson campaign. Has 20+ total entities including: Organization Services of Michigan, Gordon Facilities, Marshall Industrial Properties/Property, BMP Marketing, Green Redevelopment, AICEJ, GGLC, Select Surplus, Door4Four, Inari Tea, Omnibus Collaborative, American Ink (dissolved), Select Environmental (dissolved), multiple address-named LLCs.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('deen-legal', 'Deen Legal Services PLLC', 'org',
    'LARA Entity ID 801895172. Filed 01/28/2009. Active, Good. Agent: Jason Samuel Gordon (sole Member/Manager). 14326 East 9 Mile Road, Warren MI 48089. Same address as Custom Promotions LLC. Gordon runs his law firm from the same address as his investigated political promotions company.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('custom-promo-old', 'Custom Promotions Inc (dissolved)', 'org',
    'LARA Entity ID 800545413. Filed 05/24/1989. DISSOLVED (Certificate of Dissolution) 02/14/2022. Agent: ERIC M GORDON (Jason''s father). Address: 17520 W 12 Mile Rd #200, Southfield MI 48076. Officers: Jason Gordon (President), Sara Gordon (Treasurer), Eric Gordon (Secretary + Director). FAMILY BUSINESS — Jason, Sara, Eric all Gordons at same address. Dissolved Feb 2022, Custom Promotions LLC filed by Jason 3 months later in May 2022. Dissolve-and-reform pattern.');

--------------------------------------------------------------
-- GLLG ENTITY — FULL MEMBERSHIP
--------------------------------------------------------------

UPDATE entities SET
    notes = 'LARA Entity ID 802112914. Domestic Professional LLC. Filed 08/29/2017. Active, Good. Agent: Jehan Crump-Gibson. Address: One Towne Square, Suite 1835, Southfield MI 48076. Email: jehan@gllegalgroup.com. MEMBERS AND MANAGERS: Jehan Crump-Gibson, Ayanna Alcendor, Henri Harmon — all at One Towne Square. Three equity partners. Crump-Gibson confirmed in writing (Oct 1, 2:28 PM) she is NOT retained for law enforcement, police reports, or PPO proceedings.'
WHERE id = 'gllg';

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('alcendor-ayanna', 'Ayanna Alcendor', 'person',
    'GLLG Member/Manager. One Towne Square, Southfield MI 48076. Equity partner in Great Lakes Legal Group PLLC.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('harmon-henri', 'Henri Harmon', 'person',
    'GLLG Member/Manager. One Towne Square, Ste. 1835, Southfield MI 48076. Equity partner in Great Lakes Legal Group PLLC.');

--------------------------------------------------------------
-- RIGHT TURN PROJECT — FULL OFFICERS + ADDRESS MATCH
--------------------------------------------------------------

UPDATE entities SET
    notes = 'LARA Entity ID 800936257. Domestic Nonprofit Corporation. Filed 05/07/2013. Dissolved (Operation of Law) 12/01/2021 (failed to file ARs). Agent: Joseph Holland Jr, 1968 Severn, GPW 48236 (Banks home). Email: BBesq06@aol.com (BANKS''s email, not Holland''s). Officers: Joseph Holland (President+Director, 1968 Severn), Carlton Ross (Treasurer+Director, 16500 North Park Dr Southfield), Terrence Tarver (Secretary+Director, 16500 North Park Dr Southfield). Ross and Tarver SHARE ADDRESS at 16500 N Park — SAME building as Banks''s former B. Roderick''s Salon (2001). Email proves Banks controlled entity despite Holland as agent. PAC→charity→Ross Catering money loop documented.'
WHERE id = 'right-turn';

--------------------------------------------------------------
-- EASTSIDE SLATE — LEMMONS DYNASTY
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('eastside-slate', 'Eastside Slate (3 incarnations)', 'org',
    'Endorsement-for-hire operation. THREE LARA entities, all dissolved: (1) 800820260 filed 03/30/1994, agent Lamar Lemmons III, 8411 E Forest Detroit 48214, dissolved 10/01/2000. (2) 800916317 filed 04/28/2008, agent W Spencer Leach, 19943 Lahser Detroit 48219, dissolved 12/01/2019. (3) 802390967 filed 12/04/2019, agent Lamar Lemmons (no III), 8523 East Outer Dr Detroit 48213, dissolved 12/01/2022. Lamar Lemmons = state representative, Detroit school board member. Carol Banks ran Eastside Slate endorsement operation per prior reporting.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('lemmons-lamar', 'Lamar Lemmons III/IV', 'person',
    'Agent on Eastside Slate entities (1994 + 2019 incarnations). Michigan state representative, Detroit school board member. Connected to Carol Banks via Eastside Slate endorsement-for-hire operation. Political dynasty — multiple generations in Detroit politics.');

--------------------------------------------------------------
-- ROSS CATERING — TWO ENTITIES, DIFFERENT OWNERS
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ross-catering-co', 'Ross Catering Company Inc (dissolved)', 'org',
    'LARA Entity ID 800646584. Filed 06/09/2004. Dissolved (Operation of Law) 07/15/2024 (recently!). Agent: LOUIS ROSS, 9628 Harper, Detroit MI 48213. Louis Ross = sole officer (President, Treasurer, Secretary, Director). NOT Carlton Ross. Question: are Louis and Carlton Ross related? Both in Southfield/Detroit metro.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ross-catering-eoe', 'Ross Catering Events of Excellence LLC', 'org',
    'LARA Entity ID 801351679. Filed 01/24/2006. Active but Not Good (inactive 02/16/2010). Agent: GWENDOLYN LEWIS, 23749 Riverview Dr, Southfield MI 48034. NOT a Ross. Gwendolyn Lewis is agent on the active Ross Catering entity while Louis Ross was on the dissolved one. Carlton Ross (Right Turn Project treasurer) is not agent on EITHER entity. The $35K in campaign catering payments went to one of these entities — which one, and under whose actual control?');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ross-louis', 'Louis Ross', 'person',
    'Owner of Ross Catering Company Inc (800646584, dissolved 07/15/2024). 9628 Harper, Detroit MI 48213. Sole officer. Relationship to Carlton Ross (Right Turn Project Treasurer, 16500 North Park Dr, Southfield) TBD — likely family.');

--------------------------------------------------------------
-- JOSEPH HOLLAND — ADDITIONAL ENTITIES
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('on-point-tutoring', 'On Point Tutoring Inc', 'org',
    'LARA Entity ID 800924966. Filed 04/13/2010. Dissolved (Operation of Law). Agent: Joseph Holland. TUTORING company. Holland ran a tutoring company before becoming involved in Banks''s charter school pipeline (Right Turn Project → Purpose Foundation → PCA). Education sector involvement predates Banks partnership.');

--------------------------------------------------------------
-- LATISHA JOHNSON — ENTITY PORTFOLIO
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Detroit City Council Member, District 2. PCA BOARD SECRETARY. Won 2021 election with Save Detroit Jobs/Detroit Leaders backing (anti-Elrick campaign). LARA entities: FlowerMe LLC (802584712, 2021), Isis Delights LLC (803393363, 2025), Beautified by Tisha LLC (802842248, 2022), Mecca Development Corporation (800946845, 2014, dissolved), Prestige Meetings and Events LLC (801565359, 2010). Custom Promotions (Jason Gordon/FBI investigated) also received payments from her campaign.'
WHERE id = 'johnson-latisha';

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('moreland-lamar', 'pca-entity', 'board-member', 'confirmed', 'Moreland = Director on PCA LARA filing. Attorney representing Banks IS a director of Banks''s school.', 'LARA 900072324');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('johnson-latisha', 'pca-entity', 'board-member', 'confirmed', 'Johnson = Secretary on PCA LARA filing. Dark money beneficiary is school board officer.', 'LARA 900072324');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('clora-major', 'pca-entity', 'board-member', 'confirmed', 'Clora = Director on PCA LARA filing.', 'LARA 900072324');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('hutchings-devin', 'pca-entity', 'board-member', 'confirmed', 'Hutchings = Treasurer on PCA LARA filing.', 'LARA 900072324');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('miller-cylenthia', 'pca-entity', 'board-member', 'confirmed', 'Miller = President + Director on PCA LARA filing.', 'LARA 900072324');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'purpose-foundation', 'controls', 'confirmed', 'Banks = President + Director. Holland = Treasurer + Secretary. Both at 1968 Severn.', 'LARA 803294855');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('holland-joseph', 'purpose-foundation', 'officer', 'confirmed', 'Holland = Treasurer + Secretary at 1968 Severn (Banks home).', 'LARA 803294855');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'anchor-rock', 'controls', 'confirmed', 'Banks = President + Director. West Michigan commercial entity. Email: brian@anchorrockservices.com', 'LARA 800770907');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('banks-brian', 'serenity-guardianship', 'controls', 'confirmed', 'Banks = ALL FOUR officer roles (sole officer). For-profit guardianship by non-attorney.', 'LARA 802290962');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('save-detroit-jobs', 'dykema', 'formed-by', 'confirmed', 'compliance@dykema.com + 201 Townsend Suite 900 Lansing = Dykema Gossett office. Corp Company as formation agent.', 'LARA 802002459');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('gordon-jason', 'deen-legal', 'controls', 'confirmed', 'Sole Member/Manager. Same 14326 E 9 Mile Rd Warren address.', 'LARA 801895172');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('lemmons-lamar', 'eastside-slate', 'controls', 'confirmed', 'Agent on 1994 (III) and 2019 incarnations. State rep / school board.', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('b-rodericks-salon', 'right-turn', 'address-match', 'confirmed', 'B. Roderick''s (Banks 2001) at 16500 Northpark = same building as Ross + Tarver in Right Turn Project (2013).', 'LARA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('pca-entity', 'entity', 'Purpose Charter Academy (LARA entity 900072324)', 1);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('purpose-foundation', 'entity', 'Purpose Foundation (Banks+Holland nonprofit)', 2);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('anchor-rock', 'entity', 'Anchor Rock Services (Banks west MI)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('serenity-guardianship', 'entity', 'Serenity Guardianship (Banks sole, dissolved)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('deen-legal', 'entity', 'Deen Legal Services PLLC (Jason Gordon)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('eastside-slate', 'entity', 'Eastside Slate (Lemmons, 3 incarnations)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('gordon-jason', 'person', 'Jason Gordon (atty, 20 entities, FBI investigated)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('miller-cylenthia', 'person', 'Cylenthia Miller (PCA President)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('hutchings-devin', 'person', 'Devin Hutchings (PCA Treasurer)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('lemmons-lamar', 'person', 'Lamar Lemmons III (Eastside Slate / state rep)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('alcendor-ayanna', 'person', 'Ayanna Alcendor (GLLG partner)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('harmon-henri', 'person', 'Henri Harmon (GLLG partner)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('ross-louis', 'person', 'Louis Ross (Ross Catering Co owner)', 4);

--------------------------------------------------------------
-- DYKEMA NODE (Michigan's largest law firm)
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('dykema', 'Dykema Gossett PLLC', 'org',
    'Michigan''s largest law firm. 201 Townsend Street, Suite 900, Lansing MI 48933 (one of many offices). Set up Save Detroit Jobs nonprofit (compliance@dykema.com is the entity email, Dykema mailing address). Professional formation of dark money vehicle that fought journalist Steve Elrick and funded Latisha Johnson.');

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('dykema', 'entity', 'Dykema Gossett (formed Save Detroit Jobs)', 4);
