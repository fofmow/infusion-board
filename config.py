from dataclasses import dataclass
from os import environ
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger

from storage.executor import DataBaseExecutor

BOT_TOKEN = environ.get("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

db = DataBaseExecutor()

WEB_APP_URL = environ.get("WEB_APP_URL")

SUPPORT_TG_ACCOUNT_URL = environ.get("SUPPORT_TG_ACCOUNT_URL")

MODERATORS_TG_IDS = eval(environ.get("MODERATORS_TG_IDS"))

DEFAULT_ACTIVATION_WORD = "ПОРТАЛ АГРЕГАЦИИ"


@dataclass(frozen=True, slots=True)
class BotPath:
    ROOT_DIR = Path(__file__).resolve().parent
    STORAGE_DIR = ROOT_DIR / "storage"
    SETTINGS_JSON = STORAGE_DIR / "auth.json"


logger.add(BotPath.ROOT_DIR / "logs" / "dev.log", format="{time} {level} {message}",
           level="DEBUG", compression="zip", rotation="1 MB")
