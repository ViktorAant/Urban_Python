import re

def symbol_count(in_str):
    in_str = in_str.replace('Ч', '4')
    str_len = len(in_str)

    rl = len(re.findall(r'[АБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗ]\s*[A-Z]', in_str))
    lr = len(re.findall(r'[A-Z]\s*[АБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗ]', in_str))

    ld = len(re.findall(r'[A-Z]\s*[-?:3ЭШЩ8Ю().,9014\'57=2/6+]', in_str))
    dl = len(re.findall(r'[-?:3ЭШЩ8Ю().,9014\'57=2/6+]\s*[A-Z]', in_str))

    rd = len(re.findall(r'[АБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗ]\s*[-?:3ЭШЩ8Ю().,9014\'57=2/6+]', in_str))
    dr = len(re.findall(r'[-?:3ЭШЩ8Ю().,9014\'57=2/6+]\s*[АБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗ]', in_str))

    return (1 + str_len + rl + lr + ld + dl + rd + dr)

print(symbol_count('ВЫПИСКА ИЗ СУТОЧНОГО ПЛАНА ПО АЭРОДРОМУ UAAA ЗА 0211 ЧАСТЬ1'))
