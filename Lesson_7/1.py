"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def bubble(random_list):
    n = 1
    list_is_sorted = True
    while n < len(random_list):
        for i in range(len(random_list) - n):
            if random_list[i] < random_list[i + 1]:
                random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
                list_is_sorted = False
        if list_is_sorted:
            break
        n += 1
    return random_list


r_list = [random.randint(-100, 100) for _ in range(10)]
print(r_list)
print(bubble(r_list))
