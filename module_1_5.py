# module_1_5.py

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

immutable_var = (1, 2, 3, 'Луна', False)
print('Кортеж из нескольких элементов разных типов данных:', immutable_var)
# следущая строка при выполнении вызывает ошибку, так является примером попытки изменить кортеж
# immutable_var[0] = 'need'
# Неизменяемость (immutability) кортежей означает, что после их создания вы не можете изменить их содержимое.

immutable_var_new = ([1, 2], 3, 'Луна', False)
print(immutable_var_new)
# immutable_var_new = immutable_var_new [0][1] = 9
# print(immutable_var_new, id(immutable_var_new[0]))

mutable_list = [9, 8, 7, 'chip', True]
print(mutable_list)
mutable_list[1] = 0
print(mutable_list)
