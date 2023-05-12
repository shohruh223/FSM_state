from aiogram.dispatcher.filters.state import StatesGroup, State


class AddUserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    email = State()
    photo = State()


class EditUserState(StatesGroup):
    id = State() # 0
    check_name = State() # 1
    name = State() # == 2 user[2]
    age = State()
    phone_number = State()
    email = State()
    photo = State()


class DeleteUserState(StatesGroup):
    id = State()
    confirm = State()