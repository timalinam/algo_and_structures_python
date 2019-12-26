# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
number_of_letter = int(input('Введите номер буквы в алфавите (от 1 до 26)\n'))
letter = chr(number_of_letter + 96)
print(f'Под номером {number_of_letter} находится буква {letter}')