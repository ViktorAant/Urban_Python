'''
Введение в потоки
Цель: понять как работают потоки на практике, решив задачу
'''
import threading
from time import sleep


def write_words(word_count, file_name):
    # word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова
    with open(file_name, 'w') as file:
        for num_line in range(word_count):
            file.write(f"Какое-то слово № {num_line + 1}\n")
            sleep(0.1)
    return f"Завершилась запись в файл {file_name}"


write_words(10, 'example1.txt')
# write_words(30, 'example2.txt')
# write_words(200, 'example3.txt')
# write_words(100, 'example4.txt')

thread = threading.Thread(write_words(10, 'example5.txt'))
# thread2 = threading.Thread(write_words, args=(30, 'example6.txt',))
# thread3 = threading.Thread(write_words, args=(200, 'example7.txt',))
# thread4 = threading.Thread(write_words, args=(100, 'example8.txt',))
thread.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread3.join()
thread.join()