from common.create_bot import bot, dp, on_startup
from aiogram import executor, types
from keyboards import get_location


async def command_start(message: types.Message):
    await message.answer('Hi', reply_markup=get_location)


async def position(message: types.Message):
    pos = message.location
    print(pos)


dp.register_message_handler(position, content_types=['location'])
dp.register_message_handler(command_start, commands=['start'])

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup())
