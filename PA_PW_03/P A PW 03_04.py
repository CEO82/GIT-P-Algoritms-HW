"""

Определить, какое число в массиве встречается чаще всего.

Для преподавателя: т.к. в массиве часто генерируются числа с одинаковым максимальным кол-вом вхождения в массив,
я сделал так что в ответе выводятся все числа имеющие одинаковое максимальное кол-во вхождений в массив

"""

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f'Исходный массив:\n{array}')

def key_d(dict_1, value):
    temp_dict = {}
    print(f'Числа которые чаще всего втсречаются в массиве это: ')
    for key, val in dict_1.items():
        if val == value:
            print(key, end=', ')

count_d = {}
big_n = 0
big_ch = 0
for i in array:
    count_d[i] = array.count(i)

#print(count_d) """Выводит словарь с парой число и кол-во его вхождений в массив"""

for z in count_d:
    #print(f' {z} {count_d[z]}') """Визуальная проверка кол-ва вхождений чичла в массив"""
    if count_d[z] > big_n:
        big_ch = z
        big_n = count_d[z]
#print(f'{big_ch= } {big_n= }') """Проверка максимального вхождения числа"""

answ = key_d(count_d, big_n)



