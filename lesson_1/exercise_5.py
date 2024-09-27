"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчёте на одного сотрудника
"""

revenue = int(input('Enter a revenue: '))
costs = int(input("Enter a costs: "))

if revenue > costs:
    print('Congrats! You`re doing great ')
    profit = revenue - costs
    print(f'Income equals {(profit/ revenue) * 100:.2f}%')

    employers = int(input("Enter a number of employers: "))

    print(f'Profit by employers equal {profit / employers}')

elif revenue < costs:
    print('Let`s do better next time!')
else:
    print('Good job! That`s the break-even')