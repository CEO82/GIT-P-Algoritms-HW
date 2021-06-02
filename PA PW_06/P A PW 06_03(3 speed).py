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
import timeit


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
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(f'Исходный массив: {array}')

def str_time(array):
    count = 0
    even_arr = ''
    for i in array:
        if i % 2 == 0:
            even_arr = even_arr + str(count) + ','
        count += 1
    # print(f'Индексы положительных чисел: {even_arr}')

def lst_time(array):
    count = 0
    even_arr = []
    for i in array:
        if i % 2 == 0:
            even_arr.append(count)
        count += 1


t_str = timeit.timeit('str_time(array)', number=1000000, globals=globals())
t_list = timeit.timeit('lst_time(array)', number=1000000, globals=globals())
print(f'{t_str= } {t_list= }')

# variable_dict = {'SIZE':SIZE , 'MIN_ITEM': MIN_ITEM, 'MAX_ITEM': MAX_ITEM,
#                  'array': array, 'print': print, 'count': count, 'even_arr': even_arr, }
#
# size_sum = 0
# for key, value in variable_dict.items():
#     size_sum += memory(value)
#     print(f' {memory(value)} байт, в-> {key} --> {value}')
#
# print(f'\nДля работы программы требуется {size_sum} байт ОП')


"""
Выводы:
3-й вариант решения.
система 64 бита.

Исходный массив: [51, 65, 43, 48, 30, 56, 66, 19, 61, 78]
Индексы положительных чисел: 3,4,5,6,9,
 28 байт, в-> SIZE --> 10
 24 байт, в-> MIN_ITEM --> 0
 28 байт, в-> MAX_ITEM --> 100
 464 байт, в-> array --> [51, 65, 43, 48, 30, 56, 66, 19, 61, 78]
 72 байт, в-> print --> <built-in function print>
 28 байт, в-> count --> 10
 59 байт, в-> even_arr --> 3,4,5,6,9,

Для работы программы требуется 703 байт ОП

использование строки дало снижение расхода памяти на 21,8% в сравнении с 1-м вариантом и на 276% быстрее чем 2-й вариант
думаю это хороший показатель. При этом нужно учитывать что временные затраты на конкатинацию чисел в строку будут 
значительно выше чем при добавлении в список с права (временные затраты на добавление в список происходят от 1,5 до 2,3
раз быстрее чем конкатинация в строке). По этому нужно понимать что в приоритете. Память или скорость.
Предполагаю что скорость.


t_str= 3.9796505079999998 t_list= 1.7280180429999996

"""