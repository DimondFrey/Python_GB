"""
Задание 1

Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
"""
#
string = input("Enter your name: ")
print(f'Hello {string}, good news everyone')

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
height_in_meters = height / 100

print(f'{string} you index is {weight / height_in_meters ** 2 :.2f}')
