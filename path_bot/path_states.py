from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BadRequest
from aiogram import types
from aiogram.dispatcher import FSMContext
from create_bot import bot, dp
from path_keyboards import create_keyboard, start_keyboard, create_disks_keyboard
from const import D, img_formats, video_formats
from pathlib import Path
import os


class PathState(StatesGroup):
    level_0 = State()
    level_1 = State()
    level_2 = State()
    level_3 = State()
    level_4 = State()
    level_5 = State()
    level_6 = State()
    level_7 = State()
    level_8 = State()
    level_9 = State()
    level_10 = State()
    level_11 = State()
    last_level = State()


async def _create_path(data):
    r = ''
    for i in data:
        r += data[i] + "\\\\"
    return Path(r)


async def _del_last_key(data: dict):
    for i in range(12, -1, -1):
        _key = f"level_{i}"
        if data.get(_key):
            del data[_key]
            break


async def _send_file(call, state, kb):
    if os.stat(Path(kb)).st_size > 5000000:
        await bot.send_message(call.from_user.id, f'Слишком большой файл (более 50мб)')
    else:
        try:
            if Path(kb).suffix in img_formats:
                await bot.send_photo(call.from_user.id, open(Path(kb), 'rb'))
            elif Path(kb).suffix in video_formats:
                await bot.send_video(call.from_user.id, open(Path(kb), 'rb'))
            else:
                await bot.send_document(call.from_user.id, open(Path(kb), 'rb'))
        except BadRequest:
            await bot.send_message(call.from_user.id, "Пустой файл!")
    D.clear()
    await bot.send_message(call.from_user.id, 'Чтобы начать нажмите: /start')
    await state.reset_state()


async def _state_actions(call, state, kb):
    if kb.is_file():
        await _send_file(call, state, kb)
    else:
        await bot.send_message(call.from_user.id, kb, reply_markup=await create_keyboard(kb))
        await PathState.next()


async def start_state(message: types.Message, state: FSMContext):
    if message.from_user.id in [int(os.getenv('ADMIN_1_ID')), int(os.getenv('ADMIN_2_ID'))]:
        await state.set_state(PathState.level_0)
        await bot.send_message(message.from_user.id, "Начнем!", reply_markup=start_keyboard)
        await message.answer('Выберите диск', reply_markup=await create_disks_keyboard())
    else:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEJQc1kghXlYMaCK_hMxxuGzLgosnSQWQAC9QADVp29Cq5uEBf1pScoLwQ')
        await bot.send_message(message.from_user.id, 'Вы кто такие, я вас не звал, идите нахуй!!!')


async def cancel_state(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Отменено!!!')
    await bot.send_message(message.from_user.id, 'Чтобы начать нажмите: /start')
    await state.reset_state()
    D.clear()


async def goback_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await _del_last_key(data)
        if data:
            kb = await _create_path(data)
            await PathState.previous()
            await bot.send_message(message.from_user.id, kb, reply_markup=await create_keyboard(kb))
        else:
            await state.set_state(PathState.level_0)
            await message.answer('Выберите диск', reply_markup=await create_disks_keyboard())


async def any_level_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data[data.state.split(':')[1]] = D[call.data]
        kb = await _create_path(data)
    await _state_actions(call, state, kb)


async def last_level_handler(call: types.CallbackQuery, state: FSMContext):
    await any_level_handler(call, state)
    await state.finish()
    await bot.send_message(call.from_user.id, 'Run out of levels')


def register():
    dp.register_message_handler(start_state, commands=['start'])
    dp.register_message_handler(cancel_state, commands=['cancel'], state='*')
    dp.register_message_handler(goback_state, commands=['back'], state='*')
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_0)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_1)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_2)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_3)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_4)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_5)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_6)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_7)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_8)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_9)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_10)
    dp.register_callback_query_handler(any_level_handler, state=PathState.level_11)
    dp.register_callback_query_handler(last_level_handler, state=PathState.last_level)
