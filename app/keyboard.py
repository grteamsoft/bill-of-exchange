"""
This file will create button structures that we will use
"""
from telegram import InlineKeyboardButton, \
    InlineKeyboardMarkup, ParseMode, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

"""
Buttons from the bottom menu
"""
BUTTON1_ADD_DEBT = "ADD DEBT"
BUTTON2_PAY_DEBT = "PAY DEBT"
BUTTON3_LIST_DEBT = "LIST OF DEBTS"
BUTTON4_INFO = "INFORMATION"

"""
Menu buttons that will be in the chat
"""
CALLBACK_BUTTON1 = "callback_button1"
CALLBACK_BUTTON2 = "callback_button2"
CALLBACK_BUTTON3 = "callback_button3"
CALLBACK_BUTTON4 = "callback_button4"
CALLBACK_BUTTON5_BACK = "callback_button5_back"
CALLBACK_BUTTON6 = "callback_button6"
CALLBACK_BUTTON7 = "callback_button7"
CALLBACK_BUTTON8 = "callback_button8"
CALLBACK_BUTTON9 = "callback_button9"
CALLBACK_BUTTON10 = "callback_button10"
CALLBACK_BUTTON11 = "callback_button11"

TITLES = {
    CALLBACK_BUTTON1: "Add Debtor 🔥",
    CALLBACK_BUTTON2: "List of Debtors 📝",
    CALLBACK_BUTTON3: " Debtor 1",
    CALLBACK_BUTTON4: "Debtor 2",
    CALLBACK_BUTTON5_BACK: "Back 🔙",
    CALLBACK_BUTTON6: "Debtor 3",
    CALLBACK_BUTTON7: "Debtor 4",
    CALLBACK_BUTTON8: "Debtor 5",
    CALLBACK_BUTTON9: "Debtor 6",
    CALLBACK_BUTTON10: "Find/Add Contact",
    CALLBACK_BUTTON11: "List of Contacts"}

"""
Creating the structure of buttons in the chat menu
"""
def get_keyboard_inline():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1], callback_data=CALLBACK_BUTTON1),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2], callback_data=CALLBACK_BUTTON2)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_BACK], callback_data=CALLBACK_BUTTON5_BACK)
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_add_debt_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON10], callback_data=CALLBACK_BUTTON10),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON11], callback_data=CALLBACK_BUTTON11),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_BACK], callback_data=CALLBACK_BUTTON5_BACK)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_debt_keyboard_inline():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3], callback_data=CALLBACK_BUTTON3),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4], callback_data=CALLBACK_BUTTON4)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6], callback_data=CALLBACK_BUTTON6),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7], callback_data=CALLBACK_BUTTON7)
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8], callback_data=CALLBACK_BUTTON8),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON9], callback_data=CALLBACK_BUTTON9)
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

"""
creating bottom menu buttons
"""
def get_start_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON1_ADD_DEBT),
            KeyboardButton(BUTTON2_PAY_DEBT),
        ],
        [
            KeyboardButton(BUTTON3_LIST_DEBT)
        ],
        [
            KeyboardButton(BUTTON4_INFO)
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True)
