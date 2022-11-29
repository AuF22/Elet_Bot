from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_payment = InlineKeyboardMarkup(row_width=1,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text='Платежные терминалы', callback_data='Платежные терминалы')],
                                       [InlineKeyboardButton(text='Платежные карты ЭЛКАРТ', callback_data='Платежные карты ЭЛКАРТ')],
                                       [InlineKeyboardButton(text='Электронные кошельки', callback_data='Электронные кошельки')],
                                       [InlineKeyboardButton(text='Кассы', callback_data='Кассы')]
                                   ])