# DaSean Mitchell — Active Study Guide

**Status**: In class at DSDT (started ~Sep 2026)
**Course**: CompTIA certification track (confirm which cert is current)
**School Lab**: Hack The Box Enterprise (Academy modules, Dedicated Labs, Pwnbox)
**Home Station**: Swiftgate (dedicated computer at [REDACTED_ADDR_2])
**Mentor**: Kevin Mok (hardware, networking, mesh lab)

---

## CURRENT CERT — CONFIRM WITH DASEAN

DaSean: which CompTIA exam are you studying for right now?

| If He Says... | Exam Code | This Guide Section |
|---------------|-----------|-------------------|
| A+ | 220-1201 (Core 1) + 220-1202 (Core 2) | Section A below |
| Network+ | N10-009 | Section B below |
| Security+ | SY0-701 | Section C below |
| CySA+ | CS0-004 | Section D below |

---

## SECTION A: CompTIA A+ (220-1201 / 220-1202)

Two separate exams. Most programs do Core 1 first, then Core 2.

### Core 1 (220-1201) — Hardware & Networking

| Domain | Weight | Key Topics |
|--------|--------|-----------|
| Hardware | 25% | Motherboards, CPUs, RAM, storage (SSD/NVMe/SATA), PSUs, GPUs, cooling, form factors |
| Hardware & Network Troubleshooting | 28% | 7-step methodology, POST codes, BSOD, boot failures, cable testing, network connectivity |
| Networking | 23% | TCP/IP, ports (top 30), DNS, DHCP, VLANs, wireless standards, cable types, firewalls |
| Mobile Devices | 13% | Laptop components, mobile OS config, accessories, connectivity, troubleshooting |
| Virtualization & Cloud | 11% | Hypervisors (Type 1/2), VMs, cloud models (IaaS/PaaS/SaaS), containers |

### Core 2 (220-1202) — OS & Security

| Domain | Weight | Key Topics |
|--------|--------|-----------|
| Operating Systems | 28% | Windows (Task Manager, CMD, services), Linux (CLI, permissions), macOS basics, mobile OS |
| Security | 28% | Malware types, encryption, MFA, firewalls, social engineering, wireless security, physical security |
| Software Troubleshooting | 23% | OS issues, app crashes, browser problems, mobile device issues |
| Operational Procedures | 21% | Documentation, change management, backup/recovery, safety, communication, scripting basics |

### A+ Study Plan (8 weeks if taken alongside DSDT class)

| Week | Focus | At Home (Swiftgate) | At School (HTB) |
|------|-------|--------------------|-----------------|
| 1–2 | Core 1: Hardware + Mobile | Open Swiftgate, name components. Open Kevin's desktops. Compare form factors. | HTB Academy: Windows/Linux Fundamentals modules |
| 3–4 | Core 1: Networking + Cloud + Troubleshooting | Wireshark on the mesh. Trace a ping. Map IPs. | HTB: Networking modules, Introduction to Networking |
| 5 | **Take Core 1 exam** | Practice tests — drill until 85%+ | Review weak domains |
| 6–7 | Core 2: OS + Security | Linux CLI on Swiftgate. Harden a system. Set up fail2ban. | HTB: Linux Privilege Escalation, Web Security basics |
| 8 | Core 2: Software + Ops + Mock | Full practice exam on Swiftgate | Final review |

### A+ Free Resources

| Resource | What | Link |
|----------|------|------|
| Professor Messer A+ | Free video course (Core 1 + Core 2) | professormesser.com |
| CareerEmployer A+ Guide | Free study guide + quizzes | careeremployer.com/test-prep/study-guides/comptia-a-study-guide |
| ExamCompass | Free practice tests by topic | examcompass.com |
| Exam Objectives (on USB) | Official blueprint — print and check off | `06_CompTIA_A+_Core1_220-1201_Exam_Objectives.pdf` |

---

## SECTION B: CompTIA Network+ (N10-009)

See `DSDT_CLASS_PREP.md` for the full breakdown. Summary:

| Domain | Weight |
|--------|--------|
| Networking Concepts | 23% |
| Network Implementation | 20% |
| Network Operations | 19% |
| Network Security | 14% |
| Network Troubleshooting | 24% |

**Kevin's mesh IS the lab.** Map it, trace packets, break things, fix them.

---

## SECTION C: CompTIA Security+ (SY0-701)

| Domain | Weight |
|--------|--------|
| General Security Concepts | 12% |
| Threats, Vulnerabilities & Mitigations | 22% |
| Security Architecture | 18% |
| Security Operations | 28% |
| Security Program Management & Oversight | 20% |

