# Стиль кода часть II. Цикл While

numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

ii = 0
max_ii = len(numbers)
while ii < max_ii:
    num_ii = numbers[ii]
    if num_ii > 0:
        print(num_ii)
    elif num_ii < 0:
        break
    ii = ii + 1