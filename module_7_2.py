# Домашнее задание по теме "Позиционирование в файле".
# Цель:   Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.
#         Написать усовершенствованную функцию записи.

def custom_write(file_name, strings):
    # принимает аргументы file_name - название файла для записи, strings - список строк для записи.
    # Функция должна:
    #     Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    #     Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    #     а значением - записываемая строка.
    #     Для получения номера байта начала строки используйте метод tell() перед записью.
    file = open(file_name, "w", encoding='utf-8')
    cursor = file.tell()
    line = 1
    dict = {}
    for s in strings:
        dict[(line, cursor)] = s
        file.write(s + '\n')
        cursor = file.tell()
        line += 1
    file.close()
    return dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
