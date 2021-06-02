"""

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти.

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти
(укажите какую задачу вы взяли в комментарии);

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный;

● результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей
ОС и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.

Исходное задание:

Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

"""



import random
import sys
from collections import  deque


def memory(x):
    #print(f'{type(x)=} {sys.getsizeof(x)=} {x=}')

    size_x = sys.getsizeof(x)
    # print(f'1 {size_x= }')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                # print(f'2 {size_x= }')
                # print(f'{sys.getsizeof(key)= }')
                size_x = size_x + sys.getsizeof(key)
                # print(f'3 {size_x= }')
                # print(f'{sys.getsizeof(value)= }')
                size_x = size_x + sys.getsizeof(value)
                # print(f'4 {size_x= }')

                # memory(key)
                # memory(value)
        elif not isinstance(x, str):
            for item in x:
                size_x = size_x + sys.getsizeof(item)
                # memory(item)
    # print(f'{size_x= }')
    return size_x

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = deque(random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE))
print(f'Исходный массив: {array}')

count = 0
even_arr = set()
for i in array:
    if i % 2 == 0:
        even_arr.add(count)
    count += 1
print(f'Индексы положительных чисел: {even_arr}')


variable_dict = {'SIZE':SIZE , 'MIN_ITEM': MIN_ITEM, 'MAX_ITEM': MAX_ITEM,
                 'array': array, 'print': print, 'count': count, 'even_arr': even_arr, }

size_sum = 0
for key, value in variable_dict.items():
    size_sum += memory(value)
    print(f' {memory(value)} байт, в-> {key} --> {value}')

print(f'\nДля работы программы требуется {size_sum} байт ОП')


"""
Выводы:
2-й вариант решения.
система 64 бита.

Исходный массив: deque([100, 39, 0, 82, 35, 59, 93, 100, 80, 61])
Индексы положительных чисел: {0, 2, 3, 7, 8}
 28 байт, в-> SIZE --> 10
 24 байт, в-> MIN_ITEM --> 0
 28 байт, в-> MAX_ITEM --> 100
 900 байт, в-> array --> deque([100, 39, 0, 82, 35, 59, 93, 100, 80, 61])
 72 байт, в-> print --> <built-in function print>
 28 байт, в-> count --> 10
 864 байт, в-> even_arr --> {0, 2, 3, 7, 8}

Для работы программы требуется 1944 байт ОП

Использование множества и очереди дало отрицательный результат, затраты памяти увеличились в 2,16 раза.
Думаю список even_arr заменить на строку. А array оставить списком.


"""