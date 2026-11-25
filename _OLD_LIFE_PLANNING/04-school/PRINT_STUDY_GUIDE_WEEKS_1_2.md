# CompTIA Foundations — Weeks 1–2 Study Guide

DaSean Mitchell | DSDT College | 2026

INSTRUCTIONS: For each term, mark your level. Be honest — this isn't
a test. It's a map so Kevin knows where to focus.

    [X] = I can explain this to someone else
    [~] = I've heard of it / sort of know it
    [ ] = New to me

---

## 1. HARDWARE COMPONENTS

Every computer — phone, laptop, server, Raspberry Pi — has these parts.

| # | Term | What It Is | Level |
|---|------|-----------|-------|
| 1 | **CPU** (Central Processing Unit) | The brain. Executes instructions. Measured in GHz (speed) and cores (parallel work). | [ ] |
| 2 | **RAM** (Random Access Memory) | Short-term memory. Fast but gone when power is off. Measured in GB. | [ ] |
| 3 | **Storage** (SSD / HDD / NVMe) | Long-term memory. Keeps data when powered off. SSD = fast, no moving parts. HDD = spinning disk, cheaper. NVMe = fastest, plugs into motherboard directly. | [ ] |
| 4 | **Motherboard** | The backbone. Everything plugs into it. Has slots for CPU, RAM, storage, expansion cards. | [ ] |
| 5 | **PSU** (Power Supply Unit) | Converts wall power (AC) to the DC voltages the components need. Measured in watts. | [ ] |
| 6 | **GPU** (Graphics Processing Unit) | Processes visual output. Can be integrated (built into CPU) or discrete (separate card). | [ ] |
| 7 | **NIC** (Network Interface Card) | Connects the computer to a network. Can be wired (Ethernet) or wireless (Wi-Fi). | [ ] |
| 8 | **BIOS / UEFI** | Firmware that runs first when you power on. Checks hardware (POST), then hands off to the OS. UEFI is the modern version of BIOS. | [ ] |
| 9 | **POST** (Power-On Self-Test) | The hardware check that runs before the OS loads. Beep codes tell you what failed. | [ ] |
| 10 | **Heatsink / Fan** | Keeps the CPU cool. Without cooling, the CPU throttles or dies. | [ ] |
| 11 | **Form Factor** | Physical size/shape standard. ATX = full-size desktop. mATX = smaller. ITX = tiny. Laptops have proprietary layouts. | [ ] |
| 12 | **Peripheral** | Any external device: monitor, keyboard, mouse, printer, USB drive. | [ ] |

### Quick Check — Hardware

Can you answer these? Write your answers in the margin.

1. What happens if you pull the RAM out of a running computer?
2. What's the difference between SSD and HDD? Which is faster?
3. What does POST stand for, and when does it run?
4. If a computer won't display anything on screen, what component
   might be the problem? (Name at least two possibilities.)

---

## 2. DATA & NUMBER SYSTEMS

Computers think in electricity: on or off. Everything else is built
from that.

| # | Term | What It Is | Level |
|---|------|-----------|-------|
| 13 | **Binary** | Base-2 number system. Only digits 0 and 1. Each digit is a "bit." | [ ] |
| 14 | **Bit** | The smallest unit of data. A single 0 or 1. | [ ] |
| 15 | **Byte** | 8 bits. Can represent values 0–255. One character of text. | [ ] |
| 16 | **KB / MB / GB / TB** | Kilobyte = ~1,000 bytes. Megabyte = ~1 million. Gigabyte = ~1 billion. Terabyte = ~1 trillion. | [ ] |
| 17 | **Hexadecimal (Hex)** | Base-16 number system (0–9 then A–F). Used for MAC addresses, colors, memory addresses. FF in hex = 255 in decimal = 11111111 in binary. | [ ] |
| 18 | **ASCII** | A way to encode text as numbers. 'A' = 65. 'a' = 97. '0' = 48. | [ ] |
| 19 | **Boolean** | True or false. Yes or no. 1 or 0. The basis of all logic in computing. | [ ] |

### Quick Check — Data

1. How many bits in a byte?
2. Convert binary 1010 to decimal. (Hint: 8+0+2+0 = ?)
3. Is 1 GB bigger or smaller than 1 TB?
4. What number does hex "FF" represent in decimal?

---

## 3. OPERATING SYSTEMS

The software that manages hardware and runs your programs.

