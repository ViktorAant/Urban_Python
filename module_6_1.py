# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    alive = True  # (живой)
    fed = False  # (накормленный)

    def __init__(self, name):
        self.name = name  # индивидуальное название каждого животного

    # Метод eat должен работать следующим образом:
    # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
    # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
    # Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant():
    edible = False  # (съедобность)

    def __init__(self, name):
        self.name = name  # индивидуальное название каждого растения


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True  # (переопределить при наследовании)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
# print(p1.edible, p2.edible)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
