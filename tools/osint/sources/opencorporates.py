"""OpenCorporates — company search across jurisdictions.

Free tier: no key needed, rate limited.
Docs: https://api.opencorporates.com/documentation/API-Reference
"""

from __future__ import annotations
import httpx
from sources.base import Source
from models import SearchResult
from config import get_key


API_BASE = "https://api.opencorporates.com/v0.4"


class OpenCorporatesSource(Source):
    name = "opencorporates"
    requires_key = True

    def available(self) -> bool:
        return get_key("OPENCORPORATES_API_KEY") is not None

    def _params(self, extra: dict | None = None) -> dict:
        params = {}
        key = get_key("OPENCORPORATES_API_KEY")
        if key:
            params["api_token"] = key
        if extra:
            params.update(extra)
        return params

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        r = await self._search_companies(person["name"], person["id"], person["name"])
        results.append(r)
        for alias in person.get("aliases", []):
            if alias != person["name"]:
                r = await self._search_companies(alias, person["id"], person["name"])
                results.append(r)
        r = await self._search_officers(person["name"], person["id"], person["name"])
        results.append(r)
        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        r = await self._search_companies(entity["name"], entity["id"], entity["name"])
        return [r]

    async def _search_companies(self, query: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"company: {query}",
        )
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                params = self._params({
                    "q": query,
                    "jurisdiction_code": "us_mi",
                    "order": "score",
                })
                resp = await client.get(f"{API_BASE}/companies/search", params=params)
                resp.raise_for_status()
                data = resp.json()
                result.raw_data = data
                for item in data.get("results", {}).get("companies", []):
                    co = item.get("company", {})
                    result.hits.append({
                        "name": co.get("name"),
                        "company_number": co.get("company_number"),
                        "jurisdiction": co.get("jurisdiction_code"),
                        "status": co.get("current_status"),
                        "incorporation_date": co.get("incorporation_date"),
                        "dissolution_date": co.get("dissolution_date"),
                        "company_type": co.get("company_type"),
                        "registered_address": co.get("registered_address_in_full"),
                        "agent_name": co.get("agent_name"),
                        "opencorporates_url": co.get("opencorporates_url"),
                    })
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_officers(self, query: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"officer: {query}",
        )
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                params = self._params({
                    "q": query,
                    "jurisdiction_code": "us_mi",
                })
                resp = await client.get(f"{API_BASE}/officers/search", params=params)
                resp.raise_for_status()
                data = resp.json()
                result.raw_data = data
                for item in data.get("results", {}).get("officers", []):
                    off = item.get("officer", {})
                    co = off.get("company", {})
                    result.hits.append({
                        "officer_name": off.get("name"),
                        "position": off.get("position"),
                        "start_date": off.get("start_date"),
                        "end_date": off.get("end_date"),
                        "company_name": co.get("name"),
                        "company_number": co.get("company_number"),
                        "company_jurisdiction": co.get("jurisdiction_code"),
                        "opencorporates_url": off.get("opencorporates_url"),
                    })
        except Exception as e:
            result.error = str(e)
        return result

