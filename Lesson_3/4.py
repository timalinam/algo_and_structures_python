# 4.	Определить, какое число в массиве встречается чаще всего.


numbers = [int(i)
           for i in input('Введите список чисел через пробел\n').split(' ')]

max_number = numbers[0]
max_times = 1

for i in range(len(numbers)):
    times = 1
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            times += 1
    if times > max_times:
        max_times = times
        max_number = numbers[i]

if max_times > 1:
    print(
        f'Чаще всего встречается число {max_number}, оно встретилось {max_times} раз')
else:
    print('Нет повторяющихся чисел')
