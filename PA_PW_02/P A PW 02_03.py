"""

Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

"""


usr_num = str(input('Введите любое положительное целое число: '))

transf_num = usr_num[ : : -1]
count_0 =0

for i in transf_num:
    if i == '0':
        count_0 += 1
    else:
        break

transf_num = transf_num[count_0:]
print(f'Число задом на перед будет {transf_num}')
