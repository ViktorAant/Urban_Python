# Дополнительное практическое задание по модулю*

def calculate_structure_sum(data_structure):
    result = 0
    for i in data_structure:
        type_ = type(i)
        if type_ == int:
            result += int(i)
        elif type_ == str:
            result += len(i)
        elif type_ == dict:
            for key, value in (i.items()):
                result += calculate_structure_sum(key)
                if type(value) == int:
                    result += value
                else:
                    result += calculate_structure_sum(value)
        else:
            result += calculate_structure_sum(i)
    return result
    
#----------------------    
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
