from datetime import datetime, timedelta
from typing import Iterator

from storage.models import User, Stage
from storage.settings import MOSCOW_TZ


class DataBaseExecutor:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataBaseExecutor, cls).__new__(cls)
        return cls.instance

    @staticmethod
    async def create_new_instance(model, data: dict):
        model.create(**data)

    @staticmethod
    async def get_user_by_tg_id(tg_id: int) -> User | None:
        return User.get_or_none(User.tg_id == tg_id)

    @classmethod
    async def get_more_one_day_inactive_users(cls) -> Iterator[User]:
        one_day_ago = datetime.now(tz=MOSCOW_TZ) - timedelta(days=1)
        inactive_users = User.select().where(User.last_activity_dt < one_day_ago)
        return (
            user for user in inactive_users
            if not await cls.user_is_complete_all_stages(user)
        )

    @staticmethod
    async def user_is_complete_all_stages(user: User) -> bool:
        last_stage = Stage.select().order_by(User.id.desc()).first()
        return last_stage in user.completed_stages
