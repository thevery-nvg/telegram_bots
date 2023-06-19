from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

get_location_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Send location', request_location=True))