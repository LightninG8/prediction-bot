from aiogram.utils import executor


from create_bot import dp


from handlers import predict, bot_messages

async def on_startup(chat_id):
  print('Bot has been started')




predict.register_handlers_predict(dp)
bot_messages.register_handlers_bot_messages(dp)


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
