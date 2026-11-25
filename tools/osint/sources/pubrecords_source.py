"""PubRecords — US public records intelligence.

Companies (OpenCorporates), SEC EDGAR, federal courts (RECAP/CourtListener),
federal spending (USASpending), and professional licenses.

Free dev key included for evaluation (30 calls/day).
Set PUBRECORDS_API_KEY in .env to use a production key.
"""

from __future__ import annotations
from pubrecords import PubRecords
from sources.base import Source
from models import SearchResult
from config import get_key

DEV_KEY = "pubrecords-dev-key-001"


class PubRecordsSource(Source):
    name = "pubrecords"
    requires_key = False

    def _client(self) -> PubRecords:
        key = get_key("PUBRECORDS_API_KEY") or DEV_KEY
        return PubRecords(api_key=key)

    async def search_person(self, person: dict) -> list[SearchResult]:
        results = []
        name = person["name"]

        r = await self._search_companies(name, person["id"], person["name"])
        results.append(r)

        r = await self._search_court_cases(name, person["id"], person["name"])
        results.append(r)

        r = await self._search_federal_spending(name, person["id"], person["name"])
        results.append(r)

        for entity_id in person.get("known_entities", []):
            from config import get_entity
            entity = get_entity(entity_id)
            if entity:
                r = await self._search_companies(entity["name"], person["id"], person["name"])
                results.append(r)
                r = await self._search_federal_spending(entity["name"], person["id"], person["name"])
                results.append(r)

        return results

    async def search_entity(self, entity: dict) -> list[SearchResult]:
        results = []
        r = await self._search_companies(entity["name"], entity["id"], entity["name"])
        results.append(r)

        if entity.get("lara_id"):
            r = await self._get_company_details(
                entity["lara_id"], "us_mi", entity["id"], entity["name"]
            )
            results.append(r)

        r = await self._search_federal_spending(entity["name"], entity["id"], entity["name"])
        results.append(r)

        r = await self._search_court_cases(entity["name"], entity["id"], entity["name"])
        results.append(r)

        return results

    async def _search_companies(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"companies: {name}",
        )
        try:
            with self._client() as client:
                data = client.search_companies(name=name, state="MI")
                result.raw_data = data if isinstance(data, dict) else {"response": str(data)}
                if isinstance(data, dict):
                    for co in data.get("companies", data.get("results", [])):
                        if isinstance(co, dict):
                            result.hits.append({
                                "name": co.get("name"),
                                "company_number": co.get("company_number"),
                                "jurisdiction": co.get("jurisdiction_code"),
                                "status": co.get("current_status"),
                                "incorporation_date": co.get("incorporation_date"),
                                "registered_address": co.get("registered_address_in_full"),
                                "agent": co.get("agent_name"),
                            })
                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            result.hits.append(item)
        except Exception as e:
            result.error = str(e)
        return result

    async def _get_company_details(
        self, company_id: str, jurisdiction: str, target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"company_details: {company_id} ({jurisdiction})",
        )
        try:
            with self._client() as client:
                data = client.get_company_details(
                    company_id=company_id, jurisdiction=jurisdiction
                )
                result.raw_data = data if isinstance(data, dict) else {"response": str(data)}
                if isinstance(data, dict):
                    result.hits.append(data)
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_court_cases(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"court_cases: {name}",
        )
        try:
            with self._client() as client:
                data = client.search_court_cases(party_name=name)
                result.raw_data = data if isinstance(data, dict) else {"response": str(data)}
                if isinstance(data, dict):
                    for case in data.get("cases", data.get("results", [])):
                        if isinstance(case, dict):
                            result.hits.append({
                                "case_name": case.get("caseName") or case.get("case_name"),
                                "court": case.get("court") or case.get("court_name"),
                                "date_filed": case.get("dateFiled") or case.get("date_filed"),
                                "docket_number": case.get("docketNumber") or case.get("docket_number"),
                                "status": case.get("status"),
                                "url": case.get("absolute_url") or case.get("url"),
                            })
                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            result.hits.append(item)
        except Exception as e:
            result.error = str(e)
        return result

    async def _search_federal_spending(self, name: str, target_id: str, target_name: str) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"federal_spending: {name}",
        )
        try:
            with self._client() as client:
                data = client.lookup_federal_spending(recipient_name=name)
                result.raw_data = data if isinstance(data, dict) else {"response": str(data)}
                if isinstance(data, dict):
                    for award in data.get("awards", data.get("results", [])):
                        if isinstance(award, dict):
                            result.hits.append({
                                "recipient": award.get("recipient_name"),
                                "agency": award.get("awarding_agency_name"),
                                "amount": award.get("total_obligation"),
                                "description": award.get("description") or award.get("award_description"),
                                "date": award.get("action_date") or award.get("date_signed"),
                            })
                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            result.hits.append(item)
        except Exception as e:
            result.error = str(e)
        return result

