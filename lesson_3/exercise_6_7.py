"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text

7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию i
"""

def int_func():

    text = input("Enter text: ").split()
    cap_text = []

    def check_word(ch_word):
        checked_word = ''
        for w in ch_word:
            if 97 < ord(w) < 122:
                checked_word += w
                return checked_word
            else:
                break

    for word in text:
        if check_word(word):
            word = word.capitalize()
            cap_text.append(word)
        else:
            cap_text.append(word)

    return ' '.join(cap_text)

print(int_func())