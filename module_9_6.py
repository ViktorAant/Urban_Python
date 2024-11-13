'''
Генераторы
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
'''


def all_variants(text):
    lent = len(text)    # длина входной строки
    for ln in range(1, lent):  # длина подстроки
        for p in range(lent):  # позиция начала подстроки
            if p + ln > lent:  # условие выхода за правую границу входной строки
                break
            s = text[p:p + ln]  # достаем подстроку
            yield s


a = all_variants("abc")
for i in a:
    print(i)
