"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile
from guppy import hpy


@profile
def denominator0():
    h = hpy()
    numbers = [i for i in range(2, 100000)]
    denominators = [i for i in range(2, 10)]
    info = {}

    for i in denominators:
        s = 0
        for j in numbers:
            if j % i == 0:
                s += 1
        info[i] = s

    for key, value in info.items():
        print(f'На {key} делится {value} элементов')

    print()
    print(h.heap())


@profile
def denominator1():
    h = hpy()
    numbers = [i for i in range(2, 100000)]
    denominators = [i for i in range(2, 10)]

    for i in denominators:
        s = 0
        for j in numbers:
            if j % i == 0:
                s += 1
        print(f'На {i} делится {s} элементов')

    print()
    print(h.heap())


@profile
def denominator2():
    h = hpy()
    for i in range(2, 10):
        s = 0
        for j in range(2, 100000):
            if j % i == 0:
                s += 1
        print(f'На {i} делится {s} элементов')

    print()
    print(h.heap())


if __name__ == "__main__":
    denominator0()
    denominator1()
    denominator2()

'''
Python 3.7
64-разрядная операционная система Windows 10.
 

Для тестирования выделения памяти напишем три реализации первой задачи третьего урока и изменим условие, 
чтобы более наглядно видеть разницу. 
"В диапазоне натуральных чисел от 2 до 99999 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."

В реализации denominator0() изначально создается два списка numbers и denominators, а так же данные о делителях хранятся
в словаре info и выводятся пользователю с помощью отдельного цикла. Данный подход съедает дополнительную память для хранения объектов.


В реализации denominator1() данные о делителях не хранятся в словаре, а выводятся сразу в момент вычисления. Это сокращает
выделяемую память.

В реализации denominator2() отсутствует словарь, а так же списки чисел numbers и denominators. Вместо них интерпритатор проходится
по генератору. Это так же сокращает выделяемую память

denominator0() Total size = 5956943 bytes
denominator1() Total size = 5955191 bytes
denominator2() Total size = 4010433 bytes

'''