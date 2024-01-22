import datetime

print('-' * 100)

print('Задача №1')
# Создайте класс Date, представляющий дату.
# Реализуйте магические методы сравнения дат (==, !=, <, >, <=, >=) на основе сравнения года, месяца и дня.

list_dates = []


class Date:
    def __init__(self, date):
        self.date = date

        dates = {}
        dates['day'] = self.date[:2]
        dates['month'] = self.date[3:5]
        dates['year'] = self.date[6:]
        list_dates.append(dates)

    def __eq__(self, year):
        print(f'Январские даты {year} года:')
        for date in list_dates:
            if date['year'] == year:
                print(f'{date["day"]}.{date["month"]}.{date["year"]}')


date_1 = Date(datetime.date.today().strftime('%d.%m.%Y'))
date_2 = Date(datetime.date(2023, 12, 11).strftime('%d.%m.%Y'))
date_3 = Date(datetime.date(2023, 10, 22).strftime('%d.%m.%Y'))
date_4 = Date(datetime.date(2024, 1, 2).strftime('%d.%m.%Y'))
date_5 = Date(datetime.date(2024, 12, 2).strftime('%d.%m.%Y'))
date_6 = Date(datetime.date(2023, 12, 12).strftime('%d.%m.%Y'))

date_1.__eq__('2024')

print('-' * 100)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №2')
# Создайте класс Book, представляющий книгу.
# Реализуйте магические методы сравнения (==, !=, <, >, <=, >=) на основе сравнения года издания книги.
# Книги сравниваются по году издания.

list_books = []


class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.autor = autor
        self.year = year

        books = {}
        books['title'] = self.title
        books['autor'] = self.autor
        books['year'] = self.year
        list_books.append(books)

    def __le__(self, year):
        print(f'Книги с датой издания не позднее {year} года:')
        for book in list_books:
            if book['year'] <= year:
                print(f'"{book["title"]}" ({book["autor"]}), {book["year"]} г.')


book_1 = Book('Час Презрения', 'Анджей Сапковский', 1999)
book_2 = Book('Королевство плоти и огня', 'Джениффер Ли', 2020)
book_3 = Book('Пламя и кровь. Пляска смерти', 'Джордж Р.Р. Мартин', 2018)
book_4 = Book('Тень света', 'Андрей Васильев', 2018)
book_5 = Book('Драконья традиция', 'Ная Геярова', 2020)
book_6 = Book('Лавр', 'Евгений Водолазкин', 2012)

book_1.__le__(2015)

print('-' * 100)
