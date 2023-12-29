import datetime

print('- ' * 80)

print('Задача №1')
# Класс Книга должен содержать информацию о названии, авторе и жанре книги.

books = [
    {
        'title': 'Гарри Поттер и Филосовский камень',
        'genre': 'Фэнтези',
        'author': 'Джоан Роулинг'
    },
    {
        'title': 'Метро 2033',
        'genre': 'Фантастика',
        'author': 'Дмитрий Глуховский'
    },
    {
        'title': 'Кладбище домашних животных',
        'genre': 'Мистика',
        'author': 'Стивен Кинг'
    },
]


class Book:
    print('Книги:')

    def __init__(self, title, genre, author):
        self.title = title
        self.genre = genre
        self.author = author
        print(f'* * *\nНазвание книги --> {title}\nЖанр --> {genre}\nАвтор --> {author}')


for book in books:
    Book(title=book['title'], genre=book['genre'], author=book['author'])

print('- ' * 80)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №2')
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе.

accounts = [
    {
        'person': 'Max Peterson',
        'balance': 125500
    },
    {
        'person': 'Jessica Li',
        'balance': 45650
    },
    {
        'person': 'Ronald Parker',
        'balance': 80999
    }
]


class BankAccount:
    print('Банковские аккаунты:')

    def __init__(self, person, balance):
        self.person = person
        self.balance = balance
        print(f'\nВладелец --> {person}\nБаланс --> {balance}$')


for acc in accounts:
    BankAccount(person=acc['person'], balance=acc['balance'])

print('- ' * 80)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №3')
# Класс Авиабилет должен содержать данные о рейсе, дате, месте и стоимости.
# Методы должны позволять бронировать билеты, отменять бронь и просматривать доступные рейсы.

flights_date = []
flights = []
num = 0

for i in range(3, 14, 4):
    num += 1
    res = datetime.datetime.now() + datetime.timedelta(days=i)
    flights_date.append(str(num) + ') ' + res.strftime("%d.%m.%Y в %H:%M"))
    flights.append(res)

try:
    print(f'Сегодня --> {datetime.datetime.now().strftime("%d.%m.%Y")}\nБлижайшие рейсы --> {", ".join(flights_date)}')
    user = int(input('Выберите дату бронирования рейса. Введите одно число (например: 1) --> '))


    class AirTicket:
        print('\nИнформация о рейсе:\n* * *')

        def __init__(self, time, date, departure, arrival, cost, duration):
            self.time = time
            self.date = date
            self.departure = departure
            self.arrival = arrival
            self.cost = cost
            self.duration = duration
            date_arrival = time + datetime.timedelta(hours=duration)
            print(f'Дата --> {date.strftime("%d.%m.%Y")}\nВылет --> {time.strftime("%H:%M")}, {departure}\n'
                  f'Прилет --> {date_arrival.strftime("%d.%m.%y в %H:%M")}, {arrival}\n'
                  f'Длительность --> {duration}ч\nСтоимость --> {cost} руб.')


    air_ticket = AirTicket(time=flights[user - 1], date=flights[user - 1], departure='Москва, Россия',
                           arrival='Лос-Анджелес, США', cost=6000, duration=15)

    user_2 = int(input('\nБронировать билет? Введите число, где 0 - это "да", а 1 - это "нет" (например: 0) --> '))

    while True:
        if user_2 == 0:
            print(f'Ваш рейс забронирован на {flights[user - 1].strftime("%d.%m.%Y в %H:%M")}')
            break
        else:
            print(f'\nБлижайшие рейсы --> {", ".join(flights_date)}')
            user = int(input('Выберите дату бронирования рейса. Введите одно число (например: 1) --> '))
            print('\nИнформация о рейсе:\n* * *')
            air_ticket = AirTicket(time=flights[user - 1], date=flights[user - 1], departure='Москва, Россия',
                                   arrival='Лос-Анджелес, США', cost=6000, duration=15)
            user_2 = int(input('\nБронировать билет? Введите число, где 0 - это "да", '
                               'а 1 - это "нет" (например: 0) --> '))

