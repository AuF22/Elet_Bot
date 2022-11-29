from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_loan = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text='Онлайн кредиты', callback_data='Онлайн кредиты')],
                                    [InlineKeyboardButton(text='До зарплаты', callback_data='До зарплаты')],
                                    [InlineKeyboardButton(text='Доступный', callback_data='Доступный')],
                                    [InlineKeyboardButton(text='Обеспеченный', callback_data='Обеспеченный')],
                                    [InlineKeyboardButton(text='Элет Кредиты', callback_data='Элет Кредиты')],
                                    [InlineKeyboardButton(text='Элет-Курулуш', callback_data='Элет-Курулуш_rus')]
                                ])
