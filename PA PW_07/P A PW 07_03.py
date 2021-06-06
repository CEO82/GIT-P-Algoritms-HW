"""

Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).

При решении использован алгоритм quickselect

"""

import random

navel_fn = random.choice # Функция по установке опорного элемента


def quickselect(lst, ind, navel_fn):
    pass
    if len(lst) == 1:
        return lst[0]

    navel = navel_fn(lst)

    left = [num for num in lst if num < navel]
    right = [num for num in lst if num > navel]
    navels = [num for num in lst if num == navel]

    if ind < len(left):
        # если длинна левого списка больше индекса, повтороно обходим левый список
        return quickselect(left, ind, navel_fn)
    elif ind < len(left) + len(navels):
        # ура медиана нашлась сама по себе ;)))
        return navels[0]
    else:
        # если длинна правого списка больше индекса, повтороно обходим правый список
        return quickselect(right, ind - len(left) - len(navels), navel_fn)


# array = [5, 18, 31, 1, 7, 18, 3, 4, 31, 6, 2]

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE * 2 + 1)]

# 2m + 1

median = quickselect(array, len(array) / 2, navel_fn)

print(f'исходный массив:\n{array}')
print(f'медиана в массиве = {median}')
print(f'{sorted(array)}\n:отсортированный массив')