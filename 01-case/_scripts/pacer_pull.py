"""
PACER Docket Puller
Authenticates via PACER Auth API, then pulls docket reports from CM/ECF.
Saves docket HTML to local files for analysis.

Usage:  python pacer_pull.py
        (prompts for PACER username/password at runtime — never stored)
"""
import requests
import getpass
import sys
import os
import time
import re

AUTH_URL = "https://pacer.login.uscourts.gov/services/cso-auth"
MIEB_BASE = "https://ecf.mieb.uscourts.gov"

CASES = [
    {"label": "Holland_BK2", "number": "14-46410", "description": "Holland Ch.7 #2 (2014)"},
    {"label": "Holland_BK3", "number": "14-51632", "description": "Holland Ch.7 #3 (2014)"},
    {"label": "Banks_BK3",   "number": "97-45020", "description": "Banks 3rd BK (1997)"},
    {"label": "BMF",         "number": "05-80955", "description": "BMF RICO docket"},
]

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "02-evidence", "pacer-docs")
os.makedirs(OUT_DIR, exist_ok=True)


def authenticate(username, password):
    """Get PACER auth token."""
    print("[*] Authenticating with PACER...")
    resp = requests.post(AUTH_URL, json={
        "loginId": username,
        "password": password,
    }, headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    resp.raise_for_status()
    data = resp.json()
    if data.get("loginResult") != "0":
        print(f"[!] Auth failed: {data.get('errorDescription', 'unknown error')}")
        sys.exit(1)
    token = data["nextGenCSO"]
    print(f"[+] Authenticated. Token length: {len(token)}")
    if data.get("errorDescription"):
        print(f"    Note: {data['errorDescription']}")
    return token


def get_case_id(session, case_number):
    """Search MIEB for a case number and return the internal case ID."""
    url = f"{MIEB_BASE}/cgi-bin/iquery.pl"
    resp = session.get(url)
    
    form_data = {
        "case_num": case_number,
        "UserType": "",
    }
    resp = session.post(url, data=form_data)
    
    if resp.status_code == 200:
        text = resp.text
        match = re.search(r'DktRpt\.pl\?(\d+)', text)
        if match:
            return match.group(1)
        match = re.search(r'iquery\.pl\?(\d+)', text)
        if match:
            case_id_url = match.group(1)
            return case_id_url
    return None


def pull_docket(session, case_number, label):
    """Pull docket report for a case. Returns (case_id, html_text) or (None, None)."""
    print(f"\n{'='*60}")
    print(f"[*] Pulling docket for {label}: {case_number}")
    print(f"{'='*60}")
    
    search_url = f"{MIEB_BASE}/cgi-bin/iquery.pl"
    resp = session.get(search_url)
    print(f"    Query page: {resp.status_code}")
    
    resp = session.post(search_url, data={"case_num": case_number})
    print(f"    Case search: {resp.status_code}, {len(resp.text)} bytes")
    
    case_id_match = re.search(r'DktRpt\.pl\?(\d+)', resp.text)
    if not case_id_match:
        case_id_match = re.search(r'iquery\.pl\?(\d+-L_\d+_\d+-\d+)', resp.text)
    
    if not case_id_match:
        case_header = re.search(r'(\d{2}-\d{4,6})-?\w*\s+(.+?)(?:<|$)', resp.text)
        if case_header:
            print(f"    Found case header: {case_header.group(0)[:80]}")
        
        case_id_match = re.search(r'all_case_ids["\s]*(?:value=["\']\s*)(\d+)', resp.text)
    
    if not case_id_match:
        print(f"[!] Could not find case ID for {case_number}")
        out_path = os.path.join(OUT_DIR, f"{label}_SEARCH_RESULT.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(resp.text)
        print(f"    Saved search result to {out_path}")
        
        case_info = extract_case_info_from_query(resp.text)
        if case_info:
            print(f"    Case info found: {case_info}")
        return None, resp.text
    
    case_id = case_id_match.group(1)
    print(f"    Case ID: {case_id}")
    
    docket_url = f"{MIEB_BASE}/cgi-bin/DktRpt.pl?{case_id}"
    resp = session.get(docket_url)
    print(f"    Docket form: {resp.status_code}")
    
    docket_data = {
        "all_case_ids": case_id,
        "case_num": f"2:{case_number.replace('-', '-bk-')}",
        "date_type": "filed",
        "date_from": "",
        "date_to": "",
        "documents_numbered_from_": "0",
        "documents_numbered_to_": "99999999",
        "terminated_parties": "on",
        "page_count": "on",
        "output_format": "html",
        "sort1": "oldest date first",
    }
    
    resp = session.post(docket_url, data=docket_data)
    print(f"    Docket report: {resp.status_code}, {len(resp.text)} bytes")
    
    out_path = os.path.join(OUT_DIR, f"{label}_{case_number}_DOCKET.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(resp.text)
    print(f"    Saved to {out_path}")
    
    return case_id, resp.text


def extract_case_info_from_query(html):
    """Extract basic case info from a query result page."""
    info = {}
    for pattern, key in [
        (r'Case type:\s*(\w+)', 'type'),
        (r'Chapter:\s*(\d+)', 'chapter'),
        (r'Date filed:\s*([\d/]+)', 'filed'),
        (r'Date terminated:\s*([\d/]+)', 'terminated'),
        (r'Judge:\s*(.+?)(?:<|\n)', 'judge'),
        (r'Debtor dismissed:\s*([\d/]+)', 'dismissed'),
        (r'Debtor discharged:\s*([\d/]+)', 'discharged'),
    ]:
        m = re.search(pattern, html)
        if m:
            info[key] = m.group(1).strip()
    return info


def parse_docket_entries(html):
    """Parse docket entries from HTML, return summary."""
    entries = []
    
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    
    schedule_entries = []
    for m in re.finditer(r'(\d{2}/\d{2}/\d{4})\s+(\d+)\s+\((\d+)\s+pgs?\)', text):
        date, doc_num, pages = m.group(1), m.group(2), m.group(3)
        start = m.end()
        snippet = text[start:start+200].strip()
        entries.append({
            "date": date,
            "doc": doc_num,
            "pages": pages,
            "text": snippet[:150],
        })
        
        if any(kw in snippet.lower() for kw in ['schedule', 'statement of financial', 'sofa', 'plan']):
            schedule_entries.append({
                "date": date,
                "doc": doc_num,
                "pages": pages,
                "text": snippet[:150],
            })
    
    return entries, schedule_entries


def main():
    print("=" * 60)
    print("  PACER DOCKET PULLER — Holland/Banks BK Cases")
    print("=" * 60)
    print()
    
    username = input("PACER Username: ").strip()
    password = getpass.getpass("PACER Password: ")
    
    token = authenticate(username, password)
    
    session = requests.Session()
    session.cookies.set("NextGenCSO", token, domain=".uscourts.gov")
    session.cookies.set("PacerSession", token, domain=".uscourts.gov")
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    })
    
    verify_url = f"{MIEB_BASE}/cgi-bin/login.pl"
    resp = session.get(verify_url)
    if "Log Out" in resp.text or "Welcome" in resp.text:
        print("[+] Session verified — logged into MIEB CM/ECF")
    else:
        print(f"[!] Session may not be authenticated. Status: {resp.status_code}")
        print(f"    Response snippet: {resp.text[:200]}")
    
    results = {}
    for case in CASES:
        case_id, html = pull_docket(session, case["number"], case["label"])
        results[case["label"]] = {
            "case_id": case_id,
            "number": case["number"],
            "description": case["description"],
        }
        
        if html:
            entries, key_docs = parse_docket_entries(html)
            results[case["label"]]["total_entries"] = len(entries)
            results[case["label"]]["key_docs"] = key_docs
            print(f"    Parsed {len(entries)} entries, {len(key_docs)} key documents")
        
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    for label, info in results.items():
        print(f"\n  {label} ({info['number']}): {info['description']}")
        print(f"    Case ID: {info.get('case_id', 'NOT FOUND')}")
        print(f"    Total entries: {info.get('total_entries', '?')}")
        if info.get("key_docs"):
            for kd in info["key_docs"]:
                print(f"    📌 Doc #{kd['doc']} ({kd['pages']} pgs, {kd['date']}): {kd['text'][:80]}...")
    
    print("\n[*] Done. Check pacer-docs/ for saved HTML files.")
    print("[*] Kevin: open the HTML files in browser to identify exact docs to pull.")


if __name__ == "__main__":
    main()
