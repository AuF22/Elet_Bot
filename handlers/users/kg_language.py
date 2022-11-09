from loader import dp
from keyboards.default.keyboard_kg import kb_kg
from aiogram import types


@dp.message_handler(text='KG')
async def kyrgyz(message: types.Message):
    await message.answer(text='Сиз кыргыз тилин тандадыныз', reply_markup=kb_kg)