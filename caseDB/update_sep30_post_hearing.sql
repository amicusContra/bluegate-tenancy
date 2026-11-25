-- ============================================================
-- UPDATE: Sep 29-30, 2026 — Post-Hearing Blitz
-- ============================================================

-- NEW ENTITIES
INSERT OR IGNORE INTO entities (id, name, type, notes) VALUES
('ellis-tracey', 'Tracey Ellis', 'person', 'Purpose CFO. Named defendant in amended 4349.');
INSERT OR IGNORE INTO entities (id, name, type, notes) VALUES
('judge-tremblay', 'Hon. Patricia A. Tremblay', 'person', 'Judge, 30th Circuit Ingham. Kevin PPO vs Banks.');
INSERT OR IGNORE INTO entities (id, name, type, notes) VALUES
('dr-charles-mok', 'Dr. Charles D. Mok, D.O.', 'person', 'Kevin father. Board-certified surgeon 35+ years. Chicago College of Osteopathic Medicine 1989. MSU Assistant Clinical Professor. Banks defamed him Sep 29.');

-- UPDATE CASES — PPO denials + appeals
UPDATE cases SET status = 'denied-appealing' WHERE id = '26-4432-PP';
UPDATE cases SET status = 'denied-appealing' WHERE id = '26-4435-PH';
UPDATE cases SET status = 'denied-appealing' WHERE id = '26-4436-PH';

-- NEW CASE: Kevin PPO vs Banks (Tremblay)
INSERT OR IGNORE INTO cases (id, court, judge, caption, case_type, status, notes) VALUES
('26-ppo-mok-banks', 'ingham-30th', 'judge-tremblay', 'Mok v. Banks', 'ppo-harassment', 'active', 'Kevin PPO against Banks. Hearing ~Oct 20. Filed before DaSean returned. Now loaded with Sep 29 evidence.');

-- NEW RELATIONSHIPS
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('banks-brian', 'holland-joseph', 'domestic-partner', 'Cohabitating domestic and economic unit since at least 2007. Shared addresses, joint property, trust successor, foundation officers.', 'Wayne ROD, LARA, PACER, MDOC', '2007-06-01');
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('banks-brian', 'dr-charles-mok', 'defamation', 'Banks called Dr. Mok a fraud in group email Sep 29 2026. Defamation per se of licensed professional.', 'Email chain Sep 29', '2026-09-29');
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('ellis-tracey', 'purpose-group', 'employer', 'Purpose CFO. Financial officer.', 'Corporate records');
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('holland-joseph', 'banks-brian', 'trust-successor', '1st Successor Trustee of Brian Banks Living Trust. Controls 1968 Severn if Banks dies/incapacitated.', 'Wayne ROD Trust Certificate 2025307266', '2025-11-07');

-- NEW EVIDENCE: Sep 29 email chain
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('banks-email-cease-desist', 'Banks cease-and-desist email + Dr. Brian Banks', 'email', 'Email bbanks@macdowellprep.com', '2026-09-29', 'Banks sends cease-and-desist, signs Dr. Brian Banks. No legal authority.', '["2026-4301-CZ","2026-4349-CZ","26-ppo-mok-banks"]');
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('banks-email-double-doctor', 'Banks Dr. Dr. Brian Banks - double doctor email', 'email', 'Email chain Sep 29', '2026-09-29', 'Banks affirms Dr. Dr. Brian Banks - double doctor. Acknowledges MSU JD.', '["2026-4349-CZ","26-ppo-mok-banks"]');
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('banks-email-law-degree', 'Banks my having a law degree email', 'email', 'Email chain Sep 29', '2026-09-29', 'Banks writes my having a law degree without denial. Confirms recordings of all five hearings exist.', '["2026-4349-CZ","26-ppo-mok-banks"]');
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('banks-email-dr-mok-defame', 'Banks defames Dr. Charles Mok as fraud', 'email', 'Email chain Sep 29', '2026-09-29', 'Banks: we are both frauds!!! Dr. Charles Mok. Defamation per se of board-certified surgeon.', '["2026-4349-CZ","26-ppo-mok-banks"]');
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('leon-email-threat-sep29', 'Leon Smith threat: just like the last one', 'email', 'Email oneomega1970@gmail.com', '2026-09-29', 'God will handle this situation, just like the last one. References Sep 2 assault. Written threat.', '["2026-4301-CZ","26-4436-PH"]');
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('shayla-email-service-sep29', 'Shayla claims email service is illegal', 'email', 'Email smith.shayla2013@yahoo.com', '2026-09-29', 'Shayla: You were not granted permission to serve me via alternate submissions. Confirms receipt by responding.', '["2026-4301-CZ","26-4432-PP","26-108221-DC"]');
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, date, description, case_ids) VALUES
('aop-discovery', 'Affidavit of Parentage discovered in Shayla complaint', 'document', 'Wayne County 26-108221-DC Paragraph 6', '2026-09-29', 'Shayla Complaint para 6 confirms AOP. Her Answer para 1: Paternity was acknowledged. Withheld from PPO hearing.', '["26-108221-DC","26-4432-PP","26-4435-PH","26-4436-PH"]');

