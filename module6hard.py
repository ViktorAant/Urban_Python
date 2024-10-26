class Figure():
    sides_count = 0
    __sides = []
    __colour = [0, 0, 0]
    filled = 0

    def get_colour(self):
        # возвращает список RGB цветов
        return self.__colour

    def __is_valid_colour(self, colour):
        # служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой
        # нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)
        if 0 <= colour[0] <= 255 and 0 <= colour[1] <= 255 and 0 <= colour[2] <= 255:
            return True
        else:
            return False

    def set_colour(self, r, g, b):
        # принимает параметры r, g, b - числа и изменяет атрибут __colour на соответствующие значения,
        # предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_colour([r, g, b]):
            self.__colour = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        # служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
        # и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        if ( (isinstance(self, Cube) and len(new_sides) == 1) or (not isinstance(self, Cube) and len(new_sides) == self.sides_count) ) and min(new_sides) > 0:
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        if isinstance(self, Cube):
            return list(self.__sides*12)
        else:
            return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, colour, *side):
        self.set_colour(colour[0], colour[1], colour[2])
        if not self._Figure__is_valid_sides(*side):
            self.set_sides(1)
        else:
            self.set_sides(*side)
        __radius = self._Figure__sides[0] / 3.14 / 2

    def get_square(self):
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colour, *side):
        self.set_colour(colour[0], colour[1], colour[2])
        if not self._Figure__is_valid_sides(*side):
            self.set_sides(1)
        else:
            # Необходимым и достаточным условием существования треугольника является выполнение следующих неравенств:
            # a+b>c, a+c>b, b+c>a, (a>0, b>0, c>0)
            a = self.get_sides()[0]
            b = self.get_sides()[1]
            c = self.get_sides()[2]
            if (a + b > c or a + c > b or b + c > a):
                self.set_sides(*side)
            else:
                self.set_sides(1)

    def get_square(self):
        # возвращает площадь треугольника. (можно рассчитать по формуле Герона)
        p = len(self) / 2
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, colour, *side):
        self.set_colour(colour[0], colour[1], colour[2])
        self.set_sides(*side)
        if not self._Figure__is_valid_sides(*side):
            self.set_sides(1)

    def get_volume(self):
        # возвращает объём куба
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_colour(55, 66, 77) # Изменится
print(circle1.get_colour())
cube1.set_colour(300, 70, 15) # Не изменится
print(cube1.get_colour())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
