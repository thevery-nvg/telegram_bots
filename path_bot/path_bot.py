from aiogram import executor
from create_bot import bot, dp
from path_states import register

register()


def on_startup():
    print("Бот успешно запущен")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup(), skip_updates=True)
