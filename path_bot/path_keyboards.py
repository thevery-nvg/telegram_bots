
from pathlib import Path
import psutil
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('/start').insert('/back').insert('/cancel')



async def create_disks_keyboard():
    disc_choose = InlineKeyboardMarkup(row_width=len(psutil.disk_partitions()))
    for item in psutil.disk_partitions():
        disc_choose.insert(InlineKeyboardButton(item.device, callback_data=item.device))
    return disc_choose


FOLDER_ICON = u'\U0001F4E6'
FILE_ICON = u'\U00002705'
CROSS_ICON = u'\U0000274C'


async def create_keyboard(directory: Path):
    kb = InlineKeyboardMarkup(row_width=1)
    for item in directory.iterdir():
        t = ''
        if item.is_file():
            icon = FILE_ICON
            if os.stat(item).st_size > 5000000:
                icon = CROSS_ICON
        else:
            icon = FOLDER_ICON
        if len(item.name) > 35:
            icon = CROSS_ICON
            t = '...'
        kb.add(InlineKeyboardButton(f"{item.name[:35]}{t} {icon}", callback_data=f"{item.name[:35]}"))
    return kb
