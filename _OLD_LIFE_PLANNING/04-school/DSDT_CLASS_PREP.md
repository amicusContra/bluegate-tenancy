# DSDT VET TEC 2.0 — Class Prep & Study Plan

**Student**: DaSean Eddie Mitchell
**Program**: Technology Professional 6 — DSDT College, Detroit, MI
**Start Date**: September 14, 2026 (orientation completed July 16, 2026)
**Status**: MODULE 1 INCOMPLETE — see note below
**Format**: Mon–Wed in-person, Detroit campus (distance learning also approved)
**Funding**: VA VET TEC 2.0 — tuition covered, BAH $2,361/mo during enrollment
**Total Hours**: 240 clock hours (core curriculum)
**Home Station**: Swiftgate (dedicated computer at [REDACTED_ADDR_2])
**See also**: `STUDY_GUIDE.md` for active study plan + home lab setup

---

## MODULE 1 STATUS — August 19, 2026

**Result**: Did not pass Module 1 (Network+).
**Cause**: DaSean started a week late. DSDT promised an extension to
compensate. The extension was not honored. He was held to the same
deadline as students who started on time. This is not a failure of
ability — it is an institutional failure to deliver on a commitment.

**Reframe — this is actually good:**

1. **Zero cost**: VET TEC covered everything. No financial loss.
2. **Free knowledge**: Every class he attended was free instruction.
   He now has a foundation in networking concepts he didn't have before.
3. **Prep for real college**: DSDT was always a bootcamp, not a degree
   program. The real play is LCC (Lansing Community College) for an
   associate's degree in Cybersecurity — NSA/DHS designated program,
   4 miles from home, GI Bill eligible.
4. **Continuing to attend**: Showing up to remaining classes is free
   knowledge with no downside. The material carries over.
5. **Pushback opportunity**: The broken extension promise is documentable.
   Kevin will follow up with DSDT administration.

**Next step**: LCC spring semester 2027 — Associate of Applied Science
in Cybersecurity (Program 1832). See `LEARNING_PATH.md` for details.

**For court**: DaSean enrolled in a VA-funded technology program,
attended classes, commuted 3 hours round trip to keep his daughters
in a stable home, and is now transitioning to a degree program at
an NSA-designated institution 4 miles from his house. The DSDT module
result is irrelevant — the trajectory is what matters.

---

## PROGRAM STRUCTURE

The Tech Pro 6 program is sequential — each cert builds on the last:

| Phase | Certification | Exam Code | Questions | Time | Pass Score | Exam Fee |
|-------|--------------|-----------|-----------|------|------------|----------|
| 1 | **CompTIA Network+** | N10-009 | 90 max | 90 min | 720/900 | $369 |
| 2 | **CompTIA Security+** | SY0-701 | 90 max | 90 min | 750/900 | $404 |
| 3 | **CompTIA CySA+** | CS0-004 (V4) | 85 max | 165 min | 750/900 | $404 |

**Critical note**: CySA+ V3 (CS0-003) retired June 23, 2026. DaSean will sit
for V4 (CS0-004), which adds AI security concepts, ZTNA, SASE, and SBOM.
Any study materials should target V4 / CS0-004 objectives.

VET TEC covers exam vouchers. Confirm with DSDT whether retake vouchers
are included if a first attempt doesn't pass.

---

## THE 8-WEEK HEAD START (July 17 – September 14)

DaSean has exactly 8 weeks before class begins. This is the recommended
study window for Network+. If he arrives on Day 1 already Network+-ready,
the entire program pace becomes manageable and he's ahead of every
classmate who walks in cold.

**Goal**: Walk into DSDT on September 14 able to pass Network+ within
the first 2–3 weeks of class.

### Week-by-Week Network+ Pre-Study

