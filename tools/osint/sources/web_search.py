"""Web search source — uses scraping proxy to search Google-indexed public records.

Searches micompanyregistry.com, companiesmi.com, allpeople.com, and
other indexed mirrors of government databases.
Routes through ScrapingAnt/ScrapFly proxy when available for Cloudflare bypass.
"""

from __future__ import annotations
import httpx
from bs4 import BeautifulSoup
from sources.base import Source
from sources.scraping_proxy import fetch_url
from models import SearchResult

INDEXED_SITES = [
    "micompanyregistry.com",
    "companiesmi.com",
    "allpeople.com",
    "opengovus.com",
    "ballotpedia.org",
    "transparencyusa.org",
]


class WebSearchSource(Source):
    name = "web_search"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        name = person["name"]
        r = await self._search_lara_mirror(name, person["id"], person["name"])
        results.append(r)

        r = await self._search_companiesmi(name, person["id"], person["name"])
        results.append(r)

        for entity_id in person.get("known_entities", []):
            from config import get_entity
            entity = get_entity(entity_id)
            if entity:
                r = await self._search_lara_mirror(entity["name"], person["id"], person["name"])
                results.append(r)

        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        r = await self._search_lara_mirror(entity["name"], entity["id"], entity["name"])
        results.append(r)
        r = await self._search_companiesmi(entity["name"], entity["id"], entity["name"])
        results.append(r)
        return results

    async def _search_lara_mirror(self, query: str, target_id: str, target_name: str) -> SearchResult:
        """Search micompanyregistry.com for entity data, using proxy if available."""
        slug = (
            query.lower()
            .replace(",", "")
            .replace(".", "")
            .replace("&", "")
            .replace("  ", " ")
            .strip()
            .replace(" ", "-")
            .replace("--", "-")
        )
        url = f"https://www.micompanyregistry.com/companies/{slug}/"

        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"lara_mirror: {query}",
        )
        try:
            fetched = await fetch_url(url, js_render=True, timeout=45)
            result.raw_data = {"url": url, "status": fetched["status_code"], "proxy": fetched["proxy_used"]}
            text = fetched["html"] or ""
            if fetched["status_code"] == 200 and "security" not in text[:500].lower():
                hit = self._extract_company_info(text)
                if hit:
                    hit["fetched_via"] = fetched["proxy_used"] or "direct"
                    result.hits.append(hit)
            elif "security" in text[:500].lower() or "cloudflare" in text[:1000].lower():
                result.hits.append({
                    "note": "Cloudflare challenge persisted even with proxy",
                    "url": url,
                    "proxy_used": fetched["proxy_used"],
                })
            else:
                result.hits.append({
                    "note": f"HTTP {fetched['status_code']}",
                    "url": url,
                    "proxy_used": fetched["proxy_used"],
                })
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_companiesmi(self, query: str, target_id: str, target_name: str) -> SearchResult:
        """Search companiesmi.com — another LARA mirror with different bot protection."""
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"companiesmi: {query}",
        )
        try:
            search_url = f"https://companiesmi.com/search?q={query.replace(' ', '+')}"
            async with httpx.AsyncClient(timeout=20, follow_redirects=True) as client:
                resp = await client.get(search_url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/128.0 Safari/537.36",
                })
                result.raw_data = {"url": search_url, "status": resp.status_code}
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    for link in soup.select("a[href*='/company/']"):
                        text = link.get_text(strip=True)
                        href = link.get("href", "")
                        if text and href:
                            result.hits.append({
                                "name": text,
                                "url": f"https://companiesmi.com{href}" if not href.startswith("http") else href,
                            })
        except Exception as e:
            result.error = str(e)
        return result

    def _extract_company_info(self, html: str) -> dict | None:
        soup = BeautifulSoup(html, "html.parser")
        info = {}

        h1 = soup.find("h1")
        if h1:
            info["name"] = h1.get_text(strip=True)

        for text_node in soup.find_all(string=True):
            t = text_node.strip()
            parent = text_node.parent
            if not t or not parent:
                continue
            t_lower = t.lower()
            if "business id" in t_lower:
                next_el = parent.find_next_sibling() or parent.find_next()
                if next_el:
                    info["business_id"] = next_el.get_text(strip=True)
            elif "registered on" in t_lower and "as a" in t_lower:
                info["registration_info"] = t
            elif "agent name" in t_lower:
                next_el = parent.find_next_sibling() or parent.find_next()
                if next_el:
                    info["agent"] = next_el.get_text(strip=True)
            elif "status" in t_lower and ("active" in t_lower or "inactive" in t_lower):
                info["status"] = t

        page_text = soup.get_text()
        if "Active" in page_text and "business id" in page_text.lower():
            for line in page_text.split("\n"):
                line = line.strip()
                if line.startswith("8") and len(line) == 9 and line.isdigit():
                    info["business_id"] = line
                if "registered on" in line.lower():
                    info["registration_info"] = line

        other = []
        other_heading = soup.find(string=lambda t: t and "Other companies" in t if t else False)
        if other_heading:
            ul = other_heading.find_next("ul") if other_heading else None
            if ul:
                for li in ul.find_all("li"):
                    other.append(li.get_text(strip=True))
        if other:
            info["other_entities_same_agent"] = other

        return info if info else None

