from functools import reduce
from functools import partial
from itertools import count
from itertools import cycle
from math import isfinite

generator = (param * param for param in range(0, 5))

for el in generator:
    print(el)


def generator():
    for el in (10, 20, 30):
        yield el


g = generator()
print(g)

for el in g:
    print(el)

def my_func (prev_el, el):
    return prev_el + el

print(reduce(my_func, [10, 20, 30]))

def my_func_2 (param_1, param_2):
    return param_1 ** param_2

new_my_func_2 = partial(my_func_2, 2)

print(new_my_func_2)
print(new_my_func_2(4))


for el in count(7):
    if el > 15:
        break
    else:
        print(el)

c = 0
for el in cycle('ABC'):
    if c > 10:
        break
    print(el)
    c += 1

print(isfinite(1))
