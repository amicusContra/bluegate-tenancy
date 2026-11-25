-- caseDB update: Oct 4, 2026 (LARA Betweens Pull — Agent Portfolios)
-- Source: LARA API SearchByOption=3 (search by registered agent name)
--
-- CRITICAL FINDINGS:
-- 1. W. SPENCER LEACH: Professional political machine operator. 13 entities.
--    Batch-filed slate + party orgs on same days. Eastside Slate, Michigan
--    Black Democrats, Detroit Democratic/Democrat Club, Democratic Progressive
--    Alliance, Accountability Slate, Detroiters for Good Government.
-- 2. KENNETH DANIELS: 15 entities. Real estate/construction empire.
--    Save Detroit Jobs president is a major developer (Daniels Realty Group,
--    KANDICO Construction, DANCOM Properties, multiple investment LLCs).
-- 3. GWENDOLYN LEWIS: 15 entities. Ran Women's Democratic Club of Detroit.
--    Real estate developer. Agent on Ross Catering Events of Excellence.
-- 4. LOUIS ROSS + LOUIS ROSS III: Multi-generational. Louis owns Ross Catering Co,
--    Genesis Communications. Louis III owns DDT Construction, J&L Florals.
-- 5. DEVIN HUTCHINGS: PCA Treasurer based in Ypsilanti (not Detroit).
--    Email: devinjhutchings@gmail.com
--
-- Run: sqlite3 caseDB.sqlite < update_oct4_lara_betweens.sql

--------------------------------------------------------------
-- W. SPENCER LEACH — POLITICAL MACHINE INFRASTRUCTURE
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('leach-spencer', 'W. Spencer Leach', 'person',
    'Professional political machine operator. Agent on 13+ LARA entities. Batch-filed political organizations on same days: (04/28/2008): Eastside Slate, Eastside Community Slate (800916318), Michigan Black Democrats (800916316) — consecutive entity IDs! (05/15/2015): Detroit Democratic Club (800938179), Detroit Democrat Club (800938180), Democratic Progressive Alliance (800938181), Sankofa Renaissance Homes (800938456) — also consecutive/near IDs! Also: Accountability Slate (800930859, 2011), Detroiters for Good Government LLC (801598387, 2011, ACTIVE), The Songhai Group LLC (801659651, 2012, Active), The Azania Group Inc (800751893, 2012), The Sudanese Group Inc (800754057, 2012), SBC Historical Committee (800916611, 2008). Pan-African naming (Songhai, Azania, Sankofa). Address: 19943 Lahser, Detroit 48219. Connected to Carol Banks Eastside Slate endorsement-for-hire operation.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('detroiters-good-govt', 'Detroiters for Good Government LLC', 'org',
    'LARA Entity ID 801598387. Filed 08/30/2011. ACTIVE. Agent: W Spencer Leach. Political influence LLC — still operational. Only Active Spencer Leach political entity alongside Songhai Group.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('eastside-community-slate', 'Eastside Community Slate', 'org',
    'LARA Entity ID 800916318. Filed 04/28/2008 (SAME DAY as Eastside Slate and Michigan Black Democrats). Dissolved. Agent: W Spencer Leach. Variant of Eastside Slate — batch-filed alongside it.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('mi-black-democrats', 'Michigan Black Democrats', 'org',
    'LARA Entity ID 800916316. Filed 04/28/2008 (SAME DAY as both Eastside Slates). Dissolved. Agent: W Spencer Leach. Part of batch-filed political organization infrastructure.');

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('accountability-slate', 'Accountability Slate', 'org',
    'LARA Entity ID 800930859. Filed 09/09/2011. Dissolved. Agent: W Spencer Leach. Another endorsement slate entity.');

--------------------------------------------------------------
-- KENNETH DANIELS — DEVELOPMENT EMPIRE
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Save Detroit Jobs President + Director. 13560 E. McNichols, Detroit 48205 (SDJ address). 15+ LARA entities: DANCOM Properties LLC (2025), Bowie Landscaping LLC (2001), K.W.D Style LLC (2012, as Kenneth Daniels III), Daniels Realty Group LLC (2006), KANDICO Services LLC (2018), J Whitt Enterprises LLC (2019), IJI Investments LLC (2017), KANDICO Construction LLC (2001), IOS Investments LLC (2018), K & K Transloading and Logistics Services LLC (2020), Da Taco Spot LLC (2022), Fireborn Training LLC (2019), We Care Services LLC (2017, as III), KAIDEN Enterprises LLC (2025), Summit Global LLC (2026). Major real estate developer + construction operator. SDJ is just ONE of his 15+ entities. "KANDICO" = "K AND I CO" = Kenneth and another person.'
WHERE id = 'daniels-kenneth';

-- If entity doesn't exist yet, create it
INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('daniels-kenneth', 'Kenneth Daniels / Kenneth Daniels III', 'person',
    'Save Detroit Jobs President + Director. 13560 E. McNichols, Detroit 48205 (SDJ address). 15+ LARA entities including Daniels Realty Group, KANDICO Construction/Services, DANCOM Properties, IJI/IOS Investments, K&K Transloading, Da Taco Spot, Fireborn Training, We Care Services, Summit Global. Major real estate developer operating Save Detroit Jobs as ONE entity in a 15+ entity empire.');

