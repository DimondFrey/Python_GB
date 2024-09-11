"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
from operator import index

rating = [4, 4, 4 , 3, 3, 2, 2, 2]

el = int(input("Enter a number: "))

for rat in rating:
    if rat > el:
        if rating.index(rat) != len(rating) - rating.count(rat):
            print(f'rat > el {rat} {el}')
        else:
            rating.append(el)
            print(rating)
            break
    elif rat == el:
        count_el = rating.count(el)
        index_el = rating.index(el)
        rating.insert(index_el + count_el, float(el))
        print(rating)
        break
    elif rat < el:
        index_el = rating.index(rat)
        rating.insert(index_el, el)
        print(rating)
        break
