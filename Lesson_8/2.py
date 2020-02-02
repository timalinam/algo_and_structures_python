"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


user_str = input('Введите строку состоящую из маленьких букв\n')
lists = []
for i in range(0, len(user_str) + 1):
    for j in range(i + 1, len(user_str) + 1):
        lists.append(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())

lists.remove(hashlib.sha1(user_str.encode('utf-8')).hexdigest())


print(f'Колличество различных подстрок в строке {user_str} равно {len(set(lists))}')
