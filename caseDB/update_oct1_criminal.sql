-- caseDB update: Oct 1 criminal referrals + damages supplement
-- Run: Get-Content update_oct1_criminal.sql | sqlite3 caseDB.sqlite

-- New entities: law enforcement + prosecutor
INSERT OR IGNORE INTO entities (id, name, type, aliases, addresses, phone, email, notes)
VALUES
  ('dpd', 'Detroit Police Department', 'agency', NULL, '["Detroit, MI"]', NULL, NULL, 'Banks filed retaliatory Report #26-0909-0176 on Sep 9, same day as civil service.'),
  ('gpw-pd', 'Grosse Pointe Woods Police Department', 'agency', NULL, '["20025 Mack Plaza Dr, Grosse Pointe Woods, MI 48236"]', '(313) 343-2400', NULL, 'Banks filed retaliatory Report #26-7615 on Sep 28. Det. Adams investigating. Kevin briefed on recorded line Oct 1.'),
  ('ingham-prosecutor', 'Ingham County Prosecuting Attorney', 'agency', NULL, '["303 W. Kalamazoo St., 4th Floor, Lansing, MI 48933"]', NULL, NULL, 'Criminal referral for Banks false police reports drafted Oct 1.'),
  ('det-adams', 'Detective Adams', 'person', NULL, '["Grosse Pointe Woods, MI"]', '(313) 343-2412', NULL, 'GPW PD detective investigating Report #26-7615. Called Kevin Oct 1, recorded line. Professional. Kevin briefed full case context including criminal history, federal referrals, counsel info, and detroit.primals.eco URL (NATO phonetic).');

-- Wire Adams to GPW PD
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, start_date, notes)
VALUES
  ('det-adams', 'gpw-pd', 'employee-of', 'Detective at GPW PD investigating Report #26-7615', 'phone call Oct 1', '2026-10-01', NULL);

-- Banks filed reports with both departments
INSERT OR IGNORE INTO relationships (entity_a, entity_b, rel_type, description, source, start_date, notes)
VALUES
  ('banks', 'dpd', 'complainant-to', 'Filed retaliatory Report #26-0909-0176 on Sep 9 — same day as civil service in 4349-CZ', 'DPD records', '2026-09-09', 'First retaliatory false report'),
  ('banks', 'gpw-pd', 'complainant-to', 'Filed retaliatory Report #26-7615 on Sep 28 — same day as preservation letters received', 'GPW PD records', '2026-09-28', 'Second retaliatory false report. "Evidence" = handmade anniversary card.');

-- New agency referrals
INSERT OR IGNORE INTO agency_referrals (id, agency_id, date_sent, subject, status, notes)
VALUES
  ('ref-ingham-prosecutor-oct1', 'ingham-prosecutor', '2026-10-01', 'Banks false police reports + obstruction of Ingham proceedings', 'drafted', 'Criminal referral: 2 retaliatory reports (DPD #26-0909-0176, GPW #26-7615) filed on exact dates of legal service. MCL 750.411a, 750.505, 750.122(7)(a). Crump-Gibson disclaimer cited.'),
  ('ref-usps-oig-supp-oct1', 'usps-oig', '2026-10-01', 'Banks retaliation against federal complainant', 'drafted', 'Supplement to Cases #174517, #202990, #208322. Witness intimidation per 18 USC 1512-1513. Two retaliatory reports targeting federal complainant.'),
  ('ref-fbi-supp-oct1', 'fbi', '2026-10-01', 'Banks witness intimidation pattern', 'drafted', 'Supplement to Sep 21-22 referral. Two retaliatory reports, jurisdiction shopping (DPD then GPW), counsel disclaimer. 18 USC 1512(b)(3), 1513(e).');

