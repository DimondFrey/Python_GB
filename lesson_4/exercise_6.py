"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

var_count = (x for x in count(int(input("Enter a number: "))))

print(next(var_count))
print(next(var_count))

def count_f(x):
    for el in count(x):
        if el > 40:
            break
        print(el)



count_f(20)

var_cycle = ( x for x in cycle(list(input("Enter letters: ").split())))

print(next(var_cycle))
print(next(var_cycle))
print(next(var_cycle))

def cycle_f(l):
    c = 0
    for el in cycle(l):
        if c > 10:
            break
        print(el)
        c += 1


cycle_f(["A", "B", "C"])

