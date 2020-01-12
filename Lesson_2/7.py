"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
from sys import setrecursionlimit

setrecursionlimit(100000)

print('Вычисление суммы с помощью цикла')

n = int(input('Введите число\n'))
sum1 = 0
sum2 = 0

for i in range(1, n + 1):
    sum1 += i

sum2 = n * (n + 1) / 2

if sum1 == sum2:
    print('Выражение 1+2+...+n = n(n+1)/2 верно')
else:
    print('Выражение 1+2+...+n = n(n+1)/2 неверно')

print('Вычисление суммы с помощью рекурсии')

n = int(input('Введите число\n'))



def sum_n(n):
    if n == 1:
        return n
    else:
        return n + sum_n(n - 1)


sum3 = sum_n(n)
sum4 = n * (n + 1) / 2

if sum3 == sum4:
    print('Выражение 1+2+...+n = n(n+1)/2 верно')
else:
    print('Выражение 1+2+...+n = n(n+1)/2 неверно')
