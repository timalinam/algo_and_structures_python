"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random

numbers = [int(random() * 10) for i in range(11)]

print(numbers)

if numbers[0] > numbers[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, len(numbers)):
    if numbers[i] < numbers[min1]:
        temp = min1
        min1 = i
        if numbers[temp] < numbers[min2]:
            min2 = temp
    elif numbers[i] < numbers[min2]:
        min2 = i

print(numbers[min1], numbers[min2])
