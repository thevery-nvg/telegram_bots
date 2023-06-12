from aiogram import types, Dispatcher
import os

from store_bot import aio_keyboards as kb
from .admin_add_item import register_add_item


async def admin_panel_button(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_1_ID')):
        await message.answer('Вы вошли в админ-панель', reply_markup=kb.admin_panel)
    else:
        await message.reply('Я вас не понимаю')


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_panel_button, text='Админ-панель')
    register_add_item(dp)
