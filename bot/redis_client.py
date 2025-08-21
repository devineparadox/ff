import redis
from config import settings, parse_redis_url

if settings.REDIS_URL:
    redis_config = parse_redis_url(settings.REDIS_URL)
    redis_client = redis.Redis(
        host=redis_config["host"],
        port=redis_config["port"],
        db=redis_config["db"],
        password=redis_config["password"],
        decode_responses=True,
    )
else:
    redis_client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
    )
