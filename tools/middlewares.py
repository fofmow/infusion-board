from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from config import HR_TG_ID


class IsModerator(BoundFilter):
    async def check(self, message: Message | CallbackQuery) -> bool:
        return message.from_user.id == HR_TG_ID
