from aiogram import types, Dispatcher
from create_bot import dp, bot
import os


async def on_startup(dp):
    await bot.set_webhook(str(os.environ['URL_APP']))

async def on_shutdown(dp):
    await bot.delete_webhook()