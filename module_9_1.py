# Введение в функциональное программирование
"""
Введение в функциональное программирование.
Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.
"""


def apply_all_func(int_list, *functions):
    # int_list - список из чисел (int, float)
    # *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    # Эта функция должна:
    # Вызвать каждую функцию к переданному списку int_list
    # Возвращать словарь, где ключом будет название вызванной функции,
    # а значением - её результат работы со списком int_list
    if not isinstance(int_list, list) or not all([isinstance(item, (int, float)) for item in int_list]):
        print('Первый аргумент должен быть списком и состоять только из чисел. Мы получили: ', int_list)
        return None
    results = {}
    for ff in functions:
        results[ff.__name__] = ff(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
