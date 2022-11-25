from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    text = """
Вы находитесь в главном меню, выберите язык обслуживания
Сиз негизги менюдасыз, тейлөө тилин тандаңыз

-----------------------------
🔹 RU - Русский язык
🔹 KG - Кыргыз тили
-----------------------------
"""
    await message.answer('Выберите язык обслуживания', reply_markup=kb_menu)
