# Домашнее задание по теме "Оператор "with".
# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
import string

tabl = str.maketrans(',.=!?;:', '       ')
tab2 = str.maketrans(' - ', '   ')


class WordsFinder():
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        self.all_words = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                str = file.read()
                low_str = str.lower()
                str = low_str.translate(tabl)
                new_str = str.translate(tab2)
                str = new_str.split()
                self.all_words[f] = str
        return self.all_words

    def find(self, word):
        all_words = self.get_all_words()
        founded = {}
        for key, value in all_words.items():
            try:
                founded[key] = value.index(word.lower()) + 1
            except ValueError:
                continue
        return founded

    def count(self, word):
        all_words = self.get_all_words()
        number_of_words = {}
        for key, value in all_words.items():
            try:
                number_of_words[key] = value.count(word.lower())
            except ValueError:
                continue
        return number_of_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
