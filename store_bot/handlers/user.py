from aiogram import Dispatcher, types
import os
from common.create_bot import bot
from store_bot import alc_database as db, aio_keyboards as kb


async def cmd_start(message: types.Message):
    """Отвечает на команду /start"""
    await db.cmd_start_db(message.from_user.id, message.from_user.full_name)
    await message.answer_sticker(sticker='CAACAgQAAxkBAAIB5mR6_--SM_V4xu7dr7vS88WhIlMWAAJMCAAC0WEYUmM7uZq6kk8cLwQ')
    if message.from_user.id == int(os.getenv('ADMIN_1_ID')):
        await message.answer(f'Вы авторизованы как администратор, {message.from_user.full_name}',
                             reply_markup=kb.admin_keyboard)
    else:
        await message.answer(text=f"Welcome back, {message.from_user.full_name}", reply_markup=kb.main_keyboard)


async def show_catalog(callback_query: types.CallbackQuery):
    options = {
        'Футболки': 'Футболка',
        'Брюки': 'Брюки',
        'Обувь': 'Обувь',
        'misc': 'You are choose misc',
        'buy': 'fuck off',
        'addtocart': 'fuck off'

    }
    message_text = options.get(callback_query.data)
    if message_text:
        if callback_query.data in ['buy', 'addtocart']:
            await bot.send_message(chat_id=callback_query.from_user.id, text=f"{message_text.lower()}")
            return

        await bot.send_message(chat_id=callback_query.from_user.id, text=f"Вы выбрали {message_text.lower()}")
        items =await db.get_category_items(message_text)
        for item in items:
            await bot.send_photo(chat_id=callback_query.from_user.id,
                                 photo=item['photo'],
                                 caption=item['desc'],
                                 disable_notification=True,
                                 reply_markup=kb.buy)
            break


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_callback_query_handler(show_catalog)
