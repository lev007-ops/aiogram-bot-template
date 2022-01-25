from aiogram import types

from data.config import BOT_COMMANDS


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(c[0], c[1]) for c in BOT_COMMANDS
        ]
    )