**Free course**: Professor Messer SY0-701 (121 videos, 15 hours, free on YouTube)

---

## SECTION D: CompTIA CySA+ (CS0-004)

See `DSDT_CLASS_PREP.md` for the full breakdown. This is the capstone.

---

## HACK THE BOX ENTERPRISE — HOW TO USE IT

DaSean has Enterprise access through DSDT. This is a massive advantage.
Here's how to get the most out of it:

### What HTB Enterprise Gives You

| Feature | What It Is | How DaSean Uses It |
|---------|-----------|-------------------|
| **Academy Modules** | Structured courses (theory + labs) | Follow the paths assigned by DSDT. Complete every module. |
| **Academy Paths** | Curated module sequences by topic | Check if there's an A+/Net+/Sec+ aligned path |
| **Dedicated Labs** | Isolated machines to hack | Practice after completing related modules |
| **Pwnbox** | Browser-based Kali Linux — no setup | Use this when Swiftgate isn't available |
| **HTB Coach** | AI tutor inside modules | Ask it questions when stuck. Don't skip it. |
| **MITRE ATT&CK Mapping** | Each module shows which techniques it covers | Track your technique coverage over time |

### HTB Study Strategy

1. **Before class**: Preview the module topic on HTB. Read the theory sections.
2. **During class**: Follow the instructor. Take notes on what differs from HTB.
3. **After class**: Complete the HTB module exercises. Do the interactive labs.
4. **Weekend**: Attempt a Dedicated Lab machine related to the week's topic.

### Key HTB Academy Modules (Likely Relevant)

| Module | Cert Alignment | Priority |
|--------|---------------|----------|
| Windows Fundamentals | A+ Core 2 | High |
| Linux Fundamentals | A+ Core 2, Sec+, CySA+ | Critical |
| Introduction to Networking | Net+, A+ Core 1 | High |
| Web Requests | Sec+, CySA+ | Medium |
| Introduction to Active Directory | Sec+, CySA+ | Medium |
| Incident Handling Process | CySA+ | Later |
| Network Enumeration with Nmap | CySA+, PenTest | Later |

---

## HOME LAB — THE HACKBOX ON THE MESH

Yes, you can absolutely put a hackable target on the mesh. Here's the
architecture and the critical safety rules.

### Network Topology

```
INTERNET
    |
[Kevin's Router/Firewall]
    |
    +-- MESH NETWORK (production) --+-- Southgate (Kevin's work machines)
    |                               +-- Bluegate (kid stuff)
    |                               +-- Swiftgate (DaSean's workstation)
    |
    +-- ISOLATED LAB VLAN/SUBNET ---+-- HackPi (Raspberry Pi — vulnerable targets)
                                    |   Docker containers: DVWA, Juice Shop, etc.
                                    |   IP: 10.99.99.x/24 (example)
                                    |
                                    +-- Swiftgate connects to BOTH networks
                                        (production for internet/study,
                                         lab VLAN for attacking HackPi)
```

### CRITICAL SAFETY RULES

1. **HackPi NEVER touches the internet.** Its containers are deliberately
   broken. If they're on the open network, anyone can exploit them.

2. **Isolate the lab subnet.** Either:
   - Use a separate physical NIC / USB ethernet adapter on Swiftgate
     plugged into HackPi directly (simplest)
   - Create a VLAN on Kevin's managed switch (cleanest)
   - Use Docker's `internal: true` network mode on HackPi (software-only)

3. **Swiftgate is dual-homed**: one connection to the mesh (internet,
   HTB, study), one connection to the lab subnet (attacking HackPi).

4. **Never bridge the lab to production.** If the Pi can ping the router,
   it can reach the internet. That's a vulnerability pointing outward.

### Option 1: Raspberry Pi as HackPi (Recommended)

**Hardware**: Raspberry Pi 4 (4GB+) or Pi 5. Kevin likely has one.

**Setup**:

```bash
# On the Raspberry Pi (Raspberry Pi OS Lite 64-bit)

# 1. Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# 2. Install Portainer for easy container management
docker volume create portainer_data
docker run -d -p 9000:9000 --name portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# 3. Create an isolated Docker network
docker network create --internal hacknet

# 4. Deploy DVWA (Damn Vulnerable Web App)
docker run -d --name dvwa --network hacknet \
  -p 8080:80 vulnerables/web-dvwa

# 5. Deploy OWASP Juice Shop
docker run -d --name juiceshop --network hacknet \
  -p 3000:3000 bkimminich/juice-shop

# 6. Deploy WebGoat (OWASP training app)
docker run -d --name webgoat --network hacknet \
  -p 8081:8080 webgoat/webgoat
```

