import re
from pathlib import Path
import psutil
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('/start').insert('/back').insert('/cancel')

from const import FOLDER_ICON, FILE_ICON, LARGE_FILE, D


async def create_disks_keyboard():
    disc_choose = InlineKeyboardMarkup(row_width=len(psutil.disk_partitions()))
    for item in psutil.disk_partitions():
        dev_hash = str(hash(item.device))
        D[dev_hash] = item.device
        disc_choose.insert(InlineKeyboardButton(item.device, callback_data=dev_hash))
    return disc_choose


async def create_keyboard(directory: Path):
    kb = InlineKeyboardMarkup(row_width=1)
    try:
        for item in directory.iterdir():
            item_hash = str(hash(item.name))
            D[item_hash] = item.name
            if item.is_file():
                icon = FILE_ICON
                if os.stat(item).st_size > 5000000:
                    icon = LARGE_FILE
            else:
                icon = FOLDER_ICON
            kb.add(InlineKeyboardButton(f"{icon}{item.name}", callback_data=item_hash))
        return kb
    except FileNotFoundError:
        return kb.add(InlineKeyboardButton(f"❌TOO LARGE NAME, PLEASE PRESS /back❌",
                                           callback_data=f"Error"))
    except PermissionError:
        return kb.add(InlineKeyboardButton(f"❌ACCESS DENIED, PLEASE PRESS /back❌",
                                           callback_data=f"Error"))
