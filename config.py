from dataclasses import dataclass
from os import environ
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import WebAppInfo
from loguru import logger

from storage.executor import DataBaseExecutor

BOT_TOKEN = environ.get("BOT_TOKEN")

WEB_APP_URL = environ.get("WEB_APP_URL")

HR_TG_ACCOUNT_URL = environ.get("HR_TG_ACCOUNT_URL")

HR_TG_ID = int(environ.get("HR_TG_ID"))

DEFAULT_ACTIVATION_WORD = environ.get("DEFAULT_ACTIVATION_WORD")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

db = DataBaseExecutor()

web_app = WebAppInfo(url=WEB_APP_URL)


@dataclass(frozen=True, slots=True)
class BotPath:
    ROOT_DIR = Path(__file__).resolve().parent
    STORAGE_DIR = ROOT_DIR / "storage"
    STATIC_DIR = ROOT_DIR / "static"
    SETTINGS_JSON = STORAGE_DIR / "auth.json"


logger.add(BotPath.ROOT_DIR / "logs" / "dev.log", format="{time} {level} {message}",
           level="DEBUG", compression="zip", rotation="1 MB")
