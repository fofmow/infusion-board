from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from buttons import moderator_home_buttons
from config import dp
from states.moderator import SettingAuthData
from tools.json_executor import json_settings
from tools.middlewares import IsModerator


@dp.message_handler(IsModerator(), commands=["moderator"])
async def show_admin_panel(message: Message):
    await message.answer(
        "<b>Управление Параметрами Бота</b>",
        reply_markup=moderator_home_buttons
    )


@dp.callback_query_handler(IsModerator(), text="set_auth_word")
async def request_for_new_auth_setting_word(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        "<b>Введите новое кодовое слово (от 6 до 36 символов). "
        "Новые сотрудники смогут легко авторизоваться по нему в боте</b>"
    )
    await SettingAuthData.enter_auth_word.set()


@dp.message_handler(IsModerator(), content_types=["text"], state=SettingAuthData.enter_auth_word)
async def keep_received_auth_word(message: Message, state: FSMContext):
    if not await auth_word_length_is_correct(message.text):
        return await message.answer(
            "<b>Длина слова не входит в диапазон 6-36 символов. "
            "Попробуйте ввести другой код</b>"
        )
    
    await state.finish()
    await json_settings.update_start_code_word(message.text)
    return await message.answer(
        f"<b>Новое кодовое слово авторизации ({message.text}) сохранено ✔️</b>"
    )


async def auth_word_length_is_correct(word: str):
    return 6 <= len(word) <= 36
