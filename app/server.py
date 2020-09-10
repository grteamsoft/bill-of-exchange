from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters,\
    CallbackQueryHandler
import os, datetime
import logging.config
import keyboard, psycopg2

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
    # now = datetime.datetime.now()
    chat_id = update.effective_message.chat_id
    #current_text =update.effective_message.text

    def ADD_DEBT_KEYBOARD():
        context.bot.send_message(
            chat_id=chat_id,
            text="Add a new contact to send a request or \n"
                 "choose from the list with whom you have already worked",
            reply_markup=keyboard.get_add_debt_keyboard(),
        )

    def DEBT_KEYBOARD():
        context.bot.send_message(
            chat_id=chat_id,
            text=" There will be something like a menu in which it will be visible to whom you have already sent requests \n"
                 "Each button below the message will connect you with the contact you have already contacted.\n"
                 "I also don’t know how to implementь",
            reply_markup=keyboard.get_debt_keyboard_inline(),
        )

    def GET_KEYBOARD():
        context.bot.send_message(
            chat_id=chat_id,
            text="Choose an action",
            reply_markup=keyboard.get_keyboard_inline()
        )

    def select_keyboard(argument):
        switcher = {
            keyboard.KEYBOARD_INLINE['ADD_DEBT_INLINE']['code'] : ADD_DEBT_KEYBOARD,
            keyboard.KEYBOARD_INLINE['LIST_DEBT_INLINE']['code']: DEBT_KEYBOARD,
            keyboard.KEYBOARD_INLINE['BACK_INLINE']['code']: GET_KEYBOARD,
        }
        func = switcher.get(argument, lambda: "Error")
        return func()
    select_keyboard(data)

@debug_requests
def add_debt(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Add a new contact or select an existing one",
        reply_markup=keyboard.get_keyboard_inline()
    )

@debug_requests
def pay_debt(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="A list of lenders for payment will be displayed.",
        reply_markup=keyboard.get_debt_keyboard_inline()
    )

@debug_requests
def do_start(update, context):
    text = "Hello! This is a bot for tracking, sharing your purchases / accounts \n" \
           "For information, click the Information button."
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        reply_markup=keyboard.get_start_keyboard()
    )

@debug_requests
def do_echo(update, context):
    username = context.user_data
    chat_id = update.message.chat_id
    text = update.message.text
    if text == keyboard.ADD_DEBT_KEYBOARD:
        return add_debt(update, context)
    elif text == keyboard.PAY_DEBT_KEYBOARD:
        return pay_debt(update, context)
    elif text == keyboard.LIST_DEBT_KEYBOARD:
        return do_list_debt(update, context)
    elif text == keyboard.INFO_KEYBOARD:
        return do_info(update, context)
    else:
        reply_text = "USER ID = {} \n The bot is still under development\n" \
                     "You wrote: {}\n" \
                     "USERNAME = {}".format(chat_id, text, username)
        context.bot.send_message(
            chat_id=chat_id,
            text=reply_text,
            reply_markup = keyboard.get_start_keyboard(),
        )

def do_info(update, context):
    text = "With the help of the bot, you can share a common check!\n" \
           "To do this, click the add debt button, select the contact (or the name of the debtor)," \
           "and write the amount of debt in a line and for what, then send a request to the name of the debtor"

    """"""
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO USERS (telegram_id, last_name, first_name, create_at) VALUES (55555, 'Alex', 'Alexandr', '2020-09-10')")
    cursor.close()
    conn.commit()

    conn.close()

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        reply_markup=keyboard.get_start_keyboard()
    )

def do_list_debt(update, context):

    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    text = str(records)

    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text=text,
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
    dp = updater.dispatcher
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
