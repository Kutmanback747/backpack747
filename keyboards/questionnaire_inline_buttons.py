from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Math",
        callback_data="Math"
    )
    mojo_button = InlineKeyboardButton(
        "English 🔥",
        callback_data="english"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def python_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_math"
    )
    python_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_math"
    )
    markup.add(python_button)
    markup.add(python_no_button)
    return markup