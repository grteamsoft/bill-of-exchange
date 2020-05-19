from telegram import Bot, Update, InlineKeyboardButton, \
    InlineKeyboardMarkup, ParseMode, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters,\
    CallbackQueryHandler
import os, logging, datetime, requests
from subprocess import Popen, PIPE
import logging.config
from keyboard import *


LOGGING = {
    'disable_existing_loggers': True,
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s.%(funcName)s | %(asctime)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
logging.config.dictConfig(LOGGING)
logger=logging.getLogger('scope.name')
stderr_log_handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(stderr_log_handler)


def debug_requests(f):
    """
    Telegram event decorator
    """
    def inner(*args, **kwargs):
        try:
            logger.info(f"Function call {f.__name__}")
            return f(*args, **kwargs)
        except Exception:
            logger.exception(f"Error in handler {f.__name__}")
            raise
    return inner


API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

"""
Handler for chat buttons
"""
def keyboard_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    data = query.data
    now = datetime.datetime.now()
    chat_id = update.effective_message.chat_id
    current_text =update.effective_message.text
    if data == CALLBACK_BUTTON1:
        context.bot.send_message(
            chat_id=chat_id,
            text="Add a new contact to send a request or \n"
                 "choose from the list with whom you have already worked",
            reply_markup=get_add_debt_keyboard(),
        )
    elif data == CALLBACK_BUTTON2:
        context.bot.send_message(
            chat_id=chat_id,
            text=" There will be something like a menu in which it will be visible to whom you have already sent requests \n"
                 "Each button below the message will connect you with the contact you have already contacted.\n"
                 "I also don’t know how to implementь",
            reply_markup=get_debt_keyboard_inline(),
        )
    elif data == CALLBACK_BUTTON5_BACK:
        context.bot.send_message(
            chat_id=chat_id,
            text="Choose an action",
            reply_markup=get_keyboard_inline()
        )

@debug_requests
def add_debt(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Add a new contact or select an existing one",
        reply_markup=get_keyboard_inline()
    )

@debug_requests
def pay_debt(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="A list of lenders for payment will be displayed.",
        reply_markup=get_debt_keyboard_inline()
    )

@debug_requests
def do_start(update, context):
    #chat_id =475038836
    text = "Hello! This is a bot for tracking, sharing your purchases / accounts \n" \
           "For information, click the Information button."
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        reply_markup=get_start_keyboard()
    )

@debug_requests
def do_echo(update, context):
    username = context.user_data
    chat_id = update.message.chat_id
    text = update.message.text
    if text == BUTTON1_ADD_DEBT:
        return add_debt(update, context)
    elif text == BUTTON2_PAY_DEBT:
        return pay_debt(update, context)
    elif text == BUTTON3_LIST_DEBT:
        return do_list_debt(update, context)
    elif text == BUTTON4_INFO:
        return do_info(update, context)
    else:
        reply_text = "USER ID = {} \n The bot is still under development\n" \
                     "You wrote: {}\n" \
                     "USERNAME = {}".format(chat_id, text, username)
        context.bot.send_message(
            chat_id=chat_id,
            text=reply_text,
            reply_markup = get_start_keyboard(),
        )

def do_info(update, context):
    text = "With the help of the bot, you can share a common check!\n" \
           "To do this, click the add debt button, select the contact (or the name of the debtor)," \
           "and write the amount of debt in a line and for what, then send a request to the name of the debtor"
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        reply_markup=get_start_keyboard()
    )

def do_list_debt(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text="A list of debtors will be displayed."
    )

def do_list_my_debt(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text="A list of my debts will be displayed."
    )


def main():
    logger.info("Start Bot ...")
    updater = Updater(API_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    #bot = Bot(token = API_TOKEN)
    #updater = Updater(bot=bot)

    start_handler = CommandHandler("start", do_start)
    info_handler = CommandHandler("info", do_info)

    message_handler = MessageHandler(Filters.command | Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)


    dp.add_handler(start_handler)

    dp.add_handler(info_handler)


    dp.add_handler(message_handler)
    dp.add_handler(buttons_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    logger.info('server started')
    main()