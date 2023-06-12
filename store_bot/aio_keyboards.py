from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Каталог').add('Корзина').add('Контакты')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Каталог').insert('Корзина').insert('Контакты').add(
    'Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True).row('Добавить товар', "Удалить товар", "Сделать рассылку")

catalog_list = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Футболки', callback_data='Футболки'),
                                                     InlineKeyboardButton('Брюки', callback_data='Брюки'),
                                                     InlineKeyboardButton('Обувь', callback_data='Обувь'),
                                                     InlineKeyboardButton('Разное', callback_data='misc'))

location_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Отправить геолокацию", request_location=True))

buy = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('Buy',callback_data='buy')).insert(InlineKeyboardButton('Add to cart',callback_data='addtocart'))
cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')
