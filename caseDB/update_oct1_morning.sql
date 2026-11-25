-- caseDB update: Oct 1, 2026 morning
-- Brings database current with Sep 29-30 PPO hearing, Crump-Gibson entry,
-- MDE complaint, FOIA Round 2, MOAHR FOIA, all new entities
-- Run: cd caseDB; sqlite3 caseDB.sqlite < update_oct1_morning.sql

-- ============================================================
-- NEW ENTITIES
-- ============================================================

-- Crump-Gibson + GLLG
INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('crump-gibson-jehan', 'Jehan Crump-Gibson', 'person', NULL,
 '[{"street":"1 Towne Square Ste 1835","city":"Southfield","state":"MI","zip":"48076","source":"GLLG website","current":true}]',
 NULL, 'jehan@gllegalgroup.com',
 'Attorney. Entered Sep 30. Banks in 4301, ALL defendants in 4349. Great Lakes Legal Group PLLC.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('gllg', 'Great Lakes Legal Group PLLC', 'org', NULL,
 '[{"street":"1 Towne Square Ste 1835","city":"Southfield","state":"MI","zip":"48076","source":"GLLG website","current":true}]',
 NULL, 'admin@gllegalgroup.com',
 'Domain: gllegalgroup.com (double L). Crump-Gibson''s firm.');

-- Meihn + Foley Mansfield
INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('meihn-gregory', 'Gregory M. Meihn', 'person', NULL,
 '[{"street":"130 E. 9 Mile Rd","city":"Ferndale","state":"MI","zip":"48220","source":"Foley Mansfield","current":true}]',
 '248-721-4200', 'gmeihn@foleymansfield.com',
 'Partner, Foley & Mansfield PLLP. MacDowell board attorney. MSU MS, Toledo JD. Weekly meetings with Banks.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('foley-mansfield', 'Foley & Mansfield PLLP', 'org', NULL,
 '[{"street":"130 E. 9 Mile Rd","city":"Ferndale","state":"MI","zip":"48220","source":"firm website","current":true}]',
 '248-721-4200', 'communications@foleymansfield.com',
 'National firm. 150+ attorneys.');

-- TCR 22-12 witnesses
INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('shulman-terrence', 'Terrence Shulman', 'person', '["LMSW"]', NULL,
 NULL, NULL,
 'TCR 22-12 witness. Licensed social worker. Self-described recovering theft addict. Cannot diagnose PTSD. State Bar referral 2011. 6 sessions 2011, 12 sessions 2020-2021.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('leno-michele', 'Michele Leno', 'person', '["Ph.D."]', NULL,
 NULL, NULL,
 'TCR 22-12 witness. Psychologist. Saybrook doctorate (low-residency). Specialty: athletes, social media — NOT PTSD/forensic. 13 sessions over 2 months. Concluded Banks is person of integrity.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('vitti-nicolai', 'Nicolai Vitti', 'person', '["Ph.D."]', NULL,
 NULL, NULL,
 'DPSCD Superintendent. Mentored Banks. Testified at TCR 22-12. Authorized PCA charter Jul 2025.');

-- Wells Stallworth + Stallworth dynasty
INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('wells-stallworth-nicole', 'Nicole Wells Stallworth', 'person', NULL, NULL,
 NULL, 'nwells@childrensctr.net',
 'MacDowell Board Chair. Former CEO, The Children''s Center. Wife of Thomas Stallworth III. Signs Condition #7 compliance verifications.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('childrens-center', 'The Children''s Center', 'org', '["TCC"]',
 '[{"street":"79 W. Alexandrine","city":"Detroit","state":"MI","zip":"48201","source":"TCC website","current":true}]',
 '313-831-5535', NULL,
 'Wells Stallworth was CEO (~Jul 2023-2025). Ellis is CFO. Pipeline from board chair network into Banks enterprise financial operations.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('stallworth-thomas-iii', 'Thomas Stallworth III', 'person', NULL, NULL,
 NULL, NULL,
 'Former state rep. Husband of Nicole Wells Stallworth. Father of Misha Stallworth West.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('stallworth-west-misha', 'Misha Stallworth West', 'person', NULL, NULL,
 NULL, NULL,
 'DPSCD Board member. Thomas Stallworth III''s daughter. Charter authorization pipeline.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('stallworth-keith', 'Keith Stallworth', 'person', NULL, NULL,
 NULL, NULL,
 'Former state rep, Wayne County commissioner. Pled guilty federal financial crime 2003 (laundering drug money through Tiger''s Lounge). Brother of Thomas III.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('stallworth-alma', 'Alma Stallworth', 'person', NULL, NULL,
 NULL, NULL,
 'Matriarch. Former state representative. Mother of Keith and Thomas III.');

