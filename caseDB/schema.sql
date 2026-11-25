-- Case Intelligence Database — Schema
-- sqlite3 caseDB.sqlite < schema.sql
-- Designed for cross-case evidence tracking, exhibit subsetting,
-- and relational queries across all proceedings.

PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

--------------------------------------------------------------
-- ENTITIES: people, orgs, courts, agencies, schools
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS entities (
    id          TEXT PRIMARY KEY,    -- slug: 'banks-brian', 'pca', 'wayne-circuit'
    name        TEXT NOT NULL,
    type        TEXT NOT NULL,       -- person, org, court, agency, school, entity, pac
    aliases     TEXT,                -- JSON array of alternate names
    addresses   TEXT,                -- JSON array of {street, city, state, zip, source, current}
    phone       TEXT,
    email       TEXT,
    notes       TEXT,
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

--------------------------------------------------------------
-- CASES: every case number across all courts
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS cases (
    id          TEXT PRIMARY KEY,    -- case number: '2026-4301-CZ'
    court       TEXT,                -- 'ingham-30th', 'wayne-3rd', 'ed-mich'
    judge       TEXT,                -- entity_id of judge
    caption     TEXT,                -- 'Mok v. Smith et al.'
    case_type   TEXT,                -- civil, ppo-domestic, ppo-harassment, custody, bankruptcy, foia
    filed_date  TEXT,
    status      TEXT,                -- active, default-pending, closed, dismissed
    notes       TEXT,
    created_at  TEXT DEFAULT (datetime('now'))
);

--------------------------------------------------------------
-- CASE_PARTIES: who plays what role in each case
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS case_parties (
    case_id     TEXT NOT NULL REFERENCES cases(id),
    entity_id   TEXT NOT NULL REFERENCES entities(id),
    role        TEXT NOT NULL,       -- plaintiff, defendant, petitioner, respondent, witness, expert, representative, judge, referee
    notes       TEXT,
    PRIMARY KEY (case_id, entity_id, role)
);

--------------------------------------------------------------
-- EVENTS: master timeline across all cases
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS events (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,       -- ISO date: '2026-09-02'
    date_approx INTEGER DEFAULT 0,  -- 1 if date is approximate
    title       TEXT NOT NULL,       -- short: 'Leon assaults DaSean'
    description TEXT,                -- longer narrative
    case_ids    TEXT,                -- JSON array of related case IDs
    entity_ids  TEXT,                -- JSON array of involved entity IDs
    source      TEXT,                -- 'Ring camera', 'ICHAT', 'Wayne ROD'
    evidence_ids TEXT,               -- JSON array of evidence item IDs
    significance TEXT,               -- why this matters
    created_at  TEXT DEFAULT (datetime('now'))
);

--------------------------------------------------------------
-- DOCUMENTS: every filing, motion, letter, form
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS documents (
    id          TEXT PRIMARY KEY,    -- slug: 'motion-alt-service-sep17'
    title       TEXT NOT NULL,
    doc_type    TEXT NOT NULL,       -- motion, complaint, ppo-petition, demand-letter, spoliation, subpoena, foia, affidavit, declaration, invoice, ps3665, exhibit
    file_path   TEXT,                -- relative to repo root
    case_ids    TEXT,                -- JSON array of case IDs this relates to
    filed_date  TEXT,                -- when filed/sent
    filed_with  TEXT,                -- court/agency/recipient entity_id
    status      TEXT,                -- drafted, filed, served, responded, denied
    notes       TEXT,
    created_at  TEXT DEFAULT (datetime('now'))
);

--------------------------------------------------------------
-- EVIDENCE: specific pieces of evidence (texts, video, docs)
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS evidence (
    id          TEXT PRIMARY KEY,    -- slug: 'ring-camera-sep2'
    title       TEXT NOT NULL,
    ev_type     TEXT NOT NULL,       -- video, photo, text-message, email, document, recording, public-record, financial, testimony
    source      TEXT,                -- where it came from
    file_path   TEXT,                -- if stored locally
    description TEXT,
    date        TEXT,                -- date of the evidence itself
    entity_ids  TEXT,                -- JSON array of entities involved
    case_ids    TEXT,                -- JSON array of cases it's relevant to
    authenticity TEXT,               -- how authenticated: 'Ring timestamp+geolocation', 'USPS tracking', 'Wayne ROD certified'
    notes       TEXT,
    created_at  TEXT DEFAULT (datetime('now'))
);

--------------------------------------------------------------
-- EXHIBITS: maps evidence/documents to specific hearings
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS exhibits (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    hearing_id  TEXT NOT NULL,       -- 'ppo-hearing-sep29', 'foc-oct7'
    tab         TEXT,                -- 'Tab 3A', 'Tab 4B'
    evidence_id TEXT REFERENCES evidence(id),
    document_id TEXT REFERENCES documents(id),
    description TEXT,                -- what this exhibit shows
    offered     INTEGER DEFAULT 0,  -- 1 if offered to court
    admitted    INTEGER DEFAULT 0,  -- 1 if admitted
    notes       TEXT
);

--------------------------------------------------------------
-- RELATIONSHIPS: entity-to-entity connections
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS relationships (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_a    TEXT NOT NULL REFERENCES entities(id),
    entity_b    TEXT NOT NULL REFERENCES entities(id),
    rel_type    TEXT NOT NULL,       -- family, employer, board-member, attorney, co-owner, campaign-payment, co-conspirator, judge-of
    description TEXT,
    source      TEXT,
    start_date  TEXT,
    end_date    TEXT,
    amount      REAL,               -- for financial relationships
    notes       TEXT
);

--------------------------------------------------------------
-- PROPERTIES: real property records
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS properties (
    id          TEXT PRIMARY KEY,    -- address slug: '1968-severn'
    address     TEXT NOT NULL,
    city        TEXT,
    state       TEXT DEFAULT 'MI',
    zip         TEXT,
    owner_ids   TEXT,                -- JSON array of entity IDs
    doc_numbers TEXT,                -- JSON array of ROD doc numbers
    purchase_price REAL,
    mortgage    REAL,
    notes       TEXT
);

--------------------------------------------------------------
-- SERVICE_LOG: tracking service attempts on each party
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS service_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id     TEXT REFERENCES cases(id),
    entity_id   TEXT REFERENCES entities(id),
    date        TEXT NOT NULL,
    method      TEXT,                -- certified, first-class, process-server, email, text, fax
    address     TEXT,
    tracking    TEXT,                -- USPS tracking number
    result      TEXT,                -- delivered, forged, returned, acknowledged, no-response
    ps3665      INTEGER DEFAULT 0,  -- 1 if on PS Form 3665
    notes       TEXT
);

