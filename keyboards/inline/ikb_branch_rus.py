from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

branches = {
    'ГОЛОВОНОЙ ОФИС': """Адрес: г.Бишкек, ул. Московская, 125 (пересекает ул.Логвиненко)
Телефоны: 0 (550) 933811, 0 (701) 933811,0 (777) 933811
Эл.почта: elet@elet.kg
Режим работы: 8:30-17:00
Перерыв: 12:00-13:00"""
}


ikb_next = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text='Следующий', callback_data='')]
                                ])
