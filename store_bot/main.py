from aiogram import executor, types

import alc_database as db
from common.create_bot import dp


async def on_startup(_):
    await db.db_start()
    print(f'Бот успешно запущен')


# Подгружаем юзер-хендлеры
from handlers.admin.admin_main import register_admin_handlers
from handlers import user, misc




register_admin_handlers(dp)
misc.register_misc_handlers(dp)
user.register_user_handlers(dp)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Я вас не понимаю")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,on_shutdown=db.connection.close())


