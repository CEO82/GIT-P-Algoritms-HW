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

print('Второй вариант кода')

def time_research_2(size, min_itm, max_itm):
    SIZE = size
    MIN_ITEM = min_itm
    MAX_ITEM = max_itm
    # array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
    array = []
    for n in range(size):
        array.append(random.randint(MIN_ITEM, MAX_ITEM))

    # print(f'Исходный массив:\n{array}')

    max_n = MIN_ITEM
    max_n_i = 0
    min_n = MAX_ITEM
    min_n_i = 0
    # count = 0

    for p, i in enumerate(array, 0):
        if max_n < i:
            max_n = i
            max_n_i = p
        if min_n > i:
            min_n = i
            min_n_i = p
        # count += 1

    # array.insert(min_n_i, max_n)
    # array.pop(min_n_i + 1)
    # array.insert(max_n_i, min_n)
    # array.pop(max_n_i + 1)

    array[max_n_i], array[min_n_i] = array[min_n_i], array[max_n_i]

    return array


resault = time_research_2(10, -1000, 1000)

print(f'Изменный массив:\n{resault}')

N = 10 # кол-во элементов в массиве
M = -1000
K = 1000

meas_n = 5  # колличество измерений
step_N = 10  # шаг изменения кол-ва N
step_M_K = 1
# step_K = 1

for n in range(1, meas_n + 1):
    t = timeit.timeit('time_research_2(N, M, K)', number=1000, globals=globals())
    print(f'{n} при N = {N:6.0f} время выполнения {t} ')
    N = N * step_N
    M = M * step_M_K
    K = K * step_M_K

cProfile.run('time_research(100000000, M, K)')

"""
2-й вариант выводы:

1 при N =     10 время выполнения 0.017908817 
2 при N =    100 время выполнения 0.152364572 
3 при N =   1000 время выполнения 1.4254703 
4 при N =  10000 время выполнения 14.607691739000002 
5 при N = 100000 время выполнения 164.40197318100002 

Для данного вариант время выполнения программы при изменении колличества элементов массива с 10 до 100000 
изменяется линейно кратно 10. При этотм время выполнения немного больше чем в варианте 1, хотя я предполагал 
что изменения ускорят работу программы.

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.566    3.566  315.364  315.364 <string>:1(<module>)
        1   30.560   30.560  311.798  311.798 P A PW 04_01.py:25(time_research)
        1   49.343   49.343  280.645  280.645 P A PW 04_01.py:29(<listcomp>)
100000000   86.633    0.000  180.372    0.000 random.py:200(randrange)
100000000   50.930    0.000  231.302    0.000 random.py:244(randint)
100000000   63.640    0.000   93.740    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.002    0.002  315.366  315.366 {built-in method builtins.exec}
100000000   13.723    0.000   13.723    0.000 {method 'bit_length' of 'int' objects}
        1    0.001    0.001    0.001    0.001 {method 'disable' of '_lsprof.Profiler' objects}
102349556   16.376    0.000   16.376    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.403    0.201    0.403    0.201 {method 'insert' of 'list' objects}
        2    0.189    0.095    0.189    0.095 {method 'pop' of 'list' objects}

При том-же числе N что и в первом варианте временные затраты по процессам значительно возрасли. Основные зартраты на:
Создание случайных чисел
создание массива

Как и в предыдущем варианте.



"""
