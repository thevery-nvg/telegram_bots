from create_bot import bot
from aiogram import types, Dispatcher
from aio_keyboards import catalog_list


# @dp.message_handler(text='Каталог')
async def catalog_button(message: types.Message):
    await message.answer('Выберите категорию', reply_markup=catalog_list)


# @dp.message_handler(text='Корзина')
async def cart_button(message: types.Message):
    await message.answer('Корзина пуста!')


# @dp.message_handler(text='Контакты')
async def contacts_button(message: types.Message):
    await message.answer('Нет контактов')


async def callback_query_keyboard(callback_query: types.CallbackQuery):
    options = {
        't-shirt': 'You are choose t-shirts',
        'pants': 'You are choose pants',
        'misc': 'You are choose misc',
        'boots': 'You are choose boots'

    }
    message_text = options.get(callback_query.data)
    if message_text:
        await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)


def register_misc_handlers(dp: Dispatcher):
    dp.register_message_handler(catalog_button, text='Каталог')
    dp.register_message_handler(cart_button, text='Корзина')
    dp.register_message_handler(contacts_button, text='Контакты')
    dp.register_callback_query_handler(callback_query_keyboard)
