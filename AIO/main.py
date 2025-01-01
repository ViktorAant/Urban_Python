from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7589123348:AAF7YNKzA1Qi11UqHe26tQFzLPAIFe-5ixo"
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(text = ["www", "sss"])
async def all_message(message):
    print("Urban сообщение!")

@dp.message_handler(commands = ["start"])
async def all_message(message):
    print("Command сообщение!")

@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
