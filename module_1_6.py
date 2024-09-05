# module_1_6

my_dict = {'Иван': 1950, 'Дмитрий': 1960, 'Екатерина': 1970, 'Матильда': 2000}
print(my_dict)
print(my_dict['Матильда'])
print(my_dict.get('Фома'))
my_dict.update({'Зинаида': 2002,
                'Серафим': 2011})
print(my_dict)
print(my_dict.pop('Дмитрий'))
print(my_dict)

my_set = {1,1,2,2,2,'Tmp','tmp',False,True}
print(my_set)
my_set.update({99, 'Фарида'})
print(my_set)
my_set.remove('Фарида')
print(my_set)