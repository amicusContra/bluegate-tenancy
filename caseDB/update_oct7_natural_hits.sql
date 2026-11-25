-- ═══════════════════════════════════════════════════════════════
-- NATURAL HIT SCAN — Oct 7 2026
-- Training subsystem: search known actors in new contexts,
-- record organic co-occurrences as new edges.
-- Pattern: actor(A) appears in context(B) → new edge(A→B)
-- ═══════════════════════════════════════════════════════════════

-- ═══ HIT 1: Todd Perkins ran for Detroit Mayor 2025 ═══
-- Banks' personal attorney + gun case defense attorney for Judge Miller
-- ran for mayor of the same city where his client operates charter schools.
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('todd_perkins_mayoral', 'Todd Perkins (Mayoral Candidate)', 'political', 2, 'detroit',
  'Ran for Detroit Mayor Aug 2025. Raised $219K. Owns Perkins Law Group. Also city attorney for Highland Park.');

-- RECIPROCAL DONATIONS: Perkins ↔ Gay-Dagnogo
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('gay_dagnogo', 'todd_perkins', 'donation', 'money',
  'Donated $750 to Perkins mayoral campaign', 'Crain''s Detroit Business Jul 2025', 750);

INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('todd_perkins', 'gay_dagnogo', 'donation', 'money',
  'Donated $500 to Gay-Dagnogo Strong Women Lead PAC', 'TransparencyUSA', 500);

-- Perkins judicial donation network
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('todd_perkins', 'bill_mcconico', 'donation', 'money',
  '$1,500 to 36th District Judge campaign', 'TransparencyUSA', 1500);
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('todd_perkins', 'vonda_evans', 'donation', 'money',
  '$1,000 to Court of Appeals Judge campaign', 'TransparencyUSA', 1000);
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('todd_perkins', 'elizabeth_clement', 'donation', 'money',
  '$500 to Supreme Court retention campaign', 'TransparencyUSA', 500);
-- Also: Bridget Mary Hathaway ($1,250), Debra Nance ($1,250),
-- Dan Christ ($1,000), David Perkins ($1,000), Aliyah Sabree ($750),
-- Macomb Crimefighters PAC ($1,250)

-- ═══ HIT 2: Gasper Fiore → Perkins donor ═══
-- "Baron of Bribery" — convicted of bribing politicians for towing contracts
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('fiore', 'Gasper Fiore', 'actor', 3, 'detroit',
  'Towing titan. 21mo federal prison for bribing Clinton Twp trustee ($7K). Also bribed Kilpatrick, DPD Deputy Chief Washington ($3K), Conyers. Grosse Pointe Shores.');

INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('fiore', 'todd_perkins', 'donation', 'money',
  '$500 to Perkins mayoral campaign', 'Crain''s Detroit Business', 500);

-- ═══ HIT 3: Kenneth Daniels — convicted felon ═══
-- SDJ President was convicted of structuring financial transactions
-- for a $21M drug ring. 1 year federal prison.
UPDATE nodes SET detail = 
  'SDJ President. Former State Rep (1999-2004). CONVICTED: 1yr federal prison — structured $19K for drug kingpin Carlos Powell ($21M ring). Powell brothers got life. Appointed by Kilpatrick to Detroit Water Board. Also on Detroit Board of Education.'
WHERE id = 'daniels';

