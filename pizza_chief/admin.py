import os

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types
from common.create_bot import dp,bot


class Admin(StatesGroup):
    photo = State()
    name = State()
    desc = State()
    price = State()


async def cm_load(message: types.Message):
    if message.from_user.id != int(os.getenv('ADMIN_1_ID')):
        await message.answer('Get lost!')
        return
    await Admin.photo.set()
    await message.reply('Load photo')



async def cm_cancel(message: types.Message, state: FSMContext):
    await message.answer('CANCELED')
    await state.reset_state()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await Admin.next()
    await message.reply('Enter name')


async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Admin.next()
    await message.reply('Enter description')


async def get_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await Admin.next()
    await message.reply('Enter price')


async def get_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    # here must be adding variable "state" to database
    await message.reply('Success')
    await state.finish()


def register_admin_handlers():
    dp.register_message_handler(cm_load, commands=['load'], state=None)
    dp.register_message_handler(cm_cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cm_cancel, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=Admin.photo)
    dp.register_message_handler(get_name, state=Admin.name)
    dp.register_message_handler(get_desc, state=Admin.desc)
    dp.register_message_handler(get_price, state=Admin.price)
