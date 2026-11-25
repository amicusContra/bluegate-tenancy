"""Scraping proxy — routes requests through ScrapingAnt or ScrapFly for Cloudflare bypass.

Provides a drop-in `fetch_url` function that:
1. Tries ScrapingAnt if SCRAPINGANT_API_KEY is set (10k free credits/month)
2. Falls back to ScrapFly if SCRAPFLY_API_KEY is set (1k free credits/month)
3. Falls back to direct httpx fetch if no proxy key is available

ScrapingAnt: JS rendering + residential proxy, returns rendered HTML
ScrapFly: JS rendering + anti-bot bypass, returns rendered HTML
"""

from __future__ import annotations
import httpx
from config import get_key


def _get_scrapingant_key() -> str | None:
    return get_key("SCRAPINGANT_API_KEY")


def _get_scrapfly_key() -> str | None:
    return get_key("SCRAPFLY_API_KEY")


def proxy_available() -> bool:
    return bool(_get_scrapingant_key() or _get_scrapfly_key())


async def fetch_url(
    url: str,
    js_render: bool = True,
    timeout: int = 60,
    proxy_name: str | None = None,
) -> dict:
    """Fetch a URL through scraping proxy, returning rendered HTML.

    Args:
        url: Target URL to fetch
        js_render: Enable JavaScript rendering (needed for SPA/React sites)
        timeout: Request timeout in seconds
        proxy_name: Force a specific proxy ("scrapingant" or "scrapfly")

    Returns:
        dict with keys: html, status_code, url, proxy_used, error
    """
    result = {"html": "", "status_code": 0, "url": url, "proxy_used": None, "error": None}

    ant_key = _get_scrapingant_key()
    fly_key = _get_scrapfly_key()

    if proxy_name == "scrapingant" or (not proxy_name and ant_key):
        if ant_key:
            r = await _fetch_scrapingant(url, ant_key, js_render, timeout)
            if r["status_code"] == 200 and len(r.get("html", "")) > 500:
                return r
            # Log why proxy failed but continue to next option
            if not result.get("error"):
                result = r

    if proxy_name == "scrapfly" or (not proxy_name and fly_key and result.get("status_code") != 200):
        if fly_key:
            r = await _fetch_scrapfly(url, fly_key, js_render, timeout)
            if r["status_code"] == 200 and len(r.get("html", "")) > 500:
                return r
            if not result.get("error"):
                result = r

    if result.get("status_code") != 200 or len(result.get("html", "")) < 500:
        r = await _fetch_direct(url, timeout)
        if r["status_code"] == 200 and "cloudflare" not in r.get("html", "").lower()[:1000]:
            return r
        if not result.get("html"):
            result = r

    return result


async def _fetch_scrapingant(url: str, api_key: str, js_render: bool, timeout: int) -> dict:
    """Fetch via ScrapingAnt Web Scraping API."""
    result = {"html": "", "status_code": 0, "url": url, "proxy_used": "scrapingant", "error": None}
    try:
        params = {
            "url": url,
            "x-api-key": api_key,
            "browser": "true" if js_render else "false",
            "proxy_type": "residential",
            "wait_for_selector": "body",
        }
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(
                "https://api.scrapingant.com/v2/general",
                params=params,
            )
            result["status_code"] = resp.status_code
            if resp.status_code == 200:
                result["html"] = resp.text
            elif resp.status_code == 404:
                result["error"] = f"ScrapingAnt: site unreachable (Cloudflare may be blocking)"
            elif resp.status_code == 422:
                result["error"] = f"ScrapingAnt rejected URL (422): {resp.text[:200]}"
            elif resp.status_code == 423:
                result["error"] = "ScrapingAnt: API credits exhausted"
            else:
                result["error"] = f"ScrapingAnt HTTP {resp.status_code}: {resp.text[:200]}"
    except httpx.TimeoutException:
        result["error"] = "ScrapingAnt timeout (JS rendering can take 30-60s)"
    except Exception as e:
        result["error"] = f"ScrapingAnt error: {e}"
    return result


async def _fetch_scrapfly(url: str, api_key: str, js_render: bool, timeout: int) -> dict:
    """Fetch via ScrapFly Web Scraping API."""
    result = {"html": "", "status_code": 0, "url": url, "proxy_used": "scrapfly", "error": None}
    try:
        params = {
            "key": api_key,
            "url": url,
            "render_js": "true" if js_render else "false",
            "asp": "true",  # anti-scraping protection bypass
            "country": "us",
        }
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(
                "https://api.scrapfly.io/scrape",
                params=params,
            )
            result["status_code"] = resp.status_code
            if resp.status_code == 200:
                data = resp.json()
                result["html"] = data.get("result", {}).get("content", "")
                result["status_code"] = data.get("result", {}).get("status_code", 200)
            else:
                result["error"] = f"ScrapFly HTTP {resp.status_code}: {resp.text[:200]}"
    except Exception as e:
        result["error"] = f"ScrapFly error: {e}"
    return result


async def _fetch_direct(url: str, timeout: int) -> dict:
    """Direct fetch without proxy (fallback)."""
    result = {"html": "", "status_code": 0, "url": url, "proxy_used": "direct", "error": None}
    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            resp = await client.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/128.0.0.0 Safari/537.36",
                },
            )
            result["status_code"] = resp.status_code
            result["html"] = resp.text
    except Exception as e:
        result["error"] = f"Direct fetch error: {e}"
    return result