-- PATTERN: Barrett calls Lawrence "convicted felon" (expunged pipeline protest)
-- while Banks' network has ACTUAL convicted felons:
--   Daniels (SDJ president): federal drug money laundering
--   Fiore (Perkins donor): bribery
--   Holland (co-resident): cocaine dealing (MDOC #443789)
-- INSERT INTO pattern_registry
INSERT INTO patterns (id, name, investigations, detail)
VALUES ('felon_inversion', 'Convicted Felon Inversion Pattern', 'detroit,mi7',
  'Barrett weaponizes "convicted felon" against Lawrence (expunged 2013 protest). Meanwhile Banks network employs actual convicted felons: Kenneth Daniels (SDJ president, drug money $21M), Joseph Holland Jr. (MDOC #443789, cocaine), Gasper Fiore (Perkins donor, bribery). The label is projection.');

-- ═══ HIT 4: Dykema authored Michigan charter school law ═══
-- 1993 PA 362. Richard D. McLellan + Leonard C. Wolfe.
-- Same firm → wrote the law → defended it in court → formed SDJ → funded Barrett
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('dykema', 'charter_law_1993', 'authored', 'power',
  'McLellan + Wolfe authored 1993 PA 362 (charter school legislation). Also led defense in Council of Orgs v. Engler.',
  'Founders Library, Dykema.com, 455 Mich 557 (1997)');

-- PATTERN: Dykema 30-year arc
INSERT INTO patterns (id, name, investigations, detail)
VALUES ('dykema_arc', 'Dykema 30-Year Charter Arc', 'detroit,mi7',
  '1993: Authored charter school law (PA 362). 1997: Defended it at MSC. 2000s: Represented universities in establishing charters. 2016: Formed SDJ dark money vehicle for Banks network. 2021: SDJ fought Elrick, installed Johnson on Banks board. 2026: Dykema PAC donates $4K to Barrett. The firm that created the system protects the corruption within it.');

-- ═══ HIT 5: SDJ deep structure ═══
-- Knox, Wilk, Moore — all Dykema-connected
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('knox', 'Keenann Knox', 'actor', 3, 'detroit',
  'Impact Church pastor (east side). SDJ/Detroit Leaders president. Our Neighborhoods First officer. Former Detroit Board of Ethics member. Lives in St. Clair Shores.');
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('wilk', 'W. Alan Wilk', 'actor', 3, 'detroit',
  'Dykema attorney. Filed paperwork for SDJ AND Our Neighborhoods First. Also Duggan campaign lawyer. "Not authorized to speak to the press."');
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('renae_moore', 'Renae Moore', 'actor', 3, 'detroit',
  'SDJ Asst Secretary. Duggan campaign compliance officer. Dykema employee. Triple-role: dark money + campaign + law firm.');
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('carol_banks', 'Carol Banks', 'actor', 2, 'detroit',
  'Eastside Slate operator. Home raided by FBI. SDJ paid her $18K+ in "unspecified reimbursements." Under federal investigation re: whether city officials benefited from SDJ/Eastside Slate donations.');
INSERT INTO nodes (id, label, type, tier, investigation, detail)
VALUES ('onf', 'Our Neighborhoods First', 'entity', 3, 'detroit',
  'Dark money nonprofit. Led by Duggan appointees (Lorna Thomas, Betty Brooks). Attack ads against Duggan opponents. Prop N bond campaign. Website via Domains By Proxy.');

INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('knox', 'sdj', 'governance', 'power', 'President of SDJ/Detroit Leaders', 'Deadline Detroit, ProPublica');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('knox', 'onf', 'governance', 'power', 'Officer of Our Neighborhoods First', 'Deadline Detroit');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('wilk', 'sdj', 'formation', 'power', 'Filed SDJ paperwork (Dykema attorney)', 'Deadline Detroit');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('wilk', 'onf', 'formation', 'power', 'Filed ONF paperwork (Dykema attorney)', 'Deadline Detroit');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('sdj', 'carol_banks', 'payment', 'money', '$18K+ "unspecified reimbursements"', 'Deadline Detroit');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('carol_banks', 'eastside_slate', 'governance', 'power', 'Operates endorsement org', 'Deadline Detroit');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('renae_moore', 'sdj', 'governance', 'power', 'Asst Secretary', 'ProPublica 990');
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('renae_moore', 'dykema', 'employment', 'power', 'Employee', 'Deadline Detroit');

-- SDJ 2016 donors
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('bcbs_mi', 'sdj', 'donation', 'money', 'Blue Cross Blue Shield of Michigan donor', 'Campaign finance records', NULL);
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('moroun_pac', 'sdj', 'donation', 'money', 'Turn Around Wayne County PAC (Moroun/Central Transport)', 'Campaign finance records', NULL);
INSERT INTO edges (source, target, type, flow, label, source_doc, amount)
VALUES ('schostak_pac', 'sdj', 'donation', 'money', 'Schostak Family PAC (former GOP chairman)', 'Campaign finance records', NULL);

-- ═══ HIT 6: Sheffield-Bettison OIG investigation (Sep 2026) ═══
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('bettison', 'oig', 'investigation', 'power',
  'OIG opened investigation Sep 2026. Bettison called activist Jahdante Smith to remove social media photos of Sheffield with Marvin Walker.',
  'ClickOnDetroit Sep 22 2026, Detroit News Sep 22 2026');

-- ═══ HIT 7: Holland Jr. — Opportunities For All Michigan ═══
INSERT INTO edges (source, target, type, flow, label, source_doc)
VALUES ('holland', 'ofa_michigan', 'governance', 'power',
  'Officer of Opportunities For All Michigan (EIN 87-2342269). PO Box 361183, Grosse Pointe 48236. Tax-exempt.',
  'IRS e-Postcard');

-- ═══ TRAINING SUBSYSTEM PATTERNS ═══
-- Each natural hit follows a pattern we can use to predict future hits.

INSERT INTO training_signals (pattern_type, query_template, hit_rate, notes) VALUES
  ('reciprocal_donations', 'Search actor A donations → find actor B. Then search actor B donations → find actor A.', 'HIGH',
   'Gay-Dagnogo ↔ Perkins reciprocal. Suggests mutual support networks are discoverable by searching both directions.'),
  ('attorney_as_candidate', 'Search defense attorneys for political campaigns in same jurisdiction.', 'HIGH',
   'Perkins (Banks attorney) ran for Detroit Mayor. Defense attorneys who run for office may be building networks, not just practicing law.'),
  ('felon_donor_network', 'Search donor lists for convicted individuals.', 'HIGH',
   'Fiore (convicted briber) donated to Perkins. Convicted individuals who donate post-release reveal continued network participation.'),
  ('dark_money_officer_overlap', 'Search dark money org officers across multiple orgs.', 'HIGH',
   'Knox appears in SDJ AND ONF. Wilk filed paperwork for BOTH. Moore is SDJ officer AND Dykema employee AND Duggan campaign. Same people run multiple dark money vehicles.'),
  ('law_firm_as_architect', 'Search law firms for legislative authorship history.', 'MEDIUM',
   'Dykema authored charter school law AND formed dark money vehicle AND donated to federal candidate. Firms that write laws may later exploit them.'),
  ('appointed_by_convicted', 'Search appointees of convicted officials for continued participation.', 'MEDIUM',
   'Daniels appointed by Kilpatrick to Water Board. Kilpatrick appointees who remain active signal embedded network survival post-conviction.');
