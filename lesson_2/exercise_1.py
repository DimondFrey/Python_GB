"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе
"""

my_list = [1, 2.3, 3 + 4j, None, True, 0b1010, ord("c"), [1, 2], (3.4, 53.3), {1, 2, 3}, \
           {None:False, 'c':None}, frozenset([1, 2, 3])]

for el in my_list:
    print(type(el))