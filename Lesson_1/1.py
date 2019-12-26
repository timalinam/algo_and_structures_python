# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = int(input('Введите трехзначное число\n'))
sum_numbers = (number % 10) + ((number // 10) % 10) + (number // 100)
pr_numbers = (number % 10) * ((number // 10) % 10) * (number // 100)
print(f'сумма цифр числа {number} равна {sum_numbers}')
print(f'произведение цифр числа {number} равно {pr_numbers}')

