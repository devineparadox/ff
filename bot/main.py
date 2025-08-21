import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.config import settings
from bot.routes import register_routes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("freefire-bot")

async def main():
    if not settings.TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set in environment")
    bot = Bot(settings.TELEGRAM_BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    register_routes(dp)

    @dp.message(CommandStart())
    async def start(m: Message):
        await m.answer("👋 FreeFire Bot ready. Try:\n<code>get 10000001</code>")

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
