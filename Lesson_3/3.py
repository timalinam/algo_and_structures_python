# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random

numbers = [int(random() * 100) for i in range(11)]

print(numbers)
max_number_index = 0
min_numbers_index = 0

for i in range(len(numbers)):
    if numbers[i] > numbers[max_number_index]:
        max_number_index = i
    if numbers[i] < numbers[min_numbers_index]:
        min_numbers_index = i

numbers[max_number_index], numbers[min_numbers_index] = numbers[min_numbers_index], numbers[max_number_index]
print(numbers)
