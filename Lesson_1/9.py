# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

number1, number2, number3 = [int(i) for i in input('Введите три разных числа через пробел\n').split(' ')]
middle = 0
if (number1 > number2 and number1 < number3) or (number1 > number3 and number1 < number2):
    print(f'Среднее число {number1}')
elif (number2 > number1 and number2 < number3) or (number2 > number3 and number2 < number1):
    print(f'Среднее число {number2}')
elif (number3 > number1 and number3 < number2) or (number3 > number3 and number3 < number2):
    print(f'Среднее число {number3}')
else:
    print('Вы ввели одинаковые числа')