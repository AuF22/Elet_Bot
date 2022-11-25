from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_kg = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Насыялар'),
        KeyboardButton(text='Төлөө ыкмалары')
    ],
    [
        KeyboardButton(text='Онлайн насыялар'),
        KeyboardButton(text='Биздин Филиалдар')
    ],
    [
        KeyboardButton(text='Адис менен байланышуу')
    ],
], resize_keyboard=True)
