"""

Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

"""
print(f'\n\t\tТаблица символов в кодировке ASCII\n')
count = 1
for char in range(32, 128):
    if count % 10 != 0:
        print(f' {char:3}: {chr(char)}', end=' |')
    else:
        print(f' {char:3}: {chr(char)}')
    count += 1