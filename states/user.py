from aiogram.dispatcher.filters.state import StatesGroup, State


class UserAuth(StatesGroup):
    input_code_word = State()
    input_department = State()
