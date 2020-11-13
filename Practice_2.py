from random import randint


def compare(arg, pos):
    print(f'arg = {arg}, prev_arg = {num_list[pos-1]}')
    if arg > num_list[pos-1]:
        return arg


num_list = [randint(0, item * 100) for item in range(1, 7)]

print(num_list)

sort_list = [item for item in num_list[1:] if compare(item, num_list.index(item))]

print(sort_list)