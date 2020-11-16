from itertools import count


def fact (n):
    m = 1
    for ind in count(1):
        if ind > n:
            break
        else:
            m *= ind
            yield m

x = int(input('Введите число: '))
ind = 0
for el in fact(x):
    if ind == x:
        break
    else:
        print(el)