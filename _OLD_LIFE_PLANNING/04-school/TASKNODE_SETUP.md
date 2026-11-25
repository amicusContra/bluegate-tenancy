# Task Node — Ephemeral Lab Box

A NUC (or any x86 box) that can be wiped, reimaged, and redeployed
to any gate on the mesh in under 15 minutes.

**Hardware**: Intel NUC, 16GB DDR3, 250GB SSD, dead CMOS (irrelevant)
**OS**: Ubuntu Server 24.04 LTS (headless)
**Role**: Whatever it's told to be. Hacklab, SIEM, test target, dev box.

---

## CONCEPT

```
                REIMAGE USB (stays with NUC)
                    |
                    v
    +--[NUC: Task Node]--+
    |  Ubuntu Server      |
    |  Docker             |    <-- cat6 to any gate
    |  SSH (key auth)     |
    |  DHCP (auto-IP)     |
    +---------------------+
              |
    +---------+---------+---------+
    |         |         |         |
 Swiftgate  Southgate  Bluegate  (any future gate)
  DaSean's   Kevin's    house
  study      work       network

```

The NUC has no identity. It's a blank box that:
1. Boots from SSD → runs whatever was last deployed
2. Boots from USB → wipes SSD, fresh OS + Docker, ready in 15 min
3. Gets its role from a Docker Compose file pulled after boot

USB present = factory reset. USB absent = normal boot.

---

## THE REIMAGE USB

One USB stick. Plug it in, power on, walk away. When it's done, the
NUC has a clean Ubuntu Server + Docker + SSH, ready for any role.

### Build the USB on Swiftgate (one time)

**Step 1: Download Ubuntu Server 24.04 LTS ISO**

```bash
# On Swiftgate (Linux) or download via browser on Windows
# ~2.5GB download
wget https://releases.ubuntu.com/24.04/ubuntu-24.04-live-server-amd64.iso
```