-- NEW EVENTS
INSERT OR IGNORE INTO events (date, title, description, case_ids, source, significance) VALUES
('2026-09-29', 'PPO hearing — all 3 denied by Koenig', 'Judge Koenig denies all 3 PPO petitions. Admonishes Kevin for UPL. Shayla stays silent about AOP.', '["26-4432-PP","26-4435-PH","26-4436-PH"]', 'Court hearing', 'Dress rehearsal. AOP discovery changes everything.');
INSERT OR IGNORE INTO events (date, title, description, case_ids, source, significance) VALUES
('2026-09-29', 'AOP discovered in Shayla complaint', 'Kevin discovers Shayla Complaint para 6 confirms AOP existed all along.', '["26-108221-DC","26-4432-PP"]', 'Court filing review', 'Flips entire case. DaSean is legal parent since birth.');
INSERT OR IGNORE INTO events (date, title, description, case_ids, source, significance) VALUES
('2026-09-29', 'Email blitz — all 3 defendants respond with threats and admissions', 'Banks escalates to Dr. Dr. and defames Dr. Mok. Leon threatens violence. Shayla misquotes MCR. All confirm receipt.', '["2026-4301-CZ","2026-4349-CZ"]', 'Email chain', 'Coordination confirmed. Each response is an exhibit.');
INSERT OR IGNORE INTO events (date, title, description, case_ids, source, significance) VALUES
('2026-09-30', 'Kevin sends proof packet — 27 evidence files', 'After Banks claims ignorance, Kevin stages 27 files proving full knowledge of Banks-Holland partnership.', '["2026-4349-CZ","26-ppo-mok-banks"]', 'Proof packet email', 'Banks realizes Kevin has had the complete picture for weeks.');

-- NEW CASE PARTIES
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('26-ppo-mok-banks', 'mok-kevin', 'petitioner');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('26-ppo-mok-banks', 'banks-brian', 'respondent');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('26-ppo-mok-banks', 'judge-tremblay', 'judge');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4349-CZ', 'holland-joseph', 'defendant');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4349-CZ', 'ellis-tracey', 'defendant');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4349-CZ', 'purpose-group', 'defendant');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4349-CZ', 'pca', 'defendant');
INSERT OR IGNORE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4349-CZ', 'purpose-foundation', 'defendant');

-- NEW HEARINGS
INSERT OR IGNORE INTO hearings (id, case_ids, date, judge_id, hearing_type, status, notes) VALUES
('ppo-mok-banks-oct20', '["26-ppo-mok-banks"]', '2026-10-20', 'judge-tremblay', 'ppo', 'scheduled', 'Kevin PPO vs Banks. Fully loaded with Sep 29 evidence.');
INSERT OR IGNORE INTO hearings (id, case_ids, date, judge_id, hearing_type, status, notes) VALUES
('foc-oct7', '["26-108221-DC"]', '2026-10-07', 'referee-biggar', 'foc', 'scheduled', 'GAL motion. Thin packet.');
INSERT OR IGNORE INTO hearings (id, case_ids, date, time, judge_id, hearing_type, status, notes) VALUES
('cmc-oct9', '["26-108221-DC"]', '2026-10-09', '12:00', 'judge-triplett', 'motion', 'scheduled', 'Zoom. Venue transfer + GAL.');

-- PROPERTIES
INSERT OR IGNORE INTO properties (id, address, city, zip, owner_ids, doc_numbers, notes) VALUES
('1968-severn', '1968 Severn Rd', 'Grosse Pointe Woods', '48236', '["banks-brian"]', '["2018023312","2024223261","2025307266","2025307267"]', 'In Brian Banks Living Trust since Aug 2024. Holland is 1st successor trustee. HELOC $93,700.');
INSERT OR IGNORE INTO properties (id, address, city, zip, owner_ids, doc_numbers, notes) VALUES
('21553-newcastle', '21553 Newcastle Rd', 'Harper Woods', '48225', '["banks-brian","holland-joseph"]', '["2007402847"]', 'JTWRS since June 2007. $1 QCD. Holland concealed this in BK3.');
INSERT OR IGNORE INTO properties (id, address, city, zip, owner_ids, doc_numbers, notes) VALUES
('21456-newcastle', '21456 Newcastle Rd', 'Harper Woods', '48225', '["banks-brian"]', '[]', 'Banks prior address. Justin Banks successor trustee #2.');
