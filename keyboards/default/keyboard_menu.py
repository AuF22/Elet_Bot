from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='RU'),
        KeyboardButton(text='KG')
    ],
    [
        KeyboardButton(text='Привет')
    ]
])
