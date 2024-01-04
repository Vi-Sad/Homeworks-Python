from snowflake_functions import *

print('- ' * 80)

print('Задача №1')
# Реализовать класс Snowflake:
# - Атрибуты: размер, форма.
# - Методы: change_size(new_size), change_shape(new_shape).
# - НЕОБЯЗАТЕЛЬНО: Интерфейс для изменения размера и формы снежинки

user_size = 100
user_shape = 6
user_snowflake = Snowflake(user_size, user_shape)

try:
    while True:
        user_change = int(input('* * *\nВыберите команду:\n1. Изменить размер снежинки\n2. Изменить количество '
                                'сегментов снежинки\n3. Посмотреть данные о снежинке\n4. Посмотреть снежинку\n'
                                '5. Выйти из программы\nВведи число --> '))
        if user_change == 1:
            user_size = int(input('* * *\nКакой размер будет у снежинки? Введи число --> '))
            user_snowflake.change_size(user_size)
        elif user_change == 2:
            user_shape = int(input('* * *\nСколько сегментов будет у снежинки? Введи число --> '))
            user_snowflake.change_shape(user_shape)
        elif user_change == 3:
            print(user_snowflake.info_snowflake())
        elif user_change == 4:
            print(user_snowflake.look_snowflake())
        elif user_change == 5:
            print('* * *\nПрограмма успешно завершена')
            print('- ' * 80)
            break
        else:
            break
except:
    print('* * *\nОшибка! Пожалуйста, повторите попытку')
    print('- ' * 80)
