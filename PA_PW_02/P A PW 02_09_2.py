"""

Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

"""


def char_summ(usr_num):
    num_sum = 0
    usr_n_str = str(usr_num)
    for i in usr_n_str:
        num_sum += int(i)
    return num_sum

big_sum = 0
big_num = 0


while True:
    usr_num = int(input(f'\nВведите любое целое число больше 0\nДля выхода введите 0\nВаш ввод --> '))
    if usr_num == 0:
        break

    inp_sum = char_summ(usr_num)

    if big_sum > inp_sum:
        pass
    else:
        big_sum = inp_sum
        big_num = usr_num

print(f'\nЧисло с наибольшей суммой цифр это {big_num}\nСумма его цифр составляет {big_sum}')