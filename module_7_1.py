class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        txt = file.read()
        file.close()
        return txt

    def add(self, *products):
        # принимает неограниченное количество объектов класса Product.
        # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        # Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
        store = self.get_products()
        file = open(self.__file_name, "a")
        for p in [*products]:
            if str(p) in store:
                print(f'Продукт {p} уже есть в магазине')
            else:
                file.write(str(p) + '\n')
        file.close()


class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # возвращает строку в формате '<название>, <вес>, <категория>'.
        # Все данные в строке разделены запятой с пробелами.
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
