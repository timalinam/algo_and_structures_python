"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input('Введите число\n'))

print('Решение с помощью цикла: ')

f = 10
i = 0
unit = ''
EVEN = 0
ODD = 0

while number % 10**i != number:
    unit = ((number % 10**(i+1) - number % 10**i) / 10**i)
    if unit % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    i += 1
print(f'Четных цифр {EVEN}, нечетных цифр {ODD}')

EVEN = 0
ODD = 0

print('Решение с помощью рекурсии: ')


def odd_even(number):
    global EVEN
    global ODD
    dig = number % 10
    if dig % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    if number // 10 == 0:
        print(f'Четных цифр {EVEN}, нечетных цифр {ODD}')
        return
    number = number // 10
    odd_even(number)


odd_even(number)

