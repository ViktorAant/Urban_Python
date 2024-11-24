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
            # Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его
            # методом release.
            if self.balance > 500 and self.lock.locked():  # зачем это вообще?!
                self.lock.release()
            inc_balance = random.randint(50, 500)
            self.balance += inc_balance
            print(f"Пополнение: {inc_balance}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for n in range(100):
            dec_balance = random.randint(50, 500)
            print(f"Запрос на {dec_balance}")
            if self.balance - dec_balance >= 0:
                self.balance -= dec_balance
                print(f"Снятие: {dec_balance}. Баланс: {self.balance}")
            else:
                # Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён,
                # недостаточно средств" и заблокировать поток методом acquire.
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire() # два варианта: если цикл deposit уже закончен, то получим ВЕЧНУЮ блокировку
                                    #               независимо от окончания deposit получаем ВЕЧНУЮ блокировку
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
