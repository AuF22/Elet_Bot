from aiogram import types
from loader import dp
from keyboards.default.keyboard_rus import kb_rus


@dp.message_handler(text='RU')
async def russian(message: types.Message):
    await message.answer(text='Вы выбрали русский', reply_markup=kb_rus)