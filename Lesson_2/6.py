"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import random

print('Решение с помощью цикла')

RANDOM_NUMBER = int(random() * 100 + 1)
NUM = 0

while NUM != 10:
    print('Угадайте число от 1 до 100\n')
    number = int(input())
    if number > RANDOM_NUMBER:
        print('Ваше число больше загаданного')
    elif number < RANDOM_NUMBER:
        print('Ваше число меньше загаданного')
    elif number == RANDOM_NUMBER:
        print('Вы угадали!!!')
        break
    NUM += 1

print('Решение с помощью рекурсии')

RANDOM_NUMBER = int(random() * 100 + 1)
NUM = 0


def guess():
    global NUM
    if NUM == 10:
        print('Вы проиграли, загаданное число', RANDOM_NUMBER)
        return
    print('Угадайте число от 1 до 100\n')
    number = int(input())
    if number > RANDOM_NUMBER:
        print('Ваше число больше загаданного')
    elif number < RANDOM_NUMBER:
        print('Ваше число меньше загаданного')
    elif number == RANDOM_NUMBER:
        print('Вы угадали!!!')
        return
    NUM += 1
    guess()


guess()
