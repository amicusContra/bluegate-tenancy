"""Michigan campaign finance — TransparencyUSA and SOS CFRS.

TransparencyUSA provides a searchable interface for MI campaign finance data.
Now includes HTML parsing to extract payee amounts, dates, and committee connections.
"""

from __future__ import annotations
import re
import httpx
from bs4 import BeautifulSoup
from sources.base import Source
from models import SearchResult

TRANSPARENCY_BASE = "https://www.transparencyusa.org"


class CampaignFinanceSource(Source):
    name = "campaign_finance"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        cf = person.get("searches", {}).get("campaign_finance")
        if not cf:
            return []
        results = []
        r = await self._search_payee(person["name"], person["id"], person["name"])
        results.append(r)
        for alias in person.get("aliases", []):
            if alias != person["name"]:
                r = await self._search_payee(alias, person["id"], person["name"])
                results.append(r)
        if isinstance(cf, dict):
            if cf.get("committee_name"):
                r = await self._search_committee(cf["committee_name"], person["id"], person["name"])
                results.append(r)
            if cf.get("related_name"):
                r = await self._search_payee(cf["related_name"], person["id"], person["name"])
                results.append(r)
        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        r = await self._search_payee(entity["name"], entity["id"], entity["name"])
        results.append(r)
        r = await self._search_committee(entity["name"], entity["id"], entity["name"])
        results.append(r)
        return results

    async def _search_payee(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"payee: {name}",
        )
        url = f"{TRANSPARENCY_BASE}/mi/payee/{name.lower().replace(' ', '-')}"
        try:
            async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
                resp = await client.get(
                    url,
                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
                )
                result.raw_data = {"url": str(resp.url), "status": resp.status_code}
                if resp.status_code == 200:
                    hits = self._parse_payee_page(resp.text, str(resp.url))
                    result.hits.extend(hits)
                else:
                    search_url = f"{TRANSPARENCY_BASE}/mi/search?query={name.replace(' ', '+')}"
                    search_resp = await client.get(
                        search_url,
                        headers={"User-Agent": "Mozilla/5.0"},
                    )
                    if search_resp.status_code == 200:
                        hits = self._parse_search_results(search_resp.text, name)
                        result.hits.extend(hits)
                    else:
                        result.hits.append({
                            "note": f"No payee page (HTTP {resp.status_code})",
                            "search_url": search_url,
                        })
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_committee(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"committee: {name}",
        )
        slug = name.lower().replace(" ", "-").replace(",", "")
        url = f"{TRANSPARENCY_BASE}/mi/committee/{slug}"
        try:
            async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
                resp = await client.get(
                    url,
                    headers={"User-Agent": "Mozilla/5.0"},
                )
                result.raw_data = {"url": str(resp.url), "status": resp.status_code}
                if resp.status_code == 200:
                    hits = self._parse_committee_page(resp.text, str(resp.url))
                    result.hits.extend(hits)
                else:
                    result.hits.append({
                        "url": str(resp.url),
                        "status_code": resp.status_code,
                        "accessible": False,
                    })
        except Exception as e:
            result.error = str(e)
        return result

    def _parse_payee_page(self, html: str, url: str) -> list[dict]:
        hits = []
        soup = BeautifulSoup(html, "html.parser")

        title = soup.find("h1") or soup.find("h2")
        summary = {"url": url}
        if title:
            summary["payee_name"] = title.get_text(strip=True)

        total_el = soup.find(string=re.compile(r"\$[\d,]+"))
        if total_el:
            amounts = re.findall(r"\$([\d,]+(?:\.\d{2})?)", str(total_el.parent) if total_el.parent else str(total_el))
            if amounts:
                summary["total_amount"] = amounts[0]

        tables = soup.find_all("table")
        if tables:
            for table in tables:
                rows = table.find_all("tr")
                headers = [th.get_text(strip=True).lower() for th in rows[0].find_all(["th", "td"])] if rows else []
                for row in rows[1:]:
                    cells = [td.get_text(strip=True) for td in row.find_all("td")]
                    if cells and len(cells) >= 2:
                        hit = {"url": url}
                        for i, cell in enumerate(cells):
                            if i < len(headers):
                                hit[headers[i]] = cell
                            else:
                                hit[f"col_{i}"] = cell
                        hits.append(hit)

        if not hits:
            text = soup.get_text(separator="\n")
            amounts = re.findall(r"\$([\d,]+(?:\.\d{2})?)", text)
            dates = re.findall(r"\d{1,2}/\d{1,2}/\d{4}", text)
            summary["amounts_found"] = amounts[:10] if amounts else []
            summary["dates_found"] = dates[:10] if dates else []
            hits.append(summary)

        return hits

    def _parse_committee_page(self, html: str, url: str) -> list[dict]:
        hits = []
        soup = BeautifulSoup(html, "html.parser")

        title = soup.find("h1") or soup.find("h2")
        summary = {"url": url, "accessible": True}
        if title:
            summary["committee_name"] = title.get_text(strip=True)

        text = soup.get_text(separator="\n")
        amounts = re.findall(r"\$([\d,]+(?:\.\d{2})?)", text)
        if amounts:
            summary["amounts_found"] = amounts[:10]

        links = soup.find_all("a", href=True)
        related = []
        for a in links:
            href = a.get("href", "")
            if "/mi/payee/" in href or "/mi/committee/" in href:
                related.append({"name": a.get_text(strip=True), "url": href})
        if related:
            summary["related_entities"] = related[:20]

        hits.append(summary)
        return hits

    def _parse_search_results(self, html: str, query: str) -> list[dict]:
        hits = []
        soup = BeautifulSoup(html, "html.parser")

        links = soup.find_all("a", href=True)
        for a in links:
            href = a.get("href", "")
            text = a.get_text(strip=True)
            if query.lower().split()[0].lower() in text.lower() and (
                "/mi/payee/" in href or "/mi/committee/" in href or "/mi/candidate/" in href
            ):
                hits.append({
                    "name": text,
                    "url": f"{TRANSPARENCY_BASE}{href}" if href.startswith("/") else href,
                    "type": "payee" if "/payee/" in href else "committee" if "/committee/" in href else "candidate",
                })

        if not hits:
            hits.append({"note": f"Search returned no matching links for '{query}'"})

        return hits

