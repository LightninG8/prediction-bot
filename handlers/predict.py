from aiogram import types, Dispatcher
import random
import inspect

from messages import MESSAGES

async def predict (message: types.Message):
  await message.reply(
    inspect.cleandoc(f'''
    🥠 {message.from_user.first_name}, предсказание для тебя:
    
    „{random.choice(MESSAGES)}“''')
  )

# регистрируем хэндлеры
def register_handlers_predict(dp: Dispatcher):
  dp.register_message_handler(predict, text_contains=['🥠'])
