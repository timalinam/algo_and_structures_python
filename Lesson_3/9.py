# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
n = 5
m = 4
numbers = [[int(random() * 10) for i in range(m)] for j in range(n)]

min_in_column = []

for j in range(m):
    min_element = 10
    for i in range(n):
        element = numbers[i][j]
        if min_element > element:
            min_element = element
    min_in_column.append(min_element)

max_element = 0

for i in min_in_column:
    if i > max_element:
        max_element = i

print(numbers)
print(min_in_column)
print(max_element)
