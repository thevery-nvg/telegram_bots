from aiogram import Dispatcher,types
import os
from create_bot import bot
import alc_database as db
import aio_keyboards as kb


# @dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """Отвечает на команду /start"""
    await db.cmd_start_db(message.from_user.id, message.from_user.full_name)
    await message.answer_sticker(sticker='CAACAgQAAxkBAAIB5mR6_--SM_V4xu7dr7vS88WhIlMWAAJMCAAC0WEYUmM7uZq6kk8cLwQ')
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизованы как администратор, {message.from_user.full_name}',
                             reply_markup=kb.admin_keyboard)
    else:
        await message.answer(text=f"Welcome back, {message.from_user.full_name}", reply_markup=kb.main_keyboard)

async def cmd_get_loc(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,text='Пожалуйста отправьте свое местоположение',reply_markup=kb.location_button)

async def read_loc(message:types.Message):
    print(message.location.latitude)
    print(message.location.longitude)



def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(cmd_start,commands=['start'])
    dp.register_message_handler(cmd_get_loc, commands=['loc'])
    dp.register_message_handler(read_loc,content_types=['location'])