"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран
"""


with open("number_list.txt", "w+", encoding="utf-8") as nf:
    str_list = input("Enter a number list: ").split()
    numbers_list = list(map(int, str_list))
    print(f"Before Sum: {sum(numbers_list)}")
    nf.write(' '.join(str_list))

with open("number_list.txt", 'r', encoding="utf-8") as lf:
    num = lf.read()
    print(f"After SUM : {sum(map(int, num.split()))}")