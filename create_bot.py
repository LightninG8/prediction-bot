from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config



bot = Bot(token=config.APP_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
