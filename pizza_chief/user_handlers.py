from common.create_bot import dp, bot
from aiogram import types


async def command_start(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker="CAACAgQAAxkBAAEJQdpkghcfgKdri0mxkj-ZILMYYqH23gACTAgAAtFhGFJjO7maupJPHC8E")
    await bot.send_message(chat_id=message.from_user.id, text='Welcome!')


async def command_open_hours(message: types.Message):
    await message.answer("ПН-ПТ с 8:00 до 22:00 СБ-ВС 10:00 до 21:00")


async def command_location(message: types.Message):
    await message.answer('Третья улица строителей, дом 25, квартира 12')


def register():
    dp.register_message_handler(command_start, commands=['start', 'help'])
