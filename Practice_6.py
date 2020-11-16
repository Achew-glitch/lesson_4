from itertools import count
from itertools import cycle

global num_iter_int
num_iter_int = []


def iter_int(start_num):
    for ind in count(start_num):
        if ind > 10:
            break
        else:
            print(ind)
            num_iter_int.append(ind)


iter_int(3)
print(len(num_iter_int))

c = 0

for el in cycle(num_iter_int):
    if c > len(num_iter_int) - 1:
        break
    print(el)
    c += 1
