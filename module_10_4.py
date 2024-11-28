'''
Очереди для обмена данными между потоками
Цель: Применить очереди в работе с потоками, используя класс Queue.
'''
import time
import random
import threading
from queue import Queue


class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe():
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = [tab for tab in args]
        self.list_active_guests = {}
        print([self.tables[i].number for i in range(len(self.tables))])

    def guest_arrival(self, *guests):  # (прибытие гостей)
        for g in range(len(guests)):
            self.list_active_guests[guests[g].name] = None
            luck = False
            for i in range(len(self.tables)):
                if self.tables[i].guest == None:
                    luck = True
                    self.tables[i].guest = guests[g].name
                    tr = threading.Thread(None, guests[g].run)
                    tr.start()
                    print(f"{guests[g].name} сел(-а) за стол номер {self.tables[i].number}")
                    self.list_active_guests[guests[g].name] = tr
                    break
            if not luck:
                self.queue.put(guests[g].name)
                print(f"{guests[g].name} в очереди")

    def discuss_guests(self):
        while not (self.queue.empty() and [i for i in range(len(self.tables)) if self.tables[i].guest != None] == []):
            # выходим если очередь пустая и нет занятых столов
            for guest, trd in self.list_active_guests.items():
                if trd != None and not trd.is_alive():
                    for t in range(len(tables)):
                        if tables[t].guest == guest:
                            print(f"{guest} покушал(-а) и ушёл(ушла)")
                            print(f"Стол номер {t + 1} свободен")
                            tables[t].guest = None  # освобождаем стол
                            self.list_active_guests[guest] = None  # покушал - удаляем из списка активных гостей
                            if not self.queue.empty():  # есть еще очередь в наш ресторан?
                                new_guest = self.queue.get()
                                for guest in guests:
                                    if guest.name == new_guest:
                                        tables[t].guest = new_guest
                                        tr = threading.Thread(None, guest.run)
                                        print(
                                            f"{new_guest} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[t].number}")
                                        self.list_active_guests[new_guest] = tr
                                        tr.start()
        print('Все счастливы и пошли пить пиво)')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
