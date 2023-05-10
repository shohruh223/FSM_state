from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.user_inline_button import inline_user_button
from loader import dp, db
from states.user_state import AddUserState, EditUserState


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
    elif callback.data == "all_user":
        users = db.all_user()
        for user in users:
            # users_info += f"{user[1]}, {user[2]}, {user[3]}, {user[4]}, {user[5]}"
            await callback.message.answer_photo(photo=user[5],
                                                caption=f"Foydalanuvchini ismi {user[1]},\n"
                                                        f"yoshi {user[2]},\n"
                                                        f"Telefon raqami {user[3]},"
                                                        f"Emaili {user[4]}")
    elif callback.data == "update_user":
        await callback.message.answer(text="Foydalanuvchi tahrirlash",
                                      reply_markup=ReplyKeyboardRemove())
        await EditUserState.id.set()
        await callback.message.answer("Qaysi id tegishli foydalanuvchini tahrirlamoqchisiz")

