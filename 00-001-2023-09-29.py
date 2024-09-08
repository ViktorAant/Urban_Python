# 00-001-2023-09-29 Условная конструкция. Операторы if, elif, else
first = 3
second = 3
third = 3

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)