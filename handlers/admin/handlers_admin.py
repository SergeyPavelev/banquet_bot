from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from text.admin import text_admin
from keyboards.admin import keyboard_admin


router = Router()

# Выводится главное меню
@router.callback_query(F.data == 'main_menu')
async def main_menu(callback: CallbackQuery):
    await callback.message.answer(text=text_admin.main_munu, reply_markup=keyboard_admin.start_menu_admin)

# Выводится панель администратора
@router.callback_query(F.data == 'admin_panel')
async def get_admin_panel(callback: CallbackQuery):
    await callback.message.answer(text=text_admin.admin_panel, reply_markup=keyboard_admin.admin_panel_menu)

# Выводится список функций редактирования списка пользователей
@router.callback_query(F.data == 'edit_list_users')
async def edit_list_users(callback: CallbackQuery):
    await callback.message.answer(text=text_admin.edit_list_users, reply_markup=keyboard_admin.edit_list_users_menu)

# Выводится список функций редактирования списка заданий
@router.callback_query(F.data == 'edit_list_tasks')
async def edit_list_tasks(callback: CallbackQuery):
    await callback.message.answer(text=text_admin.edit_list_tasks, reply_markup=keyboard_admin.edit_list_tasks_menu)
