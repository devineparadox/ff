from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")
    WEBHOOK_SECRET: str = os.getenv("WEBHOOK_SECRET", "")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB: int = int(os.getenv("REDIS_DB", "0"))
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "")

settings = Settings()

def parse_redis_url(url: str):
    """Parse redis://[:password]@host:port/db into parts."""
    if not url or not url.startswith("redis://"):
        return None
    body = url[len("redis://"):]
    password = ""
    host = "localhost"
    port = 6379
    db = 0
    if "@" in body:
        auth, rest = body.split("@", 1)
        password = auth[1:] if auth.startswith(":") else auth
    else:
        rest = body
    if "/" in rest:
        hostport, dbs = rest.split("/", 1)
        try:
            db = int(dbs)
        except ValueError:
            db = 0
    else:
        hostport = rest
    if ":" in hostport:
        host, port_s = hostport.split(":", 1)
        try:
            port = int(port_s)
        except ValueError:
            port = 6379
    else:
        host = hostport
    return {"host": host, "port": port, "db": db, "password": password}
