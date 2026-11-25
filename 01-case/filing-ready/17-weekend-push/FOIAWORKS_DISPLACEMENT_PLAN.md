# FOIAworks Displacement — Signal Outside, Data Liberated

## CONCEPT

FOIAworks has two assets:
1. A database of 3,537 Michigan public bodies
2. A FOIA submission pipeline

Both are built from PUBLIC government data. We can replicate
both — better, free, with zero data collection — and put them
where people find them BEFORE they find FOIAworks.

When the signal is better outside the honeypot, the honeypot
catches nothing useful.

---

## MOVE 1: SEO DISPLACEMENT

### The Warning Page Already Exists

barry.primals.eco/investigate/foiaworks-warning/
"FOIAworks: Do Not Use. Here's Why. Here Are Alternatives."

### Make It Rank

The page needs to outrank foiaworks.com for these searches:
- "foiaworks"
- "foiaworks.com"
- "michigan foia software"
- "foia request michigan"
- "foiaworks review"
- "foiaworks privacy"

**How:**
- Title tag: "FOIAworks Review — No Privacy Policy, $74K Sanctions"
- Cross-link from every barry.primals.eco evidence page
- Cross-link from clutch.primals.eco
- Rita links from clutchjustice.com articles (her domain has authority)
- Include the exact queries people will search in the content
- Structured data (FAQ schema) for Google rich snippets

Google already indexes barry.primals.eco. The warning page just
needs internal link weight and keyword targeting. When someone
Googles "foiaworks" they should see the warning on page 1.

---

## MOVE 2: LIBERATE THE PUBLIC BODY DATABASE

### What FOIAworks Has

3,537 Michigan public body pages. Each one maps:
- Agency name
- Type (city, township, county, school district, etc.)
- FOIA coordinator info
- Contact details

### Where That Data Actually Comes From

ALL of it is government directory data:

| Source | What It Has | URL |
|--------|-------------|-----|
| **Michigan.gov** | State agency directory | michigan.gov/agencies |
| **MPSC ITSP** | Registered telecom providers | mpsc.my.site.com/itsp |
| **MDE** | School districts + charter schools | mischooldata.org |
| **LARA** | Business entities | mibusinessregistry.lara.state.mi.us |
| **Secretary of State** | County clerks | michigan.gov/sos |
| **Census** | Municipal boundaries / names | census.gov |
| **Michigan Township Assoc** | Township directory | michigantownships.org |
| **Michigan Municipal League** | City/village directory | mml.org |
| **MTA** | County directory | micounties.org |

### The Liberation Plan

Build a CLEAN public body directory:
- Open source (public GitHub repo)
- Static site (no server, no database, no sessions)
- Zero data collection (no accounts, no tracking, no cookies)
- Machine-readable (JSON/CSV download)
- Updated from government sources

**Format:** A simple static page per agency type:
```
/michigan-foia/cities/
/michigan-foia/townships/
/michigan-foia/counties/
/michigan-foia/school-districts/
/michigan-foia/state-agencies/
```

Each page: agency name, FOIA coordinator, contact info, link to
the actual government website. No login. No platform. No pipeline.
Just the data.

**Host it on:** barry.primals.eco or a new dedicated subdomain.
Or clutchjustice.com (Rita's domain, higher authority).

### Why This Kills FOIAworks

If the same data is available for free, with better privacy, on
a site that ranks higher, then FOIAworks has no value proposition.
Nobody needs to create an account. Nobody needs to pay $4.95-$69.95.
Nobody needs to give Ellison their identity and investigation targets.

The data was always public. We organized it. Without the honeypot.

---

## MOVE 3: ALTERNATIVE FOIA TOOLS

### Already Documented

barry.primals.eco/investigate/foiaworks-warning/ lists:
- Clutch Justice FOIA Generator (client-side, no data stored)
- MuckRock (nonprofit, published privacy policy)
- Write your own (templates provided)
- Your own attorney (privilege protects communications)

### Add to the Arsenal

| Tool | What It Does | Privacy |
|------|-------------|---------|
| **Clutch Justice FOIA Generator** | Client-side letter generator | Zero server collection |
| **barry.primals.eco FOIA Toolkit** | Templates + Hemlock-specific requests | Static pages, no tracking |
| **Public body directory** (new) | Agency contacts, free download | No accounts, no tracking |
| **MuckRock** | Full FOIA platform | 501(c)(3), published policy |
| **FOIA Machine** (if active) | Open source FOIA tool | Published policy |

Every alternative we surface = one fewer person walking into
the FOIAworks honeypot.

---

## MOVE 4: COORDINATION WITH RITA

### Her Side
- Clutch Justice publishes Ellison investigation coverage
- She has the lived experience (SLAPP target, harassment victim)
- Her bylines carry credibility with Michigan press
- clutchjustice.com has domain authority for Michigan legal searches
- She links to barry.primals.eco evidence pages
- **Her next story: Ellison infrastructure scan + FOIAworks**

### Our Side
- eco.primal@pm.me sends "found you" pairs
- barry.primals.eco publishes evidence and analysis pages
- detroit.primals.eco publishes Detroit investigation
- No personal identity on our publications

### What They See
- Clutch Justice articles (Rita's name, her credibility)
- barry.primals.eco analysis (ecoPrimal, no name)
- "Found you" emails (eco.primal@pm.me, no name)
- Cross-links between the sites

### What They KNOW
- Rita and ecoPrimal are aligned
- That's it. That's all the info they have.

### What They DON'T Know
- Who ecoPrimal is
- Where the analysis is produced
- How many people are involved
- What we know that isn't published yet
- Which agencies we've contacted
- When the next wave comes

The relationship between Rita and ecoPrimal is visible
but opaque. They can see the alignment but not the structure.
Curiosity is the admission price.

---

## TIMELINE

### This Week
- [x] FOIAworks infrastructure scan published
- [x] LakeNet signal trace published
- [ ] Opsonization emails staged (8 agencies)
- [ ] Round 2 "found you" pairs staged (6 pairs)
- [ ] Rita briefed on infrastructure scan findings

### Next Week (Post-Weekend Push)
- [ ] Opsonization emails sent simultaneously
- [ ] Round 2 pairs sent (Detroit actors)
- [ ] Rita publishes FOIAworks/infrastructure story
- [ ] SEO displacement targeting begins
- [ ] Public body directory data compilation starts

### Ongoing
- [ ] Passive monitoring (DNS, certs, sitemap, Wayback)
- [ ] Public body directory build-out
- [ ] Additional FOIA guide pages
- [ ] Press follow-ups as agencies respond

---

## THE POINT

FOIAworks is shitty quality on shitty hosting with shitty security
run by a shitty person. We don't need to attack it. We just need
to be better, be first in search results, and make its data freely
available without the honeypot.

The data is public. We liberate it.
The tools are simple. We publish them.
The warning is factual. We rank it.
The agencies see him. We tagged him.
Rita reports. We notify.

They know we're aligned. Good.
That's all they know. Also good.
