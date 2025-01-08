'''
Доработка бота
Цель: подготовить Telegram-бота для взаимодействия с базой данных
'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

calculate = KeyboardButton(text='Рассчитать')
information = KeyboardButton(text='Информация')
buy = KeyboardButton(text='Купить')
kb = ReplyKeyboardMarkup(resize_keyboard=True).add(calculate, buy, information)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
calculate = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(calculate, formulas)

bkb = InlineKeyboardMarkup(resize_keyboard=True)
buy1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
buy2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
buy3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
buy4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
bkb.add(buy1, buy2, buy3, buy4)


@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer_photo(photo=open('pics/1.png', 'rb'), \
                               caption='\rНазвание: Product1 | Описание: описание 1 | Цена: 100\n')
    await message.answer_photo(photo=open('pics/2.png', 'rb'), \
                               caption='\rНазвание: Product2 | Описание: описание 2 | Цена: 200\n')
    await message.answer_photo(photo=open('pics/3.png', 'rb'), \
                               caption='\rНазвание: Product3 | Описание: описание 3 | Цена: 300\n')
    await message.answer_photo(photo=open('pics/4.png', 'rb'), \
                               caption='\rНазвание: Product4 | Описание: описание 4 | Цена: 400\n', \
                               reply_markup=bkb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def set_age(call):
    await call.message.answer(
        "Упрощенный вариант формулы Миффлина-Сан Жеора:\n \
        для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n \
        для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


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
            f"Упрощенный вариант формулы Миффлина-Сан Жеора для женщин. \
            {(10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) - float(161)}")
    else:
        await message.answer(
            f"Упрощенный вариант формулы Миффлина-Сан Жеора для мужиков. \
            {(10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) + float(5)}")
    await state.finish()


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer("Информация о боте.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
