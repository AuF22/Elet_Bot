from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_loan = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text='Онлайн насыя', callback_data='Онлайн насыя')],
                                    [InlineKeyboardButton(text='Айлыкка чейин', callback_data='Айлыкка чейин')],
                                    [InlineKeyboardButton(text='Жеткиликтүү', callback_data='Жеткиликтүү')],
                                    [InlineKeyboardButton(text='Камсыздалган', callback_data='Камсыздалган')],
                                    [InlineKeyboardButton(text='Элет Насыялары', callback_data='Элет Насыялары')],
                                    [InlineKeyboardButton(text='Элет-Курулуш', callback_data='Элет-Курулуш_kg')]
                                ])
