print('-' * 100)

print('Задача №1')
# Создать класс "Person" с атрибутами "name", "age", "email" и методами для чтения и записи данных всех трех атрибутов.
# Реализовать валидацию для атрибута "age": должно быть положительным целым числом.

user_name = 'Victoria'
user_age = 22
user_email = 'sadovskaya.vicka@yandex.ru'


class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    @staticmethod
    def check_age(age):
        if age > 0 and type(age) == int:
            return f'{age} (валидный)'
        else:
            return f'{age} (НЕ валидный)'

    @staticmethod
    def check_email(email):
        if type(email) == str and ('@yandex.ru' in email or '@gmail.com' in email):
            return f'{email} (валидный)'
        else:
            return f'{email} (НЕ валидный)'

    def name(self):
        return self.name

    def age(self):
        return self.age

    def email(self):
        return self.email


try:
    user = Person(user_name, user_age, user_email)
    print(f'Имя --> {user.name}\nВозраст --> {user.check_age(user.age)}\nEmail --> {user.check_email(user.email)}')
except ValueError:
    print('НЕ валидные данные')

print('-' * 100)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №2')
# Создать класс "Product" с атрибутами "name", "price", "quantity" и методами для чтения и записи данных всех атрибутов.
# Реализовать валидацию для атрибута "price": должно быть положительным целым или дробным числом.

user_name = 'Яблоко'
user_price = 50
user_quantity = 2


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def check_price(price):
        if (type(price) == int or type(price) == float) and price > 0:
            return f'{price} (валидная)'
        else:
            return f'{price} (НЕ валидная)'

    @staticmethod
    def check_quantity(quantity):
        if type(quantity) == int and quantity > 0:
            return f'{quantity} (валидное)'
        else:
            return f'{quantity} (НЕ валидное)'

    def name(self):
        return self.name

    def price(self):
        return self.price

    def quantity(self):
        return self.quantity


user = Product(user_name, user_price, user_quantity)

try:
    while True:
        user_command = int(input('* * *\nВыбери команду:\n1. Посмотреть информацию\n2. Изменить продукт\n'
                                 '3. Изменить цену\n4. Изменить количество\n5. Проверить на валидность\n'
                                 '6. Выйти из программы\nВведи число --> '))
        if user_command == 1:
            payment = user.price * user.quantity
            if user.price <= 0 or user.quantity <= 0:
                print('* * *\nГде-то пресутсвуют НЕ валидные данные. Сделай проверку на валидность')
            else:
                print(f'* * *\nПродукт: {user.name}\nЦена за 1 шт.: {user.price} руб.\nКоличество шт.: {user.quantity}'
                      f'\nК оплате: {round(payment, 2)} руб.')
        elif user_command == 2:
            user_name = input('* * *\nВведи название продукта --> ')
            user = Product(user_name, user_price, user_quantity)
        elif user_command == 3:
            user_price = float(input('* * *\nВведи цену продукта за 1 шт. --> '))
            user = Product(user_name, user_price, user_quantity)
        elif user_command == 4:
            user_quantity = int(input('* * *\nВведи количество шт. --> '))
            user = Product(user_name, user_price, user_quantity)
        elif user_command == 5:
            print(
                f'* * *\nЦена --> {user.check_price(user.price)}\nКоличество --> {user.check_quantity(user.quantity)}')
        elif user_command == 6:
            print('* * *\nПрограмма успешно завершена')
            print('-' * 100)
            break
        else:
            print(f'* * *\nКоманды "{user_command}" НЕ существует')
except ValueError:
    print('* * *\nОшибка! Ввод некорректных данных. Повтори попытку')
