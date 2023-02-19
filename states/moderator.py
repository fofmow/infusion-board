from aiogram.dispatcher.filters.state import StatesGroup, State


class SettingAuthData(StatesGroup):
    enter_auth_word = State()
