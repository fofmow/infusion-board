from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import HR_TG_ACCOUNT_URL, web_app

web_app_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Открыть Приложение", web_app=web_app)
)

hr_contact_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Написать HR", url=HR_TG_ACCOUNT_URL)
)

moderator_home_buttons = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Задать Кодовое Слово", callback_data="set_auth_word"),
    InlineKeyboardButton("Статистика по Новичкам", callback_data="students_summary"),
    InlineKeyboardButton("Разослать Уведомления", callback_data="send_notifications"),
)

async def selecting_department_buttons(departments):
    ...