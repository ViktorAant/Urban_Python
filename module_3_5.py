# Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):
    str_number = str(number)
    if not(str_number.isnumeric()):
        return (f'Аргумент содержит символы, отличные от числовых: "{str_number}"')
    if number < 1:
        return 1
    first = int(str_number[:1])    
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else: 
        return first
        
print(get_multiplied_digits(240))