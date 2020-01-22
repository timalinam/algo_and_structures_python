"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""
import timeit
import cProfile


def print_max_negative1():
    num = [-1, 0, 5, 6, 7, 8, -2, 12, 13, -14, -5, 6, 87, -3, 7, 9, 12, 19, 99, 100, -100, 3, 4]
    max_negative = 0
    max_negative_index = 0
    for i in num:
        if i < 0 and max_negative == 0:
            max_negative = i
            max_negative_index = num.index(i)
        elif i < 0 and abs(i) < abs(max_negative):
            max_negative = i
            max_negative_index = num.index(i)

    if max_negative < 0:
        print(f'Максимальное отрицательное число = {max_negative}')
        print(f'Его индекс = {max_negative_index}')
    else:
        print('В массиве нет отрицательных элементов')


def print_max_negative2():
    num = [-1, 0, 5, 6, 7, 8, -2, 12, 13, -14, -5, 6, 87, -3, 7, 9, 12, 19, 99, 100, -100, 3, 4]
    max_negative = 0
    max_negative_index = 0
    max_negative_l = False

    for i in num:
        if i < 0:
            max_negative_l = True
            for j in num:
                if 0 > j > i:
                    max_negative_l = False
            if max_negative_l:
                max_negative = i
                max_negative_index = num.index(max_negative)

    if max_negative == 0:
        print('В массиве нет отрицательных элементов')
    else:
        print(f'Максимальное отрицательное число = {max_negative}')
        print(f'Его индекс = {max_negative_index}')


if __name__ == '__main__':
    print(timeit.timeit("print_max_negative1()", setup="from __main__ import print_max_negative1", number=100000))
    print(timeit.timeit("print_max_negative2()", setup="from __main__ import print_max_negative2", number=100000))
    cProfile.run(f"print_max_negative1()")
    cProfile.run(f"print_max_negative2()")


"""
Алгоритм print_max_negative1 имеет один цикл, значит его сложность O(n)
Время выполнения алгоритма при number=100000 равна 0.337306736

В алгоритме print_max_negative2 есть два цикла, при этом один находится внтури другого, значит его сложность O(n2).
Время выполнения алгоритма при number=10000 равна 0.818162424

Изначально данные алгоримы предназначены для печати максимального отрицательного элемента в заданном массиве.
Для упрощения тестирования, числа вводятся не с клавиатуры, а уже заданы в коде.
При увеличении числа элементов в массиве в алгоритме print_max_negative1 время будет расти линейно, 
а в алгоритме print_max_negative2 - квадратично. Из чего можно сделать вывод, что первый 
алгоритм эффективнее и быстрее второго. 
"""