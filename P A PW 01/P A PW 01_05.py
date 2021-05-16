"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

"""

a = input('Введите 1-й латинский символ: ')
b = input('Введите 2-й латинский символ: ')

position_a = ord(a) - 96
position_b = ord(b) - 96

print(f'положение символа {a} в латинском алфавите равно: {position_a}')
print(f'положение символа {b} в латинском алфавите равно: {position_b}')

if position_a > position_b:
    count = position_a - position_b - 1
else:
    count = position_b - position_a - 1

print(f'Колличество символов в алфавите между символами {a} и {b} равно {count}')



