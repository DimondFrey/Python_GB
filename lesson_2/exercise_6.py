"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.
Пример готовой структуры:
[
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например, название. Тогда значение — список
значений-характеристик, например, список названий товаров.
Пример:
{
'название': ['компьютер', 'принтер', 'сканер'],
'цена': [20000, 6000, 2000],
'количество': [5, 2, 7],
'ед': ['шт.']
}
"""

delivers  = list()

while True:
    print('Add | Print | Remove | Stats | Done')
    option = input("Enter one of options: ")

    if option == 'Add':
        while True:
            dict_delivers = {}
            print(dict_delivers)
            title = input('Enter name of the delivery: ')
            cost = input("Enter a cost of the delivery: ")
            value = input("Enter value of the delivery: ")
            units = input("Enter units of the delivery: ")

            print("error | done | exit")
            next_move = input("Enter Add or Error")
            if next_move == 'error':
                continue
            elif next_move == "done":
                dict_delivers.update({'title': title, 'cost': float(cost), 'value': int(value), 'units': units})
                delivers.append((len(delivers) + 1, dict_delivers))
                print(delivers)
                continue
            elif next_move == "exit":
                dict_delivers.update({'title': title, 'cost': float(cost), 'value': int(value), 'units': units})
                delivers.append((len(delivers) + 1, dict_delivers))
                print(delivers)
                break


    elif option == 'Print':
        for delivery in delivers:
            print(delivery)
            continue

    elif option == 'Remove':
        pass

    elif option == 'Stats':
        stats_dict = {}
        for delivery in delivers:
            for k,v in delivery[1].items():
                stats_dict.setdefault(k, []).append(v)
        print("[")
        for k, v in stats_dict.items():
            print(f"{k} : {v}")
        print("]")


    elif option == 'Done':
        print("End of the program. Bye!")
        break

    else:
        print('Enter a correct option')