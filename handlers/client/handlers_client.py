from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from text.client import text_client
from keyboards.client import keyboard_client
from keyboards.admin import keyboard_admin
from config_data.config import ID_ADMINS
from database.database import Database


router = Router()
db = Database('db.sqlite3')

# Выводится главное меню пользователя по команде /start
@router.message(Command('start'))
@router.callback_query(F.data == 'main_menu_client')
async def start_handlers(message: Message | CallbackQuery):
    if isinstance(message, Message):
        if message.from_user.id in ID_ADMINS:
            await message.answer(text=text_client.start_message, reply_markup=keyboard_admin.start_menu_admin)
        else:
            await message.answer(text=text_client.start_message, reply_markup=keyboard_client.start_menu_client)
    elif isinstance(message, CallbackQuery):
        await message.message.delete()
        if message.from_user.id in ID_ADMINS:
            await message.message.answer(text=text_client.main_menu, reply_markup=keyboard_admin.start_menu_admin)
        else:
            await message.message.answer(text=text_client.main_menu, reply_markup=keyboard_client.start_menu_client)

# Генерируем рандомных пользователя и задание и выводим полученные значения
@router.callback_query(F.data == 'generate_values')
async def generate_values(callback: CallbackQuery):
    await callback.message.delete()
        
    await callback.message.answer(text=db.generate_values(), reply_markup=keyboard_client.main_menu_client)
