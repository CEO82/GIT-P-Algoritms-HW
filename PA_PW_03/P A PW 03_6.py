"""

В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

"""

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 101
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f'Исходный массив:\n{array}')

max_n = MIN_ITEM
max_n_i = 0
min_n = MAX_ITEM
min_n_i = 0
count = 0
range_sum = 0

for i in array:
    if max_n < i:
        max_n = i
        max_n_i = count
    if min_n > i:
        min_n = i
        min_n_i = count
    count += 1

if max_n_i < min_n_i:
    max_n_i, min_n_i = min_n_i, max_n_i

for z in array[min_n_i + 1: max_n_i]:
    range_sum += z

#print(f'{max_n= }, {min_n= }') """Просмотр макс и мин чисел массива"""
#print(f'Индекс:\nМаксимального числа: {max_n_i}, Минимального числа: {min_n_i}') """Просмотр индексов мин и макс чисел"""

print(f'Сумма элементов в диапазоне между минимальным и максимальным числом равна {range_sum}')

