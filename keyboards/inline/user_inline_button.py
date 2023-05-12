from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_user_button() -> InlineKeyboardButton:
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Add User", callback_data="add_user")
    button2 = InlineKeyboardButton(text="All User", callback_data="all_user")
    button3 = InlineKeyboardButton(text="Get User", callback_data="get_user")
    button4 = InlineKeyboardButton(text="Update User", callback_data="update_user")
    button5 = InlineKeyboardButton(text="Delete User", callback_data="delete_user")
    ikm.add(button, button2, button3, button4, button5)
    return ikm


def get_pagination_buttons(current_page, total_pages):
    buttons = []
    if current_page > 1:
        buttons.append(
            InlineKeyboardButton('<<', callback_data=f'pagination:1')
        )
        buttons.append(
            InlineKeyboardButton('<', callback_data=f'pagination:{current_page - 1}')
        )
    if current_page < total_pages:
        buttons.append(
            InlineKeyboardButton('>', callback_data=f'pagination:{current_page + 1}')
        )
        buttons.append(
            InlineKeyboardButton('>>', callback_data=f'pagination:{total_pages}')
        )
    return buttons