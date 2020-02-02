"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def merge_sort(random_list):
    if len(random_list) > 1:
        mid = len(random_list) // 2

        left_half = random_list[:mid]
        right_half = random_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                random_list[k] = left_half[i]
                i = i + 1
            else:
                random_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            random_list[k] = left_half[i]
            i = i+1
            k = k+1

        while j < len(right_half):
            random_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    return random_list


r_list = [random.uniform(0, 50) for _ in range(10)]
print(r_list)
print(merge_sort(r_list))
