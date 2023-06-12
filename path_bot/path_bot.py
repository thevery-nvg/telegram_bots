from aiogram import executor
from create_bot import dp
from path_states import register




def on_startup():
    print(f"Бот успешно запущен")


if __name__ == '__main__':
    register(dp)
    executor.start_polling(dp, on_startup=on_startup(), skip_updates=True)
