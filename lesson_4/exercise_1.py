"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def salary(sal, hours, bonus):
    return f'Заработная плата сотрудника: {(float(sal) * float(hours)) + float(bonus)}'

print(salary(argv[1], argv[2], argv[3]))