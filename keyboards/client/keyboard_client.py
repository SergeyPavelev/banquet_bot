from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# Клавиатура для обычного пользователя
start_inline_buttons_client = [
    [InlineKeyboardButton(text='Сгенерировать значения', callback_data='generate_values')],
]

start_menu_client = InlineKeyboardMarkup(inline_keyboard=start_inline_buttons_client)

