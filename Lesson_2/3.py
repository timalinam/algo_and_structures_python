"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
number = int(input('Введите число\n'))
r_number = 0
while number > 0:
    r_number = r_number * 10 + number % 10
    number = number//10
print(r_number)

print('Решение с помощью рекурсии')

number = int(input('Введите число\n'))


def reverse_number(number):
    if number < 10:
        return number
    temp = number
    digits = 0
    while temp > 9:
        temp = temp // 10
        digits += 1
    return (number % 10) * (10 ** digits) + reverse_number(number // 10)


print(reverse_number(number))
