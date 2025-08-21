import redis
from bot.config import settings, parse_redis_url

# Global redis client (singleton)
def create_redis_client():
    if settings.REDIS_URL:
        parts = parse_redis_url(settings.REDIS_URL) or {}
        return redis.Redis(
            host=parts.get("host", settings.REDIS_HOST),
            port=parts.get("port", settings.REDIS_PORT),
            db=parts.get("db", settings.REDIS_DB),
            password=(parts.get("password") or settings.REDIS_PASSWORD) or None,
            decode_responses=True,
        )
    else:
        return redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD or None,
            decode_responses=True,
        )

# initialize once
redis_client = create_redis_client()

# ---------------------------
# Utility functions
# ---------------------------
def incr_like(key: str) -> int:
    """Increment like counter for a key."""
    return redis_client.incr(key)

def get_count(key: str) -> int:
    """Get integer value for a key."""
    val = redis_client.get(key)
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
