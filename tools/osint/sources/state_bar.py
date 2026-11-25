"""State Bar of Michigan — attorney license verification.

Member directory: https://www.reliaguide.com/SBM (formerly zeekbeek.com/SBM)
Direct search: https://member.michbar.org/
"""

from __future__ import annotations
import httpx
from bs4 import BeautifulSoup
from sources.base import Source
from models import SearchResult


SEARCH_URL = "https://www.reliaguide.com/SBM/member/search"


class StateBarSource(Source):
    name = "state_bar_mi"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        if not person.get("searches", {}).get("state_bar"):
            return []
        parts = person["name"].split()
        last = parts[-1] if parts else person["name"]
        first = parts[0] if len(parts) > 1 else ""
        r = await self._search_attorney(first, last, person["id"], person["name"])
        return [r]

    async def _search_attorney(
        self, first: str, last: str, target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"attorney: {first} {last}",
        )
        try:
            async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
                resp = await client.get(
                    SEARCH_URL,
                    params={"FirstName": first, "LastName": last},
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 Chrome/128.0 Safari/537.36",
                    },
                )
                result.raw_data = {"url": str(resp.url), "status": resp.status_code}
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    hits = self._parse_results(soup)
                    if hits:
                        result.hits = hits
                    else:
                        result.hits.append({
                            "note": f"No attorney found matching '{first} {last}'",
                            "conclusion": "NOT LICENSED in Michigan",
                        })
        except Exception as e:
            result.error = str(e)
        return result

    def _parse_results(self, soup: BeautifulSoup) -> list[dict]:
        hits = []
        cards = soup.select(".member-card, .search-result, .result-item, tr.member")
        for card in cards:
            hit = {}
            name_el = card.select_one(".member-name, .name, h3, td:first-child")
            if name_el:
                hit["name"] = name_el.get_text(strip=True)
            pnum = card.select_one(".p-number, .bar-number, .member-id")
            if pnum:
                hit["bar_number"] = pnum.get_text(strip=True)
            status = card.select_one(".status, .member-status")
            if status:
                hit["status"] = status.get_text(strip=True)
            loc = card.select_one(".location, .city-state")
            if loc:
                hit["location"] = loc.get_text(strip=True)
            if hit:
                hits.append(hit)

        if not hits:
            for text_block in soup.select("p, div"):
                t = text_block.get_text(strip=True).lower()
                if "no results" in t or "no members found" in t:
                    return [{"note": "No results", "conclusion": "NOT LICENSED"}]

        return hits