--------------------------------------------------------------
-- AGENCY_REFERRALS: what went to which agency
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS agency_referrals (
    id          TEXT PRIMARY KEY,    -- 'fbi-sep22', 'oig-174517'
    agency_id   TEXT REFERENCES entities(id),
    date_sent   TEXT,
    case_number TEXT,                -- agency's case/reference number
    subject     TEXT,
    status      TEXT,                -- sent, acknowledged, active, closed
    response_date TEXT,
    response_notes TEXT,
    notes       TEXT
);

--------------------------------------------------------------
-- FOIA_REQUESTS: tracking FOIA submissions
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS foia_requests (
    id          TEXT PRIMARY KEY,
    agency_id   TEXT REFERENCES entities(id),
    date_sent   TEXT,
    due_date    TEXT,                -- 5 business days from sent
    subject     TEXT,
    status      TEXT,                -- sent, responded, denied, appealed, lawsuit-filed
    response_date TEXT,
    response_notes TEXT,
    file_path   TEXT,                -- path to response docs
    notes       TEXT
);

--------------------------------------------------------------
-- HEARINGS: all scheduled hearings
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hearings (
    id          TEXT PRIMARY KEY,    -- 'ppo-hearing-sep29'
    case_ids    TEXT,                -- JSON array
    date        TEXT NOT NULL,
    time        TEXT,
    judge_id    TEXT REFERENCES entities(id),
    courtroom   TEXT,
    court_address TEXT,
    hearing_type TEXT,               -- ppo, custody, default, motion, foc
    status      TEXT,                -- scheduled, completed, continued, cancelled
    outcome     TEXT,
    notes       TEXT
);

