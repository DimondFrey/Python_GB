"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
километров. Каждый день спортсмен увеличивал результат на 10% относительно
предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
менее b километров. Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.
"""

first_day_km = int(input("Enter how many kilometers you run the first day: "))
goal_day_km = int(input("Enter how many kilometers you run the goal day: "))


while first_day_km < goal_day_km:
    first_day_km = first_day_km + first_day_km * 0.1

print(f'{first_day_km:.02f} km')