-- MacDowell board members
INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('washington-artesia', 'Artesia Washington', 'person', NULL, NULL,
 '248-415-2500', 'artesiam@irvineheadinjury.com',
 'MacDowell Board Treasurer. Executive Director, Irvine Neuro Rehabilitation LLC.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('hall-verkeydia', 'Verkeydia Hall', 'person', '["Esq"]', NULL,
 '248-270-6262', NULL,
 'MacDowell Board Director. Attorney. Crump Hall of Justice Law Firm PLLC.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('longstreet-kristine', 'Kristine Longstreet', 'person', NULL, NULL,
 '313-474-3200', NULL,
 'MacDowell Board Director. Managing Director, Neighborhood Defender Service Detroit.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('mcgee-tynisha', 'Dr. Tynisha McGee', 'person', '["Ed.D"]', NULL,
 NULL, NULL,
 'MacDowell Board Treasurer. District Dean, Wayne County Community College.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('reed-hendon-caryn', 'Dr. Caryn Reed-Hendon', 'person', '["Ph.D."]', NULL,
 NULL, NULL,
 'MacDowell Board Vice Chair. Manager, Office of Diversity & Inclusion, Henry Ford Medical Group.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('preuss-ric', 'Ric Preuss', 'person', NULL, NULL,
 NULL, NULL,
 'MacDowell Board Secretary. Business Agent, IBEW Local 58. Public Lighting Authority board.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('coffee-winston', 'Winston Coffee', 'person', NULL, NULL,
 NULL, NULL,
 'MacDowell Board Director. Director of Alumni Engagement, Midnight Golf / College Career & Beyond.');

-- Agencies
INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('mde-professional-practice', 'MDE Professional Practice', 'agency', NULL, NULL,
 NULL, 'MDE-Professional-Practice@Michigan.gov',
 'Office of Educator Excellence. Handles administrator certificate complaints under R 380.124.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('moahr', 'Michigan Office of Administrative Hearings and Rules', 'agency', '["MOAHR"]', NULL,
 '517-335-2484', 'MOAHR-FOIA@michigan.gov',
 'Holds TCR 22-12 hearing record. David Head directed Kevin here for hearing docs.');

INSERT OR REPLACE INTO entities (id, name, type, aliases, addresses, phone, email, notes) VALUES
('head-david', 'David Head', 'person', NULL, NULL,
 '517-855-1139', NULL,
 'MDE FOIA Coordinator. Exemplary service. Commendation filed Oct 1. Signaled compliance docs exist but weren''t requested.');

-- Update existing entities with new info
UPDATE entities SET notes = '9 felony convictions. SID 2029469K. Claims J.D. (MSU, real) — no bar admission (felonies prevented). Walden doctorate real but no IRB. TCR 22-12 issued 7 conditions Aug 2023.'
WHERE id = 'banks-brian';

UPDATE entities SET notes = 'FOIA responded Sep 25. David Head coordinator. Second request Oct 1 (compliance verifications). Formal complaint filed Oct 1.'
WHERE id = 'mde';

