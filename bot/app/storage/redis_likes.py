import redis
from bot.config import settings, parse_redis_url

def get_redis():
    url = settings.REDIS_URL
    if url:
        parts = parse_redis_url(url) or {}
        pool = redis.ConnectionPool(
            host=parts.get('host', settings.REDIS_HOST),
            port=parts.get('port', settings.REDIS_PORT),
            db=parts.get('db', settings.REDIS_DB),
            password=(parts.get('password') or settings.REDIS_PASSWORD) or None,
            decode_responses=True,
        )
    else:
        pool = redis.ConnectionPool(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD or None,
            decode_responses=True,
        )
    return redis.Redis(connection_pool=pool)

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
