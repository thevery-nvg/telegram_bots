from store_bot.create_bot import bot
from aiogram import types, Dispatcher
from store_bot.aio_keyboards import catalog_list


async def catalog_button(message: types.Message):
    await message.answer('Выберите категорию', reply_markup=catalog_list)


async def cart_button(message: types.Message):
    await message.answer('Корзина пуста!')


async def contacts_button(message: types.Message):
    await message.answer('Нет контактов')


def register_misc_handlers(dp: Dispatcher):
    dp.register_message_handler(catalog_button, text='Каталог')
    dp.register_message_handler(cart_button, text='Корзина')
    dp.register_message_handler(contacts_button, text='Контакты')
