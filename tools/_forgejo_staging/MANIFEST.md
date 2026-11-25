# FORGEJO PUBLIC RECORD — STAGING MANIFEST
## Generated: September 19, 2026 07:45
## Repo: https://git.primals.eco/publicRecord/detroit

---

## FILES TO PUSH

| # | Category | Filename | Size | Status |
|---|----------|----------|------|--------|
| 1 | filings | `2026-09-22_federal_master_packet.pdf` | 147,416 B | Ready |
| 2 | filings | `2026-09-22_journalist_briefing_packet.pdf` | 22,500 B | Ready |
| 3 | filings | `2026-09-17_oig_supplement_forgery.md` | 8,766 B | Ready |
| 4 | filings | `2026-09-16_complaint_chain_master.md` | 10,999 B | Ready |
| 5 | filings | `2026-09-17_motion_alternative_service.md` | 12,123 B | Ready |
| 6 | evidence | `2026-09-17_oig_supplement_proof_package.pdf` | 1,177,833 B | Ready |
| 7 | evidence | `2026-09-02_ring_exhibit_keyframes.pdf` | 12,758,204 B | Ready |
| 8 | correspondence | `2026-09-18_banks_ppo_service_email.txt` | 2,050 B | Ready |

**Total files:** 8
**Total size:** 14,139,891 bytes (13808 KB)

---

## WHAT STAYS PRIVATE (DO NOT PUSH)

| Item | Why |
|------|-----|
| Strategy docs (battle plan, assessment) | Operational intelligence |
| DaSean briefing | Private strategy communication |
| OSINT scrape results | Raw operational data |
| Book transcripts (Banks, BMF) | Copyright + analysis methodology |
| PACER scrapers + credentials | Tool security |
| PPO tracker, checklists | Operational status |
| Deployment day plan | Timing/tactical intelligence |
| SCRAPING_MATRIX | Operational methodology |

---

## PUSH SEQUENCE

### Option A: From Windows (if Forgejo SSH is configured)
```powershell
# Add Forgejo remote to bluegate-tenancy
cd C:\Users\mokke\jobHunt\bluegate-tenancy
# This won't work directly — different repo structure
# Use Option B instead
```

### Option B: From Server (recommended)
```bash
# 1. SSH into primals.eco server
ssh sporegate@primals.eco

# 2. Navigate to local clone
cd ~/Development/detroit

# 3. Transfer staged files (from Windows via scp/rsync)
# From Windows:
#   scp -r C:\Users\mokke\jobHunt\bluegate-tenancy\tools\_forgejo_staging\* sporegate@primals.eco:~/Development/detroit/

# 4. Or run the push script
bash PUSH_COMMANDS.sh
```

### Option C: Direct git push from server with manual file drops
```bash
cd ~/Development/detroit
# Copy each file into the right directory, commit, push
# See PUSH_COMMANDS.sh for individual commit messages
```

---

## DEPLOYMENT DAY INTEGRATION

Add as **Phase 0** of Deployment Day (before portal submissions):

1. Push all files to Forgejo
2. Verify public access at https://git.primals.eco/publicRecord/detroit
3. Include the repo URL in journalist emails:
   > "Full evidence with git provenance: https://git.primals.eco/publicRecord/detroit"
4. Each agency email can also reference the public repo
5. The git commit hashes serve as tamper-evident timestamps
