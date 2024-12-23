'''
Асинхронность на практике
Цель: приобрести навык использования асинхронного запуска функций на практике
'''
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_n in range(5):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {ball_n + 1}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    man1 = asyncio.create_task(start_strongman('Вася', 1))
    man2 = asyncio.create_task(start_strongman('Федя', 2))
    man3 = asyncio.create_task(start_strongman('Клим', 3))
    await man1
    await man2
    await man3

asyncio.run(start_tournament())

