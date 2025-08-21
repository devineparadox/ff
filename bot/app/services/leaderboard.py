from typing import Dict
from bot.app.api_client import ApiClient

api = ApiClient()

async def get_leaderboard(region: str, mode: str) -> Dict:
    """Return leaderboard for region/mode.
    Implement scraping/authorized endpoints here.
    """
    return {
        "region": region,
        "mode": mode,
        "top": [],
        "note": "Implement real datasource in services/leaderboard.py"
    }
