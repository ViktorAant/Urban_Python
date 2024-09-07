# 00:00|Дополнительное практическое задание по модулю

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avr_marks_of_students = []

studs = sorted(list(students))
print(studs)
for i in range(len(grades)):
    avr_marks_of_students.append(round(sum(grades[i])/len(grades[i]),2))

my_dict = dict(zip(studs, avr_marks_of_students))
print(my_dict)
