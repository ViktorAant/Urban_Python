# Цикл for. Элементы списка. Полезные функции в цикле"
# предполагаем, что список неупорядочен и может содержать неположительныеные
# В not_primes сохраняем только положительные не простые числа, большие 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
max_num = max(numbers)
#print('Max=',max_num)
primes = []
not_primes = []
for i in numbers:
#    print(i)
    if i <= 1:
#        not_primes.append(i)
        continue
    elif i == 2:
        primes.append(i)
    else:
        is_prime = False
        for k in range(max_num):
            divider = k + 1
            if is_prime == True: 
                break # перебор закончен
            if divider == 1 or divider >= i:
                continue
            else: 
#                print(f'{i} / {divider}', i % divider)
                if i % divider == 0:
                    not_primes.append(i)
                    break # число не простое, выходим из цикла
                else: 
                    is_prime = True
                    primes.append(i)
#                    print(i)
print('primes=', primes)
print('not_primes=', not_primes)