| Week | Dates | Focus | Kevin's Mesh Lab |
|------|-------|-------|-----------------|
| 1 | Jul 17–23 | OSI model, TCP/IP stack, common ports & protocols | Walk the mesh: identify each device, its role, which OSI layer it operates at |
| 2 | Jul 24–30 | IPv4/IPv6 addressing, subnetting (CIDR /24 → /30) | Map Kevin's subnet layout, identify address ranges, practice subnetting by hand |
| 3 | Jul 31–Aug 6 | Cabling, connectors, switching, VLANs, STP | Trace physical cables in the mesh, identify cable types, look at switch configs |
| 4 | Aug 7–13 | Routing fundamentals (static, dynamic, BGP, OSPF, NAT) | Examine the mesh router config, trace a packet from Bluegate to Southgate |
| 5 | Aug 14–20 | Wireless standards, WAN tech, SD-WAN, cloud networking | Map the wireless topology between houses, examine AP settings |
| 6 | Aug 21–27 | Network security — zero trust, hardening, common attacks | Run Wireshark on the mesh, identify traffic patterns, discuss threat models |
| 7 | Aug 28–Sep 3 | Troubleshooting methodology, common issues, diagnostic tools | Break things on purpose — Kevin introduces faults, DaSean troubleshoots |
| 8 | Sep 4–13 | Full practice exams, drill weak areas, target 80%+ | Timed practice tests, review missed questions, final lab walkthrough |

### Daily Study Routine (Suggested)

