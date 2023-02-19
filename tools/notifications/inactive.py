import random

from config import db, HR_TG_ID
from static.constants import ONE_DAY_INACTIVE_MESSAGES, THREE_DAYS_INACTIVE_MESSAGES
from storage.models import User
from tools.misc import send_message_from_bot
from tools.notifications.periodes import InactivePeriodStatus


async def call_inactive_users_to_action():
    """ Отправка сотрудникам мотивационных сообщений после одного дня бездействия.
    Уведомление для HR после одного и трех дней бездействия сотрудника """
    
    more_one_day_inactive = await db.get_inactive_users(
        more_days=1, not_equal_status=InactivePeriodStatus.MORE_DAY
    )
    async for user in more_one_day_inactive:
        await send_message_from_bot(user.tg_id, f"<b>{random.choice(ONE_DAY_INACTIVE_MESSAGES)}</b>")
        await send_message_from_bot(HR_TG_ID, f"<b>{str(user)} не проходил модули более суток</b>")
        await update_user_inactive_period(user, new_status=InactivePeriodStatus.MORE_DAY)
    
    more_three_days_inactive = await db.get_inactive_users(
        more_days=3, not_equal_status=InactivePeriodStatus.MORE_THREE_DAYS
    )
    async for user in more_three_days_inactive:
        await send_message_from_bot(user.tg_id, f"<b>{random.choice(THREE_DAYS_INACTIVE_MESSAGES)}</b>")
        await send_message_from_bot(HR_TG_ID, f"<b>{str(user)} не проходил модули более 3х дней</b>")
        await update_user_inactive_period(user, new_status=InactivePeriodStatus.MORE_THREE_DAYS)


async def update_user_inactive_period(user: User, new_status: InactivePeriodStatus):
    user.inactive_notification_period = new_status
    user.save()
