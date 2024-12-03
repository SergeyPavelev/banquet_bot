from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from text.client import text_client
from keyboards.client import keyboard_client
from keyboards.admin import keyboard_admin
from config_data.config import ID_ADMINS


router = Router()

# Выводится главное меню
@router.message(Command('start'))
async def start_handlers(message: Message):
    if message.from_user.id in ID_ADMINS:
        await message.answer(text=text_client.start_message, reply_markup=keyboard_admin.start_menu_admin)
    else:
        await message.answer(text=text_client.start_message, reply_markup=keyboard_client.start_menu_client)
