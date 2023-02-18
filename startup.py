import random

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from config import MODERATORS_TG_IDS, DEFAULT_ACTIVATION_WORD, db
from tools.json_executor import json_settings
from tools.misc import send_message_from_bot


async def check_start_code_word_on_existence():
    if not await json_settings.get_start_code_word():
        for tg_id in MODERATORS_TG_IDS:
            await send_message_from_bot(
                tg_id,
                text="<b>Warning! Кодовое слово для активации бота не установлено!</b>\n\n"
                     "Чтобы изменить параметр, введите команду /moderator и кликните "
                     "кнопку <b>«Задать Кодовое Слово»</b>.\n\nПароль по умолчанию: "
                     f"«{DEFAULT_ACTIVATION_WORD}»"
            )


ONE_DAY_INACTIVE_MESSAGES = [
    "Ой, кажется вы не занимались более одного дня! Пора продлить прогресс",
    "Помните, что самолёт взлетает против ветра? Пора начать обучение!",
    "Занимаясь ежедневно, Вы значительно повышаете шанс достижения результата "
]


async def call_inactive_users_to_action():
    more_one_day_inactive = await db.get_more_one_day_inactive_users()
    async for user in more_one_day_inactive:
        await send_message_from_bot(user.tg_id, random.choice(ONE_DAY_INACTIVE_MESSAGES))


async def on_startup(_):
    scheduler = AsyncIOScheduler()
    half_hour_trigger = IntervalTrigger(minutes=30)

    scheduler.add_job(check_start_code_word_on_existence, trigger=half_hour_trigger)
    scheduler.add_job(call_inactive_users_to_action, trigger=half_hour_trigger)
    scheduler.start()

    await check_start_code_word_on_existence()
    await call_inactive_users_to_action()
