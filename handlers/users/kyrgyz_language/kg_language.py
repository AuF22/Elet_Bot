from loader import dp
from keyboards.default.keyboard_kg import kb_kg
from aiogram import types
from keyboards.inline.ikb_loans_kg import ikb_loan
from keyboards.inline.ikb_payments_kg import ikb_payment


@dp.message_handler(text='KG')
async def kyrgyz(message: types.Message):
    await message.answer(text='Сиз кыргыз тилин тандадыныз', reply_markup=kb_kg)


@dp.message_handler(text='Насыялар')
async def loans(message: types.Message):
    text = """
Төмөнкү өнүмдөрдүн бирин тандаңыз
    """
    await message.answer(text=text, reply_markup=ikb_loan)


@dp.message_handler(text="Төлөө ыкмалары")
async def payment_methods(message: types.Message):
    text = """
Погасить кредит Компании можно через:

Для оплаты кредита достаточно в меню экрана или по поисковику найти услугу приема платежей на погашение кредитов МФК "Элет-Капитал", ввести № кредитного договора, удостовериться в правильности ввода № договора по совпадению букв на экране с вашим ФИО и внести сумму погашения.
"""
    await message.answer(text=text, reply_markup=ikb_payment)


@dp.message_handler(text='Онлайн насыялар')
async def online(message: types.Message):
    await message.answer(text='Жакында инструкцияны кошобуз')


@dp.message_handler(text='Биздин Филиалдар')
async def our_branch(message: types.Message):
    text = """

"""
    await message.answer(text='Скоро...')


@dp.message_handler(text='Адис менен байланышуу')
async def call_center(message: types.Message):
    message_id_f = message.message_id
    await message.answer("""Сураныч төмөнкү формада билдирүү жөнөтүңүз:
Сурооңуздун маңызы
Сизге ыңгайлуу байланыш ыкмасы (Telegram/WhatsApp/Telephone)
Байланыш үчүн байланыш маалыматыңыз
Мисалы:""")
    await message.answer("""
Саламатсызбы, мен идентификациядан өтө албай жатам
Telegram
0 700 12 34 56
""")

    async def send_to_call():
        @dp.message_handler(content_types='text')
        async def sender(msg: types.Message):
            await dp.bot.send_message(chat_id=655771477, text=msg.text)
            await msg.answer("Сиздин кат жөнөтүлдү, жакында сиз менен адис байланышат")

    await send_to_call()
