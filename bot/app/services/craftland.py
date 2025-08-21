from typing import Dict
from bot.app.api_client import ApiClient
from bot.app.storage.redis_likes import get_count, map_key

api = ApiClient()

async def get_map_info(region: str, code: str) -> Dict:
    """Return Craftland map info by region and code.
    Implement scraping/authorized endpoints here.
    """
    likes = get_count(map_key(code))
    return {
        "region": region,
        "code": code,
        "name": "Unknown",
        "creator": "Unknown",
        "likes": likes,
        "note": "Implement real datasource in services/craftland.py"
    }