**Step 2: Generate an SSH key pair (if you don't have one)**

```bash
ssh-keygen -t ed25519 -C "kevin@mesh" -f ~/.ssh/tasknode_key
# This creates:
#   ~/.ssh/tasknode_key      (private - stays on your machines)
#   ~/.ssh/tasknode_key.pub  (public - goes on the NUC)
```

Copy the public key content — you'll paste it into the autoinstall
config below.

**Step 3: Create the autoinstall config**

Save this as `user-data` on the USB alongside the ISO. Replace
`YOUR_SSH_PUBLIC_KEY_HERE` with the contents of `tasknode_key.pub`.

```yaml
#cloud-config
autoinstall:
  version: 1
  locale: en_US.UTF-8
  keyboard:
    layout: us
  identity:
    hostname: tasknode
    username: ops
    # password hash for "changeme" (change on first login)
    password: "[withheld]"
  ssh:
    install-server: true
    authorized-keys:
      - YOUR_SSH_PUBLIC_KEY_HERE
    allow-pw: false
  storage:
    layout:
      name: direct
  packages:
    - docker.io
    - docker-compose-v2
    - net-tools
    - curl
    - htop
    - git
  late-commands:
    - curtin in-target -- systemctl enable docker
    - curtin in-target -- usermod -aG docker ops
  user-data:
    disable_root: true
    package_update: true
    package_upgrade: true
```

**Step 4: Build the USB**

On Linux/WSL:
```bash
# Write ISO to USB (replace /dev/sdX with your USB device)
sudo dd if=ubuntu-24.04-live-server-amd64.iso of=/dev/sdX bs=4M status=progress

# Mount the USB, add the autoinstall directory
# (exact method depends on USB partition layout after dd)
# The autoinstall file goes in a specific location on the USB
# See Ubuntu autoinstall docs for partition layout
```

On Windows, use **Ventoy** — it's simpler:
1. Install Ventoy on the USB stick (ventoy.net)
2. Copy the Ubuntu ISO onto the USB's main partition
3. Create a folder `ventoy` on the USB
4. Place the `user-data` file inside `ventoy/`
5. Ventoy auto-detects the autoinstall config

**Step 5: Test it**

Plug USB into NUC. Power on. If BIOS defaults to USB boot (likely
with dead CMOS), it starts automatically. If not, tap F10/F12 for
boot menu on startup — one-time selection.

Walk away. Come back in 10–15 minutes. NUC is ready.

---

## AFTER REIMAGE — FIRST CONNECT

The NUC is on DHCP. Find it from whatever gate it's plugged into:

```bash
# From Swiftgate (or whatever gate the NUC is cat6'd to)

# Option 1: If connected directly via cat6 (no router between)
# Set a static IP on Swiftgate's second NIC or USB ethernet adapter
# e.g., Swiftgate = 10.99.99.1, NUC will get link-local or you
# can set NUC static in autoinstall config

# Option 2: If both on the mesh (NUC plugged into a switch)
# Scan the local network to find it
nmap -sn 192.168.1.0/24 | grep -B2 "tasknode"
# or
arp -a

# Connect
ssh -i ~/.ssh/tasknode_key ops@<nuc-ip>
```

Once in, you're root-capable via `sudo` and Docker is ready.

---

## ROLE DEPLOYMENT — DOCKER COMPOSE FILES

The NUC's job is defined by which compose file you pull onto it.
Keep these on Swiftgate (or in a git repo on the mesh) and SCP
them over after a fresh image.

### Role: Hacklab (DaSean's practice targets)

Save as `hacklab.yml`:

```yaml
services:
  dvwa:
    image: vulnerables/web-dvwa
    ports:
      - "8080:80"
    restart: unless-stopped

  juiceshop:
    image: bkimminich/juice-shop
    ports:
      - "3000:3000"
    restart: unless-stopped

  webgoat:
    image: webgoat/webgoat
    ports:
      - "8081:8080"
    restart: unless-stopped

  webwolf:
    image: webgoat/webwolf
    ports:
      - "9090:9090"
    restart: unless-stopped

networks:
  default:
    driver: bridge
    internal: true
```

Deploy:
```bash
scp -i ~/.ssh/tasknode_key hacklab.yml ops@<nuc-ip>:~/
ssh -i ~/.ssh/tasknode_key ops@<nuc-ip> "docker compose -f hacklab.yml up -d"
```

DaSean attacks from Swiftgate: `http://<nuc-ip>:8080` (DVWA),
`:3000` (Juice Shop), `:8081` (WebGoat).

### Role: SIEM Lab (defensive practice)

Save as `siem.yml`:

```yaml
services:
  wazuh-manager:
    image: wazuh/wazuh-manager:4.9.2
    ports:
      - "1514:1514/udp"
      - "1515:1515"
      - "55000:55000"
    environment:
      - WAZUH_MANAGER_ENROLLMENT=yes
    volumes:
      - wazuh_data:/var/ossec/data
    restart: unless-stopped

  wazuh-dashboard:
    image: wazuh/wazuh-dashboard:4.9.2
    ports:
      - "5601:5601"
    depends_on:
      - wazuh-manager
    restart: unless-stopped

volumes:
  wazuh_data:
```

Deploy same way. DaSean installs a Wazuh agent on Swiftgate that
reports to the NUC's SIEM. Then he attacks the hacklab and watches
the alerts appear in the dashboard.

### Role: Network Scanner

```yaml
services:
  openvas:
    image: greenbone/community-edition
    ports:
      - "9392:9392"
    volumes:
      - openvas_data:/var/lib/openvas
    restart: unless-stopped

volumes:
  openvas_data:
```

DaSean runs vulnerability scans against mesh devices (with Kevin's
permission) and practices reading assessment output — CySA+ Domain 2.

### Role: Kevin's Experiment (whatever you need)

Any Docker image, any config. The NUC doesn't care. It's a blank
canvas with 16GB RAM and a fast SSD.

---

## WIPE AND REBUILD

1. Plug the reimage USB into the NUC
2. Power cycle
3. Walk away for 15 minutes
4. Pull USB
5. SSH in, deploy new role

That's it. No state worth saving. If you need to preserve data
from an experiment, SCP it to Swiftgate before wiping.

---

## NETWORK ISOLATION OPTIONS

| Scenario | How to Connect | Isolation Level |
|----------|---------------|-----------------|
| Hacklab (vulnerable targets) | Direct cat6: Swiftgate ↔ NUC. Docker `internal: true`. | Full — NUC can't reach internet or mesh |
| SIEM lab (monitoring) | On mesh switch, same subnet as other gates | Open — needs to see mesh traffic |
| Scanner | On mesh switch | Open — needs to reach scan targets |
| Experiment | Your call per experiment | Varies |

**Rule of thumb**: If the containers are deliberately vulnerable
(DVWA, Juice Shop, Metasploitable), isolate with `internal: true`
or direct cat6. If they're tools (Wazuh, OpenVAS, Splunk), they
need mesh access.

---

## NAMING

| Name | What It Is |
|------|-----------|
| **Swiftgate** | DaSean's workstation (persistent, personal) |
| **Southgate** | Kevin's work machines (persistent, personal) |
| **Bluegate** | House/family space (persistent) |
| **Tasknode** | The NUC (ephemeral, role-based, any gate) |

Tasknode has no permanent identity. Its hostname is always `tasknode`
regardless of which gate it's attached to or what role it's running.
The role is defined by the compose file, not the hardware.

---

*Last updated: July 31, 2026*

