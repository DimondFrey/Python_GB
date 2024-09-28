"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

answer = []
firm_dict = {}
average_list = []
average = 0
with open("text_7.txt", 'r', encoding="utf-8") as ff:
    for line in ff.readlines():
        split_line = line.split()
        title = split_line[0]
        rubbles = int(split_line[2]) - int(split_line[3])
        if rubbles > 0:
            average_list.append(rubbles)
        firm_dict[title] = rubbles

    average = sum(average_list) / len(average_list)

answer.append(firm_dict)
answer.append({"average" : average})


with open("exe_7.json", 'w', encoding="utf-8") as af:
    json.dump(answer, af, ensure_ascii=False)









