'''
Многопроцессорное программирование
Цель: понять разницу между линейным и многопроцессорным подходом, выполнив операции обоими способами.
'''
import time
from multiprocessing import Pool

filenames = [f'./file {number}.txt' for number in range(1, 5)]

def read_info(file):
    all_data = []

    with open(file, 'r') as file:
        for readline in file:
            if readline <= " ":
                return
            all_data.append(readline)


start_time = time.time()
for name in filenames:
    read_info(name)
time_stop = time.localtime()
end_time = time.time()
execution_time = round(end_time - start_time, 2)
print(f"Время выполнения: {execution_time} секунд")

# if __name__ == '__main__':
#     start_time = time.time()
#     with Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     time_stop = time.localtime()
#     end_time = time.time()
#     execution_time = round(end_time - start_time, 2)
#     print(f"Время выполнения: {execution_time} секунд")
