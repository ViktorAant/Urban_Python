'''
Генераторы
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
'''
from mailcap import subst


def all_variants(text):
    lentxt = len(text)
    p = 1
    s = text[0]
    for ln in range(1, lentxt):      # длина подстроки
        # for p in range(lentxt):     # позиция начала подстроки
        while p + ln <= lentxt + 1:
            yield s
            s = text[p:ln]
            p += 1
        ln += 1

a = all_variants("abc")
for i in a:
    print(i)


# которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться
# подпоследовательности переданной строки.
#
# first = 'Мама мыла   раму'
# second = 'Рамена мало было'
# # Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# # Здесь ? - место написания lambda-функции.
#
# # print(list(map(lambda x, y: x.strip() == y, first, second)))
# print('_'.join(first.split()))
