from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from buttons import get_web_app_button, support_contact_button
from config import dp, bot, db, DEFAULT_ACTIVATION_WORD
from states.user import UserAuth
from tools.json_executor import json_settings
from tools.misc import register_new_user


@dp.message_handler(commands=["start"])
async def send_auth_request(message: Message):
    if await db.get_user_by_tg_id(message.from_user.id):
        return await message.answer(
            f"Доброго дня, {message.from_user.full_name}. "
            f"Основные команды уже закреплены в чате. "
            f"Для перехода к обучению нажмите кнопку ниже",
            reply_markup=await get_web_app_button()
        )

    await message.answer(
        "<b>Привет, прекрасный новичок из Росмолодежи ⭐️</b>\n"
        "Для использования бота введи кодовое слово из письма, "
        "полученного от HR"
    )
    await UserAuth.input_code_word.set()


@dp.message_handler(content_types=ContentType.PINNED_MESSAGE)
async def delete_service_messages(message: Message):
    await message.delete()


@dp.message_handler(content_types=["text"], state=UserAuth.input_code_word)
async def check_received_code_word(message: Message, state: FSMContext):
    activation_word = await json_settings.get_start_code_word()
    if message.text.lower() in [activation_word.lower(), DEFAULT_ACTIVATION_WORD]:
        await state.finish()
        await register_new_user(message.from_user)
        greeting = await message.answer(
            "Успешная авторизация! В ближайшее время Вас ждёт... Начинаем погружение 🚀\n\n"
            "Нажмите зеленую кнопку в левом нижнем углу экрана.\n\n"
            "А эти команды помогут будут помогать на протяжении всего обучения\n"
            "/contacts - Важные контакты для связи\n"
            "/command2 - ...\n"
            "/command3 - ...\n",
            reply_markup=await get_web_app_button()
        )
        return await bot.pin_chat_message(message.chat.id, greeting.message_id)

    return await message.answer(
        "Хмм... Кажется, кодовое слово введено неверно. "
        "Попробуйте еще раз"
    )


@dp.message_handler(commands=["contacts"])
async def show_contacts(message: Message):
    await message.answer(
        "8-999-888-77-77 - Горячая линия\n"
        "8-999-555-33-33 - Отдел тех. поддержки",
        reply_markup=support_contact_button
    )