--------------------------------------------------------------
-- PROVENANCE: BLAKE3 integrity + mesh braiding
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS provenance (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    record_type TEXT NOT NULL,       -- entity, case, event, evidence, document, relationship
    record_id   TEXT NOT NULL,       -- the ID in the source table
    blake3      TEXT,                -- BLAKE3 hash of the serialized record
    braided_at  TEXT,                -- when this record was braided
    collection  TEXT,                -- evidence collection name (e.g. 'mde-foia-sep25')
    merkle_root TEXT,                -- collection merkle root if applicable
    source_gate TEXT DEFAULT 'northGate',  -- which gate produced this data
    verified_by TEXT,                -- which gate/process verified
    notes       TEXT,
    UNIQUE(record_type, record_id)
);

--------------------------------------------------------------
-- GRAPH_EXPORT: node/edge format for detroit.primals.eco
--------------------------------------------------------------
CREATE TABLE IF NOT EXISTS graph_nodes (
    id          TEXT PRIMARY KEY,    -- matches entity/case/property ID
    node_type   TEXT NOT NULL,       -- person, entity, case, event, property, agency, school, judge
    label       TEXT NOT NULL,       -- display name
    tier        INTEGER,            -- 1-4 (from detroit config)
    page        TEXT,                -- detroit.primals.eco page path
    data        TEXT                 -- JSON of extra attributes
);

CREATE TABLE IF NOT EXISTS graph_edges (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    source      TEXT NOT NULL,
    target      TEXT NOT NULL,
    edge_type   TEXT NOT NULL,       -- financial, family, employer, board-member, campaign-payment, party-to, filed-in, etc.
    epistemic   TEXT DEFAULT 'record', -- record, corroborated, inference, allegation
    note        TEXT,
    source_doc  TEXT,                -- provenance: what document proves this edge
    temporal    TEXT,                -- JSON: {start_date, end_date, discovered_date}
    amount      REAL,               -- for financial edges
    UNIQUE(source, target, edge_type)
);

--------------------------------------------------------------
-- VIEWS for common queries
--------------------------------------------------------------

-- All upcoming hearings with judge names
CREATE VIEW IF NOT EXISTS v_upcoming_hearings AS
SELECT h.id, h.date, h.time, h.hearing_type, h.courtroom,
       e.name as judge_name, h.case_ids, h.status
FROM hearings h
LEFT JOIN entities e ON h.judge_id = e.id
WHERE h.status IN ('scheduled', 'continued')
ORDER BY h.date, h.time;

-- Evidence relevant to a specific case
CREATE VIEW IF NOT EXISTS v_case_evidence AS
SELECT e.id, e.title, e.ev_type, e.date, e.source, e.description,
       e.case_ids
FROM evidence e
WHERE e.case_ids IS NOT NULL
ORDER BY e.date;

-- All service attempts by entity
CREATE VIEW IF NOT EXISTS v_service_by_entity AS
SELECT sl.date, e.name, sl.method, sl.address, sl.result, sl.notes,
       sl.case_id
FROM service_log sl
JOIN entities e ON sl.entity_id = e.id
ORDER BY sl.date DESC;

-- FOIA status dashboard
CREATE VIEW IF NOT EXISTS v_foia_status AS
SELECT f.id, e.name as agency, f.date_sent, f.due_date,
       f.status, f.response_date, f.subject
FROM foia_requests f
JOIN entities e ON f.agency_id = e.id
ORDER BY f.due_date;
