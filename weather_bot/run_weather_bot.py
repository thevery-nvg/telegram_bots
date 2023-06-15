from common.create_bot import dp, on_startup
from aiogram import executor, types
from keyboards import get_location_button
from weather import get_weather


async def command_start(message: types.Message):
    await message.answer('Чтобы узнать погоду, отправьте свою геопозицию', reply_markup=get_location_button)


async def position(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    weather = get_weather(lat, lon)
    await message.answer(weather.output())


dp.register_message_handler(position, content_types=['location'])
dp.register_message_handler(command_start, commands=['start'])

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup())
