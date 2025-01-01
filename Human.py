class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print('Здравствуйте')


class Student(Human):
    def about(self):
        print('Я студент')


class Teacher(Human):
    pass