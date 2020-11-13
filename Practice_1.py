from sys import argv
from random import randint


script_name, work_time, rate = argv
print(f'Зарплата за этот месяц: {int(work_time) * int(rate) + randint(0, 15000)}')