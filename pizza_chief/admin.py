from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from common.create_bot import dp


class Admin(StatesGroup):
    photo = State()
    name = State()
    desc = State()
    price = State()


@dp.message_handler(commands=['load'], state=None)
async def cm_start(message: types.Message):
    await Admin.photo.set()
    await message.reply('Load photo')


@dp.message_handler(content_types=['photo'], state=Admin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await Admin.next()
    await message.reply('Enter name')


@dp.message_handler(state=Admin.name)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Admin.next()
    await message.reply('Enter description')


@dp.message_handler(state=Admin.desc)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await Admin.next()
    await message.reply('Enter price')


@dp.message_handler(state=Admin.price)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    # here must be adding variable "state" to database
    await message.reply('Success')
    await state.finish()
