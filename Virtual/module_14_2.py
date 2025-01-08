'''
Выбор элементов и функции в SQL запросах
Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
'''
import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*), SUM(balance) FROM Users")

total_users, all_balances = cursor.fetchall()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
