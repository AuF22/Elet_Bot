from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_rus = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Кредиты'),
        KeyboardButton(text='Способы оплаты')
    ],
    [
        KeyboardButton(text='Онлайн кредиты'),
        KeyboardButton(text='Наши Филиалы')
    ],
    [
        KeyboardButton(text='Связаться с оператором')
    ],
], resize_keyboard=True)
