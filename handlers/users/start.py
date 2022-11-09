from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default.keyboard_menu import kb_menu
from loader import dp
from keyboards.default.keyboard_kg import kb_kg


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    text = """
Саламатсызбы! Сиздерди "Элет-Капитал" ЖАК МФК кабыл алды.
\nЗдравствуйте, Вас приветствует ЗАО МФК "Элет-Капитал".
\nВыберите язык обслуживания
\nТейлоо тилин танданыз
-----------------------------
🔹 RU - Русский язык\n
🔹 KG - Кыргызский язык
-----------------------------
"""
    await message.answer(text=text, reply_markup=kb_menu)
