"""

1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Начальное задание:
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""


import random
import timeit
import cProfile

print('Первый вариант кода')

def time_research(size, min_itm, max_itm):
    SIZE = size
    MIN_ITEM = min_itm
    MAX_ITEM = max_itm
    array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
    #print(f'Исходный массив:\n{array}')

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
    return array

resault = time_research(10, -1000, 1000) # проверка что функция работает

print(f'Изменный массив:\n{resault}')

N = 10 # кол-во элементов в массиве
M = -1000
K = 1000

#print(timeit.timeit('time_research(N, M, K)', number=1000, globals=globals()))



meas_n = 5 # колличество измерений
step_N = 10 # шаг изменения кол-ва N
step_M_K = 1
#step_K = 1

for n in range(1, meas_n + 1):
    t = timeit.timeit('time_research(N, M, K)', number=1000, globals=globals())
    print(f'{n} при N = {N:6.0f} время выполнения {t} ')
    N = N * step_N
    M = M * step_M_K
    K = K * step_M_K

cProfile.run('time_research(100000000, M, K)')    



"""
1-й вариант выводы:

время выполнения:

1 при N =     10 время выполнения 0.018700836999999998 
2 при N =    100 время выполнения 0.142595376 
3 при N =   1000 время выполнения 1.376764643 
4 при N =  10000 время выполнения 13.561802947 
5 при N = 100000 время выполнения 141.726193017 

Для данного вариант время выполнения программы при изменении колличества элементов массива с 10 до 100000 
изменяется линейно кратно 10.

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.154    0.154   29.995   29.995 <string>:1(<module>)
        1    1.149    1.149   29.841   29.841 P A PW 04_01.py:24(time_research)
        1    4.964    4.964   28.652   28.652 P A PW 04_01.py:28(<listcomp>)
 10000000    8.826    0.000   18.379    0.000 random.py:200(randrange)
 10000000    5.309    0.000   23.688    0.000 random.py:244(randint)
 10000000    6.694    0.000    9.553    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000   29.995   29.995 {built-in method builtins.exec}
 10000000    1.366    0.000    1.366    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10235584    1.494    0.000    1.494    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.020    0.010    0.020    0.010 {method 'insert' of 'list' objects}
        2    0.020    0.010    0.020    0.010 {method 'pop' of 'list' objects}

Подавляющие затраты времени идут на генерацию случайных чисел для создания массива. Следующие, по величине, 
затраты затраты на генерацию самого массива (видимо так работает генератор)

"""

