-- caseDB update: Oct 4, 2026 (VENDOR ECOSYSTEM — campaign vendor contamination tracing)
-- Custom Promotions: president Jason Gordon investigated in UAW bribery scandal (FBI/IRS)
-- Also paid by Latisha Johnson campaign = Purpose Charter board secretary
-- Ross Catering: $35K+ across Banks orbit including Bullock (State Board of Ed)
-- Yancey CREDITED Banks for her election victory (Detroit News Aug 2017)
-- Bank on Banks PAC → Brenda Jones (Council President) $1K
-- Run: sqlite3 caseDB.sqlite < update_oct4_vendor_ecosystem.sql

--------------------------------------------------------------
-- Custom Promotions — UAW investigation connection
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('custom-promotions', 'Custom Promotions', 'org',
    'Southfield, MI promotional products company (asi/173237). President: Jason Gordon. Paid $10,500 by Banks for Senate. Also paid $662 by Committee to Elect Latisha Johnson (Purpose Charter board secretary). Total $12,080 from Banks orbit. CRITICAL: Gordon''s companies investigated by FBI/IRS/Labor Dept in UAW corruption scandal. His firms received $3M+ from UAW since 2013. Gordon described as "recurring focus" of UAW investigation. UAW corruption case resulted in 18+ convictions including 2 former International Presidents. Banks used a vendor under federal investigation for a different corruption probe.');

--------------------------------------------------------------
-- Ross Catering — cross-campaign vendor
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('ross-catering', 'Ross Catering', 'org',
    'Detroit catering vendor. $35,223 total received. Banks orbit: Banks for Senate $8,431, Bank on Banks PAC $6,594, Bank on Wayne County $690. Total Banks: $15,715. Also used by: Marshall Bullock (State Board of Ed member who co-endorsed with Banks) $1,800, John C. Cahalan (Wayne County Circuit Court candidate) $3,578, Rico Razo (State Rep candidate) $3,619, Michigan Democratic Future $1,860, Shri Thanedar (ran for Gov) $1,100. Cross-campaign catering connecting Banks to Bullock and judiciary candidates.');

--------------------------------------------------------------
-- Mass Mailing LLC
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('mass-mailing', 'Mass Mailing LLC', 'org',
    'Michigan mass mailing vendor. $24,240 from Banks for Senate. $5,086 from Yancey campaign. Widely used by Democratic campaigns statewide including Democratic State Central Committee ($83K in 2024 alone). Not Banks-exclusive but part of the shared vendor infrastructure.');

--------------------------------------------------------------
-- Brenda Jones — Council President, PAC recipient
--------------------------------------------------------------

INSERT OR IGNORE INTO entities (id, name, type, notes)
VALUES ('jones-brenda', 'Brenda Jones', 'person',
    'Former Detroit City Council President. Received $1,000 from Bank on Banks PAC. Also received $13K from Operating Engineers (same PAC funding Banks $10K). Part of the Banks political patronage network — PAC funds flowing to sitting council president.');

--------------------------------------------------------------
-- Yancey CREDITED Banks for her victory
--------------------------------------------------------------

-- Detroit News, Aug 10, 2017: "Yancey credits Banks, others in House primary victory"
-- She didn't just receive his money — she PUBLICLY credited him
-- He was paid $15,750 to run her campaign. She became a judge.
-- She now chairs MacDowell's board.
-- The cycle: Banks paid → Yancey elected → Yancey becomes judge → Yancey chairs his school

--------------------------------------------------------------
-- RELATIONSHIPS
--------------------------------------------------------------

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('custom-promotions', 'banks-brian', 'campaign-vendor', '$10,500 from Banks for Senate', 'TransparencyUSA',
    'President Jason Gordon investigated in UAW bribery scandal by FBI/IRS/Labor.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('custom-promotions', 'johnson-latisha', 'campaign-vendor', '$662 from Committee to Elect Latisha Johnson', 'TransparencyUSA',
    'Same vendor used by Banks AND Purpose Charter board secretary.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('ross-catering', 'bullock-marshall', 'campaign-vendor', '$1,800 from Friends to Elect Marshall Bullock', 'TransparencyUSA',
    'State Board of Ed member who co-endorsed with Banks also used Banks''s caterer.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('jones-brenda', 'banks-brian', 'pac-recipient', '$1,000 from Bank on Banks PAC', 'TransparencyUSA + Detroit News Aug 2017',
    'Council President received Banks PAC money. PAC also funded by Carpenters $10K and Operating Engineers $2.5K.');

INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, notes)
VALUES ('yancey-tenisha', 'banks-brian', 'credited', 'Yancey publicly credited Banks for her House primary victory', 'Detroit News Aug 10, 2017',
    '"Yancey credits Banks, others in House primary victory." Paid him $15,750 → won → became judge → chairs his school board. Full cycle.');

--------------------------------------------------------------
-- GRAPH EDGES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('custom-promotions', 'banks-brian', 'vendor', 'record', '$10.5K + president investigated UAW bribery', 'TransparencyUSA + ASI');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('ross-catering', 'bullock-marshall', 'vendor', 'record', '$1,800 shared caterer', 'TransparencyUSA');

INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc)
VALUES ('jones-brenda', 'banks-brian', 'pac-recipient', 'record', '$1K from Bank on Banks PAC', 'TransparencyUSA');

--------------------------------------------------------------
-- GRAPH NODES
--------------------------------------------------------------

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('custom-promotions', 'entity', 'Custom Promotions (UAW probe, $10.5K)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('ross-catering', 'entity', 'Ross Catering ($35K cross-campaign)', 4);

INSERT OR IGNORE INTO graph_nodes (id, node_type, label, tier)
VALUES ('jones-brenda', 'person', 'Brenda Jones (Council Pres, PAC $1K)', 4);