| # | Term | What It Is | Level |
|---|------|-----------|-------|
| 20 | **Operating System (OS)** | Software layer between hardware and user. Manages memory, files, processes, devices. | [ ] |
| 21 | **Windows** | Microsoft's OS. Most common on desktops/laptops. GUI-focused. Versions: 10, 11, Server. | [ ] |
| 22 | **Linux** | Open-source OS. Runs most servers, security tools, and cloud infrastructure. Many "distributions" (Ubuntu, Kali, CentOS). | [ ] |
| 23 | **macOS** | Apple's OS for Mac computers. Unix-based (similar to Linux under the hood). | [ ] |
| 24 | **CLI** (Command Line Interface) | Text-based interface. You type commands. More powerful than clicking. Essential for IT work. | [ ] |
| 25 | **GUI** (Graphical User Interface) | Visual interface with windows, icons, menus, buttons. What most people think of as "using a computer." | [ ] |
| 26 | **File System** | How the OS organizes data on storage. Windows: NTFS. Linux: ext4. macOS: APFS. | [ ] |
| 27 | **Process** | A running program. Each process has a PID (Process ID). You can list and kill processes. | [ ] |
| 28 | **Service / Daemon** | A program running in the background. A web server is a service. Daemons are Linux's version. | [ ] |
| 29 | **Driver** | Software that lets the OS talk to a specific piece of hardware. Wrong driver = device doesn't work. | [ ] |
| 30 | **Permissions** | Rules about who can read, write, or execute a file. Linux: rwx for owner/group/others. | [ ] |
| 31 | **Root / Administrator** | The highest-privilege account. Can do anything. Use carefully — mistakes here break everything. | [ ] |

### Quick Check — Operating Systems

1. Name three operating systems.
2. What's the difference between CLI and GUI?
3. What does "root" mean on a Linux system?
4. What happens if you delete a driver for your network card?

---

## 4. NETWORKING FUNDAMENTALS

How computers talk to each other.

| # | Term | What It Is | Level |
|---|------|-----------|-------|
| 32 | **Network** | Two or more devices connected to share data. Your home Wi-Fi is a network. The internet is a network of networks. | [ ] |
| 33 | **IP Address** | A device's address on a network. IPv4: four numbers 0–255 separated by dots (192.168.1.10). IPv6: longer hex format. | [ ] |
| 34 | **Subnet Mask** | Defines the boundary of a network. 255.255.255.0 means the first 3 octets are the network, the last is the device. | [ ] |
| 35 | **Default Gateway** | The router's IP address. Where your device sends traffic that isn't on the local network. | [ ] |
| 36 | **DNS** (Domain Name System) | Translates names to IP addresses. google.com → 142.250.80.46. Like a phone book for the internet. | [ ] |
| 37 | **DHCP** (Dynamic Host Configuration Protocol) | Automatically assigns IP addresses to devices when they join a network. The alternative is setting IPs manually (static). | [ ] |
| 38 | **MAC Address** | A device's physical hardware address. Burned into the NIC at the factory. 48 bits, shown in hex (AA:BB:CC:DD:EE:FF). | [ ] |
| 39 | **Router** | Connects different networks. Decides where to send packets. Operates at Layer 3 (Network). | [ ] |
| 40 | **Switch** | Connects devices within the same network. Forwards traffic based on MAC addresses. Layer 2 (Data Link). | [ ] |
| 41 | **Hub** | Old, dumb version of a switch. Sends everything to everyone. No intelligence. | [ ] |
| 42 | **Firewall** | Filters network traffic based on rules. Blocks or allows connections. Can be hardware or software. | [ ] |
| 43 | **Access Point (AP)** | Creates a wireless network. Lets Wi-Fi devices connect to the wired network. | [ ] |
| 44 | **LAN** (Local Area Network) | A network in one location (your house, one office). | [ ] |
| 45 | **WAN** (Wide Area Network) | A network spanning large distances. The internet is the biggest WAN. | [ ] |
| 46 | **VLAN** (Virtual LAN) | A logical subdivision of a network using a switch. Separates traffic without separate hardware. | [ ] |
| 47 | **Bandwidth** | How much data a connection can carry. Measured in Mbps or Gbps. Like the width of a pipe. | [ ] |
| 48 | **Latency** | How long it takes data to travel from A to B. Measured in milliseconds (ms). Like the length of a pipe. | [ ] |

### Quick Check — Networking

1. What does DNS do? Give an example.
2. What's the difference between a router and a switch?
3. Your computer's IP is 192.168.1.50, subnet mask 255.255.255.0.
   What's the network address? What's the broadcast address?
4. What does DHCP do, and what happens if it's down?
5. A device has IP 10.0.0.5 and needs to reach 8.8.8.8. Which
   device does it send the packet to first?

