"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict

hex_to_dec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def sum_hex_numbers(a, b):
    c = a + b
    if c >= 16:
        whole = c - 16
        balance = 1
    else:
        whole = c
        balance = 0
    return whole, balance


def mult_hex_numbers(a, b, balance_now):
    c = a * b + balance_now
    if c >= 16:
        balance = c//16
        whole = c % 16
    else:
        whole = c
        balance = 0
    return whole, balance


def mult_hex_numbers_all(a, b):
    a = list(reversed(a))
    b = list(reversed(b))
    n = 0
    result = 0

    mult_numbers = []

    if len(a) < len(b):
        a, b = b, a

    for letter in b:
        balance = 0
        c = []
        for letter_2 in a:
            balance_now = balance
            whole, balance = mult_hex_numbers(hex_to_dec.index(letter_2), hex_to_dec.index(letter), balance_now)
            c.append(hex_to_dec[whole])
        if balance != 0:
            c.append(hex_to_dec[balance])
        for i in range(n):
            c.insert(0, '0')
        mult_numbers.append(list(reversed(c)))
        n += 1
    result = mult_numbers[0]
    for i in range(len(mult_numbers) - 1):
        result = sum_hex_numbers_all(result, mult_numbers[i + 1])
    return result


def sum_hex_numbers_all(a, b):
    a = list(reversed(a))
    b = list(reversed(b))
    n = 0
    balance = 0

    c = []
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(a) - len(b)):
        b.append('0')
    for letter in a:
        i = hex_to_dec.index(letter)
        balance_now = balance
        whole, balance = sum_hex_numbers(i + balance_now, hex_to_dec.index(b[n]))
        c.append(hex_to_dec[whole])
        n += 1
    if balance != 0:
        c.append(hex_to_dec[balance])

    return list(reversed(c))


def number_right(str_number):
    number_is_right = True
    for i in str_number:
        if i not in hex_to_dec:
            number_is_right = False
    return number_is_right


def do_default_dict(str_number):
    def_dict = defaultdict(list)
    def_dict[str_number] = list(str_number)
    return def_dict


m = (input('Введите первое число в шестнадцатиричной системе исчесления\n')).lower()
k = (input('Введите второе число в шестнадцатиричной системе исчесления\n')).lower()

if number_right(m) and number_right(k):
    sum_user_numbers = sum_hex_numbers_all(do_default_dict(m).get(m), do_default_dict(k).get(k))
    mult_user_numbers = mult_hex_numbers_all(do_default_dict(m).get(m), do_default_dict(k).get(k))
    print(f"Сумма чисел = {(''.join(sum_user_numbers)).upper()}")
    print(f"Произведение чисел = {(''.join(mult_user_numbers)).upper()}")
else:
    print('Проверьте правильность ввода')
