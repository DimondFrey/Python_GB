"""
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл
"""
import json


new_text = []

with open("exe_4.json", "r", encoding="utf-8") as js:
    translate = dict(json.load(js)['translator'])

    with open("text_4.txt", "r+", encoding="utf-8") as fp:
        for line in fp:
            word = line.split()[0]
            number = line.split()[2]
            new_word = translate[word]
            new_text.append(' '.join([new_word, "-", number]))

with open("answer_4.txt", "w", encoding="utf-8") as af:
    af.write('\n'.join(new_text))




