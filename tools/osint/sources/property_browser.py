"""BS&A Online property search — browser-based scraper.

Covers most Michigan counties via bsaonline.com.
Searches by address and owner name.
"""

from __future__ import annotations
from sources.browser_source import BrowserSource, new_page
from models import SearchResult

BSA_URL = "https://bsaonline.com"

COUNTY_SLUGS = {
    "Wayne": "wayne-county-mi",
    "Macomb": "macomb-county-mi",
    "Monroe": "monroe-county-mi",
    "Oakland": "oakland-county-mi",
    "Ingham": "ingham-county-mi",
}


class PropertyBrowserSource(BrowserSource):
    name = "property_browser"

    async def search_person(self, person: dict) -> list[SearchResult]:
        prop_cfg = person.get("searches", {}).get("property")
        if not prop_cfg:
            return []

        results = []
        counties = prop_cfg.get("counties", ["Wayne"])

        r = await self._search_owner(
            person["name"], counties, person["id"], person["name"]
        )
        results.append(r)

        for addr in person.get("known_addresses", []):
            county = addr.get("county", "Wayne")
            r = await self._search_address(
                addr["address"], addr.get("city", ""),
                [county], person["id"], person["name"]
            )
            results.append(r)

        return results

    async def search_address(self, address: dict) -> list[SearchResult]:
        county = address.get("county", "Wayne")
        r = await self._search_address(
            address["address"], address.get("city", ""),
            [county], address["id"], address["address"]
        )
        return [r]

    async def _search_owner(
        self, name: str, counties: list[str], target_id: str, target_name: str
    ) -> SearchResult:
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"owner: {name} ({', '.join(counties)})",
        )
        try:
            async with new_page() as page:
                for county in counties:
                    slug = COUNTY_SLUGS.get(county, county.lower().replace(" ", "-") + "-mi")
                    url = f"{BSA_URL}/{slug}"
                    await self._goto_and_wait(page, url, timeout=20000)
                    await page.wait_for_timeout(2000)

                    search_input = page.locator(
                        "input[type='text'], input[type='search'], "
                        "input[placeholder*='search' i], input[placeholder*='name' i], "
                        "input[placeholder*='address' i]"
                    ).first

                    try:
                        await search_input.wait_for(timeout=8000)
                        await search_input.fill(name)
                        await page.keyboard.press("Enter")
                        await page.wait_for_timeout(3000)

                        text = await self._get_page_text(page)
                        result.raw_data[county] = {"url": page.url, "text_length": len(text)}
                        hits = self._parse_property_results(text, county, page.url)
                        result.hits.extend(hits)
                    except Exception as e:
                        result.hits.append({
                            "county": county,
                            "note": f"Search failed: {e}",
                            "url": page.url,
                        })

        except Exception as e:
            result.error = str(e)
        return result

    async def _search_address(
        self, address: str, city: str, counties: list[str],
        target_id: str, target_name: str
    ) -> SearchResult:
        query = f"{address}, {city}" if city else address
        result = SearchResult(
            source=self.name,
            target_id=target_id,
            target_name=target_name,
            query=f"address: {query}",
        )
        try:
            async with new_page() as page:
                for county in counties:
                    slug = COUNTY_SLUGS.get(county, county.lower().replace(" ", "-") + "-mi")
                    url = f"{BSA_URL}/{slug}"
                    await self._goto_and_wait(page, url, timeout=20000)
                    await page.wait_for_timeout(2000)

                    search_input = page.locator(
                        "input[type='text'], input[type='search'], "
                        "input[placeholder*='search' i], input[placeholder*='address' i]"
                    ).first

                    try:
                        await search_input.wait_for(timeout=8000)
                        await search_input.fill(query)
                        await page.keyboard.press("Enter")
                        await page.wait_for_timeout(3000)

                        text = await self._get_page_text(page)
                        result.raw_data[county] = {"url": page.url}
                        hits = self._parse_property_results(text, county, page.url)
                        result.hits.extend(hits)
                    except Exception as e:
                        result.hits.append({
                            "county": county,
                            "note": f"Search failed: {e}",
                            "url": page.url,
                        })

        except Exception as e:
            result.error = str(e)
        return result

    def _parse_property_results(self, text: str, county: str, url: str) -> list[dict]:
        hits = []
        lines = text.split("\n")

        current = {"county": county}
        for line in lines:
            line = line.strip()
            if not line:
                continue
            ll = line.lower()
            if "owner" in ll and ":" in line:
                current["owner"] = line.split(":", 1)[1].strip()
            elif "address" in ll and ":" in line:
                current["property_address"] = line.split(":", 1)[1].strip()
            elif "parcel" in ll and ":" in line:
                current["parcel_id"] = line.split(":", 1)[1].strip()
            elif "sev" in ll and ":" in line:
                current["sev"] = line.split(":", 1)[1].strip()
            elif "taxable" in ll and ":" in line:
                current["taxable_value"] = line.split(":", 1)[1].strip()
            elif "pre" in ll and "%" in line:
                current["pre_percentage"] = line
            elif "mortgage" in ll:
                current["mortgage_info"] = line

        if len(current) > 1:
            hits.append(current)

        if not hits:
            if "no results" in text.lower() or "no records" in text.lower():
                hits.append({"county": county, "note": "No results", "url": url})
            elif len(text) > 200:
                hits.append({
                    "county": county,
                    "note": "Results loaded — may need parser refinement",
                    "url": url,
                    "text_preview": text[:800],
                })
            else:
                hits.append({"county": county, "note": "Empty or error page", "url": url})

        return hits