---

## 5. THE OSI MODEL (7 LAYERS)

The OSI model describes how data moves from an application to the
wire and back. Every networking and security concept maps to a layer.

| Layer | Name | What Happens Here | Key Protocols / Devices | Level |
|-------|------|------------------|------------------------|-------|
| 7 | **Application** | User interacts with software | HTTP, HTTPS, FTP, SMTP, DNS, SSH | [ ] |
| 6 | **Presentation** | Data formatting, encryption, compression | SSL/TLS, JPEG, ASCII, encryption | [ ] |
| 5 | **Session** | Manages connections between applications | NetBIOS, RPC, sessions | [ ] |
| 4 | **Transport** | Reliable delivery (TCP) or fast delivery (UDP) | TCP, UDP, port numbers | [ ] |
| 3 | **Network** | Routing between networks, IP addressing | IP, ICMP, routers | [ ] |
| 2 | **Data Link** | Frames, MAC addresses, local delivery | Ethernet, Wi-Fi, switches, MAC | [ ] |
| 1 | **Physical** | Electrical signals on the wire | Cables, hubs, connectors, signals | [ ] |

**Memory aid**: "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way" (1→7)
Or top-down: "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing" (7→1)

### Quick Check — OSI Model

1. A router operates at which layer?
2. A switch operates at which layer?
3. Which layer handles IP addresses?
4. Which layer handles MAC addresses?
5. TCP and UDP live at which layer?
6. You're browsing a website. Which layer is HTTP?

---

## 6. PROTOCOLS & PORTS

A protocol is a set of rules for communication. A port is a numbered
door on a device where a specific service listens.

| Port | Protocol | What It Does | Secure? | Level |
|------|----------|-------------|---------|-------|
| 20/21 | **FTP** | File transfer | No | [ ] |
| 22 | **SSH** | Secure remote terminal | Yes | [ ] |
| 23 | **Telnet** | Remote terminal (unencrypted) | No | [ ] |
| 25 | **SMTP** | Sends email | No (587 is secure) | [ ] |
| 53 | **DNS** | Name resolution | No | [ ] |
| 67/68 | **DHCP** | IP address assignment | No | [ ] |
| 80 | **HTTP** | Web browsing (unencrypted) | No | [ ] |
| 110 | **POP3** | Receives email (downloads) | No | [ ] |
| 143 | **IMAP** | Receives email (syncs) | No | [ ] |
| 443 | **HTTPS** | Web browsing (encrypted) | Yes | [ ] |
| 445 | **SMB** | File sharing (Windows) | Depends | [ ] |
| 3389 | **RDP** | Remote desktop (Windows) | Depends | [ ] |

### TCP vs UDP

| | **TCP** | **UDP** |
|---|---------|---------|
| Full name | Transmission Control Protocol | User Datagram Protocol |
| Reliable? | Yes — confirms delivery | No — fire and forget |
| Speed | Slower (overhead) | Faster (no handshake) |
| Used for | Web, email, file transfer | Streaming, DNS, gaming, VoIP |
| Analogy | Certified mail (signed for) | Throwing a letter out the window |

### Quick Check — Protocols & Ports

1. What port does HTTPS use?
2. What's the difference between FTP and SSH?
3. Why is Telnet considered insecure?
4. Name a protocol that uses UDP instead of TCP. Why?
5. You need to remotely manage a Linux server. Which protocol
   and port do you use?

---

## 7. SECURITY FUNDAMENTALS

The basics that every security concept builds on.

