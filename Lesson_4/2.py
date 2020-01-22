"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit


def simp_numb():
    # Q = int(input('Введите номер простого числа\n'))
    Q = 10
    simple_numbers = 0
    number = 0
    while simple_numbers != Q:
        number_is_simple = True
        if number < 2:
            number_is_simple = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    number_is_simple = False
        if number_is_simple:
            simple_numbers += 1
            last_number = number
        number += 1

    # print(f'Под номером {Q} находится простое число: {last_number}')
    return


def simp_numb_er():
    # Q = int(input('Введите номер простого числа\n'))
    Q = 10
    list_numbers = [i for i in range(2, Q*20)]
    simple_numbers = 0

    for i in list_numbers:
        number_is_simple = True
        for j in list_numbers:
            if i % j == 0 and i != j:
                number_is_simple = False
                list_numbers.remove(i)
            elif j % i == 0 and i != j:
                list_numbers.remove(j)
        if number_is_simple:
            simple_numbers += 1
            last_number = i
        if simple_numbers == Q:
            # print(f'Под номером {Q} находится простое число: {last_number}')
            break


print(timeit.timeit("simp_numb()", setup="from __main__ import simp_numb", number=10000))
print(timeit.timeit("simp_numb_er()", setup="from __main__ import simp_numb_er", number=10000))


"""
Использование алгоритма Эратосфена эффективно при больших i(номер простого числа).

Номер простого числа = 1000 при number = 10:
    Время выполнения алгоритма Эратосфена 17.614306725
    Время выполнения алгоритма НЕЭратосфена 35.686493573
    
Номер простого числа = 10 при number = 10000:
    Время выполнения алгоритма Эратосфена 2.753383359
    Время выполнения алгоритма НЕЭратосфена 0.491893977
    
"""