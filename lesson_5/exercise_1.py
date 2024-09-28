"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""

with open('1_exercise.txt', "w+", encoding="utf-8") as file:
    while True:
        x = input("Enter a line: ")
        if len(x) == 0:
            break
        file.write(f'{x}\n')
