from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import openai
import os
import environ

env = environ.Env()
environ.Env.read_env()

bot = Bot(token=str(os.environ['TOKEN_TELEGRAM']))
openai.api_key = str(os.environ['TOKEN_OPENAI'])
dp = Dispatcher(bot)