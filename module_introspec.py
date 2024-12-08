'''
Интроспекция
Цель задания:
Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.
'''
import inspect
import re

class MyClass:
    my_class_attrib = 'Аттрибут моего класса'

    def __init__(self):
        self.count = 0

    def my_class_fun(self, x, y):
        self.x = x
        self.y = y
        self.count += 1


def introspection_info(obj):
    try:
        obj_module = obj.__module__
    except AttributeError:
        obj_module = None
    type_obj = type(obj)
    match = re.search(r'\'(.+)\'', str(type_obj))
    obj_type = match.group(1)
    obj_attributes = []
    obj_methods = []
    obj_total = {}
    for name, data in inspect.getmembers(obj):
        if inspect.isclass(data):
            pass
        elif inspect.isroutine(data):
            obj_methods.append(name)
        else:
            obj_attributes.append(name)
    obj_total['type'] = obj_type
    obj_total['attributes'] = obj_attributes
    obj_total['methods'] = obj_methods
    obj_total['module'] = obj_module
    print(obj_total)


obj = MyClass()
obj.my_class_fun(3, 4)
introspection_info((1,'42'))
introspection_info(42)
introspection_info(obj)
