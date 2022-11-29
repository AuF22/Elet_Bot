""""""
from aiogram import types
from loader import dp
from keyboards.default.keyboard_rus import kb_rus
from keyboards.inline.ikb_loans_rus import ikb_loan
from aiogram.types import CallbackQuery
from keyboards.inline.ikb_payments_rus import ikb_payment


@dp.message_handler(text='RU')
async def russian(message: types.Message):
    await message.answer(text='Вы выбрали русский язык', reply_markup=kb_rus)


@dp.message_handler(text='Кредиты')
async def loans(message: types.Message):
    text = """
Выберите один из нижеследующих продуктов
    """
    await message.answer(text=text, reply_markup=ikb_loan)


@dp.message_handler(text="Способы оплаты")
async def payment_methods(message: types.Message):
    text = """
Погасить кредит Компании можно через:

Для оплаты кредита достаточно в меню экрана или по поисковику найти услугу приема платежей на погашение кредитов МФК "Элет-Капитал", ввести № кредитного договора, удостовериться в правильности ввода № договора по совпадению букв на экране с вашим ФИО и внести сумму погашения.
"""
    await message.answer(text=text, reply_markup=ikb_payment)


@dp.message_handler(text='Онлайн кредиты')
async def online(message: types.Message):
    await message.answer(text='В скором времени добавим инструкцию')


@dp.message_handler(text='Наши Филиалы')
async def our_branch(message: types.Message):
    text = """

"""
    await message.answer(text='Скоро...')


@dp.message_handler(text='Связаться с оператором')
async def call_center(message: types.Message):
    message_id_f = message.message_id
    await message.answer("""Пожалуйста отправьте сообщение в следующей форме:
Суть вашего вопроса
Удобное для вас способ связи (Telegram/WhatsApp/Telephone)
Ваши контактные данные для связи
Пример сообщения:""")
    await message.answer("""
Добрый день, у меня не получается пройти идентификацию в личном кабинете
Telegram
0 700 12 34 56
""")

    async def send_to_call():
        @dp.message_handler(content_types='text')
        async def sender(msg: types.Message):
            await dp.bot.send_message(chat_id=655771477, text=msg.text)
            await msg.answer("Ваше письмо отправлено, в скором времени с вами свяжутся")

    await send_to_call()
