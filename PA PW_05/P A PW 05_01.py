"""

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.

"""
from collections import  deque

interpr_s = {}
positive_intrp = deque()
negative_interp = deque()
qarters = 4
count = 1
tot_sum = 0

while True:

    print('\nДалее по просьбе программы введите название организации \nи её доходы за каждый квартл года \n')

    inter_name = input('Введите название фирмы: ')
    profit_sum = 0

    for i in range(1, qarters + 1):
        profit_sum = profit_sum + int(input(f'Введите доход компании {inter_name} \nза {i}-й квартал: '))
    print(f'Прибыль компании {inter_name} за год составила {profit_sum} рублей \n')

    interpr_s[inter_name] = profit_sum
    count += 1
    tot_sum = tot_sum + profit_sum

    if int(input('Для ввода следующего предприятия введите любое число \nДля завершения ввода введите 0: ')) == 0:
        break



avr_profit = tot_sum / count
print(f'{tot_sum= } {count= } {avr_profit= }')
print(f'\n{interpr_s}')

for i in interpr_s:
    if interpr_s[i] >= avr_profit:
        positive_intrp.appendleft(i)
    else:
        negative_interp.appendleft(i)

print(f'Предприятия с доходом выше среднего: \n{positive_intrp} \nПредприятия с доходом ниже среднего\n{negative_interp}')
