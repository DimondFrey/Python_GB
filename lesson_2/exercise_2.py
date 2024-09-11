"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
"""
change_list = []

while True:
    number_to_append = input("Please text a number to append: ")
    if number_to_append == 'Done':
        for el in range(len(change_list) // 2):
            change_list[el << 1], change_list[(el << 1) + 1] = change_list[(el << 1) + 1], change_list[el << 1]

        print(change_list)
        break
    else:
        change_list.append(int(number_to_append))
