-- Holland BK docs pulled Sep 30 — the concealment proof
INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
VALUES (
    'holland-bk1-schedules',
    'Holland BK1 (09-46072) Schedules A-J — Newcastle $65K + Banks codebtor',
    'public-record',
    'PACER ED Mich Bankruptcy',
    'C:\Users\mokke\Documents\cases\evidence\pacer-indexed\holland-bankruptcies\09-46072_schedules_AJ.pdf',
    'Schedule A: 21553 Newcastle Rd Harper Woods, Joint tenant, $65,000, secured claim $137,400. Schedule H: Brian Banks XXXXX New Castle Road Harper Woods MI 48225 — codebtor. Schedule I line 13: Assistance from Co-owner/roommate (Brian Banks) $1,900/mo. Schedule I line 2: 2008 Co-owner/Roommate Brian Banks $10,000; 2007 $500; 2009 $1,166.66. 2006 Audi A6 at Newcastle, $32K. All possessions at 21553 Newcastle. 30 pages.',
    '2009-03-18',
    '["holland-joseph","banks-brian"]',
    '["2026-4349-CZ"]',
    'PACER federal court record — sworn under penalty of perjury'
);

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
VALUES (
    'holland-bk3-petition',
    'Holland BK3 (14-51632) Full Petition — Schedule A NONE, $110K discharged',
    'public-record',
    'PACER ED Mich Bankruptcy',
    'C:\Users\mokke\Documents\cases\evidence\pacer-indexed\holland-bankruptcies\14-51632_petition_full.pdf',
    'Schedule A: NONE — 0.00 real property. Summary: Total assets $6,682.29, Total liabilities $110,305.41. All discharged 11/12/2014. Prior BK cases filed within 8 years: NONE (false — had 3). Address: 20307 Lochmoor Harper Woods. 45 pages. Signed under penalty of perjury.',
    '2014-07-15',
    '["holland-joseph"]',
    '["2026-4349-CZ"]',
    'PACER federal court record — sworn under penalty of perjury'
);

INSERT OR REPLACE INTO evidence (id, title, ev_type, source, file_path, description, date, entity_ids, case_ids, authenticity)
VALUES (
    'holland-bk3-amendments',
    'Holland BK3 (14-51632) Amendments to Schedules',
    'public-record',
    'PACER ED Mich Bankruptcy',
    'C:\Users\mokke\Documents\cases\evidence\pacer-indexed\holland-bankruptcies\14-51632_amendments.pdf',
    'Doc 19 filed 09/11/2014 — Cover Sheet for Amendments to Schedules and/or Statements. What did Holland change 2 months after filing?',
    '2014-09-11',
    '["holland-joseph"]',
    '["2026-4349-CZ"]',
    'PACER federal court record'
);
