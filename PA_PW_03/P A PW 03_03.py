"""

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f'Исходный массив:\n{array}')

max_n = MIN_ITEM
max_n_i = 0
min_n = MAX_ITEM
min_n_i = 0
count = 0

for i in array:
    if max_n < i:
        max_n = i
        max_n_i = count
    if min_n > i:
        min_n = i
        min_n_i = count
    count += 1

array.insert(min_n_i, max_n)
array.pop(min_n_i + 1)
array.insert(max_n_i, min_n)
array.pop(max_n_i + 1)
print(f'Изменный массив:\n{array}')

print(f'В исходном массиве:\nМаксимальное число: {max_n}, Минимальное число: {min_n}')
print(f'Позиция (не индекс):\nМаксимального числа: {max_n_i + 1}, Минимального числа: {min_n_i + 1}')

