# TARGET TRIO — Entity Identity Hiding Behind Individual Privacy Infrastructure

**Principle:** "My identity is nobody's business" — TRUE for individuals.
But an entity is not an individual. When a 501(c)(4) spending $100K+ on elections
hides behind a privacy service designed for people, that's an entity
appropriating individual privacy to avoid public accountability.

**The trio:** Three categories of infrastructure that allow entities
to operate as if they were individuals with privacy rights.

---

## TARGET 1: DOMAINS BY PROXY — "Your Identity Is Nobody's Business But Ours"

### What It Is

Domains By Proxy (GoDaddy subsidiary, Tempe AZ) masks WHOIS registration
data so public databases show "Registration Private" instead of the entity
that actually controls the website. Designed for individuals who don't want
their home address in WHOIS. Used by entities that don't want the public
to know who runs their political websites.

### Every Instance Found

| Entity | Domain | Privacy Service | Confirmed Source |
|--------|--------|----------------|-----------------|
| **Our Neighborhoods First** | ourneighborhoodsfirst.com | Domains By Proxy | Deadline Detroit (LeDuff) |
| **Detroit Jobs First** | detroitjobsfirst.com | Domains By Proxy | Metro Times / Deadline Detroit |
| **RFFW LLC** | (no public website found) | Dykema itself as shield | MI SOS filing, addressed from Dykema office |
| **SDJ/Detroit Leaders** | (no website, lists Dykema phone) | Entity IS Dykema | IRS 990EZ phone: 517-374-9100 = Dykema Lansing |
| **FOIAworks** | foiaworks.com | GoDaddy WHOIS redaction | WHOIS (no Domains By Proxy but standard GDPR redaction via GoDaddy) |

### The Incorporation Agent Pattern

Beyond domain privacy, entities also hide behind incorporation agents:

| Entity | Registered Agent | What It Hides |
|--------|-----------------|---------------|
| Our Neighborhoods First | "The Corporation Company" (Ann Arbor) | Who actually controls the nonprofit |
| SDJ/Detroit Leaders | Filed through Dykema (Wilk/Moore) | That it's functionally a Dykema operation |
| Detroit Jobs First | Filed through Dykema (Wilk/Moore) | Same |
| RFFW LLC | Resident agent: CSC – Lawyers Incorporating Service | That it was a one-time $1M pass-through |
| Purpose Foundation | Brian Banks (self-filed) | Nothing — Banks is visible but his credentials aren't |

### Opsonization Tag

**What to coat these with:**
- WHOIS data (already published where available)
- IRS 990 filings (officer names, addresses, compensation)
- LARA entity filings (registered agents, officer changes)
- Campaign finance records (donors, expenditures)
- Deadline Detroit reporting (Neavling, LeDuff — already published)
- Motor City Muckraker reporting (already published)
- FCC filings (for broadcast advertising)

**The tag:** Each community organism sees a different angle:
- Transparency groups → "dark money hiding donors"
- Press → "Domains By Proxy: the tagline that tells the story"
- MMOP/Prop 2 advocates → "SDJ is a Dykema operation that doesn't even have its own phone number"
- 482Forward → "the nonprofit fighting community benefits was incorporated by the mayor's lawyer"

---

## TARGET 2: FOIAWORKS — The FOIA Honeypot

### What It Is

FOIAworks.com is a FOIA request platform that collects:
- **WHO** is investigating (user identity/account)
- **WHAT** they're investigating (request content)
- **WHERE** they're looking (target agency)
- **WHAT** they receive (responsive documents)

All with **no published privacy policy** (404 confirmed Oct 9, 2026).

Operated by Philip L. Ellison / Quagmire Solutions LLC from Hemlock, MI.
The same attorney who fabricated a witness, surveilled a journalist,
and whose client registered domains targeting a journalist's minor child.

### Infrastructure Mapped

