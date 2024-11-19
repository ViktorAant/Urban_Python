'''
Потоки на классах
Цель: научиться создавать классы наследованные от класса Thread.
'''
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def timer(self, name, power):
        self.boys = 100 - power
        self.days = 1
        while self.boys > 0:
            time.sleep(1)
            print(f"{name} сражается {self.days}..., осталось {self.boys} воинов.")
            self.days += 1
            self.boys -= power
        print(f"{name} одержал победу спустя {self.days} дней(дня)!")

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.timer(self.name, self.power)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()

print("Все битвы закончились!")
