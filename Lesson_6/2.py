"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


class Class_without_slots:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Class_with_slots:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


alice = Class_without_slots('Alice', 'Black', 22)
print(alice.__dict__)
harry = Class_with_slots('Harry', 'Key', 23)
print(harry.__slots__)

print(asizeof.asizeof(alice))
print(asizeof.asizeof(harry))

'''
На хранение атрибутов класса Class_without_slots выделяется памяти 296, а на хранение атрибутов класса Class_with_slots 
выделяется памяти 120. В случае, если  явно указать значение __slots__, словарь __dict__ создаваться не будет, что существенно уменьшает
выделяемую память. Использование __slots__ возможно в случае, если нет необходимости в добавлении новых атрибутов класса динамически.

'''
