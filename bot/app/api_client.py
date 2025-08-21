import httpx

class ApiClient:
    """HTTP client wrapper. Plug your public/authorized endpoints or scraping here."""
    def __init__(self, base_url: str | None = None, headers: dict | None = None):
        self.base_url = base_url.rstrip('/') if base_url else None
        self.headers = headers or {}

    async def get(self, url: str, params: dict | None = None):
        full = url if not self.base_url else f"{self.base_url}{url}"
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(full, params=params, headers=self.headers)
            r.raise_for_status()
            return r.json()

    async def get_text(self, url: str, params: dict | None = None):
        full = url if not self.base_url else f"{self.base_url}{url}"
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(full, params=params, headers=self.headers)
            r.raise_for_status()
            return r.text