UPDATE entities SET email = 'eco.primal@pm.me', notes = 'Army veteran. Eagle Scout. Background: bioethics, genetics, computational biology. Pro se plaintiff + witness. Zero convictions, zero bankruptcies. Father: Dr. Charles Mok (board-certified surgeon).'
WHERE id = 'mok-kevin';

UPDATE entities SET notes = 'MacDowell Board Chair (co-chair with Wells Stallworth). 36th District. Campaign paid Banks Strategy $383.82.'
WHERE id = 'judge-yancey';

-- ============================================================
-- CASE PARTY UPDATES
-- ============================================================

-- Banks now has attorney in 4301
INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4301-CZ', 'banks-brian', 'defendant');

INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4301-CZ', 'crump-gibson-jehan', 'attorney-defendant');

-- SAC added new defendants to 4349
INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES
('2026-4349-CZ', 'holland-joseph', 'defendant'),
('2026-4349-CZ', 'ellis-tracey', 'defendant'),
('2026-4349-CZ', 'macdowell', 'defendant'),
('2026-4349-CZ', 'purpose-group', 'defendant'),
('2026-4349-CZ', 'purpose-foundation', 'defendant'),
('2026-4349-CZ', 'crump-gibson-jehan', 'attorney-defendant');

-- PPO mok-on-banks in Ingham
INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES
('26-ppo-mok-banks', 'mok-kevin', 'petitioner'),
('26-ppo-mok-banks', 'banks-brian', 'respondent');

