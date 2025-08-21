# FreeFire-TelegramBot (Heroku + Likes)

Telegram bot skeleton mirroring FreeFire-style commands with **global likes** for UIDs, maps, and banners.
- Python (aiogram v3), async
- Redis for like counters (auto-detects `REDIS_URL` on Heroku)
- Heroku-ready (`Procfile`, `runtime.txt`)

## Commands
- `get {uid}`
- `wishlist {uid}`
- `isbanned {uid}`
- `region {uid}`
- `mapinfo {region} {map_code}`
- `Rank {region} {mode}`
- `{region} banner`
- `like {uid}`
- `like_map {map_code}`
- `like_banner {banner_id}`

> All service handlers are stubs. Plug in your own public/authorized sources in `bot/app/services/*`.

## Local Run
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# set TELEGRAM_BOT_TOKEN in .env
python -m bot.main
```

## Deploy to Heroku
```bash
heroku create my-ff-bot
git init && git add . && git commit -m "deploy"
heroku git:remote -a my-ff-bot
git push heroku main
heroku config:set TELEGRAM_BOT_TOKEN=123:abc
heroku addons:create heroku-redis:hobby-dev
heroku ps:scale worker=1
```

## 👍 Likes System (Global)
- `like {uid}` → increments likes for a player UID
- `like_map {map_code}` → increments likes for a map
- `like_banner {banner_id}` → increments likes for a banner
- `get`, `mapinfo`, `banner` responses include current like totals (fields included in stubs).

### Heroku Redis
Heroku sets `REDIS_URL` automatically; the bot parses it for you.
