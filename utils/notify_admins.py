import logging
from aiogram import Dispatcher
from Data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            text = 'Бот был запущен'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as ex:
            logging.exception(ex)
