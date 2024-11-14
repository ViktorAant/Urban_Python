'''
Декораторы
Задание: Декораторы в Python
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
'''


# Вариант 1 - с циклом "for"
# def is_prime(func):
#     def wrapper(*args):
#         original_result = func(*args)
#         prime_n = "Простое"
#         for i in range(2, int(original_result / 2) + 1):
#             if original_result % i == 0:
#                 prime_n = "Составное"
#                 break
#         print(prime_n)
#         return original_result
#     return wrapper

# Вариант 2 - с использованием исключений и сборок
def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        try:
            lst = [1 / 0 for i in range(2, int(original_result / 2) + 1) if original_result % i == 0]
        except ZeroDivisionError:
            print("Составное")
        else:
            print("Простое")
        return original_result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
