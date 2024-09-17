# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a = 1, b = 'строка', c = True):
    print(f'a = {a}, b = {b}, c = {c}')

values_list = [13, 'пятница', False] 
values_dict = {'a':True, 'b': 'String', 'c': 13}
values_list_2 = [7, 'yes']

print_params()
print_params(b = 25) 
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)