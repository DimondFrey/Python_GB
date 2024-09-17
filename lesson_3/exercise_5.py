"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def numbers_sum():

    full_result = 0

    while True:
        break_flag = False
        proxy = 0
        numbers = list(input('Enter numbers or "Q" to quit: ').split())
        for n in numbers:
            if n.isalpha() and n == 'Q':
                break_flag = True
                break
            elif n.isalpha() and not n == 'Q':
                print('For Exit Enter "Q"')
                print(f'proxy: {proxy} full result: {full_result}')
                continue
            else:
                proxy += int(n)
        full_result += proxy

        print(f'proxy: {proxy} full result: {full_result}')

        if break_flag:
            break

numbers_sum()