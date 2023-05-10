from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from states.user_state import EditUserState


@dp.message_handler(state=EditUserState.id)
async def update_user(message: types.Message, state:FSMContext):
    user_id = int(message.text)
    user = db.get_user(user_id)
    async with state.proxy() as data:
        if user:
            data['id'] = user_id
            await message.answer("Foydalanuvchini ismini o'zgartiring")
            await EditUserState.next()
        else:
            await message.answer("Bu raqamda foydalanuvchi mavjud emas")
            await state.finish()


@dp.message_handler(state=EditUserState.name)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Foydalanuvchini yoshini yangilang")
    await EditUserState.next()


@dp.message_handler(state=EditUserState.age)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await message.answer("Foydalanuvchini telefon raqamini yangilang")
    await EditUserState.next()


@dp.message_handler(state=EditUserState.phone_number)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await message.answer("Foydalanuvchini emailini yangilang")
    await EditUserState.next()


@dp.message_handler(state=EditUserState.email)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await message.answer("Foydalanuvchini rasmini yangilang")
    await EditUserState.next()


@dp.message_handler(state=EditUserState.photo, content_types="photo")
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        db.update_user(id=data['id'],
                       name=data['name'],
                       age=data['age'],
                       phone_number=data['phone_number'],
                       email=data['email'],
                       photo=data['photo'])
    await message.answer("Malumotlaringiz o'zgartirildi")
    await state.finish()