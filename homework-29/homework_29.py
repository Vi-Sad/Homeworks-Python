# Задача 1: Управление почтовым ящиком
# Риализуйте класс EmailClient, представляющий почтовый клиент.
# Класс должен содержать метод send_email, отправляющий электронное письмо.
# Создайте собственный класс исключения InvalidEmailError, который будет возбуждаться,
# если адрес электронной почты не соответствует формату.

import transliterate
import random
import colorama

print('-' * 100)


class InvalidEmailError(Exception):
    def __str__(self):
        return colorama.Fore.RED + 'НЕ верно набрана цифра или ввод недопустимого символа' + colorama.Fore.RESET + '\n'


class EmailClient:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def create_email(self):
        print('Возможные варианты Вашей будущей электронной почты:')
        random_nums = range(0, 11)
        name_en = transliterate.translit(self.name, 'ru', reversed=True)
        surname_en = transliterate.translit(self.surname, 'ru', reversed=True)
        print(f'1) {name_en}.{surname_en}@yandex.ru'.lower())
        print(f'2) {surname_en}.{name_en[:1]}_{random.choice(random_nums)}@yandex.ru'.lower())
        print(f'3) {name_en}_{random.choice(random_nums)}@yandex.ru'.lower())
        user_command = int(input('Какой вид почты использовать? Введите номер --> '))

        if user_command == 1:
            print('Почта успешно была создана:')
            return f'{name_en}.{surname_en}{random.choice(random_nums)}@yandex.ru'.lower()
        elif user_command == 2:
            print('Почта успешно была создана:')
            return f'{surname_en}.{name_en[:1]}.{random.choice(random_nums)}@yandex.ru'.lower()
        elif user_command == 3:
            print('Почта успешно была создана:')
            return f'{name_en}_{random.choice(random_nums)}@yandex.ru'.lower()
        else:
            print('Произошла ошибка:')
            raise InvalidEmailError


user_name = input('Давайте зарегистрируем Вас на Яндекс почту! Введите свое имя кириллицей --> ')
user_surname = input('Введите свою фамилию кириллицей --> ')

USER = EmailClient(user_name, user_surname)
try:
    print(USER.create_email())
except InvalidEmailError:
    print(InvalidEmailError())
    print('Давайте попробуем снова')
    print(USER.create_email())

print('-' * 100)
