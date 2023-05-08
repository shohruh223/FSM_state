from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.personal import UserState


@dp.message_handler(commands="user")
async def get_info(message: types.Message):
    await message.answer(text="Foydalanuvchi haqida malumot kiriting")
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Foydalanuvchini yoshini kiriting")
    # await UserState.age.set()
    await UserState.next()


@dp.message_handler(state=UserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await UserState.next()
    await message.answer("Foydalanuvchini raqamini kiriting")


@dp.message_handler(state=UserState.phone_number)
async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    await UserState.next()
    await message.answer("Foydalanuvchini emailini kiriting")


@dp.message_handler(state=UserState.email)
async def add_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await UserState.next()
    await message.answer("Foydalanuvchini rasmini kiriting")


@dp.message_handler(state=UserState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await state.finish()
    await message.answer("Ma'lumotingiz saqlandi")

    await message.answer_photo(photo=data['photo'],
                               caption=f"Foydalanuvchini ismi {data['name']},\n"
                         f"uning yoshi {data['age']},\n"
                         f"uning raqami {data['phone_number']},\n"
                         f"emaili {data['email']}")



