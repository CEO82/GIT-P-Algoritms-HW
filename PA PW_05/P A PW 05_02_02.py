"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
from collections import  deque

u_n_1 = list(input('Введите 1-е 16-ти ричное число: '))
u_n_2 = list(input('Введите 2-е 16-ти ричное число: '))



hex_ten_num = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}

ten_hex_num = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',

}

n_in_mind = 0

# u_n_1 = list('ffff')
# u_n_2 = list('fff')

answ = deque()

if len(u_n_2) > len(u_n_1):
    u_n_1, u_n_2 = u_n_2, u_n_1

while True:
    neg_count = -1
    c_count = 0 #счетчик циклов

    for i in u_n_2[:: -1]:


        sum_char = (hex_ten_num[u_n_1[neg_count]] + hex_ten_num[i] + n_in_mind)
        #print(f'{c_count= } {sum_char= }')
        if sum_char < 16:
            answ.appendleft(ten_hex_num[str(sum_char)])
            n_in_mind = 0

        else:
            n_in_mind = 1
            answ.appendleft(ten_hex_num[str(sum_char - 16)])


        c_count += 1

        neg_count -= 1

    if len(u_n_2) == len(u_n_1) and n_in_mind == 1:
        answ.appendleft('1')

    if len(u_n_2) == len(u_n_1):
        pass
    else:

        if n_in_mind == 0:
            #print(f'{n_in_mind= }')
            for i in u_n_1[:: len(u_n_2) * -1]:
                answ.appendleft(i)
        else:
            for i in range(len(u_n_1) - len(u_n_2) - 1, -1, -1):
                sum_char = hex_ten_num[u_n_1[i]] + n_in_mind
                if sum_char < 16:
                    answ.appendleft(ten_hex_num[str(sum_char)])
                    n_in_mind = 0

                else:
                    n_in_mind = 1
                    answ.appendleft(ten_hex_num[str(sum_char - 16)])
        #print(f'{n_in_mind= }')
        if n_in_mind == 1:
            answ.appendleft('1')


                #answ.appendleft(ten_hex_num[str(sum_char - 16)])
                #print(f'{c_count= } {sum_char= }')



    print(answ)
    break









