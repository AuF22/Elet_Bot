from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default.keyboard_menu import kb_menu
from loader import dp
from keyboards.default.keyboard_kg import kb_kg


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    text = """
Саламатсызбы! Сиздерди "Элет-Капитал" ЖАК МФК кабыл алды.
Тейлоо тилин танданыз

Здравствуйте, Вас приветствует ЗАО МФК "Элет-Капитал".
Выберите язык обслуживания

-----------------------------
🔹 RU - Русский язык
🔹 KG - Кыргыз тили
-----------------------------
"""
    await message.answer(text=text, reply_markup=kb_menu)