-- New evidence items
INSERT OR IGNORE INTO evidence (id, title, ev_type, source, description, date, entity_ids, case_ids, notes)
VALUES
  ('ev-ingham-criminal-referral', 'Ingham County Prosecutor criminal referral', 'document', 'plaintiff', 'Criminal referral for Banks false police reports — MCL 750.411a, 750.505, 750.122(7)(a)', '2026-10-01', '["banks","kevin"]', '["4349-CZ","4301-CZ"]', 'Two retaliatory reports on exact dates of legal service. Crump-Gibson disclaimer cited.'),
  ('ev-usps-oig-supp-oct1', 'USPS OIG supplement — retaliation against complainant', 'document', 'plaintiff', 'Supplement to OIG Cases #174517, #202990, #208322. Witness intimidation 18 USC 1512-1513.', '2026-10-01', '["banks","kevin"]', '["4349-CZ"]', 'Banks retaliating against the person who filed federal complaints.'),
  ('ev-fbi-supp-oct1', 'FBI supplement — witness intimidation pattern', 'document', 'plaintiff', 'Supplement to Sep 21-22 referral. Jurisdiction shopping, counsel disclaimer.', '2026-10-01', '["banks","kevin"]', '["4349-CZ"]', '18 USC 1512(b)(3), 1513(e). Two reports in two jurisdictions.'),
  ('ev-damages-supp-oct1', 'Damages supplement — attorney validation + forced deanonymization', 'document', 'plaintiff', 'Updated rate $278→$300/hr (validated by defense billing). New $275K deanonymization damage claim. Corrected aggregates.', '2026-10-01', '["kevin","banks"]', '["4349-CZ"]', 'Destruction of 12+ months pseudonymous identity architecture. Crypto-timestamped docs prove pre-Banks design intent.'),
  ('ev-anniversary-card', 'Handmade anniversary card (Banks exhibit)', 'document', 'plaintiff', 'One-month anniversary card. Craft cardstock, archival ink, decorative stamps: Just a Note, Friend to Friend, Happy Anniversary. First Amendment protected speech. Banks gave to GPW PD as trespass evidence.', '2026-09-28', '["kevin","banks"]', '["4349-CZ"]', 'Will be exhibit at trial. Protected speech. Banks treating it as criminal evidence demonstrates retaliatory mindset.');

-- New events
INSERT OR IGNORE INTO events (date, title, description, case_ids, entity_ids, source, evidence_ids, significance)
VALUES
  ('2026-10-01', 'Criminal referral to Ingham County Prosecutor drafted', 'Referral for Banks false police reports — 2 retaliatory reports filed on exact dates of legal service. MCL 750.411a, 750.505, 750.122(7)(a).', '["4349-CZ","4301-CZ"]', '["kevin","banks","ingham-prosecutor"]', 'plaintiff filing', '["ev-ingham-criminal-referral"]', 'Routes criminal prosecution through Ingham County (where civil cases are) rather than compromised Wayne County institutions.'),
  ('2026-10-01', 'Federal supplements drafted — USPS OIG + FBI', 'Supplements to existing federal complaints with retaliatory police report pattern. 18 USC 1512-1513.', '["4349-CZ"]', '["kevin","banks"]', 'plaintiff filing', '["ev-usps-oig-supp-oct1","ev-fbi-supp-oct1"]', 'Adds witness intimidation to existing mail fraud and RICO referrals.'),
  ('2026-10-01', 'Damages supplement drafted — rate validated + forced deanonymization ($275K)', 'Defense attorney retention validates $300/hr rate. New damage: destruction of pseudonymous identity architecture (12+ months, crypto-timestamped).', '["4349-CZ"]', '["kevin","banks","crump-gibson"]', 'plaintiff analysis', '["ev-damages-supp-oct1"]', 'Defense spending paradox: every dollar Banks spends defending validates plaintiffs economic damages.');

-- Graph edges for new connections
INSERT OR IGNORE INTO graph_edges (source, target, edge_type, epistemic, note, source_doc, temporal)
VALUES
  ('kevin', 'ingham-prosecutor', 'referred-to', 'record', 'Criminal referral: Banks false police reports', 'INGHAM_PROSECUTOR_CRIMINAL_REFERRAL_OCT1.md', '2026-10-01'),
  ('banks', 'dpd', 'filed-with', 'record', 'Retaliatory Report #26-0909-0176 — same day as civil service Sep 9', 'DPD records', '2026-09-09'),
  ('banks', 'gpw-pd', 'filed-with', 'record', 'Retaliatory Report #26-7615 — same day as preservation letters Sep 28', 'GPW PD records', '2026-09-28'),
  ('det-adams', 'gpw-pd', 'works-for', 'record', 'Detective investigating Report #26-7615', 'phone call', '2026-10-01'),
  ('det-adams', 'kevin', 'interviewed', 'record', 'Recorded phone call Oct 1 — Kevin briefed full case context', 'recorded call', '2026-10-01'),
  ('kevin', 'usps-oig', 'supplemented', 'record', 'Retaliation supplement to Cases #174517, #202990, #208322', 'SUPPLEMENT_USPS_OIG_RETALIATION_OCT1.md', '2026-10-01'),
  ('kevin', 'fbi', 'supplemented', 'record', 'Witness intimidation supplement to Sep 21-22 referral', 'SUPPLEMENT_FBI_WITNESS_INTIMIDATION_OCT1.md', '2026-10-01');
