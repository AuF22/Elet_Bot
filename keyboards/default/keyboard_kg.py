from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_kg = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='1'),
        KeyboardButton(text='2')
    ],
    [
        KeyboardButton(text='3'),
        KeyboardButton(text='4')
    ]
])
