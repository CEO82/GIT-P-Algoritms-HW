"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.

"""

print('Угадайте число от 0 до 100')

import random
number = random.randint(0, 100)
#print(number)

usrNumb = None
count = 1

maxCount = 10
print(f'У вас есть {maxCount} попыток')

while usrNumb != number:

    print(f'Пыпытка № {count:02} из {maxCount:02}')
    usrNumb = int(input('Введите число от 1 до 100: '))
    if count > maxCount - 1:
        print(f'У вас закончились попытки, вы проиграли.\nЗагаданное число было: {number}')
        break
    if usrNumb == number:
        print('Вы угадали!!! Поздравляем')
        break
    elif usrNumb > number:
        print('Вы ввели слишком большое число попробуйте еще раз!')
    else:
        print('Вы ввели слишком маленькое число, попробуйте еще раз!')
    count += 1

print('Конец игры')