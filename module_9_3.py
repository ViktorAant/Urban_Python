# Генераторные сборки
# Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y)]
# запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second, если их длины не равны.
# Для перебора строк попарно из двух списков используйте функцию zip.

second_result = [len(first[i]) == len(second[i]) for i in range(min(len(first), len(second)))]
# запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков
# first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

print(list(first_result))
print(list(second_result))
