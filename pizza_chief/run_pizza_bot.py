from common.create_bot import dp,on_startup
from aiogram import executor

from dotenv import load_dotenv
load_dotenv()

from user_handlers import register
register()

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup())
