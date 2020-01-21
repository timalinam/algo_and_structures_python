"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import random
n = 5
m = 4
numbers = [[int(random() * 10) for i in range(m)] for j in range(n)]

for j in range(n):
    sum_num = 0
    for i in range(m):
        sum_num += numbers[j][i]
        print(numbers[j][i], end=' ')
    print(sum_num)
