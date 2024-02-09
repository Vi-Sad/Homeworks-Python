# Copy to the terminal -> pytest homework_31.py

# Задача №1

# Напиши тестовые сценарии для данной функции и протестируйте ее при помощи pytest.

import pytest


def calculate_average(numbers: list) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)


@pytest.mark.parametrize('list_numbers, expected', [
    ([1, 2, 3], 2), ([4, 5, 6], 5.0), ([231, 312, 21], 188), ([110, 43, 5], 52.7), (['12', 56, 345], 138),
    ([100, 100, 100], 100), ([90, 5, 30], 41.6666667), ([-43, -32, 432], 119), ([-32, -2423, -4232.6], -2229.2)
])
def test_calculate_average(list_numbers, expected):
    expected_result = expected
    real_result = calculate_average(list_numbers)
    assert expected_result == real_result


# ---------------------------------------------------------------------------------------------------------------------

# Задача №2

# Напиши тестовые сценарии для данной функции и протестируйте ее при помощи pytest.

def is_prime(number: int) -> bool:
    """
    Проверяет, является ли число простым.

    :param number: Проверяемое число
    :return: True, если число простое, иначе False
    """
    if number <= 1:
        # Числа меньше или равные 1 не являются простыми
        return False
    elif number == 2:
        # 2 - единственное четное простое число
        return True
    elif number % 2 == 0:
        # Все другие четные числа не являются простыми
        return False
    else:
        # Проверяем делители от 3 до квадратного корня из числа
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


@pytest.mark.parametrize('number, expected', [
    (2, True), (1, True), (23, True), (90, False), (-2, True), (0, False), ('35', False), (1000, False), (2.5, True)
])
def test_is_prime(number, expected):
    expected_result = expected
    real_result = is_prime(number)
    assert expected_result == real_result
