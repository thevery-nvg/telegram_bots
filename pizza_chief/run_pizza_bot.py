from common.create_bot import dp
from aiogram import executor

from dotenv import load_dotenv
load_dotenv()

from user_handlers import register
register()

def on_startup():
    print(f"Бот успешно запущен")

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup())