- **Morning (before Uber)**: 30 min — watch 2–3 Professor Messer videos
- **Evening (after kids' bedtime)**: 45 min — practice questions + flashcards
- **Weekends (1 session)**: 2 hours — hands-on lab time on Kevin's mesh

Total: ~8–10 hours/week. Sustainable alongside Uber and parenting.

---

## THE THREE CERTIFICATIONS — WHAT THEY COVER

### Phase 1: CompTIA Network+ (N10-009)

The foundation. Networking is the language everything else speaks.

| Domain | Weight | What It Covers |
|--------|--------|---------------|
| Networking Concepts | 23% | OSI model, TCP/IP, ports (top 30), protocols, IPv4/IPv6, subnetting |
| Network Implementation | 20% | Routing (static/dynamic/BGP/OSPF), switching, VLANs, wireless, physical install |
| Network Operations | 19% | Documentation, monitoring (SNMP, flow, packet capture), DHCP, DNS, disaster recovery |
| Network Security | 14% | Encryption, zero trust, firewalls, IDS/IPS, authentication, geofencing |
| Network Troubleshooting | 24% | 7-step methodology, tools (ping, tracert, nslookup, Wireshark), common failures |

**Troubleshooting + Concepts = 47% of the exam.** Lead with these.

**Army parallel**: DaSean already knows radio nets, COMSEC, frequency
management, and multi-channel comms from RTO duty. Networking is the
civilian version of what he did with SINCGARS and Harris radios. The
concepts map directly — channels = frequencies, encryption = COMSEC,
routing = relay plans, troubleshooting = when the net goes down in the field.

### Phase 2: CompTIA Security+ (SY0-701)

Builds on Network+. This is where the defensive mindset kicks in.

| Domain | Weight | What It Covers |
|--------|--------|---------------|
| General Security Concepts | 12% | CIA triad, zero trust, threat actors, social engineering |
| Threats, Vulnerabilities & Mitigations | 22% | Malware types, attack vectors, hardening techniques, mitigation strategies |
| Security Architecture | 18% | Firewalls, IDS/IPS, VPNs, cloud security, infrastructure models |
| Security Operations | 28% | Monitoring, alerting, incident response, digital forensics, automation |
| Security Program Management | 20% | Risk management, compliance (NIST, HIPAA, PCI-DSS), governance, auditing |

**Security Operations is 28%.** This is the SOC analyst skill set — exactly
what CySA+ deepens.

**Professor Messer has a complete free video course** (121 videos, 15+ hours):
https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/

### Phase 3: CompTIA CySA+ (CS0-004 — V4, launched June 23, 2026)

The capstone. This is the analyst cert — hands-on threat detection
and incident response. This is the job.

| Domain | Weight | What It Covers |
|--------|--------|---------------|
| Security Operations | 34% | Architecture, logging, SIEM, EDR, threat intel, threat hunting, AI in SOC |
| Vulnerability Management | 26% | Scanning, assessment output, CVSS/EPSS prioritization, mitigation controls |
| Incident Response & Management | 24% | MITRE ATT&CK, Cyber Kill Chain, IR lifecycle, triage, evidence handling |
| Reporting & Communication | 16% | Documentation, post-incident reviews, stakeholder communication, KPIs |

**New in V4** (not in older study materials):
- AI use cases, risks, and governance in security operations
- Zero Trust Network Access (ZTNA)
- Secure Access Service Edge (SASE)
- Software Bill of Materials (SBOM)
- Exploit Prediction Scoring System (EPSS)
- Cloud-native security operations
- SOAR and XDR automation

---

## WHAT KEVIN CAN TEACH (EcoPrimals Mesh)

Kevin's multi-house mesh network is a live lab. Most students learn
networking on simulators. DaSean learns on real hardware with real traffic.

### Network+ Skills — Hands-On with the Mesh

| Skill | How to Learn It on Kevin's Mesh |
|-------|-------------------------------|
| OSI model layers | Walk each device: NIC (Layer 2), router (Layer 3), application (Layer 7). Identify which layer each device operates at. |
| IP addressing & subnetting | Map every device's IP, subnet mask, default gateway. Calculate the network/broadcast addresses by hand. |
| Switching & VLANs | If the mesh uses managed switches, examine VLAN configs. If not, discuss why/when you'd segment. |
| Routing | Trace a packet from Bluegate ([REDACTED_ADDR_2]) to Southgate (Kevin's basement). Identify each hop, NAT translation, gateway. |
| Wireless topology | Map the APs between houses — channels, SSID, encryption type, signal overlap. |
| DNS & DHCP | Check DHCP leases, DNS resolution, local DNS entries. Set up a Pi-hole or local DNS server as a project. |
| Wireshark | Capture live traffic on the mesh. Filter by protocol. Find a DNS query. Find an HTTP request. Read packet headers. |
| Cable types | Identify Cat5e/Cat6, fiber if present, coax, patch panels. Know the difference by sight and spec. |
| Troubleshooting | Kevin intentionally misconfigures something — wrong subnet mask, DNS pointing nowhere, DHCP pool exhausted. DaSean finds and fixes it. |

### Security+ Skills — Defensive Posture

| Skill | How to Learn It |
|-------|----------------|
| Firewall rules | Examine the mesh firewall config. What's allowed? What's blocked? Add a rule, test it. |
| Encryption in transit | Check which services use TLS. Find one that doesn't. Discuss the risk. |
| Authentication | Set up SSH key-based auth on a Linux box. Disable password auth. Explain why. |
| Hardening | Take a fresh Linux install, harden it: disable unnecessary services, configure firewall, set up fail2ban. |
| Monitoring & logging | Set up rsyslog or journald centralization. Send logs from one machine to another. |

### CySA+ Skills — The SOC Lab

| Skill | How to Build It |
|-------|----------------|
| SIEM deployment | Install Wazuh (free, open-source) on an Ubuntu VM. It acts as SIEM + XDR. Configure agents on mesh devices. |
| Log analysis | Ingest Windows Event Logs, Sysmon telemetry, and Linux auth logs into the SIEM. Write queries to find anomalies. |
| Threat hunting | Use the MITRE ATT&CK Navigator to map techniques. Hunt for indicators in the SIEM data. |
| Incident response | Simulate an attack (Kali VM → mesh device). Detect it in the SIEM. Contain it. Write the report. |
| Vulnerability scanning | Run OpenVAS/Greenbone against mesh devices. Read the output. Prioritize by CVSS. Remediate. |

---

## FREE STUDY RESOURCES

### Video Courses

| Resource | Cert | Cost | Link |
|----------|------|------|------|
| **Professor Messer N10-009** | Network+ | Free | professormesser.com (full course, indexed to objectives) |
| **Professor Messer SY0-701** | Security+ | Free | professormesser.com/security-plus/sy0-701/sy0-701-video/ |
| **Cybrary CySA+** | CySA+ | Free tier | cybrary.it/course/comptia-cybersecurity-analyst-cysa-cs0-003 |
| **YouTube CySA+ playlists** | CySA+ | Free | Search "CySA+ CS0-004 full course" — multiple available |
| **Coursera CySA+ (Pearson)** | CySA+ | Free audit | coursera.org (4-unit course, aligned to objectives) |

### Practice Tests & Quizzes

| Resource | Coverage | Cost | Link |
|----------|----------|------|------|
| **ExamCompass** | Net+, Sec+, CySA+ | Free | examcompass.com (topic-specific quizzes, no signup) |
| **CareerEmployer Study Guides** | Net+, CySA+ | Free | careeremployer.com/test-prep/study-guides/ |
| **CySA+ Log Analysis Tool** | CySA+ | Free | cysa-exam-prep.web.app (log analysis, CVSS calculator, timed quizzes) |
| **Professor Messer Study Groups** | Sec+ | Free | Monthly live Q&A on YouTube + Discord community |
| **SubnettingPractice.com** | Net+ | Free | Drill subnetting until it's automatic |

### Hands-On Labs (Free)

| Resource | What It Does | Link |
|----------|-------------|------|
| **Killercoda Ubuntu Playground** | Browser-based Linux labs, no install | killercoda.com/playgrounds/scenario/ubuntu |
| **CySA+ GitHub Labs (30 labs)** | Step-by-step labs aligned to CySA+ objectives | github.com/tertiarycourses/TGS-2024049211-CySAPlus |
| **Cisco Packet Tracer** | Network simulator (routing, switching, VLANs) | netacad.com (free with Cisco account) |
| **GNS3** | Advanced network emulator | gns3.com (free, runs real router images) |
| **Wazuh** | Free open-source SIEM/XDR — the SOC home lab | wazuh.com (install on any Linux VM) |
| **Splunk Free** | SIEM with 500MB/day ingest limit | splunk.com (free tier, enough for home lab) |
| **DVWA** | Deliberately vulnerable web app for attack practice | github.com/digininja/DVWA |
| **TryHackMe** | Guided cybersecurity rooms, browser-based | tryhackme.com (free tier available) |

### Official Exam Objectives (Download These First)

| Cert | Where to Get Objectives |
|------|------------------------|
| Network+ N10-009 | comptia.org → Network+ page → "Download Exam Objectives" |
| Security+ SY0-701 | comptia.org → Security+ page → "Download Exam Objectives" |
| CySA+ CS0-004 | comptia.org → CySA+ V4 page → "Download Exam Objectives" |

Print these. Every bullet point is testable. Check items off as mastered.

---

## WHAT DASEAN ALREADY KNOWS (Military Translation)

DaSean's 3+ years as an RTO in the 25th Infantry Division means he already
has instincts that most Network+ students spend weeks developing:

| Military Skill (RTO/11B) | IT Equivalent | Cert Domain |
|--------------------------|--------------|-------------|
| SINCGARS radio net management | Network topology & addressing | Net+ |
| COMSEC procedures & fill devices | Encryption, key management, PKI | Sec+ |
| Frequency assignment & deconfliction | Channel planning, interference mitigation | Net+ |
| SITREPs & SALUTE reports | Incident reporting, log documentation | CySA+ |
| Multi-net monitoring (simultaneous) | SIEM dashboard monitoring, alert triage | CySA+ |
| Field troubleshooting (net down) | 7-step troubleshooting methodology | Net+ |
| Equipment accountability ($1M+) | Asset management, inventory control | Net+ Ops |
| Operating under pressure/stress | SOC incident response under time pressure | CySA+ |
| Chain of command communications | Escalation procedures, stakeholder reporting | CySA+ |
| CLS (Combat Lifesaver) | Incident response triage (prioritize, stabilize) | CySA+ |

**Framing for DaSean**: You already did this job in a combat environment
with radios. Now you're doing it in a data center with servers. The
principles are identical. The vocabulary changes.

---

## CAREER PATHWAY AFTER CERTIFICATION

With all three certs (Network+, Security+, CySA+), DaSean qualifies for:

| Role | Typical Salary (MI) | DoD Clearance Eligible |
|------|---------------------|----------------------|
| SOC Analyst (Tier 1) | $50K–$65K | Yes (Security+ = DoD 8570 baseline) |
| SOC Analyst (Tier 2) | $65K–$85K | Yes |
| Cybersecurity Analyst | $60K–$80K | Yes |
| Vulnerability Analyst | $65K–$85K | Yes |
| Network Security Engineer | $70K–$90K | Yes |
| IT Security Specialist | $55K–$75K | Yes |
| Incident Response Analyst | $65K–$85K | Yes |

**Security+ alone satisfies DoD 8570 IAT Level II** — this opens every
federal contractor and military base IT position. With veteran preference,
DaSean is competitive for cleared positions immediately.

**Michigan-specific employers hiring CySA+ holders**:
- General Motors (Detroit/Warren)
- Ford Motor Company (Dearborn)
- DTE Energy (Detroit)
- Blue Cross Blue Shield of Michigan
- Quicken Loans / Rocket Companies (Detroit)
- State of Michigan (Lansing — walking distance)
- Consumers Energy (Lansing/Jackson)
- Federal contractors: Booz Allen, SAIC, Leidos (all hire vets)

---

## ECOPRIMALS MESH — LAB PROJECTS

These are concrete projects DaSean can build on Kevin's mesh that
double as both learning exercises and portfolio items:

### Project 1: Network Map (Week 1–2)
Build a complete network diagram of the EcoPrimals mesh.
- Physical topology: devices, cables, locations (Bluegate, Southgate)
- Logical topology: IP addresses, subnets, VLANs, routing
- Tools: pen/paper first, then draw.io or Packet Tracer
- **Portfolio value**: Shows documentation skills (Net+ Domain 3)

### Project 2: Pi-hole DNS Server (Week 3)
Deploy a Pi-hole on a Raspberry Pi or spare machine.
- Configure as the mesh's DNS server
- Block ads and tracking at the network level
- Monitor DNS query logs — see what devices are calling home
- **Portfolio value**: DNS management + security monitoring

### Project 3: Wireshark Traffic Analysis (Week 4–5)
Capture and analyze live traffic on the mesh.
- Identify protocols: HTTP, HTTPS, DNS, DHCP, ARP
- Find unencrypted traffic. Discuss the risk.
- Write a 1-page findings report
- **Portfolio value**: Packet analysis skills (Net+ & CySA+)

### Project 4: Linux Hardening (Week 5–6)
Take a fresh Ubuntu install on a mesh machine and harden it.
- Disable root SSH login, enforce key-based auth
- Configure UFW firewall rules
- Install and configure fail2ban
- Set up unattended security updates
- **Portfolio value**: System hardening (Sec+ & CySA+)

### Project 5: Wazuh SIEM Deployment (Week 6–8)
Deploy a Wazuh manager + agents across the mesh.
- Install Wazuh server on Ubuntu
- Deploy agents on Windows and Linux machines
- Configure log collection rules
- Build a dashboard for security events
- **Portfolio value**: SIEM deployment + SOC operations (CySA+)

### Project 6: Simulated Attack & Response (Post-class)
Set up Kali Linux VM. Attack a test machine (DVWA). Detect in Wazuh.
- Run Nmap scan → detect in SIEM
- Attempt brute force → detect + block with fail2ban
- Write incident response report following NIST SP 800-61
- **Portfolio value**: Full IR cycle, directly exam-relevant

---

## SCHEDULE INTEGRATION (Updated Aug 19 — Post-DSDT transition)

### Current (Aug – Dec 2026): Continue DSDT classes + self-study

| Day | DaSean's Activity | Study Opportunity |
|-----|-------------------|-------------------|
| Monday | DSDT class (Detroit) — free knowledge | In-class learning (no cost to attend) |
| Tuesday | DSDT class (Detroit) — free knowledge | In-class learning |
| Wednesday | DSDT class (Detroit) — free knowledge | In-class learning, evening review |
| Thursday | Lansing — Uber + parenting | Morning: 30 min videos. Evening: Kevin lab |
| Friday | Lansing — Uber + parenting | Morning: 30 min videos. Evening: practice Qs |
| Saturday | Parenting + flex | 2-hour lab session on Kevin's mesh |
| Sunday | Parenting + flex | Light review, flashcards during downtime |

### Spring 2027: LCC (no Detroit commute)

| Day | DaSean's Activity | Study Opportunity |
|-----|-------------------|-------------------|
| Mon–Fri | LCC classes (4 miles from home) + Uber | Class + cert study in parallel |
| Evenings | Parenting + Kevin lab sessions | Hands-on mesh work, SIEM projects |
| Weekends | Parenting + extended lab time | Portfolio projects, exam prep |

**The commute disappears.** 3 hours/day of driving becomes 3 hours/day
of studying, parenting, or earning. That's 9 hours/week he gets back.

---

## COURT RELEVANCE (Updated Aug 19 — Stronger After Transition)

This education trajectory matters for the custody case:

1. **Proactive enrollment**: DaSean enrolled in VET TEC *before* Shayla
   filed. This isn't reactive — it's planned growth.

2. **Resilience**: When DSDT failed to honor its commitment, DaSean
   didn't give up or blame anyone — he immediately pivoted to a better
   path. That's the character the court evaluates.

3. **Career pathway**: Associate's degree + three industry certs →
   $50K–$85K career floor, with bachelor's transfer path to $70K–$120K.

4. **Local investment**: LCC is 4 miles from home. No more 3-hour
   Detroit commute. More time for parenting, more time for earning.
   The education now happens IN the children's community.

5. **NSA designation**: LCC's cybersecurity program is nationally
   recognized by NSA/DHS — only ~300 schools in the country. DaSean
   is pursuing excellence, not just checking a box.

6. **Mentor access**: Kevin's professional tech background + home lab
   = built-in tutoring and career mentorship. This is part of the
   established custodial environment's advantage. No DSDT instructor
   lives next door.

7. **Self-improvement under pressure**: Despite custody litigation,
   a module setback, and active parenting, DaSean is pursuing education,
   employment, and stability simultaneously. He adapted. He didn't stop.

---

## IMMEDIATE ACTION ITEMS

- [ ] Download all three exam objectives PDFs (Network+, Security+, CySA+)
- [ ] Start Professor Messer Network+ N10-009 video playlist (Week 1)
- [ ] Create ExamCompass account — begin topic quizzes after each video module
- [ ] Map Kevin's mesh network on paper (Project 1 — physical topology)
- [ ] Practice subnetting daily at SubnettingPractice.com (5 min/day)
- [ ] Set up a study folder on the mesh computer DaSean will use
- [ ] Confirm with DSDT: will class use CS0-004 or CS0-003 materials?
- [ ] Confirm with DSDT: are exam vouchers and retake vouchers included?
- [ ] Register for Professor Messer's Discord community

---

*Last updated: July 17, 2026*
*Prepared by: Kevin Mok*

