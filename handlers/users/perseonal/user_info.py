from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.users.perseonal.pagination import get_users
from keyboards.default.user_button import cancel
from keyboards.inline.user_inline_button import inline_user_button, get_pagination_buttons
from loader import dp, db, bot
from states.user_state import AddUserState, EditUserState, DeleteUserState


@dp.message_handler(commands="cancel", state="*")
async def get_cancel(message: types.Message, state: FSMContext):
    await message.answer(text="Bekor qilindi",
                         reply_markup=inline_user_button())
    await state.finish()


@dp.message_handler(Text(equals="user"))
async def get_info(message: types.Message):
    await message.answer(text="Foydalanuvchilarni tahrirlash",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Qaysi amalni tanlaysiz",
                         reply_markup=inline_user_button())


@dp.callback_query_handler()
async def user_callback(callback: types.CallbackQuery):
    if callback.data == "add_user":
        await callback.message.answer(text="Foydalanuvchini ismini kiriting",
                                      reply_markup=ReplyKeyboardRemove())
        await AddUserState.name.set()
    elif callback.data == "update_user":
        await callback.message.answer(text="Foydalanuvchi tahrirlash",
                                      reply_markup=ReplyKeyboardRemove())
        await EditUserState.id.set()
        await callback.message.answer(text="Qaysi id tegishli foydalanuvchini tahrirlamoqchisiz",
                                      reply_markup=cancel())
    elif callback.data == "all_user":
        users = db.all_user()
        for user in users:
            await callback.message.answer_photo(photo=user[5],
                                                caption=f"Foydalanuvchini ismi {user[1]},\n"
                                                        f"yoshi {user[2]},\n"
                                                        f"Telefon raqami {user[3]},"
                                                        f"Emaili {user[4]}")
    elif callback.data == "delete_user":
        await callback.message.answer("Id ni kiriting",
                                      reply_markup=ReplyKeyboardRemove())
        await DeleteUserState.id.set()


# @dp.inline_handler(Text(equals="all_user"))
# async def inline_handler(inline_query: types.InlineQuery):
#     page_size = 5  # Sahifadagi mahsulotlar soni
#     page_number = int(inline_query.offset) // page_size + 1
#
#     users = get_users(limit=page_size, offset=(page_number - 1) * page_size)
#     total_products = len(users)
#     total_pages = (total_products // page_size) + (1 if total_products % page_size > 0 else 0)
#
#     # Sahifalash tugmalarini yaratish
#     pagination_buttons = get_pagination_buttons(page_number, total_pages)
#     keyboard = InlineKeyboardMarkup(row_width=4)
#     keyboard.add(*pagination_buttons)
#
#     # Mahsulotlarni ko'rsatish
#     results = []
#     for user in users:
#         result = types.InlineQueryResultPhoto(
#             id=str(user['id']),
#             photo_url=user['photo'],
#             thumb_url=user['photo'],
#             title=user['name'],
#             caption=f"{user['name']}\n{user['age']}\nRaqami: {user['phone_number']} emaili {user['email']}",
#             reply_markup=keyboard
#         )
#         results.append(result)
#
#     # Javobni yuborish
#     # sahifaga o'tishni belgilash uchun offsetni qaytarish
#     if total_products > page_size:
#         next_offset = str((page_number * page_size))
#         await bot.answer_inline_query(
#             inline_query.id,
#             results=results,
#             next_offset=next_offset,
#             cache_time=1
#         )
#     else:
#         await bot.answer_inline_query(
#             inline_query.id,
#             results=results,
#             cache_time=1
#         )

