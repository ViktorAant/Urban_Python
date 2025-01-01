from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage import MemoryStorage
# import aiogram.contrib.fsm_storage
import asyncio

# from ShortAboutPython import union_set

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)