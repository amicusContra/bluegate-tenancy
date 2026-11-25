"""IRS Tax Exempt Organization Search (TEOS).

Uses the IRS EO Select Check web endpoint.
Falls back to scraping proxy when httpx gets 403.
"""

from __future__ import annotations
import httpx
from bs4 import BeautifulSoup
from sources.base import Source
from sources.scraping_proxy import fetch_url, proxy_available
from models import SearchResult

SEARCH_URL = "https://apps.irs.gov/app/eos/allSearch"
TEOS_SEARCH_PAGE = "https://apps.irs.gov/app/eos/"


class IRSTEOSSource(Source):
    name = "irs_teos"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        for eid in person.get("known_entities", []):
            from config import get_entity
            entity = get_entity(eid)
            if entity and entity.get("ein"):
                r = await self._search_ein(entity["ein"], person["id"], person["name"])
                results.append(r)
            elif entity and entity.get("type") in ("domestic_nonprofit", "nonprofit", "charter_school"):
                r = await self._search_name(entity["name"], person["id"], person["name"])
                results.append(r)
        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        if entity.get("ein"):
            r = await self._search_ein(entity["ein"], entity["id"], entity["name"])
            results.append(r)
        r = await self._search_name(entity["name"], entity["id"], entity["name"])
        results.append(r)
        return results

    async def _search_ein(self, ein: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"EIN: {ein}",
        )
        try:
            async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
                resp = await client.get(
                    SEARCH_URL,
                    params={
                        "Ein": ein.replace("-", ""),
                        "city": "",
                        "state": "MI",
                        "country": "US",
                        "deductibility": "all",
                        "dispatchMethod": "searchAll",
                        "postDateFrom": "",
                        "postDateTo": "",
                        "exemptTypeCode": "al",
                        "isDescending": "false",
                        "totalResults": "25",
                        "resultsOfPage": "25",
                        "indexOfFirstRow": "0",
                    },
                    headers={"User-Agent": "Mozilla/5.0"},
                )
                if resp.status_code == 403:
                    return await self._proxy_fallback(ein, target_id, target_name, "ein")

                resp.raise_for_status()
                result.raw_data = {"status_code": resp.status_code, "url": str(resp.url)}
                if resp.headers.get("content-type", "").startswith("application/json"):
                    data = resp.json()
                    result.raw_data["json"] = data
                    for org in data if isinstance(data, list) else [data]:
                        result.hits.append({
                            "ein": org.get("ein"),
                            "name": org.get("name") or org.get("orgName"),
                            "city": org.get("city"),
                            "state": org.get("state"),
                            "status": org.get("deductibilityStatusCode") or org.get("statusCode"),
                            "ruling_date": org.get("rulingDate"),
                        })
                else:
                    return await self._proxy_fallback(ein, target_id, target_name, "ein")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 403:
                return await self._proxy_fallback(ein, target_id, target_name, "ein")
            result.error = str(e)
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_name(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"name: {name}",
        )
        try:
            async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
                resp = await client.get(
                    SEARCH_URL,
                    params={
                        "names": name,
                        "city": "",
                        "state": "MI",
                        "country": "US",
                        "deductibility": "all",
                        "dispatchMethod": "searchAll",
                        "postDateFrom": "",
                        "postDateTo": "",
                        "exemptTypeCode": "al",
                        "isDescending": "false",
                        "totalResults": "25",
                        "resultsOfPage": "25",
                        "indexOfFirstRow": "0",
                    },
                    headers={"User-Agent": "Mozilla/5.0"},
                )
                if resp.status_code == 403:
                    return await self._proxy_fallback(name, target_id, target_name, "name")

                resp.raise_for_status()
                result.raw_data = {"status_code": resp.status_code, "url": str(resp.url)}
                if resp.headers.get("content-type", "").startswith("application/json"):
                    data = resp.json()
                    result.raw_data["json"] = data
                    for org in data if isinstance(data, list) else [data]:
                        result.hits.append({
                            "ein": org.get("ein"),
                            "name": org.get("name") or org.get("orgName"),
                            "city": org.get("city"),
                            "state": org.get("state"),
                            "status": org.get("deductibilityStatusCode"),
                        })
                else:
                    return await self._proxy_fallback(name, target_id, target_name, "name")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 403:
                return await self._proxy_fallback(name, target_id, target_name, "name")
            result.error = str(e)
        except Exception as e:
            result.error = str(e)
        return result

    async def _proxy_fallback(
        self, query: str, target_id: str, target_name: str, query_type: str
    ) -> SearchResult:
        """When IRS blocks direct access, try scraping proxy to get rendered page."""
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"{query_type}_proxy: {query}",
        )

        if query_type == "ein":
            ein_clean = query.replace("-", "")
            url = f"{TEOS_SEARCH_PAGE}allSearch?Ein={ein_clean}&state=MI&country=US&deductibility=all&dispatchMethod=searchAll&exemptTypeCode=al&totalResults=25&resultsOfPage=25&indexOfFirstRow=0"
        else:
            url = f"{TEOS_SEARCH_PAGE}allSearch?names={query.replace(' ', '+')}&state=MI&country=US&deductibility=all&dispatchMethod=searchAll&exemptTypeCode=al&totalResults=25&resultsOfPage=25&indexOfFirstRow=0"

        try:
            fetched = await fetch_url(url, js_render=True, timeout=60)
            result.raw_data = {
                "url": url,
                "status": fetched["status_code"],
                "proxy": fetched["proxy_used"],
            }
            html = fetched["html"] or ""
            if fetched["status_code"] == 200 and html:
                hits = self._parse_teos_html(html)
                if hits:
                    result.hits = hits
                else:
                    result.hits.append({
                        "note": "Page fetched via proxy but no structured data found",
                        "proxy_used": fetched["proxy_used"],
                        "url": url,
                    })
            else:
                result.error = f"Proxy fetch failed: {fetched.get('error', 'unknown')}"
        except Exception as e:
            result.error = f"Proxy fallback failed: {e}"
        return result

    def _parse_teos_html(self, html: str) -> list[dict]:
        """Parse rendered IRS TEOS results page."""
        hits = []
        soup = BeautifulSoup(html, "html.parser")

        tables = soup.find_all("table")
        for table in tables:
            rows = table.find_all("tr")
            if not rows:
                continue
            headers = [th.get_text(strip=True).lower() for th in rows[0].find_all(["th", "td"])]
            for row in rows[1:]:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                if len(cells) >= 3:
                    hit = {}
                    for i, cell in enumerate(cells):
                        if i < len(headers):
                            key = headers[i].replace(" ", "_")
                            hit[key] = cell
                        else:
                            hit[f"col_{i}"] = cell
                    if hit:
                        hits.append(hit)

        if not hits:
            text = soup.get_text(separator="\n")
            for line in text.split("\n"):
                line = line.strip()
                if not line:
                    continue
                if any(w in line.lower() for w in ["exempt", "deductib", "ein", "organization"]) and len(line) < 200:
                    hits.append({"raw_line": line})

        return hits