-- ============================================================
-- NEW CASE (Kevin's PPO on Banks)
-- ============================================================
INSERT OR REPLACE INTO cases (id, court, judge, caption, case_type, filed_date, status, notes) VALUES
('26-ppo-mok-banks', 'ingham-30th', 'judge-koenig', 'Mok v. Banks', 'ppo-harassment', '2026-09-15', 'active', 'Kevin''s PPO against Banks. Separate from DaSean''s PPO cluster.');

-- Update existing case statuses
UPDATE cases SET status = 'active', notes = 'SAC filed Sep 30. 9 counts, 6 defendants. Crump-Gibson responsive pleadings mooted same day.'
WHERE id = '2026-4349-CZ';

UPDATE cases SET caption = 'Mok v. Smith et al.', notes = 'Banks is a party via 4349 civil conspiracy. Crump-Gibson entered Sep 30.'
WHERE id = '2026-4301-CZ';

-- Update PPO hearing status
UPDATE hearings SET status = 'completed', outcome = 'Dismissed procedurally. Lesson: narrow standing + specific grounds. Banks defamed Kevin on record voluntarily.'
WHERE id = 'ppo-hearing-sep29';

-- ============================================================
-- NEW RELATIONSHIPS
-- ============================================================

INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('crump-gibson-jehan', 'banks-brian', 'attorney', 'Represents Banks in 4301-CZ', 'Email Sep 30', '2026-09-30');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('crump-gibson-jehan', 'gllg', 'employer', 'Attorney at Great Lakes Legal Group PLLC', 'GLLG website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('meihn-gregory', 'macdowell', 'attorney', 'Board counsel. Weekly meetings with Banks.', 'TCR 22-12, MDE FOIA', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('meihn-gregory', 'foley-mansfield', 'employer', 'Partner', 'Firm website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('meihn-gregory', 'banks-brian', 'attorney', 'Weekly compliance meetings. Testified at TCR 22-12.', 'TCR 22-12 Final Decision', '2022-01-01');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('wells-stallworth-nicole', 'macdowell', 'board-member', 'Board Chair. Signs Condition #7 verifications.', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('wells-stallworth-nicole', 'childrens-center', 'employer', 'Former CEO (~Jul 2023-2025)', 'PR Newswire, LinkedIn', '2023-07-10');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('ellis-tracey', 'childrens-center', 'employer', 'CFO at The Children''s Center', 'TCC team page', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('wells-stallworth-nicole', 'stallworth-thomas-iii', 'family', 'Married', 'Public record', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('stallworth-west-misha', 'stallworth-thomas-iii', 'family', 'Father and daughter', 'Public record', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('stallworth-west-misha', 'dpscd', 'board-member', 'DPSCD Board member. Charter authorization pipeline.', 'DPSCD records', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('vitti-nicolai', 'dpscd', 'employer', 'Superintendent', 'DPSCD website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('vitti-nicolai', 'banks-brian', 'mentor', 'Regular mentorship meetings. Testified at TCR 22-12.', 'TCR 22-12 Final Decision', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('shulman-terrence', 'banks-brian', 'therapist', '6 sessions 2011, 12 sessions 2020-2021. State Bar referral.', 'TCR 22-12 Final Decision', '2011-01-01');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('leno-michele', 'banks-brian', 'evaluator', '13 sessions over 2 months. Concluded Banks is person of integrity.', 'TCR 22-12 Final Decision', '2020-01-01');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('stallworth-keith', 'stallworth-alma', 'family', 'Son', 'Public record', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('stallworth-thomas-iii', 'stallworth-alma', 'family', 'Son', 'Public record', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('washington-artesia', 'macdowell', 'board-member', 'Board Treasurer', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('hall-verkeydia', 'macdowell', 'board-member', 'Board Director', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('longstreet-kristine', 'macdowell', 'board-member', 'Board Director', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('mcgee-tynisha', 'macdowell', 'board-member', 'Board Treasurer', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('reed-hendon-caryn', 'macdowell', 'board-member', 'Board Vice Chair', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('preuss-ric', 'macdowell', 'board-member', 'Board Secretary', 'MacDowell website', NULL);
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source, start_date) VALUES
('coffee-winston', 'macdowell', 'board-member', 'Board Director', 'MacDowell website', NULL);

-- ============================================================
-- NEW EVENTS (Sep 29 - Oct 1)
-- ============================================================

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-09-29', 'PPO hearing — all respondents testify',
 'Banks claims video and affidavits. Shayla testifies. PPOs dismissed procedurally. Banks defames Kevin on the record voluntarily — never needed to speak.',
 '["26-ppo-mok-banks","26-4432-PP","26-4433-PH","26-4434-PH","26-4435-PH","26-4436-PH"]',
 '["banks-brian","smith-shayla","smith-leon","smith-marquita","smith-simone","mok-kevin","mitchell-dasean","judge-koenig"]',
 'Court record', 'Banks volunteered testimony without counsel. Every word is usable in 4301/4349. Lesson: standing + grounds must be narrow.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-09-29', 'Banks-Leon-Shayla email chain erupts overnight',
 'Banks sends cease-and-desist signing as Dr. Dr. Brian Banks. Claims law degree. Leon threatens. Shayla claims email service is illegal. Banks defames Dr. Charles Mok as fraud.',
 '["2026-4301-CZ","2026-4349-CZ"]',
 '["banks-brian","smith-leon","smith-shayla","mok-kevin"]',
 'Email chain Sep 29', 'All emails preserved as evidence. Party admissions throughout.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-09-30', 'Crump-Gibson enters as defense counsel',
 'Files responsive pleadings to FAC in morning. Confirms: Banks only in 4301, ALL defendants in 4349. Great Lakes Legal Group PLLC.',
 '["2026-4301-CZ","2026-4349-CZ"]',
 '["crump-gibson-jehan","banks-brian"]',
 'Email from jehan@gllegalgroup.com', 'First legitimate attorney on defense side. Responsive pleadings mooted same day by SAC.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-09-30', 'SAC filed — moots Crump-Gibson motions',
 'Kevin files Second Amended Complaint (4349), Initial Disclosures (both cases). SAC supersedes FAC per MCR 2.118. 9 counts, 6 defendants.',
 '["2026-4349-CZ","2026-4301-CZ"]',
 '["mok-kevin","crump-gibson-jehan"]',
 'Ingham County clerk', 'Crump-Gibson morning motions immediately moot. New 21-day response clock starts.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-09-30', 'MDE FOIA supplement — TCR 22-12 received',
 'David Head proactively sends TCR 22-12 Final Decision and cover letter. Notes no formal complaints have been filed against Banks.',
 '["2026-4349-CZ"]',
 '["head-david","banks-brian","mde"]',
 'MDE FOIA email', 'First receipt of the 7 conditions. Head signals compliance docs exist but were not part of the request.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-10-01', 'MDE formal complaint filed and acknowledged',
 'Complaint to Professional Practice: TCR 22-12 violations, UPL, Condition #4 evasion, §5.2 false representation. Acknowledged at 9:25 AM. 7-10 business day processing.',
 '["2026-4349-CZ"]',
 '["banks-brian","mde-professional-practice"]',
 'Email acknowledgment Oct 1', 'First formal complaint against Banks since TCR 22-12 issued. R 380.124 triggers mandatory investigation.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-10-01', 'MDE FOIA Round 2 submitted',
 'Requesting: Condition #7 compliance verifications (Wells-Stallworth signed), board correspondence, Management Agreement, DPSCD authorization records.',
 '["2026-4349-CZ"]',
 '["head-david","wells-stallworth-nicole","mde"]',
 'Email reply to David Head', 'Targets Wells-Stallworth signed verifications. Tests Condition #4 compliance.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-10-01', 'MOAHR FOIA submitted',
 'Requesting: full TCR 22-12 hearing transcript, ALJ proposal for decision, AG exceptions, responses, exhibits, procedural orders, case docket.',
 '["2026-4349-CZ"]',
 '["moahr","banks-brian"]',
 'Email to MOAHR-FOIA@michigan.gov', 'Will reveal full testimony under oath, AG arguments against certificate, cross-examination. Expect response by Oct 8-9.');

INSERT INTO events (date, title, description, case_ids, entity_ids, source, significance) VALUES
('2026-10-01', 'MDE commendation + thank you sent',
 'Commendation for FOIA team sent to MDE Office of the Superintendent (Dr. Glenn Maleyko). Thank you to David Head.',
 NULL,
 '["head-david","mde"]',
 'Email', 'Professional courtesy. Establishes relationship quality with government agencies.');

-- ============================================================
-- NEW FOIA REQUESTS
-- ============================================================

INSERT OR REPLACE INTO foia_requests (id, agency_id, date_sent, due_date, subject, status, notes) VALUES
('foia-mde-round2-oct1', 'mde', '2026-10-01', '2026-10-08',
 'Condition #7 compliance verifications, board correspondence, Management Agreement, DPSCD authorization',
 'sent', 'Targets Wells-Stallworth signed verifications. Reply to existing David Head chain.');

INSERT OR REPLACE INTO foia_requests (id, agency_id, date_sent, due_date, subject, status, notes) VALUES
('foia-moahr-oct1', 'moahr', '2026-10-01', '2026-10-08',
 'TCR 22-12 full hearing record: transcript, ALJ proposal, AG exceptions, exhibits, procedural orders',
 'sent', 'David Head directed Kevin to MOAHR for hearing docs.');

-- Update existing FOIA with supplement
UPDATE foia_requests SET response_notes = '20 files Sep 25 + TCR 22-12 supplement Sep 30'
WHERE id = 'foia-mde-sep21';

-- ============================================================
-- NEW AGENCY REFERRALS
-- ============================================================

INSERT OR REPLACE INTO agency_referrals (id, agency_id, date_sent, subject, status, response_date, response_notes) VALUES
('mde-complaint-oct1', 'mde-professional-practice', '2026-10-01',
 'Formal complaint: TCR 22-12 violations, UPL, Condition #4 evasion, §5.2 false representation, FERPA, Condition #7 verification, witness qualifications',
 'acknowledged', '2026-10-01', 'Acknowledged 9:25 AM. Processing 7-10 business days.');

-- Update JTC referral with new info
UPDATE agency_referrals SET notes = 'JTC confirmed investigation of all 6 judges Kevin traced. Notice received.'
WHERE id = 'jtc-miller';

-- ============================================================
-- NEW EVIDENCE
-- ============================================================

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('tcr-22-12-decision', 'TCR 22-12 Final Decision and Order', 'document',
 'MDE FOIA Supplement Sep 30', '2023-08-04',
 '["banks-brian","mde"]', '["2026-4349-CZ"]',
 'Government FOIA response',
 '7 conditions. Dept objected to reinstatement. AG argued against. Rice overruled. ALJ recommended no conditions. Condition #7: compliance verifications every 6 months.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('tcr-22-12-cover-letter', 'TCR 22-12 Cover Letter', 'document',
 'MDE FOIA Supplement Sep 30', '2023-08-04',
 '["banks-brian","mde"]', '["2026-4349-CZ"]',
 'Government FOIA response',
 'Accompanies the administrator certificate.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('ring-video-sep2-compressed', 'Ring camera video — Sep 2 assault (compressed for email)', 'video',
 'Ring camera', '2026-09-02',
 '["smith-leon","mitchell-dasean","smith-shayla"]', '["2026-4301-CZ","26-4436-PH"]',
 'Ring timestamp + geolocation',
 'Compressed from 63MB MOV to 4.66MB MP4 via ffmpeg (libx264, CRF 28, 720p). Original preserved.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('crump-gibson-entry-email', 'Crump-Gibson representation confirmation email', 'email',
 'jehan@gllegalgroup.com', '2026-09-30',
 '["crump-gibson-jehan","banks-brian"]', '["2026-4301-CZ","2026-4349-CZ"]',
 'Email with firm letterhead',
 'Confirms: Banks only in 4301, ALL in 4349. Filed responsive pleadings morning of Sep 30.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('banks-email-chain-sep29', 'Banks-Leon-Shayla email chain Sep 29', 'email',
 'Email chain Sep 29 overnight', '2026-09-29',
 '["banks-brian","smith-leon","smith-shayla","mok-kevin"]', '["2026-4301-CZ","2026-4349-CZ"]',
 'Email thread with headers',
 'Banks signs as Dr. Dr. Brian Banks. Claims law degree. Defames Dr. Charles Mok. Leon threatens. Shayla claims email service is illegal. All party admissions.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('parentage-confessions-03', 'Parentage / AOP confessions — Exhibit 3', 'document',
 'Shayla filing exhibits', '2026-09-05',
 '["smith-shayla","mitchell-dasean"]', '["26-108221-DC","26-4432-PP"]',
 'Party admission — Shayla filed this herself',
 'Shayla acknowledges AOP exists and claims it was filed. Kevin and DaSean did not know birth cert did not establish paternity in MI.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('9line-federal-referral', '9-Line Federal Referral Packet', 'document',
 'Kevin''s federal submission Sep 22-25', '2026-09-25',
 '["mok-kevin"]', '["2026-4349-CZ"]',
 'Filed with 8 federal agencies',
 '243 pages. Submitted to FBI, USAO, USPS OIG, DOE OIG, IRS CI, FEC, State Bar, JTC. Published to detroit site.');

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, date, entity_ids, case_ids, authenticity, notes) VALUES
('mde-complaint-ack-oct1', 'MDE Professional Practice complaint acknowledgment', 'email',
 'MDE-Professional-Practice@Michigan.gov', '2026-10-01',
 '["mde-professional-practice","banks-brian"]', '["2026-4349-CZ"]',
 'Government email receipt',
 'Acknowledged at 9:25 AM Oct 1. 7-10 business days processing. R 380.124 mandatory investigation triggered.');

-- ============================================================
-- NEW HEARINGS
-- ============================================================

-- FOC Oct 7 details
UPDATE hearings SET time = '11:15', notes = 'FOC hearing. Referee Biggar. Kevin fact witness. Narrow: one date, one denial, one document. Bring PPO orders from Koenig.'
WHERE id = 'foc-oct7';

-- ============================================================
-- DONE
-- ============================================================
SELECT 'Update complete. Run: python braid.py full' AS status;