**Access from Swiftgate**: Connect Swiftgate to HackPi via ethernet
cable (direct connection or through a dedicated switch port). Set
static IPs on both ends (e.g., Pi = 10.99.99.1, Swiftgate = 10.99.99.2).
Then DaSean browses to `http://10.99.99.1:8080` for DVWA, etc.

### Option 2: All-in-One Instant Lab (Pi-optimized)

**github.com/swayanbasu04/Instant_lab** — A complete SOC homelab for
Raspberry Pi with Docker. Includes:
- DVWA
- Juice Shop
- Kali Linux (in a container)
- Metasploit
- Parrot Security
- Pre-installed pen testing tools (nmap, nikto, sqlmap, gobuster)

One repo, clone and run. Built specifically for Pi + ARM64.

### Option 3: VoltMart Pentest Lab (Advanced)

**github.com/Baymax-armed/voltmart-pentest-lab** — Five realistic
vulnerable apps (store, bank, finance, SaaS + AI/LLM lab). Covers
280+ vulnerabilities across OWASP Top 10 AND the LLM Top 10.
Includes an offline AI assistant (no API key needed). Runs on Docker.

This is more advanced — save for after DaSean finishes A+/Net+ and
is into Security+/CySA+ territory.

### What DaSean Practices on HackPi

| Exercise | Tool | What He Learns | Cert Alignment |
|----------|------|---------------|---------------|
| Port scan HackPi | `nmap` from Swiftgate | Service discovery, port mapping | Net+, CySA+ |
| SQL injection on DVWA | Browser + Burp Suite | Input validation flaws, OWASP Top 10 | Sec+, CySA+ |
| XSS on Juice Shop | Browser | Client-side attacks, output encoding | Sec+, CySA+ |
| Brute force SSH on Pi | `hydra` from Swiftgate | Password security, account lockout | Sec+ |
| Vulnerability scan | OpenVAS/Greenbone | Assessment output analysis, CVSS scoring | CySA+ |
| Capture traffic | Wireshark on Swiftgate | Packet analysis during attacks | Net+, CySA+ |
| Write incident report | Text editor | Documentation, communication | CySA+ Domain 4 |

---

## DAILY / WEEKLY STUDY RHYTHM

### School Days (Mon–Wed in Detroit)

| When | What | Where |
|------|------|-------|
| Before class | Review yesterday's HTB module notes | Phone/tablet on transit |
| During class | Attend, take notes, ask questions | DSDT |
| After class | Complete HTB module exercises | Pwnbox or Swiftgate when home |
| Evening | 30 min practice questions on ExamCompass | Swiftgate or phone |

### Home Days (Thu–Sun in Lansing)

| When | What | Where |
|------|------|-------|
| Morning | 1–2 LPTHW exercises (if still in progress) | Swiftgate terminal |
| Midday | Uber driving / parenting | — |
| Evening (1 hr) | Professor Messer videos + practice questions | Swiftgate |
| Saturday (2 hrs) | HackPi lab session — attack, document, report | Swiftgate → HackPi |
| Sunday | Light review — flashcards, weak-area drill | Phone app or Swiftgate |

---

## PORTS, PROTOCOLS & COMMANDS TO MEMORIZE

These come up on EVERY CompTIA exam. DaSean needs these cold.

### Must-Know Ports

| Port | Protocol | Service |
|------|----------|---------|
| 20/21 | TCP | FTP (data/control) |
| 22 | TCP | SSH |
| 23 | TCP | Telnet (insecure) |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (server/client) |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 3389 | TCP | RDP |
| 389 | TCP | LDAP |
| 636 | TCP | LDAPS |
| 161/162 | UDP | SNMP |
| 587 | TCP | SMTP (submission) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 1433 | TCP | MSSQL |
| 3306 | TCP | MySQL |
| 5060 | TCP/UDP | SIP |
| 514 | UDP | Syslog |
| 49152–65535 | — | Ephemeral/dynamic |

**Drill**: flashcards, or have Kevin quiz him randomly. "Port 443?"
"HTTPS." "Port 22?" "SSH." Until it's instant.

### Must-Know Linux Commands