except:
    print('\nПроизошла ошибка! Не верно ввели данные. Повторите попытку')

print('- ' * 80)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №4')
# Реализуйте класс для управления системой бронирования отелей.
# Класс Бронь должен содержать информацию о госте, дате заезда и выезда, типе номера.
# Методы должны позволять бронировать, отменять бронь и проверять доступность номеров на определенные даты.

reservation = [
    {
        'guest': 'Max',
        'check_in_date': datetime.date(2023, 10, 1),
        'exit_date': datetime.date(2023, 10, 11),
        'number': 1,
    },
    {
        'guest': 'Jessie',
        'check_in_date': datetime.date(2023, 12, 15),
        'exit_date': datetime.date(2023, 12, 30),
        'number': 2,
    },
    {
        'guest': 'John',
        'check_in_date': datetime.date(2023, 11, 9),
        'exit_date': datetime.date(2023, 11, 13),
        'number': 3,
    },
    {
        'guest': 'Leo',
        'check_in_date': datetime.date(2023, 11, 10),
        'exit_date': datetime.date(2023, 11, 21),
        'number': 1,
    },
    {
        'guest': 'Mary',
        'check_in_date': datetime.date(2023, 12, 1),
        'exit_date': datetime.date(2023, 12, 8),
        'number': 1,
    }
]

try:
    user_name = input('Здравствуйте! Как к Вам обращаться? Введите свое имя --> ')
    user_number = int(input('Какой номер хотите забронировать? Введите номер --> '))
    user_day = int(input('На какое число будет бронироваться номер? Введите число --> '))
    user_month = int(input('На какой месяц будет бронироваться номер? Введите число месяца --> '))
    user_exit = int(input('На сколько дней хотите забронировать номер? Введите число --> '))

    user_start_date = datetime.date(2023, user_month, user_day)
    user_end_date = datetime.date(2023, user_month, user_day) + datetime.timedelta(days=user_exit)


    class Reservation:
        def __init__(self, guest, check_in_date, exit_date, number):
            self.guest = guest
            self.check_in_date = check_in_date
            self.exit_date = exit_date
            self.number = number

            for i in reservation:
                if number == i['number']:
                    if i['check_in_date'] <= check_in_date <= i['exit_date']:
                        print(f'* * *\nИзвините. Номер забронирован гостем {i["guest"]}')
                        raise

            user_reservation = int(input('\nБудете бронировать номер? Введите число, где 0 - это "да", '
                                         'а 1 - это "нет" --> '))
            while True:
                if user_reservation == 0:
                    reservation.append({'guest': guest, 'check_in_date': check_in_date, 'exit_date': exit_date,
                                        'number': number})
                    print(f'* * *\n{user_name}, Вы удачно забронировали номер №{number}\nНомером можно '
                          f'пользоваться с {user_start_date.strftime("%d.%m.%y")} по '
                          f'{user_end_date.strftime("%d.%m.%y")}')
                    break
                elif user_reservation == 1:
                    number = int(input('\nКакой номер хотите забронировать? Введите номер --> '))
                    user_day = int(input('На какое число будет бронироваться номер? Введите число --> '))
                    user_month = int(
                        input('На какой месяц будет бронироваться номер? Введите число месяца --> '))
                    user_exit = int(input('На сколько дней хотите забронировать номер? Введите число --> '))

                    check_in_date = datetime.date(2023, user_month, user_day)
                    exit_date = datetime.date(2023, user_month, user_day) + datetime.timedelta(
                        days=user_exit)

                    for i in reservation:
                        if number == i['number']:
                            if i['check_in_date'] <= check_in_date <= i['exit_date']:
                                print(f'* * *\nИзвините. Номер забронирован гостем {i["guest"]}')
                                raise

                    user_reservation = int(input('\nБудете бронировать номер? Введите число, '
                                                 'где 0 - это "да", а 1 - это "нет" --> '))


    new_guest = Reservation(guest=user_name, check_in_date=user_start_date, exit_date=user_end_date, number=user_number)
    for i in reservation:
        print(i)

except:
    print('\nПовторите попытку')