| # | Term | What It Is | Level |
|---|------|-----------|-------|
| 49 | **CIA Triad** | The three goals of security: **C**onfidentiality (only authorized people see it), **I**ntegrity (data isn't tampered with), **A**vailability (systems are up when needed). | [ ] |
| 50 | **Authentication** | Proving who you are. Password, fingerprint, smart card. "Are you who you claim to be?" | [ ] |
| 51 | **Authorization** | What you're allowed to do after authenticating. "You're logged in — can you access this file?" | [ ] |
| 52 | **Encryption** | Scrambling data so only authorized parties can read it. Uses a key to lock and unlock. | [ ] |
| 53 | **Plaintext** | Unencrypted, readable data. What you're trying to protect. | [ ] |
| 54 | **Ciphertext** | Encrypted data. Unreadable without the key. | [ ] |
| 55 | **Malware** | Malicious software. Umbrella term for viruses, worms, trojans, ransomware, spyware. | [ ] |
| 56 | **Virus** | Malware that attaches to a file and spreads when the file is opened. Needs a host. | [ ] |
| 57 | **Worm** | Malware that spreads on its own across networks. No host file needed. | [ ] |
| 58 | **Trojan** | Malware disguised as legitimate software. Looks safe, isn't. | [ ] |
| 59 | **Ransomware** | Malware that encrypts your files and demands payment for the key. | [ ] |
| 60 | **Phishing** | Fake email/message designed to trick you into giving up credentials or clicking a malicious link. | [ ] |
| 61 | **Social Engineering** | Manipulating people (not systems) to bypass security. Phishing is one type. | [ ] |
| 62 | **Firewall** | Filters traffic by rules. Can be network-based (hardware) or host-based (software on the device). | [ ] |
| 63 | **IDS** (Intrusion Detection System) | Monitors traffic and alerts when it sees something suspicious. Passive — watches, doesn't block. | [ ] |
| 64 | **IPS** (Intrusion Prevention System) | Like IDS but active — can block malicious traffic automatically. | [ ] |
| 65 | **VPN** (Virtual Private Network) | Creates an encrypted tunnel over the internet. Makes public networks act like private ones. | [ ] |
| 66 | **MFA** (Multi-Factor Authentication) | Requires 2+ types of proof: something you know (password), something you have (phone), something you are (fingerprint). | [ ] |
| 67 | **Patch** | A software update that fixes bugs or security vulnerabilities. Unpatched systems are targets. | [ ] |
| 68 | **Zero-Day** | A vulnerability with no patch available yet. The vendor has had "zero days" to fix it. | [ ] |

### Quick Check — Security

1. What are the three parts of the CIA triad?
2. What's the difference between authentication and authorization?
3. What's the difference between a virus and a worm?
4. Someone calls pretending to be IT support and asks for your
   password. What type of attack is this?
5. What does a VPN do? Why would you use one?
6. What are the three factors in multi-factor authentication?

---

## 8. TROUBLESHOOTING METHODOLOGY

CompTIA tests a specific 7-step process. Memorize it.

| Step | Action | What It Means |
|------|--------|--------------|
| 1 | **Identify the problem** | Ask questions. Gather symptoms. What changed? When did it start? |
| 2 | **Establish a theory** | Based on symptoms, what's most likely wrong? Start simple. |
| 3 | **Test the theory** | Try a fix based on your theory. If it doesn't work, go back to step 2. |
| 4 | **Establish a plan of action** | Once you know the cause, plan the full fix. Consider impact. |
| 5 | **Implement the solution** | Execute the fix. Make the change. |
| 6 | **Verify functionality** | Confirm the fix worked AND didn't break anything else. |
| 7 | **Document findings** | Write it down. What was the problem? What fixed it? For next time. |

### Quick Check — Troubleshooting

A user says "I can't get on the internet." Walk through the 7 steps.
Write a one-sentence answer for each step in the margin.

---

## SCORING YOUR SELF-ASSESSMENT

Count your marks across all sections:

| Mark | Meaning | Count |
|------|---------|-------|
| [X] | I can explain it | ____ / 68 |
| [~] | Heard of it | ____ / 68 |
| [ ] | New to me | ____ / 68 |

**If mostly [X]**: You're ahead. Focus on the Quick Check questions —
can you explain it out loud, not just recognize the term?

**If mostly [~]**: You know the landscape but need depth. Watch the
Crash Course CS or Professor Messer videos for your weak areas.

**If mostly [ ]**: Normal for someone new to IT. This guide IS the
map. Kevin will walk you through each section. No shame — the goal
is to turn every [ ] into [X] over the next few weeks.

### Priority Areas (by cert)

| If studying for... | Focus hardest on sections... |
|--------------------|-----------------------------|
| A+ | 1 (Hardware), 3 (OS), 8 (Troubleshooting) |
| Network+ | 4 (Networking), 5 (OSI), 6 (Protocols & Ports) |
| Security+ | 7 (Security), 6 (Protocols), 5 (OSI) |

---

## WHAT TO DO THIS WEEK

1. Fill out every [ ] box in this guide. Be honest.
2. Give the guide back to Kevin so he can see your gaps.
3. For every [ ] (new to me) — watch the matching Crash Course CS
   episode or Professor Messer video.
4. For every [~] (sort of know) — try to explain it out loud to
   Kevin. If you can't, it's really a [ ].
5. Next week: Kevin re-tests you verbally on the [ ] items.

---

*Print date: ___________*
*DaSean's signature: ___________*
*Kevin's review date: ___________*