| Command | What It Does |
|---------|-------------|
| `pwd` | Print working directory |
| `ls -la` | List all files with permissions |
| `cd` | Change directory |
| `cat` / `less` | View file contents |
| `grep` | Search text in files |
| `find` | Search for files |
| `chmod` / `chown` | Change permissions / ownership |
| `ps aux` | List running processes |
| `top` / `htop` | Live process monitor |
| `kill` / `killall` | Terminate processes |
| `ifconfig` / `ip addr` | Show network interfaces |
| `ping` | Test connectivity |
| `traceroute` | Trace packet path |
| `netstat -tulnp` / `ss -tulnp` | Show listening ports |
| `nmap` | Port scanner |
| `apt update && apt upgrade` | Update packages |
| `systemctl start/stop/status` | Manage services |
| `journalctl` | View system logs |
| `tail -f /var/log/syslog` | Follow log in real time |
| `df -h` | Disk space |
| `free -h` | Memory usage |

### Must-Know Windows Commands

| Command | What It Does |
|---------|-------------|
| `ipconfig /all` | Network configuration |
| `ping` | Test connectivity |
| `tracert` | Trace route |
| `nslookup` | DNS query |
| `netstat -an` | Active connections |
| `sfc /scannow` | System file checker |
| `chkdsk` | Disk check |
| `gpupdate /force` | Force group policy update |
| `tasklist` / `taskkill` | Process management |
| `msconfig` | Boot configuration |
| `eventvwr` | Event viewer |
| `devmgmt.msc` | Device manager |
| `diskmgmt.msc` | Disk management |

---

## STUDY RESOURCES SUMMARY

### Free Courses

| Resource | Covers | Link |
|----------|--------|------|
| Professor Messer (YouTube) | A+, Net+, Sec+ (full free courses) | professormesser.com |
| HTB Academy (via DSDT Enterprise) | All certs + hands-on labs | Through DSDT login |
| Khan Academy CS | Fundamentals, Python | khanacademy.org/computing |
| Crash Course CS | First principles (41 episodes) | YouTube playlist |

### Practice Tests

| Resource | Coverage |
|----------|----------|
| ExamCompass | A+, Net+, Sec+, CySA+ — free, no signup |
| CareerEmployer | A+, Net+, CySA+ — free study guides + quizzes |
| CompTIA official sample questions | All certs — from comptia.org |
| Professor Messer study groups | Monthly live Q&A on YouTube |

### Hands-On Labs

| Resource | What |
|----------|------|
| HTB Enterprise (school) | Academy modules + Dedicated Labs + Pwnbox |
| HackPi (home mesh) | DVWA, Juice Shop, WebGoat — self-hosted on Pi |
| TryHackMe (free tier) | Guided rooms, browser-based |
| Killercoda | Browser-based Linux playground |
| OverTheWire: Bandit | Learn Linux by playing a wargame |

### Books (on USB + Kevin's shelf)

| Book | What It Teaches |
|------|----------------|
| Learn Python the Hard Way (Zed Shaw) | Typing, syntax, CLI, debugging |
| CompTIA ITF+ Official Study Guide | IT fundamentals ebook (on USB) |
| Exam objectives PDFs (all certs) | Official blueprints (on USB) |

---

## MESH LAB NAME REGISTRY

| Name | Device | Location | Role |
|------|--------|----------|------|
| **Southgate** | Kevin's work machines | Kevin's basement | Development, AI, EcoPrimals |
| **Bluegate** | Kid-friendly space | [REDACTED_ADDR_2] (upstairs) | Family, homework |
| **Swiftgate** | DaSean's study computer | [REDACTED_ADDR_2] (dedicated) | DSDT coursework, HTB, study |
| **Tasknode** | Intel NUC, 16GB DDR3, 250GB SSD | Wherever it's plugged in | Ephemeral lab — hacklab, SIEM, scanner, experiments. See `TASKNODE_SETUP.md` |

---

## NEXT STEPS

- [ ] Confirm with DaSean: which CompTIA cert are you on right now?
- [ ] Kevin: set up HackPi (Pi 4/5 + Docker + DVWA + Juice Shop)
- [ ] Connect HackPi to Swiftgate via ethernet (isolated, no internet)
- [ ] DaSean: `nmap -sV 10.99.99.1` as first HackPi exercise
- [ ] Print the ports table above — tape it to the wall next to Swiftgate
- [ ] Bookmark Professor Messer playlist for whichever cert is current
- [ ] DaSean: show Kevin your HTB Academy dashboard — what modules are assigned?

---

*Last updated: July 31, 2026*
*Prepared by: Kevin Mok*

