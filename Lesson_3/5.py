#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

numbers = [int(i) for i in input('Введите список чисел через пробел\n').split(' ')]

max_negative = 0

for i in numbers:
    if i < 0 and max_negative == 0:
        max_negative = i
    elif i < 0 and abs(i) < abs(max_negative):
        max_negative = i

if max_negative < 0:
    print(f'Максимальное отрицательное число = {max_negative}')
else:
    print('В массиве нет отрицательных элементов')
