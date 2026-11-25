# Graph Schema — Case Intelligence System

Reusable directed graph model for any litigation. Nodes are typed entities;
edges are typed relationships with temporal properties. Every node and edge
carries a `first_known` timestamp — what we knew and when we knew it.

---

## NODE TYPES

| type | description | required fields | optional fields |
|------|-------------|-----------------|-----------------|
| `person` | Individual (party, witness, judge, enabler) | id, name, role | aliases, dob, addresses[], criminal_history[], credentials[] |
| `entity` | Organization, LLC, school, PAC | id, name, type | ein, registered_agent, address, status |
| `case` | Court case | id, case_no, court, caption, judge | type, filed_date, status, next_event |
| `motion` | Filed motion or document | id, title, case_id, filed_date | status, outcome, superseded_by |
| `event` | Dated occurrence (assault, service, hearing) | id, date, description | location, witnesses[], evidence[] |
| `evidence` | Document, photo, recording, record | id, type, description | source, exhibit_id, chain_of_custody |
| `agency` | Government agency receiving complaints | id, name | complaint_no, filed_date, status |
| `property` | Real estate parcel | id, address | owner, deed_date, liber_page, assessed_value |

## EDGE TYPES

| type | from → to | temporal | description |
|------|-----------|----------|-------------|
| `filed_in` | motion → case | filed_date | Motion filed in case |
| `party_to` | person → case | start_date | Person is a party. Edge data: role (plaintiff, defendant, petitioner, respondent, witness, expert, auth_rep), pro_se (bool), appears_in_person (bool) |
| `employed_by` | person → entity | start_date, end_date | Employment relationship |
| `controls` | person → entity | start_date | Ownership or control |
| `related_to` | case → case | discovered_date | Cases share parties or facts |
| `triggered_by` | event → event | — | Causal chain |
| `evidence_of` | evidence → event | collected_date | Evidence documents an event |
| `filed_with` | motion → agency | filed_date | Complaint filed with agency |
| `served_on` | motion → person | service_date, method | Service of process |
| `evasion_of` | event → motion | date | Service evasion event |
| `supersedes` | motion → motion | date | New version replaces old |
| `owns` | person → property | deed_date | Property ownership |
| `resides_at` | person → property | start_date | Residence |
| `convicted_of` | person → event | date, case_no | Criminal conviction |
| `connected_to` | person → person | discovered_date, type | Relationship (family, business, criminal, veteran_brotherhood) |
| `authorized_rep_for` | person → person | start_date, scope | Non-attorney authorized representative. Edge data: scope (filing, witness, expert), cases[], NOT_ATTORNEY=true |
| `assigned_to` | judge → case | assignment_date | Judge assigned to case |

## TEMPORAL LAYER

Every node and edge has:

```
first_known: date       # When WE first learned this fact
confirmed: date | null  # When verified (court record, FOIA, public record)
source: string          # How we know (e.g., "LEIN", "PACER", "ROD", "witness")
confidence: high|medium|low
```

This lets us reconstruct the **intelligence timeline** — what we knew at each filing,
what a reasonable person could have discovered, and what was concealed.

## GRAPH QUERIES (conceptual)

```
# All cases involving Banks
MATCH (p:person {name: "Banks"})-[:party_to]->(c:case) RETURN c

# Timeline of evasion events
MATCH (e:event)-[:evasion_of]->(m:motion) RETURN e ORDER BY e.date

# Who connects Banks to the Smiths?
MATCH path = (banks:person {id: "BANKS"})-[*1..3]-(smith:person {id: "SHAYLA"})
RETURN path

# What did we know before filing CIV-BANKS?
MATCH (n)-[r]-() WHERE r.first_known <= "2026-09-01" RETURN n, r

# Constitutional deprivation timeline
MATCH (c:case {id: "CUSTODY"})-[:filed_in]-(m:motion)
WHERE m.status = "pending" RETURN m, duration("2026-09-22" - m.filed_date) as days_waiting
```

## DESIGN PRINCIPLES

1. **Nodes are facts. Edges are relationships. Time is a property.**
2. **Every fact has provenance** — source, confidence, first_known date
3. **The graph is append-only** — new facts add nodes/edges, never delete
4. **Supersession, not mutation** — new motions supersede old ones via edges
5. **Reusable** — swap out the data, keep the schema. Works for any case.
6. **Visualization-ready** — DAG layout for court hierarchy, timeline for events
