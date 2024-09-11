"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""

seasons = sum([['зима'] * 2, ['весна'] * 3, ['лето'] * 3, ["осень"] * 3, ['зима']], [])

while True:
    n = input("Enter a month number 'Done' for finish: ")
    if n != 'Done' and int(n) <= 12:
        print(seasons[int(n) - 1])
    else:
        print("End of the program")
        break