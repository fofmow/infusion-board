from dotenv import load_dotenv

load_dotenv()

import logging
from aiogram import executor
from handlers import dp
from startup import on_startup

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
