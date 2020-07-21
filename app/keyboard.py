"""
This file will create button structures that we will use
"""
from telegram import InlineKeyboardButton, \
    InlineKeyboardMarkup, ParseMode, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

"""
Buttons from the bottom menu
"""
ADD_DEBT_KEYBOARD = "ADD DEBT"
PAY_DEBT_KEYBOARD = "PAY DEBT"
LIST_DEBT_KEYBOARD = "LIST OF DEBTS"
INFO_KEYBOARD = "INFORMATION"

"""
Menu buttons that will be in the chat
"""
KEYBOARD_INLINE = [
    ["ADD_DEBT_INLINE", "Add Debtor 🔥"],
    ["LIST_DEBT_INLINE", "List of Debtors 📝"],
    ["DEBTOR_INLINE", "Debtor 1"],
    ["BACK_INLINE", "Back 🔙"],
    ["FIND_CONT_INLINE", "Find/Add Contact"],
    ["LIST_CONT_INLINE", "List of Contacts"]]

"""
Creating the structure of buttons in the chat menu
"""
def get_keyboard_inline():
    keyboard = [
        [
            InlineKeyboardButton(KEYBOARD_INLINE[0][1], callback_data=KEYBOARD_INLINE[0][0]),
            InlineKeyboardButton(KEYBOARD_INLINE[1][1], callback_data=KEYBOARD_INLINE[1][0])
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE[3][1], callback_data=KEYBOARD_INLINE[3][0])
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_add_debt_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(KEYBOARD_INLINE[4][1], callback_data=KEYBOARD_INLINE[4][0]),
            InlineKeyboardButton(KEYBOARD_INLINE[5][1], callback_data=KEYBOARD_INLINE[5][0]),
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE[3][1], callback_data=KEYBOARD_INLINE[3][0])
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_debt_keyboard_inline():
    keyboard = [
        [
            InlineKeyboardButton(KEYBOARD_INLINE[2][1], callback_data=KEYBOARD_INLINE[2][0]),
            InlineKeyboardButton(KEYBOARD_INLINE[2][1], callback_data=KEYBOARD_INLINE[2][0])
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE[2][1], callback_data=KEYBOARD_INLINE[2][0]),
            InlineKeyboardButton(KEYBOARD_INLINE[2][1], callback_data=KEYBOARD_INLINE[2][0])
        ],
        [
            InlineKeyboardButton(KEYBOARD_INLINE[2][1], callback_data=KEYBOARD_INLINE[2][0]),
            InlineKeyboardButton(KEYBOARD_INLINE[2][1], callback_data=KEYBOARD_INLINE[2][0])
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
            KeyboardButton(INFO_KEYBOARD)
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True)
