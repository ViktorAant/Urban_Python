'''
Обзор сторонних библиотек Python
Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.
Мой выбор - requests. Я новичок в веб-программировании и решил, что знакомство с requests - хороший повод погрузиться
'''

# Python библиотека Requests на Github имеет отличные показатели: Star 52.2k  Fork 9.3k
# Установка из терминала pip install requests - прошла быстро и без проблем.
# Нашел в инете несколько статей; понравилась эта - https://python-scripts.com/requests?ysclid=m476i91m13979224021
# "Библиотека requests является стандартным инструментом для составления HTTP-запросов в Python.
#  Простой и аккуратный API значительно облегчает трудоемкий процесс создания запросов.
#  Таким образом, можно сосредоточиться на взаимодействии со службами и использовании данных в приложении."
# Поехали изучать)

# Python библиотека Requests метод GET -----------------------------------------------------
# GET является одним из самых популярных HTTP методов.
# Метод GET указывает на то, что происходит попытка извлечь данные из определенного ресурса.
# Для того, чтобы выполнить запрос GET, используется requests.get().
import requests     # не забываем импортировать модуль!

# response = requests.get('https://yandex.ru/')
# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')
# else:
#     print('Others')

# response = requests.get('https://api.github.com')
# response.content
# response.text
# response.headers

# Поиск местонахождения для запросов на GitHub
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# Заключение
# Изучение библиотеки Python requests является очень трудоемким процессом.

# похоже, что с наскока эту тему не одолеть; наверное, попозже смогу к ней вернуться