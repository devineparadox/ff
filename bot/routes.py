from aiogram import Router, F
from aiogram.types import Message
from bot.app.services.account import get_account_info, is_banned, get_wishlist, detect_region
from bot.app.services.craftland import get_map_info
from bot.app.services.leaderboard import get_leaderboard
from bot.app.services.banner import get_banners_by_region
from bot.app.storage.redis_likes import incr_like, get_count, uid_key, map_key, banner_key

router = Router()

def register_routes(dp):
    dp.include_router(router)

def format_as_kv(data: dict) -> str:
    if not data:
        return "No data."
    lines = []
    for k, v in data.items():
        lines.append(f"<b>{k}</b>: {v}")
    return "\n".join(lines)

@router.message(F.text.regexp(r"^get\s+(\d{5,})$", flags=0))
async def cmd_get(message: Message):
    uid = message.text.split()[1]
    data = await get_account_info(uid)
    await message.answer(format_as_kv(data))

@router.message(F.text.regexp(r"^wishlist\s+(\d{5,})$"))
async def cmd_wishlist(message: Message):
    uid = message.text.split()[1]
    data = await get_wishlist(uid)
    await message.answer(format_as_kv(data))

@router.message(F.text.regexp(r"^isbanned\s+(\d{5,})$"))
async def cmd_isbanned(message: Message):
    uid = message.text.split()[1]
    data = await is_banned(uid)
    await message.answer(format_as_kv(data))

@router.message(F.text.regexp(r"^region\s+(\d{5,})$"))
async def cmd_region(message: Message):
    uid = message.text.split()[1]
    data = await detect_region(uid)
    await message.answer(format_as_kv(data))

@router.message(F.text.regexp(r"^mapinfo\s+(\w+)\s+(.+)$"))
async def cmd_mapinfo(message: Message):
    _, region, code = message.text.split(maxsplit=2)
    data = await get_map_info(region.lower(), code.strip())
    await message.answer(format_as_kv(data))

@router.message(F.text.regexp(r"^Rank\s+(sg|vn|th|eu|cis|ind|br|me)\s+(br|cs)$", flags=0))
async def cmd_rank(message: Message):
    _, region, mode = message.text.split()
    data = await get_leaderboard(region.lower(), mode.lower())
    await message.answer(format_as_kv(data))

@router.message(F.text.regexp(r"^(sg|ind|cis|th|vn|tr|br|me)\s+banner$"))
async def cmd_banner(message: Message):
    region = message.text.split()[0].lower()
    data = await get_banners_by_region(region)
    await message.answer(format_as_kv(data))

# Likes
@router.message(F.text.regexp(r"^like\s+(\d{5,})$"))
async def cmd_like(message: Message):
    uid = message.text.split()[1]
    total = incr_like(uid_key(uid))
    await message.answer(f"👍 Liked UID <b>{uid}</b>. Total likes: <b>{total}</b>")

@router.message(F.text.regexp(r"^like_map\s+(.+)$"))
async def cmd_like_map(message: Message):
    code = message.text.split(maxsplit=1)[1]
    total = incr_like(map_key(code))
    await message.answer(f"🗺️ Liked map <b>{code}</b>. Total likes: <b>{total}</b>")

@router.message(F.text.regexp(r"^like_banner\s+(.+)$"))
async def cmd_like_banner(message: Message):
    bid = message.text.split(maxsplit=1)[1]
    total = incr_like(banner_key(bid))
    await message.answer(f"🖼️ Liked banner <b>{bid}</b>. Total likes: <b>{total}</b>")
