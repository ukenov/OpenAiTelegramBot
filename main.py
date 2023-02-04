from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
import os

client.register_handlers_client(dp)
executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=admin.on_startup,
    on_shutdown=admin.on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
