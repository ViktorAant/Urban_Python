class Figure():
    sides_count = 0
    __sides = []
    __color = [0, 0, 0]
    filled = 0

    def get_color(self):
        # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, color):
        # служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой
        # нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)
        if 0 <=color[0] <= 255 and 0 <= color[1] <= 255 and 0 <= color[2] <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        # принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        # предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color([r, g, b]):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        # служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
        # и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        return True  #######################

    def get_sides(self):
        # должен возвращать значение атрибута __sides.
        return self.__sides

    def __len__(self):
        # должен возвращать периметр фигуры.
        return sum(self.__sides)

    def set_sides(self, new_sides):
        # должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
        # в противном случае - менять.
        # print(f'LEN = {len(new_sides)}  SIDES = {self.sides_count}')
        if isinstance(new_sides,list):
            self.__sides = new_sides
            print('меняем старые стороны на новые))')
        else:
            self.__sides[0] = new_sides
        # if len(new_sides) == self.sides_count:
        #     self.__sides = new_sides
        #     print('меняем старые стороны на новые))')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        self.set_color(color[0], color[1], color[2])
        self.set_sides(side)
        if isinstance(self.get_sides(),list):
            print(f'У класса Circle длина объекта задана списком: {self.get_sides()}')
        else:
            __radius = self.get_sides() / 3.14 / 2
            print(self.get_sides(), 'ELSE')

    def get_square(self):
        return self.__radius ** 2 * 3.14


circle1 = Circle((200, 200, 100), [10])  # (Цвет, стороны)
print(circle1.get_color())
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
