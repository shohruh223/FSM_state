from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    email = State()
    photo = State()