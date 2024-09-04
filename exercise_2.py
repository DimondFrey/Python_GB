"""
Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time_in_seconds = int(input("Enter time in seconds: "))

if time_in_seconds // 3600 >= 1 :
    hours = time_in_seconds // 3600
    time_in_seconds = time_in_seconds - hours * 3600
else:
    hours = 0

if time_in_seconds // 60 >= 1:
    minutes = time_in_seconds // 60
    time_in_seconds = time_in_seconds - minutes * 60
else:
    minutes = 0

seconds = time_in_seconds

print(f'Time is {hours:02}:{minutes:02}:{seconds:02}')