| Component | Detail | Source |
|-----------|--------|--------|
| **Domain** | foiaworks.com | GoDaddy registrar |
| **Created** | August 4, 2025 | WHOIS |
| **Hosting** | GoDaddy shared (208.109.69.231) | DNS + rDNS |
| **Stack** | Apache + PHP 8.3.35 (custom app) | HTTP headers |
| **Admin** | cpanel.foiaworks.com (login page PUBLIC) | SSL cert SANs |
| **Email** | M365 tenant NETORGFT19358193 | DNS MX + TXT |
| **SPF** | MISCONFIGURED (authorizes GoDaddy, not M365) | DNS TXT |
| **Privacy** | 404 NOT FOUND | HTTP response |
| **Database** | 3,537 Michigan public bodies | sitemap.xml |
| **Targeting** | 11 persona pages (journalists, investigators, attorneys...) | sitemap.xml |
| **Mailing address** | 4522 W Higgins Lake Dr, Roscommon MI 48653 | OLC PLC |
| **Operator** | Quagmire Solutions LLC (LARA B0703X) | foiaworks.com/about |
| **Controller** | Philip L. Ellison (P69014) | All of the above |

### What FOIAworks Collects That Public Records Don't Protect

FOIA requests are themselves public records. But the PLATFORM collects
metadata that FOIA law doesn't address:

| Data Point | FOIA Law Says | FOIAworks Collects |
|-----------|---------------|-------------------|
| Request content | Public record | YES + account identity |
| Requester identity | Cannot be required by agency | YES (account creation) |
| IP address / device | Not addressed | YES (PHPSESSID on every visit) |
| Which agencies targeted | Public (filed requests) | YES (pre-filing browsing patterns) |
| Responsive documents | Public record | YES (uploaded/stored on platform) |
| Investigation patterns | Not addressed | YES (browsing + request history) |

### Opsonization Tag

**What to coat FOIAworks with:**
- Infrastructure scan (already published: barry.primals.eco)
- Ellison sanctions ($74,752.45 — PACER public record)
- AGC investigation (File No. 25-2363)
- Ghost witness fabrication (public court record)
- Journalist surveillance (server logs, public IP data)
- Domain registration targeting minor child (public WHOIS)
- LakeNet signal trace (public ARIN/MPSC data)

