from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from text.admin import text_admin
from keyboards.admin import keyboard_admin
from handlers.admin.states_admin import AddUser, DeleteUser, EditUser
from database.database import Database


router = Router()
db = Database(db_file='db.sqlite3')

# Выводится главное меню
@router.callback_query(F.data == 'main_menu')
async def main_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=text_admin.main_munu, reply_markup=keyboard_admin.start_menu_admin)

# Выводится панель администратора
@router.callback_query(F.data == 'admin_panel')
async def get_admin_panel(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=text_admin.admin_panel, reply_markup=keyboard_admin.admin_panel_menu)

# Выводится список функций редактирования списка пользователей
@router.callback_query(F.data == 'edit_list_users')
async def edit_list_users(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=text_admin.edit_list_users, reply_markup=keyboard_admin.edit_list_users_menu)

# Выводится список функций редактирования списка заданий
@router.callback_query(F.data == 'edit_list_tasks')
async def edit_list_tasks(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=text_admin.edit_list_tasks, reply_markup=keyboard_admin.edit_list_tasks_menu)

# Запрашиваем у пользователя имя нового пользователя
@router.callback_query(F.data == 'add_user')
async def get_name_new_user(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddUser.name_new_user)
    await callback.message.delete()
    await callback.message.answer(text=text_admin.get_name_user, reply_markup=keyboard_admin.cancel_menu)

# Новый пользователь добавляется в базу данных
@router.message(AddUser.name_new_user)
async def add_new_user(message: Message, state: FSMContext):
    name_user = message.text
    
    db.add_user(name_user=name_user)
    
    await message.answer(text=text_admin.add_user, reply_markup=keyboard_admin.edit_list_users_menu)
    await state.clear()

# Выводим список пользователей и запрашиваем id нужного пользователя
@router.callback_query(F.data == 'delete_user')
async def get_user_id_delete(callback: CallbackQuery, state: FSMContext):
    await state.set_state(DeleteUser.user_id)
    
    await callback.message.delete()
    await callback.message.answer(text=text_admin.get_id_user)
    await callback.message.answer(text=db.get_all_user(), reply_markup=keyboard_admin.cancel_menu)

# Получаем id пользователя и удаляем его из базы данных
@router.message(DeleteUser.user_id)
async def delete_user(message: Message, state: FSMContext):
    user_id = message.text
    
    db.delete_user(user_id=user_id)
    
    await message.answer(text=text_admin.delete_user, reply_markup=keyboard_admin.edit_list_users_menu)
    
    await state.clear()

# Выводим список пользователей и запрашиваем id нужного пользователя
@router.callback_query(F.data == 'edit_user')
async def get_user_id_edit(callback: CallbackQuery, state: FSMContext):
    await state.set_state(EditUser.user_id)
    
    await callback.message.delete()
    await callback.message.answer(text=text_admin.get_id_user)
    await callback.message.answer(text=db.get_all_user(), reply_markup=keyboard_admin.cancel_menu)

# Получаем id пользователя и запрашиваем новое имя пользователя
@router.message(EditUser.user_id)
async def get_id_user_edit(message: Message, state: FSMContext):
    await state.set_state(EditUser.new_name_user)
    
    user_id = message.text
    await state.update_data(user_id=user_id)
    
    await message.answer(text=text_admin.get_new_user_name, reply_markup=keyboard_admin.cancel_menu)

# Получаем новое имя пользователя и обновляем данные пользователя
@router.message(EditUser.new_name_user)
async def get_new_user_name(message: Message, state: FSMContext):
    new_name_user = message.text
    
    data_state = await state.get_data()
    user_id = data_state.get('user_id')
    
    db.edit_user_name(user_id=user_id, new_user_name=new_name_user)
    
    await message.answer(text=text_admin.edit_user, reply_markup=keyboard_admin.edit_list_users_menu)    
    await state.clear()

    
    


# Отмена state
@router.callback_query(F.data == 'cancel')
async def cancel_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(text=text_admin.cancel_text, reply_markup=keyboard_admin.admin_panel_menu)
