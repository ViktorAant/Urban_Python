'''
Создание БД, добавление, выбор и удаление элементов
Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3
'''
import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", \
                   (f"user{i + 1}", f"example{i + 1}@gmail.com", (i + 1) * 10, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE (id-1) % 2 = 0")

cursor.execute("DELETE FROM Users WHERE (id-1) % 3 = 0")

cursor.execute("SELECT username, email, age, balance FROM users WHERE age <> 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.commit()
connection.close()
