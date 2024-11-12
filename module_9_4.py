# Создание функций на лету
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.

first = 'Мама мыла раму'
second = 'Рамена мало было'
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.

print(list(map(lambda x, y: x.strip() == y, first, second)))


def get_advanced_writer(file_name):  # file_name - название файла для записи
    # Функция get_advanced_writer возвращает функцию write_everything.
    def write_everything(*data_set):  # где *data_set - неограниченное количество данных любого типа
        # Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
        with open(file_name, 'a') as f:
            f.write(str(data_set))

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
])

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
