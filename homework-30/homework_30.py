# Задача №1

# Напишите тестовые сценарии для данной функции и протестируйте ее.

def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0


# ---------------------------------------------------------------------------------------------------------------------

print('-' * 100)

print('Задача №1')

print('\nТест #1')
print('Проверяемое число -> 2')
print('Ожидаемый результат -> True')
print(f'Реальный результат -> {is_even(2)}')

print('\nТест #2')
print('Проверяемое число -> 1')
print('Ожидаемый результат -> False')
print(f'Реальный результат -> {is_even(1)}')

print('\nТест #3')
print('Проверяемое число -> -1')
print('Ожидаемый результат -> False')
print(f'Реальный результат -> {is_even(-1)}')

print('\nТест #4')
print('Проверяемое число -> -2')
print('Ожидаемый результат -> True')
print(f'Реальный результат -> {is_even(-2)}')

print('\nТест #5')
print('Проверяемое число -> 2.0')
print('Ожидаемый результат -> True')
print(f'Реальный результат -> {is_even(2.0)}')

print('\nТест #6')
print('Проверяемое число -> q')
print('Ожидаемый результат -> False')
try:
    print(f'Реальный результат -> {is_even("q")}')
except TypeError:
    print(f'Реальный результат -> TypeError')


# ---------------------------------------------------------------------------------------------------------------------

# Задача №2

# Напишите тестовые сценарии для данного класса и протестируйте его.

class Rectangle:
    """
    Класс Rectangle представляет прямоугольник.

    :param width: Ширина прямоугольника
    :param height: Высота прямоугольника
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        :return: Площадь прямоугольника
        """
        return self.width * self.height if self.width > 0 and self.height > 0 else None

    def perimeter(self) -> float:
        """
        Вычисляет периметр прямоугольника.

        :return: Периметр прямоугольника
        """
        return 2 * (self.width + self.height) if self.width > 0 and self.height > 0 else None


# Пример использования класса:
# Создаем экземпляр прямоугольника
# rectangle = Rectangle(width=5, height=10)

# Получаем и выводим площадь и периметр
# print(f"Площадь прямоугольника: {rectangle.area()}")
# print(f"Периметр прямоугольника: {rectangle.perimeter()}")

# ---------------------------------------------------------------------------------------------------------------------

print('-' * 100)

print('Задача №2')

print('\nТест №1')
rectangle = Rectangle(5, 10)
print('Проверяемая ширина -> 5')
print('Проверяемая длина -> 10')
print('Ожидаемый результат Периметра -> 30')
print(f'Реальный результат Периметра -> {rectangle.perimeter()}')
print('Ожидаемый результат Площади -> 50')
print(f'Реальный результат Площади -> {rectangle.area()}')

print('\nТест №2')
rectangle = Rectangle(2.2, 7.8)
print('Проверяемая ширина -> 2.2')
print('Проверяемая длина -> 7.8')
print('Ожидаемый результат Периметра -> 20.0')
print(f'Реальный результат Периметра -> {rectangle.perimeter()}')
print('Ожидаемый результат Площади -> 17.16')
print(f'Реальный результат Площади -> {rectangle.area()}')

print('\nТест №3')
rectangle = Rectangle(-5, 10)
print('Проверяемая ширина -> -5')
print('Проверяемая длина -> 10')
print('Ожидаемый результат Периметра -> None')
print(f'Реальный результат Периметра -> {rectangle.perimeter()}')
print('Ожидаемый результат Площади -> None')
print(f'Реальный результат Площади -> {rectangle.area()}')

print('\nТест №4')
rectangle = Rectangle('a', 5)
print('Проверяемая ширина -> a')
print('Проверяемая длина -> 5')
print('Ожидаемый результат Периметра -> None')
try:
    print(f'Реальный результат Периметра -> {rectangle.perimeter()}')
except TypeError:
    print(f'Реальный результат -> TypeError')
print('Ожидаемый результат Площади -> None')
try:
    print(f'Реальный результат Площади -> {rectangle.area()}')
except TypeError:
    print(f'Реальный результат -> TypeError')
