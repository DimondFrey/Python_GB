"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль
"""

def division():
    x = float(input("Введите первое значение: "))
    y = float(input("Введите второе значение: "))
    return x / y

try:
    print(f'{division():.05f}')
except ZeroDivisionError:
    print("Ошибка деления на ноль")