from datetime import datetime

from aiogram.types import User as AiogramUser
from aiogram.utils.exceptions import ChatNotFound, BotBlocked

from config import db, bot, logger
from storage.models import User
from storage.settings import MOSCOW_TZ


async def register_new_user(from_user: AiogramUser) -> User:
    return await db.create_new_instance(
        model=User,
        data={
            "tg_id": from_user.id,
            "registration_dt": datetime.now(tz=MOSCOW_TZ),
            "username": f"@{from_user.username}",
            "full_name": from_user.full_name
        }
    )


async def send_message_from_bot(tg_id: int, text: str, markup=None):
    """ Отправка сообщений от бота с корректной обработкой ошибок """
    
    try:
        await bot.send_message(tg_id, text=text, reply_markup=markup)
    except ChatNotFound:
        logger.info(
            f"Получатель с ID {tg_id} не найден. Отправка сообщения ({text}) не удалась"
        )
    except BotBlocked:
        logger.info(
            f"Получатель с ID {tg_id} заблокировал бота. Текст ({text}) не был отправлен"
        )
