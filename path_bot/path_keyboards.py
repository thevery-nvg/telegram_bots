import re
from pathlib import Path
import psutil
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('/start').insert('/back').insert('/cancel')

D = dict()


async def create_disks_keyboard():
    disc_choose = InlineKeyboardMarkup(row_width=len(psutil.disk_partitions()))
    for item in psutil.disk_partitions():
        D[item.device] = str(hash(item.device))
        disc_choose.insert(InlineKeyboardButton(item.device, callback_data=item.device))
    return disc_choose


FOLDER_ICON = u'\U0001F4E6'
FILE_ICON = u'\U00002705'
CROSS_ICON = u'\U0000274C'
LARGE_FILE = u'\U0001F534'


async def create_keyboard(directory: Path):
    kb = InlineKeyboardMarkup(row_width=1)
    try:
        for item in directory.iterdir():
            if item.is_file():
                icon = FILE_ICON
                if os.stat(item).st_size > 5000000:
                    icon = LARGE_FILE
            else:
                icon = FOLDER_ICON
            if re.match(r'[А-Яа-я]', item.name):
                if len(item.name) > 30: icon = CROSS_ICON if icon != LARGE_FILE else LARGE_FILE
                kb.add(InlineKeyboardButton(f"{icon}{item.name}", callback_data=f"{item.name[:30]}"))
            else:
                if len(item.name) > 64: icon = CROSS_ICON
                kb.add(InlineKeyboardButton(f"{icon}{item.name}", callback_data=f"{item.name[:64]}"))
        return kb
    except FileNotFoundError:
        return kb.add(InlineKeyboardButton(f"{CROSS_ICON}TOO LARGE NAME, PRESS /back{CROSS_ICON}",
                                           callback_data=f"FileNotFoundError"))
