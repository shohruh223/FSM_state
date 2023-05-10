from aiogram.dispatcher.filters.state import StatesGroup, State


class AddUserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    email = State()
    photo = State()


class EditUserState(StatesGroup):
    id = State()
    name = State()
    age = State()
    phone_number = State()
    email = State()
    photo = State()