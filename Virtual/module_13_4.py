'''
Машина состояний
Цель: получить навык работы с состояниями в телеграм-боте.
'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer("Признайтесь, корнет, вы - женщина? (Y/N):")
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    if data['gender'] == 'Y':
        await message.answer(
            f"Упрощенный вариант формулы Миффлина-Сан Жеора для женщин. {(10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) - float(161)}")
    else:
        await message.answer(
            f"Упрощенный вариант формулы Миффлина-Сан Жеора для мужиков. {(10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) + float(5)}")
    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
