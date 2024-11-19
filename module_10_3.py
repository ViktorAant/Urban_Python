'''
Блокировки и обработка ошибок
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
'''
import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for n in range(100):
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            inc_balance = random.randint(50, 500)
            self.balance += inc_balance
            # self.lock.acquire()
            print(f"Пополнение: {inc_balance}. Баланс: {self.balance}")
            # self.lock.release()
            time.sleep(0.001)

    def take(self):
        for n in range(100):
            dec_balance = random.randint(50, 500)
            print(f"Запрос на {dec_balance}")
            if self.balance - dec_balance >= 0:
                self.balance -= dec_balance
                print(f"Снятие: {dec_balance}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f"Итоговый баланс: {bk.balance}")
