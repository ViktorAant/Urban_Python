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
        self.lock = threading.Condition()
        self.has_money = threading.Lock()

    def deposit(self):
        for n in range(100):
            have_it = self.lock.acquire(blocking=False)
            if have_it:
                inc_balance = random.randint(50, 500)
                self.balance += inc_balance
                print(f"Пополнение: {inc_balance}. Баланс: {self.balance}")
                self.lock.release()
            if self.balance > 500 and self.lock.acquire():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for n in range(100):
            # have_it = self.lock.acquire(blocking=False)
            # if have_it:
            with self.lock:
                dec_balance = random.randint(50, 500)
                print(f"Запрос на {dec_balance}")
                if self.balance - dec_balance >= 0:
                    self.balance -= dec_balance
                    print(f"Снятие: {dec_balance}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                # self.lock.release()
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
