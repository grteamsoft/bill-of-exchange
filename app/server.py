import asyncio
import hashlib
import os
from aiogram import Bot, Dispatcher, executor, filters, types
from middlewares.access_middleware import AccessMiddleware

import db.db_service

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(AccessMiddleware(ADMIN_ID))


@dp.message_handler(filters.CommandStart())
async def send_aaa(message: types.Message):
    # So... At first I want to send something like this:
    await message.reply("Do you want to see many pussies? Are you ready?")

    # Wait a little...
    await asyncio.sleep(1)

    # Good bots should send chat actions...
    await types.ChatActions.upload_photo()

    # Create media group
    media = types.MediaGroup()

    # Attach local file
    # media.attach_photo(types.InputFile('data/cat.jpg'), 'Cat!')
    # More local files and more cats!
    # media.attach_photo(types.InputFile('data/cats.jpg'), 'More cats!')

    # You can also use URL's
    # For example: get random puss:
    media.attach_photo('http://lorempixel.com/400/200/cats/', 'Random cat.')

    # And you can also use file ID:
    # media.attach_photo('<file_id>', 'cat-cat-cat.')

    # Done! Send media group
    await message.reply_media_group(media=media)


# @dp.inline_handler()
# async def inline_echo(inline_query: types.InlineQuery):
#     # id affects both preview and content,
#     # so it has to be unique for each result
#     # (Unique identifier for this result, 1-64 Bytes)
#     # you can set your unique id's
#     # but for example i'll generate it based on text because I know, that
#     # only text will be passed in this example
#     text = inline_query.query or 'echo'
#     input_content = types.InputTextMessageContent(text)
#     result_id: str = hashlib.md5(text.encode()).hexdigest()
#     item = types.InlineQueryResultArticle(
#         id=result_id,
#         title=f'Result {text!r}',
#         input_message_content=input_content,
#     )
#     # don't forget to set cache_time=1 for testing (default is 300s or 5m)
#     await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


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
