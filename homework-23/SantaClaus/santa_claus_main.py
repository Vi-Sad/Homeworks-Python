from santa_claus_functions import *

print('-' * 100)

print('Задача №2')
# Реализовать класс SantaClaus:
# - Атрибуты: имя, возраст, количество подарков
# - Методы: give_gifts(), update_age()
# - НЕОБЯЗАТЕЛЬНО: Интерфейс для отправки подарков и обновления возраста

user_name = input('Как тебя зовут? Введи свое имя --> ')
user_age = int(input('Сколько тебе лет? Введи число --> '))
user_gift = int(input('Сколько подарков хочешь получить в новом году? Введи число --> '))

user_santa_claus = SantaClaus(user_name, user_age, user_gift)

while True:
    user_change = int(input('* * *\nВыбери команду:\n1. Изменить возраст\n2. Получить подарки\n'
                            '3. Посмотреть информацию\n4. Выйти из программы\nВведи число --> '))
    if user_change == 1:
        user_age = int(input('* * *\nДавай обновим твой возраст! Введи число --> '))
        user_santa_claus.update_age(user_age)
    elif user_change == 2:
        print(f'Загрузка...')
        user_santa_claus.give_gifts()
    elif user_change == 3:
        print(f'* * *\nТебя зовут {user_santa_claus.name}, тебе {user_santa_claus.update_age(user_age)} лет, '
              f'и ты получаешь {user_santa_claus.count_gifts} подарков!')
    elif user_change == 4:
        print(f'* * *\nУдачи тебе, {user_santa_claus.name}! Программа успешна завершена!')
        break
    else:
        print('* * *\nОшибка! Повтори попытку')
        print('-' * 100)
        break
