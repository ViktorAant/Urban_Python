# def max_in_list(lst):
#     mmax = lst[0]
#     for i in lst:
#         if mmax < i:
#             mmax = i
#
#     return mmax
#
# print(max_in_list([-2,-5,0]))

# def max_in_list(lst):
#     mmax = None
#     for i in range(len(lst)):
#         if mmax == None:
#             mmax = lst[i]
#         elif mmax < lst[i]:
#             mmax = lst[i]
#
#     return mmax
#
# print(max_in_list([-2,7,0]))

# def uniq_lst(lst):
#     uni_list = []
#     for i in lst:
#         if i in uni_list:
#             continue
#         else:
#             uni_list.append(i)
#     return uni_list
#
# print(uniq_lst([-2,7,0,7,7,1]))

# def uniq_lst(lst):
#     uni_list = lst[0]
#     for i in range(len(lst)):
#         if lst[i] in uni_list:
#             continue
#         else:
#             uni_list.append(lst[i])
#     return uni_list
#
# print(uniq_lst([-2,7,0,7,7,1]))


# def even_num(lst):
#     even_count = 0
#     for i in lst:
#         if i % 2 == 0:
#             even_count += 1
#     return even_count
#
# print(even_num([1,-4,5,0,1,2]))

# def even_num(lst):
#     even_count = 0
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0:
#             even_count += 1
#     return even_count
#
# print(even_num([1,-4,5,0]))

Дополнительное практическое задание по модулю: "Подробнее о функциях."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности


Задание "Раз, два, три, четыре, пять .... Это не всё?":
Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:

    Все числа (не важно, являются они ключами или значениям или ещё чем-то).
    Все строки (не важно, являются они ключами или значениям или ещё чем-то)


Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):

    Весь подсчёт должен выполняться одним вызовом функции.
    Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
    Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
    Для определения типа данного используйте функцию isinstance.


Файл с кодом (module_3_hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.

# -------------------------------------------------------------------------------------------------------------------

# Дополнительное практическое задание по модулю*

def calculate_structure_sum(data_structure):
  local_result = 0
  if isinstance(data_structure, int):
    local_result += data_structure
  elif isinstance(data_structure, str):
    local_result += len(data_structure)
  elif isinstance(data_structure, dict):
    for pair in data_structure.items():
      local_result += calculate_structure_sum(pair)
  elif isinstance(data_structure, list):
    for value in data_structure:
      local_result += calculate_structure_sum(value)
  elif isinstance(data_structure, tuple):
    for value in data_structure:
      local_result += calculate_structure_sum(value)
  elif isinstance(data_structure, set):
    for value in data_structure:
      local_result += calculate_structure_sum(value)
  else:
    print(f"Invalid data structure: {type(data_structure)}")
  return local_result
#----------------------
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)