"""CourtListener / RECAP — free federal court record search.

Free REST API, no key needed for basic searches.
Docs: https://www.courtlistener.com/api/rest-info/
"""

from __future__ import annotations
import httpx
from sources.base import Source
from models import SearchResult


API_BASE = "https://www.courtlistener.com/api/rest/v4"


class CourtListenerSource(Source):
    name = "courtlistener"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        name = person["name"]

        r = await self._search_dockets(name, person["id"], person["name"])
        results.append(r)

        r = await self._search_people(name, person["id"], person["name"])
        results.append(r)

        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        r = await self._search_dockets(entity["name"], entity["id"], entity["name"])
        return [r]

    async def _search_dockets(self, query: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"dockets: {query}",
        )
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.get(
                    f"{API_BASE}/search/",
                    params={
                        "q": query,
                        "type": "r",
                        "order_by": "score desc",
                    },
                    headers={"User-Agent": "OSINT-Toolkit/1.0"},
                )
                resp.raise_for_status()
                data = resp.json()
                result.raw_data = {
                    "count": data.get("count"),
                    "next": data.get("next"),
                }
                for item in data.get("results", []):
                    result.hits.append({
                        "case_name": item.get("caseName"),
                        "court": item.get("court"),
                        "court_citation": item.get("court_citation_string"),
                        "date_filed": item.get("dateFiled"),
                        "docket_number": item.get("docketNumber"),
                        "description": (item.get("snippet") or "")[:200],
                        "url": f"https://www.courtlistener.com{item['absolute_url']}"
                        if item.get("absolute_url") else None,
                    })
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_people(self, query: str, target_id: str, target_name: str) -> SearchResult:
        """Search CourtListener's people database (judges, attorneys)."""
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"people: {query}",
        )
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.get(
                    f"{API_BASE}/search/",
                    params={
                        "q": query,
                        "type": "p",
                        "order_by": "score desc",
                    },
                    headers={"User-Agent": "OSINT-Toolkit/1.0"},
                )
                resp.raise_for_status()
                data = resp.json()
                result.raw_data = {"count": data.get("count")}
                for item in data.get("results", []):
                    result.hits.append({
                        "name": item.get("name_full") or f"{item.get('name_first', '')} {item.get('name_last', '')}",
                        "court": item.get("court"),
                        "date_start": item.get("date_start"),
                        "date_end": item.get("date_granularity_start"),
                        "position_type": item.get("position_type"),
                        "political_affiliation": item.get("political_affiliation"),
                        "url": f"https://www.courtlistener.com{item['absolute_url']}"
                        if item.get("absolute_url") else None,
                    })
        except Exception as e:
            result.error = str(e)
        return result

