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


# @dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 't-shirt':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You are choose t-shirts')
    elif callback_query.data == 'pants':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You are choose pants')
    elif callback_query.data == 'boots':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You are choose boots')
    elif callback_query.data == 'misc':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You are choose misc')




def register_misc_handlers(dp: Dispatcher):
    dp.register_message_handler(catalog_button, text='Каталог')
    dp.register_message_handler(cart_button, text='Корзина')
    dp.register_message_handler(contacts_button, text='Контакты')
    dp.register_callback_query_handler(callback_query_keyboard)
