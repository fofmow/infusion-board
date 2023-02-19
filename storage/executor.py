from datetime import datetime, timedelta
from typing import Iterator

from storage.models import User, Stage, WorkDirectorate
from storage.settings import MOSCOW_TZ
from tools.notifications.periodes import InactivePeriodStatus


class DataBaseExecutor:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataBaseExecutor, cls).__new__(cls)
        return cls.instance
    
    @staticmethod
    async def create_new_instance(model, data: dict):
        return model.create(**data)
    
    @staticmethod
    async def get_user_by_tg_id(tg_id: int) -> User | None:
        return User.get_or_none(User.tg_id == tg_id)
    
    @classmethod
    async def get_inactive_users(cls, more_days: int, not_equal_status: InactivePeriodStatus) -> Iterator[User]:
        one_day_ago = datetime.now(tz=MOSCOW_TZ) - timedelta(days=more_days)
        inactive_users = User.select().where(
            (User.last_activity_dt < one_day_ago) &
            (User.inactive_notification_period < not_equal_status)
        )
        return (
            user for user in inactive_users
            if not await cls.user_is_complete_all_stages(user)
        )
    
    @staticmethod
    async def user_is_complete_all_stages(user: User) -> bool:
        last_stage = Stage.select().order_by(Stage.id.desc()).first()
        return last_stage in user.completed_stages
    
    @staticmethod
    async def get_all_directorates():
        return WorkDirectorate.select()
