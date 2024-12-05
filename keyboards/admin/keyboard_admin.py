from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# Kлавиатура для администратора
start_inline_buttons_admin = [
    [InlineKeyboardButton(text='Сгенерировать значения', callback_data='generate_values')],
    [InlineKeyboardButton(text='Панель администратора', callback_data='admin_panel')],
]

start_menu_admin = InlineKeyboardMarkup(inline_keyboard=start_inline_buttons_admin)

# Клавиатура для отмены действия
cancel_button = [[InlineKeyboardButton(text='Отмена', callback_data='cancel')]]
cancel_menu = InlineKeyboardMarkup(inline_keyboard=cancel_button)

# Клавиатура администратора
admin_panel_buttons = [
    [InlineKeyboardButton(text='Редактировать список пользователей', callback_data='edit_list_users')],
    [InlineKeyboardButton(text='Редактировать список заданий', callback_data='edit_list_tasks')],
    [InlineKeyboardButton(text='Главное меню', callback_data='main_menu_admin')],
]

admin_panel_menu = InlineKeyboardMarkup(inline_keyboard=admin_panel_buttons)

# Клавиатура для редактирования списка имен
edit_list_users_buttons = [
    [InlineKeyboardButton(text='Добавить пользователя', callback_data='add_user')],
    [InlineKeyboardButton(text='Редактировать пользователя', callback_data='edit_user')],
    [InlineKeyboardButton(text='Удалить пользователя', callback_data='delete_user')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='admin_panel')],
]

edit_list_users_menu = InlineKeyboardMarkup(inline_keyboard=edit_list_users_buttons)

# Клавиатура для редактирования списка заданий
edit_list_tasks_buttons = [
    [InlineKeyboardButton(text='Добавить задание', callback_data='add_task')],
    [InlineKeyboardButton(text='Редактировать задание', callback_data='edit_task')],
    [InlineKeyboardButton(text='Удалить задание', callback_data='delete_task')],
    [InlineKeyboardButton(text='Вернуться назад', callback_data='admin_panel')],
]

edit_list_tasks_menu = InlineKeyboardMarkup(inline_keyboard=edit_list_tasks_buttons)