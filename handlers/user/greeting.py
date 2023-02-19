import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, InputFile
from aiogram.utils.markdown import hspoiler

from buttons import web_app_button, hr_contact_button
from config import dp, bot, db, DEFAULT_ACTIVATION_WORD, HR_TG_ID, BotPath
from states.user import UserAuth
from tools.json_executor import json_settings
from tools.misc import register_new_user, send_message_from_bot


@dp.message_handler(commands=["start"])
async def send_auth_request(message: Message):
    if await db.get_user_by_tg_id(message.from_user.id):
        return await message.answer(
            f"<b>Доброго дня, {message.from_user.full_name}  ✨\n\n"
            f"Чтобы начать познание корпоративной культуры, нажмите кнопку ниже 👇🏻</b>",
            reply_markup=web_app_button
        )
    
    await message.answer(
        "<b>Привет, прекрасный новичок Росмолодежи ⭐️</b>\n"
        "Для использования бота введи кодовое слово из "
        "письма, полученного от HR"
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
        new_user = await register_new_user(message.from_user)
        # await send_message_from_bot(HR_TG_ID, f"{str(new_user)} успешно авторизовался в боте ✔️")
        greeting = await message.answer(
            "<b>Успешная авторизация. Уже совсем скоро мы:\n"
            "• Познакомимся с ценностями и миссией Росмолодежи\n"
            "• Сформируем видение задач и направлений деятельности\n"
            "• Погрузимся в корпоративную культуру\n\n"
            "А еще, мы подготовили для Вас интерактивное приложение в Телеграм. "
            "Да, именно здесь будет происходить всё самое главное и интересное. "
            "Ничего не нужно дополнительно скачивать или устанавливать. На всём пути Вас "
            "будет сопровождать Мол, его фотография немного ниже! Нажмите кнопку ниже и мы... "
            "стартуем  🚀</b>",
            reply_markup=web_app_button
        )
        await asyncio.sleep(5)
        await message.answer_photo(InputFile(path_or_bytesio=BotPath.STATIC_DIR / "hero.jpg"))
        await message.answer(
            "<b>А эти команды помогут будут помогать на протяжении всего обучения\n"
            "/contacts - важные контакты для связи\n"
            "/resources - источники знаний, комьюнити\n"
            "/journal - внутренняя жизнь, наш блог\n"
            "/documents - основные документы и шаблоны</b>\n",
            reply_markup=web_app_button
        )
        return await bot.pin_chat_message(message.chat.id, greeting.message_id)
    
    return await message.answer(
        "Хмм... Кажется, кодовое слово введено неверно 🤔\n"
        f"{hspoiler('Попробуйте еще раз')}"
    )


@dp.message_handler(commands=["contacts"])
async def show_contacts(message: Message):
    await message.answer(
        "<code>8-999-888-77-77</code> - <b>Рабочий номер телефона HR</b>\n\n"
        "<code>8-999-555-33-33</code> - <b>Отдел технической поддержки</b>",
        reply_markup=hr_contact_button
    )
