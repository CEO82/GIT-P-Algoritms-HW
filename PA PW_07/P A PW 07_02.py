"""

Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.


"""
import random

# array = [-17, 15, -100, 93, -26, 78, 70, 11, -95, -58]

# array = [5, 18, 31, 1, 7, 18]


def array_merg(l, r):
    merged_arr = []
    i = j = 0
    # print(f'{l=} {r=}')
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged_arr.append(l[i])
            i += 1
        else:
            merged_arr.append(r[j])
            j += 1

    if i < len(l):
        merged_arr += l[i:]
    if j < len(r):
        merged_arr += r[j:]

    return merged_arr


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    navel = len(lst) // 2
    left = merge_sort(lst[:navel])
    right = merge_sort(lst[navel:])
    # print(f'{left=} {right=}')
    return array_merg(left, right)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.uniform(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(f'исходный массив\n{array}')

print(f'отсортированный массив\n{merge_sort(array)}')
