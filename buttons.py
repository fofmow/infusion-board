from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import WEB_APP_URL, SUPPORT_TG_ACCOUNT_URL


async def get_web_app_button():
    web_app = WebAppInfo(url=WEB_APP_URL)
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Открыть Приложение", web_app=web_app)
    )


support_contact_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Написать HR", url=SUPPORT_TG_ACCOUNT_URL)
)
