"""

В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

"""


import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f'Исходный массив:\n{array}')

count = 0
position = 0
max_neg_num = MIN_ITEM
for i in array:

    if i < 0 and i > max_neg_num:
        max_neg_num = i
        position = count
    count += 1

print(f'Максимальное отрицательное число в массиве {max_neg_num} и его позиция в массиве {position + 1} (его индекс = {position})')