--------------------------------------------------------------
-- GWENDOLYN LEWIS — ROSS CATERING AGENT + POLITICAL OPERATIVE
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('lewis-gwendolyn', 'Gwendolyn Lewis (Lewis-Parker)', 'person',
    'Agent on Ross Catering Events of Excellence LLC. 15+ LARA entities including: Women''s Democratic Club of Detroit (802238097, 2018, Dissolved), Save Our Teens (800809143, 1994, as Lewis-Parker), Premier Real Estate Management & Acquisitions LLC (802303376, 2019), Plant A Seed Read Inc (802111475, 2017), Leland Estates Development Company LLC (801463128, 2008), KindnessWorks LLC (803342131, 2025), Let''s Hear It Again With Gwen LLC (2013+), Muffins Muffins and More Muffins LLC (900100713, 2025), AdolfoVoyat LLC (801702544, 2013), Siracusa LLC (dissolved), LVO LLC (dissolved), VDA Inc (dissolved), Paradise Unlimited Inc (dissolved). Politically active real estate developer who ran Women''s Democratic Club of Detroit. 23749 Riverview Dr, Southfield MI 48034.');

--------------------------------------------------------------
-- ELISHA BROWN — SAVE DETROIT JOBS SECRETARY
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('brown-elisha', 'Elisha Brown', 'person',
    'Save Detroit Jobs Secretary + Director. 13560 E. McNichols, Detroit 48205 (same as Daniels). LARA entities: Brown Logging LLC (802117162, filed 09/21/2017, Active), Reach One Teach One Coalition (900176989, filed 03/12/2026, Active — very recent org).');

--------------------------------------------------------------
-- DEVIN HUTCHINGS — PCA TREASURER
--------------------------------------------------------------

UPDATE entities SET
    notes = 'PCA Board Treasurer. Based in YPSILANTI (not Detroit): 2080 Whittaker Rd #206, Ypsilanti MI 48197. Email: devinjhutchings@gmail.com. LARA entities: DB Athletics LLC (802715414, 08/06/2021) and DB Strategies LLC (802710175, 07/28/2021) — both filed within 9 days at same Ypsilanti address. DB Athletics email is dbstrategiesllc@gmail.com (cross-linked).'
WHERE id = 'hutchings-devin';

--------------------------------------------------------------
-- LATISHA JOHNSON — MECCA DEVELOPMENT BOARD
--------------------------------------------------------------

-- Mecca Development Corporation board reveals her political network:
-- Wyanna Davis, Vaughn Arrington, Kathy Roddie, Kimberly Benton,
-- Ernestine Bibb, Vikki Seagraves, Erin Butler, Baraka Johnson
-- All in 48224 zip code (east Detroit, near Mack/Outer Drive)
-- Baraka Johnson = likely relative
-- Email: president@meccadc.org
-- Johnson personal address: XXXX Yorkshire Rd, Detroit MI 48224

--------------------------------------------------------------
-- LOUIS ROSS — MULTI-GENERATIONAL
--------------------------------------------------------------

UPDATE entities SET
    notes = 'Owner of Ross Catering Company Inc (800646584, dissolved 07/15/2024). 9628 Harper, Detroit MI 48213. Sole officer. Also: Genesis Communications LLC (802131129, 2017, Active). LOUIS ROSS III also exists with: DDT Construction & Networking Inc (802452244, 2020, Dissolved), J & L Florals LLC (802606126, 2021, Active). Multi-generational family. Relationship to Carlton Ross (Right Turn Project Treasurer) still TBD.'
WHERE id = 'ross-louis';

--------------------------------------------------------------
-- BRIAN MEISTE — ANCHOR ROCK PARTNER
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('meiste-brian', 'Brian Meiste', 'person',
    'Anchor Rock Services Secretary. XXXXX Crossing Ct Suite 110, Holland MI 49424. Substantial builder/developer: Brian Meiste Builders Inc (800594577, 2002), Meiste Holdings LLC (801416228, 2007), Meiste Homes North LLC (802394395, 2019), Meiste and Partners LLC (801230889, 2003), The Principles Development Group LLC (801238742, 2003), Traditions Development Group LLC (801356087, 2006), BSKS LLC (dissolved), Bella Woods HOA (dissolved). West Michigan developer partnered with Banks at Anchor Rock.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('leach-spencer', 'eastside-slate', 'controls', 'confirmed', 'Agent on 2008 Eastside Slate + Eastside Community Slate + Michigan Black Democrats (all filed same day, consecutive IDs)', 'LARA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('leach-spencer', 'detroiters-good-govt', 'controls', 'confirmed', 'Agent, filed 2011, only active political LLC', 'LARA 801598387');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('daniels-kenneth', 'save-detroit-jobs', 'officer', 'confirmed', 'President + Director. Also runs 15-entity real estate/construction empire.', 'LARA 802002459');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('lewis-gwendolyn', 'ross-catering-eoe', 'controls', 'confirmed', 'Agent on Ross Catering Events of Excellence LLC. Also ran Women''s Democratic Club of Detroit.', 'LARA 801351679');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('meiste-brian', 'anchor-rock', 'officer', 'confirmed', 'Secretary + west Michigan developer. Business partner of Banks in commercial operations.', 'LARA 800770907');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('leach-spencer', 'person', 'W. Spencer Leach (political machine operator, 13 entities)', 3);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('detroiters-good-govt', 'entity', 'Detroiters for Good Government LLC (Leach, Active)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('lewis-gwendolyn', 'person', 'Gwendolyn Lewis (Ross Catering agent, Women''s Dem Club)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('brown-elisha', 'person', 'Elisha Brown (SDJ Secretary, Reach One Teach One)', 5);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('meiste-brian', 'person', 'Brian Meiste (Anchor Rock partner, builder)', 5);
