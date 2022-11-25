from aiogram import types
from loader import dp
from keyboards.default.keyboard_rus import kb_rus
from keyboards.inline.ikb_rus import ikb_loan
from aiogram.types import CallbackQuery


@dp.message_handler(text='RU')
async def russian(message: types.Message):
    await message.answer(text='Вы выбрали русский', reply_markup=kb_rus)


@dp.message_handler(text='Кредиты')
async def loans(message: types.Message):
    text = """
Выберите один из нижеследующих продуктов
    """
    await message.answer(text=text, reply_markup=ikb_loan)


@dp.callback_query_handler(text='Онлайн кредиты')
async def online_loan(call: CallbackQuery):
    await call.message.edit_reply_markup("""ОНЛАЙН КРЕДИТ
Целевые клиенты:
Граждане КР от 21 - 65 лет, с положительной или без кредитной истории, имеющие электронные кошельки (Balance.kg / О! Деньги / ЭЛСОМ) или платежную карту Элкарт любого банка КР

Сумма кредита: 
От 1 000 сом до 15 000 сом

Срок кредита:
До 6 месяцев

Процентная ставка:
5% в месяц (60% годовых)

Комиссия за обслуживание: 0%
Необходимые документы: ID паспорт заемщика

ДРУГИЕ КРЕДИТЫ:""", reply_markup=ikb_loan)
