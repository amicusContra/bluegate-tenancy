"""ProPublica Nonprofit Explorer — free public API, no key needed.

Searches IRS 990 filings for nonprofit organizations.
Docs: https://projects.propublica.org/nonprofits/api
"""

from __future__ import annotations
import httpx
from sources.base import Source
from models import SearchResult


API_BASE = "https://projects.propublica.org/nonprofits/api/v2"
API_V3_BASE = "https://projects.propublica.org/nonprofits/api/v3"


class ProPublicaSource(Source):
    name = "propublica"
    requires_key = False

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        for eid in person.get("known_entities", []):
            from config import get_entity
            entity = get_entity(eid)
            if entity and entity.get("ein"):
                r = await self._fetch_org(entity["ein"], person["id"], person["name"])
                results.append(r)
        name = person["name"]
        r = await self._search_orgs(name, person["id"], person["name"])
        results.append(r)
        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        if entity.get("ein"):
            r = await self._fetch_org(entity["ein"], entity["id"], entity["name"])
            results.append(r)
        r = await self._search_orgs(entity["name"], entity["id"], entity["name"])
        results.append(r)
        return results

    async def _search_orgs(self, query: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"search: {query}",
        )
        try:
            async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
                # Try v2 search.json first
                resp = await client.get(
                    f"{API_BASE}/search.json",
                    params={"q": query},
                    headers={"User-Agent": "Mozilla/5.0"},
                )
                if resp.status_code != 200:
                    # Fallback: try name-path pattern /nonprofits/api/v2/organizations/{query}.json
                    slug = query.lower().replace(" ", "+")
                    resp = await client.get(
                        f"{API_BASE}/search.json",
                        params={"q": slug, "state[id]": "MI"},
                        headers={"User-Agent": "Mozilla/5.0"},
                    )

                if resp.status_code == 200:
                    data = resp.json()
                    result.raw_data = data
                    for org in data.get("organizations", []):
                        result.hits.append({
                            "ein": org.get("ein"),
                            "name": org.get("name"),
                            "city": org.get("city"),
                            "state": org.get("state"),
                            "ntee_code": org.get("ntee_code"),
                            "subsection_code": org.get("subsection_code"),
                            "total_revenue": org.get("total_revenue"),
                            "total_expenses": org.get("total_expenses"),
                        })
                else:
                    result.error = f"ProPublica API returned HTTP {resp.status_code}"
        except Exception as e:
            result.error = str(e)
        return result

    async def _fetch_org(self, ein: str, target_id: str, target_name: str) -> SearchResult:
        ein_clean = ein.replace("-", "")
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"EIN: {ein}",
        )
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.get(f"{API_BASE}/organizations/{ein_clean}.json")
                resp.raise_for_status()
                data = resp.json()
                result.raw_data = data
                org = data.get("organization", {})
                result.hits.append({
                    "ein": org.get("ein"),
                    "name": org.get("name"),
                    "address": org.get("address"),
                    "city": org.get("city"),
                    "state": org.get("state"),
                    "zipcode": org.get("zipcode"),
                    "ntee_code": org.get("ntee_code"),
                    "ruling_date": org.get("ruling_date"),
                    "tax_period": org.get("tax_period"),
                    "asset_amount": org.get("asset_amount"),
                    "income_amount": org.get("income_amount"),
                })
                for filing in data.get("filings_with_data", []):
                    result.hits.append({
                        "type": "990_filing",
                        "tax_period": filing.get("tax_prd"),
                        "tax_period_year": filing.get("tax_prd_yr"),
                        "total_revenue": filing.get("totrevenue"),
                        "total_expenses": filing.get("totfuncexpns"),
                        "total_assets_eoy": filing.get("totassetsend"),
                        "pdf_url": filing.get("pdf_url"),
                    })
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                result.error = f"EIN {ein} not found in ProPublica database"
            else:
                result.error = str(e)
        except Exception as e:
            result.error = str(e)
        return result

