from aiogram import executor
from create_bot import dp
from path_states import register_handlers


def on_startup():
    register_handlers(dp)
    print(f"Бот успешно запущен")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup(), skip_updates=True)
