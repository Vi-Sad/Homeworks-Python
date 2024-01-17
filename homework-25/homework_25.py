import datetime, random

print('-' * 100)

print('Задача №1')
# Определите класс Animal с атрибутами name (имя животного) и sound (звук, который издает животное).
# Также определить метод make_sound(), который выводит сообщение о звуке, издаваемом животным.
# Создайте дочерний класс Bird, который наследует от класса Animal.
# Добавьте атрибут flight_altitude (высота полета) и метод fly(), который выводит сообщение о полете птицы.

# Пример использования:
# Создание объектов:
# lion = Animal("Lion", "Roar")
# parrot = Bird("Parrot", "Squawk", 100)
# Вызов методов:
# lion.make_sound() - выводит сообщение о звуке льва
# parrot.make_sound() - выводит сообщение о звуке попугая
# parrot.fly() - выводит сообщение о полете птицы

animal_name, animal_sound = 'Cat', 'Meow'
bird_name, bird_sound, bird_height = 'Parrot', 'Squawk', 3


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f'* * *\nThe {self.name} says "{self.sound}"!'


class Bird(Animal):
    def __init__(self, name, sound, flight_altitude):
        super().__init__(name, sound)
        self.flight_altitude = flight_altitude

    def fly(self):
        return f'The {self.name} flies at an altitude of {self.flight_altitude} km'


animal = Animal(animal_name, animal_sound)
print(animal.make_sound())

bird = Bird(bird_name, bird_sound, bird_height)
print(bird.make_sound() + '\n' + bird.fly())

print('-' * 100)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №2')
# Определите класс IDGenerator, который генерирует уникальные идентификаторы.
# Добавьте статический метод generate_id(), который возвращает строку с уникальным идентификатором.
# Идентификатор может, например, состоять из текущей даты и случайного числа.

# Пример:
# Использование IDGenerator:
# id1 = IDGenerator.generate_id()
# id2 = IDGenerator.generate_id()
# print(f"Generated ID 1: {id1}")
# print(f"Generated ID 2: {id2}")

id = range(1000000)


class IDGenerator:
    @staticmethod
    def generate_id():
        date = datetime.date.today().strftime('%d_%m_%Y')
        id_generate = random.choice(id)
        return f'{date}_{id_generate}'


id_1 = IDGenerator.generate_id()
print(f'Generated ID 1 --> {id_1}')
id_2 = IDGenerator.generate_id()
print(f'Generated ID 2 --> {id_2}')

print('-' * 100)

# ---------------------------------------------------------------------------------------------------------------------

print('Задача №3')
# Определите класс StringUtils, который содержит classmethod count_characters(cls, input_string).
# Метод должен принимать строку и возвращать словарь, в котором ключами являются символы,
# а значениями — количество их вхождений в строку.

# Пример использования:
# Использование StringUtils:
# char_count = StringUtils.count_characters("hello world")
# print(f"Character Count: {char_count}")

string = 'hello world'
string = string.replace(' ', '')
dict_str = {}


class StringUtils:
    input_string = string

    @classmethod
    def count_characters(cls):
        for i in cls.input_string:
            dict_str[i] = cls.input_string.count(i)
        return dict_str


char_count = StringUtils.count_characters()
print(f"Character count --> {char_count}")

print('-' * 100)
