"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input("enter a number as big as your want: "))

biggest = number % 10

while number // 10 > 0:

    last = number % 10
    number = number // 10

    if last > biggest:
        biggest = last

print(biggest)

