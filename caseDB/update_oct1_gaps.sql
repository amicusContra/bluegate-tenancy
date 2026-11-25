-- Gap fix: Wire up orphan entities with relationships
-- Run after update_oct1_morning.sql

-- Connect judges to their courts via judge-of
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('judge-koenig', 'mok-kevin', 'judge-of', 'Presides over PPO cluster (26-4432 through 26-4436) + Kevin PPO on Banks', 'Court records');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('judge-stokes', 'mok-kevin', 'judge-of', 'Presides over civil cases 4301-CZ and 4349-CZ', 'Court records');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('judge-triplett', 'mitchell-dasean', 'judge-of', 'Presides over custody 26-108221-DC', 'Court records');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('referee-biggar', 'mitchell-dasean', 'judge-of', 'FOC referee, Oct 7 hearing', 'Court records');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('judge-ramsey', 'banks-brian', 'board-member', 'CJC member. PCA board connection.', 'CJC records');

-- Connect agencies to referrals via relationships
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'fbi-detroit', 'referral', 'Federal master packet Sep 22. Banks network RICO + public corruption.', 'Email/fax receipts');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'doe-oig', 'referral', 'Federal education fraud, credential forgery referral.', 'Email');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'usps-oig', 'referral', 'Cases 174517, 202990, 208322. Leon Smith mail interception + forgery.', 'OIG portal');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'jtc', 'referral', '6 judges traced. JTC confirmed investigation. Notice received.', 'JTC letter');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'state-bar', 'referral', 'Banks UPL complaint filed Aug 31.', 'State Bar portal');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'mi-ag', 'referral', 'Referral Sep 9 to AG Moreland.', 'Email');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'mde', 'referral', 'FOIA Sep 21 (responded Sep 25). Supplement Sep 30 (TCR 22-12). Formal complaint Oct 1.', 'Email chain');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'mde-professional-practice', 'referral', 'Formal complaint Oct 1 re: TCR 22-12 violations. Acknowledged 9:25 AM.', 'Email');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'moahr', 'referral', 'FOIA Oct 1 for hearing transcript.', 'Email');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('mok-kevin', 'dpd', 'referral', 'DPD FOIA for police reports. Banks told officers he was an attorney.', 'FOIA request');

-- Connect Moreland + Schmiedeknecht
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('moreland-lamar', 'mi-ag', 'employer', 'Assistant Attorney General. Argued against Banks certificate reinstatement at TCR 22-12.', 'TCR 22-12 Final Decision');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('moreland-lamar', 'banks-brian', 'adversary', 'AG representative at TCR 22-12. Argued against reinstatement. Dept objected.', 'TCR 22-12 Final Decision');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('schmiedeknecht-katie', 'mde', 'employer', 'MDE OEE Analyst. Gave Banks the admin cert loophole Feb 2022.', 'MDE FOIA');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('schmiedeknecht-katie', 'banks-brian', 'enabler', 'Told Banks he could get admin cert before TCR resolved. 2hr 24min cover-up.', 'MDE FOIA');

-- Connect David Head
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('head-david', 'mde', 'employer', 'FOIA Coordinator. Exemplary service.', 'MDE FOIA response');

-- LARA connections
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('lara', 'purpose-group', 'registrar', 'LARA 803295082. LLC registration.', 'LARA records');
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('lara', 'banks-strategy', 'registrar', 'LARA 802070120. LLC registration.', 'LARA records');

-- Wayne FOC
INSERT INTO relationships (entity_a, entity_b, rel_type, description, source) VALUES
('wayne-foc', 'mitchell-dasean', 'agency', 'FOC hearing Oct 7. Custody proceedings.', 'Court scheduling');

-- Bankruptcy case parties
INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES
('26-47542', 'smith-marquita', 'debtor');
INSERT OR REPLACE INTO case_parties (case_id, entity_id, role) VALUES
('26-49404-lsg', 'smith-simone', 'debtor');

-- Evidence entity links for orphans
UPDATE evidence SET entity_ids = '["mok-kevin"]'
WHERE id = 'ps3665-wave1' AND (entity_ids IS NULL OR entity_ids = '[]');

UPDATE evidence SET entity_ids = '["banks-brian","mok-kevin"]'
WHERE id = 'banks-email-cease-desist';

UPDATE evidence SET entity_ids = '["banks-brian"]'
WHERE id = 'banks-email-double-doctor';

UPDATE evidence SET entity_ids = '["banks-brian"]'
WHERE id = 'banks-email-law-degree';

UPDATE evidence SET entity_ids = '["banks-brian","dr-charles-mok"]'
WHERE id = 'banks-email-dr-mok-defame';

UPDATE evidence SET entity_ids = '["smith-leon","mok-kevin"]'
WHERE id = 'leon-email-threat-sep29';

UPDATE evidence SET entity_ids = '["smith-shayla","mok-kevin"]'
WHERE id = 'shayla-email-service-sep29';

UPDATE evidence SET entity_ids = '["smith-shayla","mitchell-dasean"]'
WHERE id = 'aop-discovery';

-- Update case status for PPOs (denied but appealing)
UPDATE cases SET status = 'denied-appealing', notes = 'Dismissed procedurally Sep 29. Appeals due Oct 3.'
WHERE id IN ('26-4432-PP', '26-4435-PH', '26-4436-PH') AND status = 'active';

SELECT 'Gap fixes applied.' AS status;
