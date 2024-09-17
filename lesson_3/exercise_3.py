"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""

def my_func(x1, x2, x3) -> float:
    numbers = [x1, x2, x3]
    numbers.remove(min(numbers))
    return sum(numbers)

print(my_func(-1,-2,3))



