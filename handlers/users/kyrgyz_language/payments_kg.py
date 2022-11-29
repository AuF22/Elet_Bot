""""""
from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.ikb_payments_kg import ikb_payment
from aiogram.utils.markdown import hlink


@dp.callback_query_handler(text='Төлөм терминалдары')
async def terminals(call: CallbackQuery):
    text = """
УДОБНО погасить кредит, не приходя в офис Компании, через платежные терминалы наших партнеров.

ПЛАТЕЖНЫЕ ТЕРМИНАЛЫ
1. В терминалах операторов платежных систем в меню экрана или по поисковику Вам необходимо найти услугу МФК "Элет-Капитал",
2. Ввести номер кредитного договора и удостовериться в соответствии информации на экране инициалам Заемщика (ФИО),
3. Внести сумму погашения в купюроприёмник платёжного терминала и по завершению операции получить чек с платёжного терминала

Башка төлөм ыкмалары:
"""
    list_for_terminals = ikb_payment['inline_keyboard'][::]
    del list_for_terminals[0]
    ikb_for_terminal = {'inline_keyboard': list_for_terminals}
    await call.message.edit_text(text=text, reply_markup=ikb_for_terminal)


@dp.callback_query_handler(text='Элкарт төлөм карталары')
async def elcart(call: CallbackQuery):
    text = """
УДОБНО и БЫСТРО погасить кредит, не выходя из дома через мобильные приложения и электронные кошельки наших партнеров.

ПЛАТЕЖНЫЕ КАРТЫ ЭЛКАРТ
1. В мобильном приложение «Элкарт мобайл», в меню «Банковские услуги» Вам надо выбрать МФК "Элет-Капитал".
2. Ввести номер кредитного договора в поле лицевой счет, проверить ФИО заемщика и ввести сумму погашения кредита.
3. Убедиться, что погашение кредита прошло успешно и сформирован электронный чек.

Башка төлөм ыкмалары:
"""
    list_for_elcart = ikb_payment['inline_keyboard'][::]
    del list_for_elcart[1]
    ikb_for_elcart = {'inline_keyboard': list_for_elcart}
    await call.message.edit_text(text=text, reply_markup=ikb_for_elcart)


@dp.callback_query_handler(text='Электрондук капчыктар')
async def terminals(call: CallbackQuery):
    text = """
УДОБНО и БЫСТРО погасить кредит, не выходя из дома через мобильные приложения и электронные кошельки наших партнеров.

ЭЛЕКТРОННЫЕ КОШЕЛЬКИ «О! ДЕНЬГИ», «BALANCE», «MEGAPAY» «ЭЛСОМ»
1. Вам надо зайти в приложение электронного кошелька («О!Деньги» / «Balance» / «MegaPay» / «Элсом») найти услугу по приему погашения кредитов и выбрать МФК "Элет-Капитал"
2. Ввести номер кредитного договора и сумму к погашению кредита.
3. Убедиться, что операция по погашению кредита проведена успешно и сформирован электронный чек.

Башка төлөм ыкмалары:
"""
    list_for_wallets = ikb_payment['inline_keyboard'][::]
    del list_for_wallets[2]
    ikb_for_wallets = {'inline_keyboard': list_for_wallets}
    await call.message.edit_text(text=text, reply_markup=ikb_for_wallets)


@dp.callback_query_handler(text='Кассалар')
async def terminals(call: CallbackQuery):
    text_link = hlink('Реквизиты расчетных счетов МФК «Элет-Капитал»', 'https://elet.kg/index.php?option=com_content&view=article&id=19&Itemid=120&lang=ru')
    text = f"""
КАССЫ
1. Погашение кредита через кассы филиалов Компании и отделений коммерческих Банков производится в соответствии с процедурами Компании и Банка по расчетно-кассовому обслуживанию клиентов.
2. Вам необходимо правильно назвать номер кредитного договора для оформления операции по погашению кредита и сохранить квитанцию об оплате.
3. {text_link}

Башка төлөм ыкмалары:
"""
    list_for_cash = ikb_payment['inline_keyboard'][::]
    del list_for_cash[3]
    ikb_for_cash = {'inline_keyboard': list_for_cash}
    await call.message.edit_text(text=text, reply_markup=ikb_for_cash)
