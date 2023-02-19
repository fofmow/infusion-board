from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from config import HR_TG_ID, DEFAULT_ACTIVATION_WORD
from tools.json_executor import json_settings
from tools.misc import send_message_from_bot
from tools.notifications.inactive import call_inactive_users_to_action


async def check_start_code_word_on_existence():
    """ Оповещение HR о том, что кодовое слово доступа не задано """
    
    if not await json_settings.get_start_code_word():
        await send_message_from_bot(
            HR_TG_ID,
            text="<b>Warning! Кодовое слово для активации бота не установлено!</b>\n\n"
                 "Чтобы изменить параметр, введите команду /moderator и кликните "
                 "кнопку <b>«Задать Кодовое Слово»</b>.\n\nПароль по умолчанию: "
                 f"«{DEFAULT_ACTIVATION_WORD}»"
        )


async def on_startup(_):
    scheduler = AsyncIOScheduler()
    half_hour_trigger = IntervalTrigger(minutes=30)
    
    scheduler.add_job(call_inactive_users_to_action, trigger=half_hour_trigger)
    scheduler.start()
    
    await check_start_code_word_on_existence()
    await call_inactive_users_to_action()
