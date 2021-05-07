"""
This file will create button structures that we will use
"""
from telegram import InlineKeyboardButton, \
    InlineKeyboardMarkup, ParseMode, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

"""
Buttons from the bottom menu
"""
ADD_DEBT_KEYBOARD = "ADD DEBT"
PAY_DEBT_KEYBOARD = "PAY DEBT - DELETE"
LIST_DEBT_KEYBOARD = "LIST OF DEBTS - OUTPUT"
INFO_KEYBOARD = "INFORMATION - INSERT"
TABLE_TRANSACTION = "TABLE OF TRANSACTIONS"

"""
Menu buttons that will be in the chat
"""

KEYBOARD_INLINE = {'ADD_DEBT_INLINE': {'code': "ADD_DEBT_INLINE", 'label': "Add Debtor 🔥"},
                   'LIST_DEBT_INLINE': {'code': "LIST_DEBT_INLINE", 'label': "List of Debtors 📝"},
                   'DEBTOR_INLINE': {'code': "DEBTOR_INLINE", 'label': "Debtor 1"},
                   'BACK_INLINE': {'code': "BACK_INLINE", 'label': "Back 🔙"},
                   'FIND_CONT_INLINE': {'code': "FIND_CONT_INLINE", 'label': "Find/Add Contact"},
                   'LIST_CONT_INLINE': {'code': "LIST_CONT_INLINE", 'label': "List of Contacts"}}
"""
Creating the structure of buttons in the chat menu
"""
def get_keyboard_inline():
    keyboard = [
        [
            InlineKeyboardButton(KEYBOARD_INLINE['ADD_DEBT_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['ADD_DEBT_INLINE']['code']),
            InlineKeyboardButton(KEYBOARD_INLINE['LIST_DEBT_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['LIST_DEBT_INLINE']['code'])
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE['BACK_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['BACK_INLINE']['code'])
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_add_debt_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(KEYBOARD_INLINE['FIND_CONT_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['FIND_CONT_INLINE']['code']),
            InlineKeyboardButton(KEYBOARD_INLINE['LIST_CONT_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['LIST_CONT_INLINE']['code']),
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE['BACK_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['BACK_INLINE']['code'])
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_debt_keyboard_inline():
    keyboard = [
        [
            InlineKeyboardButton(KEYBOARD_INLINE['DEBTOR_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['DEBTOR_INLINE']['code']),
            InlineKeyboardButton(KEYBOARD_INLINE['DEBTOR_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['DEBTOR_INLINE']['code'])
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE['DEBTOR_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['DEBTOR_INLINE']['code']),
            InlineKeyboardButton(KEYBOARD_INLINE['DEBTOR_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['DEBTOR_INLINE']['code'])
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE['BACK_INLINE']['label'],
                                 callback_data=KEYBOARD_INLINE['BACK_INLINE']['code'])
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

"""
creating bottom menu buttons
"""
def get_start_keyboard():
    keyboard = [
        [
            KeyboardButton(ADD_DEBT_KEYBOARD),
            KeyboardButton(PAY_DEBT_KEYBOARD),
        ],
        [
            KeyboardButton(LIST_DEBT_KEYBOARD)
        ],
        [
            KeyboardButton(INFO_KEYBOARD),
            KeyboardButton(TABLE_TRANSACTION),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True)
