# Дополнительное практическое задание по модулю 5

class UrTube:
    """
    Класс UrTube - списки пользователей и видосиков, текущий пользователь (куда-то течет))
    """
    def __init__(self):
        self.users = []
        self.videos = set()
        self.current_user = None

    def log_in(self, nickname, password):
        for uu in self.users:
            if uu.nickname == nickname and uu.password == hash(password):
                self.current_user = uu
                print("Пользователь с указанными данными найден")
                return
            else:
                print("Пользователь с указанными данными не обнаружен")
        # пытается найти пользователя в users с такими же логином и паролем.
        # Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся
        # в виде строки, а сравнивается по хэшу.
        pass

    def register(self, nickname, password, age):
        for uu in self.users:
            if nickname == uu.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        self.current_user = User(nickname, password, age)
        # Добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        # Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        # После регистрации, вход выполняется автоматически.

    def log_out(self):
        self.current_user = None
        # Для сброса текущего пользователя на None

    def add(self, *args):
        # Принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        # если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        for video in args:
            self.videos.add(video)

    def get_videos(self, video_search):
        # Принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
        # Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        ret_lst = []
        for elmt in self.videos:
            if video_search.upper() in elmt.__str__().upper():
                ret_lst.append(elmt.__str__())
        return ret_lst

    def watch_video(self, video):
        from time import sleep

        for vv in self.videos:
            if video == vv.title:
                if self.current_user != None:
                    if vv.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    else:
                        while vv.time_now < vv.duration :
                            sleep(1)
                            vv.time_now += 1
                            print(vv.time_now, end=' ')
                    vv.time_now = 0
                    print("Конец видео")
                    return
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    return
        print(f'Видео "{video}" не найдено')
        # Принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        # то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        # После текущее время просмотра данного видео сбрасывается.
        # Для метода watch_video так же учитывайте следующие особенности:
        # 1.  Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        # 2.  Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        #     В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        # 3.  Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
        #     т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        # 4.  После воспроизведения нужно выводить: "Конец видео"


class Video:
    """
    Класс видео - полезные ролики на тему IT (юмористические, интервью и т.д.)
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class User:
    """
    Класс пользователя с атрибутами логин, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# if __name__ == '__main__':
#     import re
#
#     regexUC = "[A-ZА-ЯЁ]"
#     regexN = "[0-9]"
#     database = Database()
#     while True:
#         choice = input('Привет! Выберите действие: \n1 - Вход \n2 - Регистрация \n')
#
#         user = User(input('Введите логин: '), password1 := input('Введите пароль: '), password2 := input('Повторите пароль: '))
#
#         if password1 != password2:
#             print('Пароли должны совпадать.')
#             exit()
#
#         if ' ' in password1:
#             print('Пробел в пароле недопустим.')
#             exit()
#
#         if len(password1) < 8:
#             print('Длина пароля должна быть не менее 8 символов.')
#             exit()
#
#         patternN = re.compile(regexN)
#         patternUC = re.compile(regexUC)
#
#         if patternN.search(password1) is None:
#             print('В пароле должна быть хотя бы одна цифра.')
#             exit()
#
#         if patternUC.search(password1) is None:
#             print('В пароле должна быть хотя бы одна заглавная буква.')
#             exit()
#
#         database.add_user(user.username, user.password)
# import sys
# sys.stdout.write("\r" + "%3s" %(str(vv.time_now)) + " out of " + str(vv.duration))
# sys.stdout.flush()

