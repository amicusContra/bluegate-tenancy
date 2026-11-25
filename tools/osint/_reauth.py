import httpx, json

creds = json.loads(open(".pacer_creds.json").read())
print(f"Using: {creds['username']}")

r = httpx.post(
    "https://pacer.login.uscourts.gov/services/cso-auth",
    json={"loginId": creds["username"], "password": creds["password"]},
    headers={"Content-Type": "application/json"},
    timeout=30,
)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:500]}")

if r.status_code == 200 and r.text.strip():
    body = r.text
    token = ""
    if "<nextGenCSO>" in body:
        token = body.split("<nextGenCSO>")[1].split("</nextGenCSO>")[0]
    elif body.strip().startswith("{"):
        data = r.json()
        token = data.get("nextGenCSO", data.get("token", ""))
    if token:
        from datetime import datetime, timedelta
        expiry = datetime.now() + timedelta(seconds=3540)
        json.dump({"token": token, "expiry": expiry.isoformat(), "created": datetime.now().isoformat()}, open(".pacer_token.json", "w"))
        print(f"Token refreshed! Expires: {expiry}")
    else:
        print(f"No token in response: {data}")
else:
    print("Auth failed or empty response")
