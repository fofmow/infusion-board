from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from config import MODERATORS_TG_IDS


class IsManager(BoundFilter):
    async def check(self, message: Message | CallbackQuery) -> bool:
        return message.from_user.id in MODERATORS_TG_IDS
