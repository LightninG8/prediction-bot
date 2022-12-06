from aiogram import types, Dispatcher
import random
import inspect

from create_bot import bot
from messages import MESSAGES

async def new_chat_member (message: types.Message):
  bot_obj = await bot.get_me()
  bot_id = bot_obj.id
  
  for chat_member in message.new_chat_members:
    if chat_member.id == bot_id:
      await message.reply(
        inspect.cleandoc(f'''
        Привет, я бот предсказаний!

        Я бот предсказаний! Отправь мне эмодзи "🥠" и получи предсказание на Новый год!“
      ''')
      )

# регистрируем хэндлеры
def register_handlers_bot_messages(dp: Dispatcher):
  dp.register_message_handler(new_chat_member, content_types=['new_chat_members'])
