"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
print('Решение через цикл')
sign = ''
while sign != '0':
    a = int(input('A = \n'))
    b = int(input('B = \n'))
    sign = input('Введите знак операции (*,/,+,-), или введите 0, чтобы выйти\n')
    if sign == '/':
        if b == 0:
            print('На ноль делить нельзя')
            continue
        print(a / b)
    elif sign == '*':
        print(a * b)
    elif sign == '-':
        print(a - b)
    elif sign == '+':
        print(a + b)
    elif sign != '0':
        print('Вы ввели неверный знак')


def calculator():
    a = int(input('A = \n'))
    b = int(input('B = \n'))
    sign = input('Введите знак операции (*,/,+,-), или введите 0, чтобы выйти\n')
    if sign == '/':
        if b == 0:
            print('На ноль делить нельзя')
        else:
            print(a / b)
    elif sign == '*':
        print(a * b)
    elif sign == '-':
        print(a - b)
    elif sign == '+':
        print(a + b)
    elif sign != '-' and sign != '+' and sign != '*' and sign != '/' and sign != '0':
        print('Вы ввели неверный знак')
    if sign != '0':
        calculator()
    return

print('Решение через рекурсию')

calculator()