"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

number = int(input("Enter a number: "))
print(f'Your summ is {str(number + int(str(number) * 2 ) + int(str(number) * 3 ))}')