from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add('Каталог').add('Корзина').add('Контакты')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add('Каталог').insert('Корзина').insert('Контакты').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
# admin_panel.add('Добавить товар').insert("Удалить товар").add("Сделать рассылку")  # insert добавляет кнопку слева
admin_panel.row('Добавить товар', "Удалить товар", "Сделать рассылку")  # Все кнопки в одной строке

catalog_list = InlineKeyboardMarkup(row_width=1)
catalog_list.add(InlineKeyboardButton('Футболки', callback_data='t-shirt'),
                 InlineKeyboardButton('Брюки', callback_data='pants'),
                 InlineKeyboardButton('Обувь', callback_data='boots'),
                 InlineKeyboardButton('Разное', callback_data='misc'))

location_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Отправить геолокацию", request_location=True))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')