**Displacement strategy (already documented in FOIAWORKS_DISPLACEMENT_PLAN.md):**
1. SEO — outrank foiaworks.com with factual warning page
2. Liberate the public body database (it's all government data)
3. Surface alternatives (MuckRock, Clutch Justice generator, templates)
4. Rita publishes infrastructure story (her domain has authority)

**The tag for community organisms:**
- Journalists → "the FOIA platform has no privacy policy and is run by a sanctioned attorney"
- SPJ / MI Press Association → "your members' investigation targets are being collected"
- Attorneys → "MRPC 1.6 — does using this platform waive privilege?"
- Researchers → "your research agenda is visible to a single attorney with $74K in sanctions"
- FOIA frequent filers → "the platform tracks what you browse before you even file"

---

## TARGET 3: LAKENET — The ISP Hard Infrastructure

### What It Is

LakeNet LLC (AS11910) is the only broadband ISP headquartered in
Hemlock, Michigan (pop. ~1,500). It provides fiber/wireless internet
to ~500-1,000 subscribers in a ~5 square mile area. Its IP address
(162.247.150.54) has been captured in three independent evidence streams:

1. **Surveilling a journalist's website** (WordPress logs, Apr 29, 2026)
2. **Federal court filing** (PACER ECF No. 175-4)
3. **Domain registration chain** (same period as harassment domain batch)

Philip L. Ellison's law firm is in Hemlock. He is a LakeNet subscriber.

### Infrastructure Mapped

| Component | Detail | Source |
|-----------|--------|--------|
| **ASN** | AS11910 | ARIN |
| **HQ** | 16690 Gratiot Rd, Hemlock MI 48626 | MPSC registry |
| **Officers** | Chris Fabien (CTO), Keri Fabien (Ops), Rob Bresnahan (CFO) | FCC Form 499 |
| **IPv4 Range** | 162.247.144.0/21 + 158.51.68.0/22 = 4,096 IPs | ARIN |
| **Coverage** | Hemlock, Merrill, Marion Springs, St. Charles | lakenetfiber.com |
| **Fiber** | 100+ miles, FTTH | lakenetfiber.com |
| **Peering** | 123.NET (Southfield), DET-iX | PeeringDB |
| **Upstream** | Cogent (AS174), Hurricane Electric (AS6939), Daystarr (AS21527) | BGP tables |
| **CLEC License** | Permanent, statewide MI | MPSC Order, May 2021 |
| **ROBIN Grant** | 173 miles new fiber, Midland/Saginaw/Gratiot/Bay counties | Michigan LEO |
| **FRN** | 0021411152 | FCC |
| **FCC phone** | (989) 643-5819 | MPSC |

### The Quagmire → LakeNet Pipeline

Ellison's pre-law career (Quagmire Solutions, 2000-2007) served
"internet service companies" in the same geography. LakeNet formed
in 2010. Quagmire Solutions is still active (LARA B0703X) and
now operates FOIAworks.com. Three companies at the Quagmire
registered address (1111 S Orr Rd, Hemlock) — two unidentified.

### Why LakeNet Matters for Opsonization

LakeNet is not a target. LakeNet is infrastructure. But:

1. **Every LakeNet IP in evidence = Hemlock = 5 sq mi = functionally an address**
2. **In a town of 1,500 with one ISP, the suspect pool for any 162.247.x.x hit is extremely small**
3. **Multi-capture (3 independent hits) means persistent operational use from a fixed location**
4. **The Quagmire → LakeNet pipeline means the attorney has historical ISP infrastructure knowledge**

### Opsonization Tag

**What to coat the ISP trace with:**
- ARIN WHOIS (public — anyone can verify)
- MPSC registration (public — state regulatory record)
- PeeringDB (public — network topology)
- Certificate Transparency logs (public — SSL cert reveals infrastructure)
- Court filings (public — PACER documents reference the IP)
- Server logs (Rita's — document surveillance activity)

**The tag for community organisms:**
- Saginaw ISD board → "your board president's husband runs FOIAworks from this ISP"
- MPSC commissioners → "your CLEC licensee's infrastructure is in evidence in federal court"
- MiCOG → "the FOIA 'tool' runs on infrastructure connected to journalist surveillance"
- MI Press Association → "your members are being surveilled from a 5-square-mile town"

---

## THE TRIO AS SYSTEM — Entity Privacy Infrastructure Stack

```
LAYER 3: DOMAIN PRIVACY (Domains By Proxy / GoDaddy)
  └── Hides: WHO controls the website
  └── Used by: ONF, DJF, dark money vehicles
  └── Crack: WHOIS history, IRS 990s, campaign finance filings

LAYER 2: DATA INTERMEDIARY (FOIAworks)
  └── Hides: WHO is investigating WHAT
  └── Used by: No one yet (platform is new, Aug 2025)
  └── Crack: SEO displacement, alternative tools, infrastructure scan

LAYER 1: ISP HARD INFRASTRUCTURE (LakeNet AS11910)
  └── Hides: WHERE the operator physically sits
  └── Used by: Ellison (confirmed), associates (inferred)
  └── Crack: Multi-capture IP forensics, ARIN, MPSC, server logs
```

### The Principle

An individual has privacy rights. An entity has accountability obligations.

When entities use individual-grade privacy tools to avoid accountability:
- **Domains By Proxy** → entity hides behind individual privacy service
- **FOIAworks** → entity collects individual investigators' identities
- **LakeNet small-town ISP** → entity hides behind geographic obscurity

The opsonization response:
- **Tag with public data** so every community organism recognizes the entity
- **Displace with alternatives** so the honeypot catches nothing useful
- **Document the infrastructure** so the hiding itself becomes the story

### The Tagline They Chose

"Your identity is nobody's business but ours."

They're right about individuals.
They're wrong about entities.
And they know the difference.

---

## OPSONIZATION PRIORITY ORDER

| Priority | Target | Why First |
|----------|--------|-----------|
| **1** | FOIAworks | Active honeypot collecting investigator identities NOW. Displacement is urgent. No privacy policy = no legal cover for data collection. |
| **2** | Domains By Proxy dark money | Already well-documented by Deadline Detroit, Metro Times, Motor City Muckraker. Community organisms already primed. Need distribution. |
| **3** | LakeNet infrastructure | Already published on barry.primals.eco. Technical. Requires press translation for community organisms. Most effective when combined with FOIAworks story. |

### Cross-Tag Amplification

The three targets are most powerful when tagged TOGETHER:

> "The same attorney who hides his political clients' websites
> behind Domains By Proxy, and operates from an ISP so small
> that every IP address is functionally a return address, now
> runs a FOIA platform that collects the identities of everyone
> who investigates government misconduct — with no privacy policy."

That sentence contains zero opinion. It is entirely public record.
And it makes every community organism's enzymatic pathway activate
simultaneously.

---

*An entity is not an individual. That's the target trio.*
