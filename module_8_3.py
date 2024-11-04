# Домашнее задание по теме "Создание исключений"
'''
Задача "Некорректность"
Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи.
Повторить тему ООП и принцип инкапсуляции.
'''


class Car():
    def __init__(self, model, vin, numbers):
        self.model = model  # название автомобиля (строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin  # vin номер автомобиля (целое число). Уровень доступа private
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # номера автомобиля(строка)

    def __is_valid_vin(self, vin_number):
        # принимает vin_number и проверяет его на корректность.
        # Возвращает True, если корректный, в других случаях выбрасывает исключение.
        # Уровень доступа private.
        # if isinstance(vin_number, int) and 1000000 <= vin_number and vin_number <= 9999999:
        if isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999:
            return True
        elif not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        # принимает numbers и проверяет его на корректность.
        # Возвращает True, если корректный, в других случаях выбрасывает исключение.
        # Уровень доступа private.
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        elif not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        else:
            raise IncorrectVinNumber('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, msg):
        self.message = msg  # 'Сработало исключение IncorrectVinNumber'


class IncorrectCarNumbers(Exception):
    def __init__(self, msg):
        self.message = msg  # 'Сработало исключение IncorrectCarNumbers'


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
