from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# Клавиатура для обычного пользователя
start_inline_buttons_client = [
    [InlineKeyboardButton(text='Сгенерировать значения', callback_data='generate_values')],
]

start_menu_client = InlineKeyboardMarkup(inline_keyboard=start_inline_buttons_client)

# Клавиатура после генерации значений
main_menu_client_buttons = [
    [InlineKeyboardButton(text='Сгенерировать новое значение', callback_data='generate_values')],
    [InlineKeyboardButton(text='Главное меню', callback_data='main_menu_client')],
]

main_menu_client = InlineKeyboardMarkup(inline_keyboard=main_menu_client_buttons)

