import redis
from bot.config import settings, parse_redis_url

def get_redis():
    if settings.REDIS_URL:
        # Use REDIS_URL from Heroku
        return redis.from_url(settings.REDIS_URL, decode_responses=True)
    else:
        # Fallback to manual settings
        return redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD or None,
            decode_responses=True,
        )

def incr_like(key: str) -> int:
    r = get_redis()
    return r.incr(key)

def get_count(key: str) -> int:
    r = get_redis()
    val = r.get(key)
    try:
        return int(val) if val is not None else 0
    except (TypeError, ValueError):
        return 0

def uid_key(uid: str) -> str:
    return f"like:uid:{uid}"

def map_key(code: str) -> str:
    return f"like:map:{code}"

def banner_key(bid: str) -> str:
    return f"like:banner:{bid}"
