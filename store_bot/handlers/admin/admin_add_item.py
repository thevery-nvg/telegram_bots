from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os

from store_bot.alc_database import add_item as db_add_item
from store_bot import aio_keyboards as kb


class NewOrder(StatesGroup):
    type = State()
    name = State()
    desc = State()
    price = State()
    photo = State()


async def add_item_type(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_1_ID')):
        await NewOrder.type.set()
        await message.answer("Выберите тип товара", reply_markup=kb.catalog_list)
    else:
        await message.reply('Я вас не понимаю')


async def add_item_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = call.data
    await call.message.reply("Напишите название товара", reply_markup=kb.cancel)
    await NewOrder.next()


async def add_item_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Напишите описание товара")
    await NewOrder.next()


async def add_item_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await message.answer("Напишите цену товара")
    await NewOrder.next()


async def add_item_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer("Отправьте фото")
    await NewOrder.next()


async def add_item_photo_error(message: types.Message):
    await message.answer('Это не фото!')


async def add_item_success(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await db_add_item(state)
    await message.answer("Товар успешно создан", reply_markup=kb.admin_panel)
    await state.finish()


def register_add_item(dp: Dispatcher):
    dp.register_message_handler(add_item_type, text="Добавить товар")
    dp.register_callback_query_handler(add_item_name, state=NewOrder.type)
    dp.register_message_handler(add_item_desc, state=NewOrder.name)
    dp.register_message_handler(add_item_price, state=NewOrder.desc)
    dp.register_message_handler(add_item_photo, state=NewOrder.price)
    dp.register_message_handler(add_item_photo_error, lambda message: not message.photo, state=NewOrder.photo)
    dp.register_message_handler(add_item_success, content_types=['photo'], state=NewOrder.photo)
