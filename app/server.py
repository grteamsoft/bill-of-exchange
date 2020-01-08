import os
from aiogram import Bot, Dispatcher, executor, types
from middlewares.access_middleware import AccessMiddleware

import db.db_service

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(AccessMiddleware(ADMIN_ID))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm BillOfExchangeBot!\n\
    /help - help\n\
    /my_id - get my telegram id\n")


@dp.message_handler(commands=['my_id'])
async def get_id(message: types.Message):
    await message.answer("You telegram id: " + str(message.from_user.id))


@dp.message_handler(content_types=['text'])
async def send_echo(message: types.Message):
    await message.answer("Unknown command")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
