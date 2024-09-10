# Дополнительное практическое задание по модулю 2

import random

massive = (3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
first_window = random.choice(massive)
# print('В первом окне видим число', first_window)
result = ''

for first_num in range(1, int(first_window/2) + 1): # перебираем элементы из списка для первого слагаемого
    second_num = first_num + 1
    while second_num < first_window and first_num + second_num <= first_window:
        second_window = first_num + second_num
#        print(f'{first_num} + {second_num} = {second_window}')
        if first_window % second_window == 0:
            result += f'{first_num}{second_num}'
        second_num += 1
print(result)