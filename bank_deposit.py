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
        self.has_money = threading.Condition(lock=self.lock) # Conditional Variable

    def deposit(self):
        for n in range(100):
            with self.lock:
                inc_balance = random.randint(50, 500)
                self.balance += inc_balance
                print(f"Пополнение: {inc_balance}. Баланс: {self.balance}")
                # извещаем всех ожидающих снятия блокировки
                self.has_money.notify_all()
            time.sleep(0.001)

    def take(self):
        for n in range(100):
            with self.lock:
                dec_balance = random.randint(50, 500)
                print(f"Запрос на {dec_balance}")
                if self.balance - dec_balance < 0:
                    print("Средств недостаточно, ждем денег")
                # проверка и/или ожидание условия достаточности средств
                # ожидание снятия блокировки - сон; пробуждение по has_money.notify_all())
                sufficient_money = self.has_money.wait_for(lambda: self.balance - dec_balance >= 0, 0.1)
                if sufficient_money:
                    self.balance -= dec_balance
                    print(f"Снятие: {dec_balance}. Баланс: {self.balance}")
                else:
                    # если вышли по таймауту (поток deposit закончил работу, а средств всё не хватает))
                    print("Конец программы, денег недостаточно для снятия")
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
