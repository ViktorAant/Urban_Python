def digits(*args):
    total = 1
    for number in args:
        total *= number ** 2
        print(total)
    return(len(str(total)))

print(digits(2, 3, 4))
print(36*16)