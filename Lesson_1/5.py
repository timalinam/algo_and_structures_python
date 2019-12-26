#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

letter1, letter2 = [ord(i) for i in input('Введите две буквы от a до z через пробел\n').split(' ')]
place_letter1 = letter1 - 96
place_letter2 = letter2 - 96
if place_letter2 - place_letter1 >= 0:
    number_of_letters = place_letter2 - place_letter1 - 1
else:
    number_of_letters = place_letter1 - place_letter2 - 1

print(f'Первая буква стоит на {place_letter1} месте')
print(f'Вторая буква стоит на {place_letter2} месте')
print(f'Колличество букв между ними: {number_of_letters}')