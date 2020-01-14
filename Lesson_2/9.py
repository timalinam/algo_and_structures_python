"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

max_sum = 0
sum_num = 0

L = [int(i) for i in input('Введите последовательность чисел через пробел\n').split(' ')]

for num in L:
    i = 0
    sum_num = 0
    while num % 10 ** i != num:
        unit = ((num % 10 ** (i + 1) - num % 10 ** i) / 10 ** i)
        sum_num += unit
        i += 1
    if sum_num > max_sum:
        max_sum = sum_num
        max_num = num

print('Число с максимальной суммой цифр: ', max_num)
print('Сумма цифр данного числа: ', max_sum)


