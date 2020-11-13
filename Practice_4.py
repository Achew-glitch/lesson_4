from random import randint


def clear_repetitions(item):
    count_num = num_list.count(item)
    if count_num == 1:
        return item


num_list = [randint(0, int(item / 2)) for item in range(1, 250)]

print(num_list)

sort_list = [item for item in num_list if clear_repetitions(item)]

print(sort_list)
