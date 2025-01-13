'''
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:

    id - целое число, первичный ключ
    title(название продукта) - текст (не пустой)
    description(описание) - текст
    price(цена) - целое число (не пустой)

get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
'''
import logging

from config import *
import sqlite3
import random

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL, 
    email TEXT NOT NULL, 
    age INT NOT NULL,
    balance INT NOT NULL
    );
    ''')
    connection.commit()


def fill_table():
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
                       (f'Product {i}', f'Описание {i}', f'{i}00'))
    connection.commit()


def get_all_products():
    return cursor.execute('SELECT * FROM Products').fetchall()


def is_included(username):
    check_user = cursor.execute('''
    SELECT * FROM Users WHERE username = ?
    ''', (username,))
    if check_user.fetchone():
        return True
    else:
        return False


def add_user(username, email, age):
    if not is_included(username):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
        connection.commit()
