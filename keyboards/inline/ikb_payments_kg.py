from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_payment = InlineKeyboardMarkup(row_width=1,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text='Төлөм терминалдары', callback_data='Төлөм терминалдары')],
                                       [InlineKeyboardButton(text='Элкарт төлөм карталары', callback_data='Элкарт төлөм карталары')],
                                       [InlineKeyboardButton(text='Электрондук капчыктар', callback_data='Электрондук капчыктар')],
                                       [InlineKeyboardButton(text='Кассалар', callback_data='Кассалар')]
                                   ])
