"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

with open("exercise_2.txt", 'r', encoding='utf-8') as f:
    total_words = 0
    for counter, line in enumerate(f.readlines()):
        words = line.split()
        for word in words:
            total_words += 1
    print(f"Total Amount of lines: {counter + 1}")
    print(f"Total Number of Words: {total_words}")