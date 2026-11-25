"""Michigan LARA MiBusiness Registry — entity search.

The old LARA portal (cofs.lara.state.mi.us) was retired June 2025.
New portal: michigan.gov/corpentitysearch

This module uses micompanyregistry.com as a mirror (Google-indexed)
and routes through ScrapingAnt/ScrapFly proxy to bypass Cloudflare.
Falls back to direct httpx if no proxy key is available.
"""

from __future__ import annotations
import httpx
from bs4 import BeautifulSoup
from sources.base import Source
from sources.scraping_proxy import fetch_url, proxy_available
from models import SearchResult


MIRROR_SEARCH = "https://www.micompanyregistry.com/companies/"
NEW_PORTAL = "https://michigan.gov/corpentitysearch"


class LARASource(Source):
    name = "lara"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        lara_cfg = person.get("searches", {}).get("lara", {})
        if not lara_cfg:
            return results

        if lara_cfg.get("agent_name"):
            r = await self._search_entity_name(person["name"], person["id"], person["name"])
            results.append(r)

        for entity_id in lara_cfg.get("entity_ids", []):
            r = await self._search_by_id(entity_id, person["id"], person["name"])
            results.append(r)

        if lara_cfg.get("entity_name"):
            r = await self._search_entity_name(
                lara_cfg["entity_name"], person["id"], person["name"]
            )
            results.append(r)

        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        if entity.get("lara_id"):
            r = await self._search_by_id(entity["lara_id"], entity["id"], entity["name"])
            results.append(r)
        r = await self._search_entity_name(entity["name"], entity["id"], entity["name"])
        results.append(r)
        return results

    async def _search_entity_name(self, query: str, target_id: str, target_name: str) -> SearchResult:
        """Search the mirror site for entity/agent name, using proxy if available."""
        slug = query.lower().replace(" ", "-").replace(",", "").replace(".", "")
        slug = slug.replace("--", "-").strip("-")
        url = f"{MIRROR_SEARCH}{slug}/"

        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"entity/agent: {query}",
        )
        try:
            fetched = await fetch_url(url, js_render=True, timeout=45)
            result.raw_data = {
                "url": url,
                "status": fetched["status_code"],
                "proxy": fetched["proxy_used"],
            }
            html = fetched["html"]
            if fetched["status_code"] == 200 and html and "security" not in html.lower()[:500]:
                soup = BeautifulSoup(html, "html.parser")
                result.hits = self._parse_mirror_page(soup)
                if result.hits:
                    result.hits[0]["fetched_via"] = fetched["proxy_used"] or "direct"
            else:
                result.hits.append({
                    "note": f"Mirror {'blocked by Cloudflare' if 'cloudflare' in (html or '').lower()[:1000] else 'returned ' + str(fetched['status_code'])}",
                    "proxy_used": fetched["proxy_used"],
                    "official_url": NEW_PORTAL,
                    "manual_search": query,
                })
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_by_id(self, entity_id: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"LARA ID: {entity_id}",
        )
        result.hits.append({
            "note": "Direct ID lookup requires official portal",
            "url": NEW_PORTAL,
            "lara_id": entity_id,
            "manual_action": f"Search entity ID {entity_id} at {NEW_PORTAL}",
        })
        return result

    def _parse_mirror_page(self, soup: BeautifulSoup) -> list[dict]:
        hits = []
        hit = {}
        for el in soup.select("h1, .field-label, .field-value, dt, dd"):
            text = el.get_text(strip=True)
            if el.name == "h1":
                hit["entity_name"] = text
            tag = el.get("class", [])
            if "field-label" in tag or el.name == "dt":
                hit["_last_label"] = text
            if "field-value" in tag or el.name == "dd":
                label = hit.pop("_last_label", "")
                if label:
                    key = label.lower().replace(" ", "_").replace(":", "").replace("/", "_")
                    hit[key] = text

        directors = []
        dir_section = soup.find(string=lambda t: t and "Director" in t if t else False)
        if dir_section:
            table = dir_section.find_parent("section") or dir_section.find_parent("div")
            if table:
                for row in table.find_all("tr"):
                    cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                    if cells:
                        directors.append(" | ".join(cells))

        other_companies = []
        other_section = soup.find(string=lambda t: t and "Other companies" in t if t else False)
        if other_section:
            ul = other_section.find_next("ul")
            if ul:
                for li in ul.find_all("li"):
                    other_companies.append(li.get_text(strip=True))

        hit.pop("_last_label", None)
        if directors:
            hit["directors"] = directors
        if other_companies:
            hit["other_entities_same_agent"] = other_companies
        if hit:
            hits.append(hit)
        return hits

