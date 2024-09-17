"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
"""

def info(name, surname, year, city, email, phone ) -> str:
    return f'Имя {name}, {surname}, Год {year}, Город {city}, Почта {email}, Телефон {phone}'

print(info(name="Ivan", surname="Ivanovich", year="1942", city="London", email="london@city", phone="+32 (535) 34-34" ))