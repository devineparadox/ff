from typing import Dict
from bot.app.api_client import ApiClient
from bot.app.utils.uid_region import region_from_uid
from bot.app.storage.redis_likes import get_count, uid_key

api = ApiClient()

async def get_account_info(uid: str) -> Dict:
    """Return basic account info by UID.
    Implement using public/authorized data sources. This stub returns demo data.
    """
    likes = get_count(uid_key(uid))
    return {
        "uid": uid,
        "nickname": "Unknown",
        "level": "N/A",
        "guild": "N/A",
        "likes": likes,
        "note": "Implement real datasource in services/account.py"
    }

async def get_wishlist(uid: str) -> Dict:
    return {
        "uid": uid,
        "wishlist": [],
        "note": "Implement real datasource in services/account.py"
    }

async def is_banned(uid: str) -> Dict:
    likes = get_count(uid_key(uid))
    return {
        "uid": uid,
        "banned": False,
        "likes": likes,
        "note": "Implement real datasource in services/account.py"
    }

async def detect_region(uid: str) -> Dict:
    region = region_from_uid(uid)
    return {"uid": uid, "region": region}
