from aiogram import executor, types
from aiogram.dispatcher import FSMContext
import os
from pathlib import Path

from aiogram.utils.exceptions import BadRequest

from create_bot import bot, dp
from path_keyboards import create_keyboard, start_keyboard, create_disks_keyboard
from const import D, img_formats,video_formats
from path_states import PathState


async def _create_path(data):
    r = ''
    for i in data:
        r += data[i] + "\\\\"
    return Path(r)


async def _clear_data(data: dict):
    for i in range(12, -1, -1):
        _key = f"level_{i}"
        if data.get(_key):
            del data[_key]
            break


async def send_file(call, state, kb):
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


async def state_actions(call, state, kb):
    if kb.is_file():
        await send_file(call, state, kb)
    else:
        await bot.send_message(call.from_user.id, kb, reply_markup=await create_keyboard(kb))
        await PathState.next()


def on_startup():
    print("Бот успешно запущен")


@dp.message_handler(commands=['start'])
async def start_state(message: types.Message, state: FSMContext):
    if message.from_user.id in [int(os.getenv('ADMIN_1_ID')), int(os.getenv('ADMIN_2_ID'))]:
        await state.set_state(PathState.level_0)
        await bot.send_message(message.from_user.id, "Начнем!", reply_markup=start_keyboard)
        await message.answer('Выберите диск', reply_markup=await create_disks_keyboard())
    else:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEJQc1kghXlYMaCK_hMxxuGzLgosnSQWQAC9QADVp29Cq5uEBf1pScoLwQ')
        await bot.send_message(message.from_user.id, 'Вы кто такие, я вас не звал, идите нахуй!!!')


@dp.message_handler(commands=['cancel'], state='*')
async def cancel_state(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Отменено!!!')
    await bot.send_message(message.from_user.id, 'Чтобы начать нажмите: /start')
    await state.reset_state()
    D.clear()


@dp.message_handler(commands=['back'], state='*')
async def goback_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await _clear_data(data)
        if data:
            kb = await _create_path(data)
            await PathState.previous()
            await bot.send_message(message.from_user.id, kb, reply_markup=await create_keyboard(kb))
        else:
            await state.set_state(PathState.level_0)
            await message.answer('Выберите диск', reply_markup=await create_disks_keyboard())


@dp.callback_query_handler(state=PathState.level_0)
async def set_level_0(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_0'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_1)
async def set_level_1(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_1'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_2)
async def set_level_2(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_2'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_3)
async def set_level_3(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_3'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_4)
async def set_level_4(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_4'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_5)
async def set_level_5(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_5'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_6)
async def set_level_6(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_6'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_7)
async def set_level_7(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_7'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_8)
async def set_level_8(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_8'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_9)
async def set_level_9(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_9'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_10)
async def set_level_10(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_10'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_11)
async def set_level_11(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_11'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)


@dp.callback_query_handler(state=PathState.level_12)
async def set_level_12(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['level_12'] = D[call.data]
        kb = await _create_path(data)
    await state_actions(call, state, kb)
    await state.finish()
    await bot.send_message(call.from_user.id, 'Run out of levels')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup(), skip_updates=True)
