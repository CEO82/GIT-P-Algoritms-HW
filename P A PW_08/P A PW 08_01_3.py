"""

Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9

"""


usr_str = input('Введите ваш текст-> ')
# usr_str = 'ывывс'

hoarder = set()
diap = len(usr_str) - 1

for i in range(diap):
    first_i = 0
    last_i = 1 + i
    for n in range(len(usr_str)):
        # print(f'{first_i= } {last_i= }')
        # print(usr_str[first_i: last_i])
        if hash(usr_str) != hash(usr_str[first_i: last_i]) and usr_str[first_i: last_i] != 0:
            hoarder.add(usr_str[first_i: last_i])
        first_i += 1
        last_i += 1
    # print(f'{count= }')
    # last_i = 1 + count

print(f'Колличество уникальных подстрок в строке:\n>{usr_str}<\nРавно:\n{len(hoarder)} ед.')
