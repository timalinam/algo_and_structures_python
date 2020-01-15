"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random

numbers = [int(random() * 10) for i in range(11)]

print(numbers)
max_number_index = 0
min_numbers_index = 0

for i in range(len(numbers)):
    if numbers[i] > numbers[max_number_index]:
        max_number_index = i
    if numbers[i] < numbers[min_numbers_index]:
        min_numbers_index = i

if max_number_index < min_numbers_index:
    a = max_number_index
    b = min_numbers_index
else:
    a = min_numbers_index
    b = max_number_index

sum_num = 0

for i in range(a + 1, b):
    sum_num += numbers[i]

print(sum_num)
