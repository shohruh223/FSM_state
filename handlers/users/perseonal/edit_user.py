from aiogram import types
from aiogram.dispatcher import FSMContext
import re
from loader import dp, db
from states.user_state import EditUserState


@dp.message_handler(state=EditUserState.id)
async def edit_user(message: types.Message, state: FSMContext):
    # try:
    user_id = int(message.text)
    user = db.get_user(id=user_id)
    # except ValueError:
    #     await message.answer("Id xato kiritildi")
    #     await state.finish()

    if not user:
        await message.answer("Bunaqa id tegishli foydalanuvchi mavjud emas")
        await state.finish()
    else:
        async with state.proxy() as data:
            data['id'] = message.text

        await EditUserState.next()
        await message.answer("Foydalanuvchini ismini yangilangni hohlaysizmi (ha/yo'1)")


@dp.message_handler(state=EditUserState.check_name)
async def check_name(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        await EditUserState.next()
        await message.answer("Foydalanuvchini ismini yangilash")
    else:
        await EditUserState.age.set()
        await message.answer("Foydalanuvchini yoshini yangilang")


@dp.message_handler(state=EditUserState.name)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await EditUserState.next()
    await message.answer("Foydalanuvchini yoshini yangilang")


@dp.message_handler(state=EditUserState.age)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = message.text
        except ValueError:
            await message.answer("Foydalanuvchini yoshi xato kiritildi")
    await EditUserState.next()
    await message.answer("Foydalanuvchini telefon raqamini yangilang")


@dp.message_handler(state=EditUserState.phone_number)
async def edit_name(message: types.Message, state: FSMContext):
    PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    phone_number = re.match(PHONE_REGEX, message.text)
    if phone_number:
        async with state.proxy() as data:
            data['phone_number'] = message.text
        await EditUserState.next()
        await message.answer("Foydalanuvchini emailini yangilang")
    else:
        await message.answer("Telefon raqam xato kiritildi")


@dp.message_handler(state=EditUserState.email)
async def edit_name(message: types.Message, state: FSMContext):
    EMAIL_REGEX = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
    email = re.match(EMAIL_REGEX, message.text)
    if email:
        async with state.proxy() as data:
            data['email'] = message.text
        await EditUserState.next()
        await message.answer("Foydalanuvchini rasmini yangilang")
    else:
        await message.answer("Email xato kiritildi")


@dp.message_handler(state=EditUserState.photo, content_types=['photo'])
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[2].file_id
    await state.finish()
    db.update_user(id=data['id'],
                   name=data['name'],
                   age=data['age'],
                   phone_number=data['phone_number'],
                   email=data['email'],
                   photo=data['photo'])
    await message.answer("malumotlaringiz saqlandi")


