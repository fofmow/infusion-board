import aiofiles
import ujson

from config import BotPath


class JSONSettingsExecutor:
    def __new__(cls):
        if not hasattr(JSONSettingsExecutor, "instance"):
            cls.instance = super(JSONSettingsExecutor, cls).__new__(cls)
        return cls.instance
    
    @staticmethod
    async def get_value_by_key(key: str):
        async with aiofiles.open(BotPath.SETTINGS_JSON) as json_file:
            settings: dict = ujson.loads(await json_file.read())
        return settings.get(key)
    
    @staticmethod
    async def update(key: str, new_value: str):
        async with aiofiles.open(BotPath.SETTINGS_JSON) as json_file:
            settings: dict = ujson.loads(await json_file.read())
            settings[key] = new_value
        
        async with aiofiles.open(BotPath.SETTINGS_JSON, mode="w", encoding="utf-8") as json_file:
            await json_file.write(ujson.dumps(settings, ensure_ascii=False, indent=4))
    
    @classmethod
    async def get_start_code_word(cls) -> str:
        return await cls.get_value_by_key("start_code_word")
    
    @classmethod
    async def update_start_code_word(cls, new_password: str) -> None:
        await cls.update("start_code_word", new_password)


json_settings = JSONSettingsExecutor()
