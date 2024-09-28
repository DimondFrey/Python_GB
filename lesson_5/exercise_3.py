"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
"""

with open("salary.txt", "r", encoding="utf-8") as fp:
    sum_salary = 0
    for counter, line in enumerate(fp.readlines()):
        salary = float(line.split()[1])
        if salary < 20000:
            print(line, end='')
        sum_salary += salary
    print(f"Average Salary {sum_salary / (counter + 1) }")
