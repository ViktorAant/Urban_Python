# Функции

list_ = ['one', 'two', 'three'] # , 'well', 'aaron', 'zebra'
list2_ = [1, 2, 5]
dict_ = {'a': 1, 'c': 3, 'b': 2}
for i, k in dict_.items(): # in dict_:  # range(len(list_)):
   print(i, k)  # print(i, dict_[i])
#for count, value in enumerate(list_):
#    print(count, value)
#print(list_, max(list_), min(list_), sum(list2_))
def test(a=2, b=True):
    print(a, b)
test(**{'a': 7, 'b': 3})