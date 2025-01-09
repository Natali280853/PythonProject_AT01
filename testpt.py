import pytest
from mainpt import check


def test_check():
    assert check(6) == True


def test_check2():
    assert check(3) == False


# Первый элемент кортежа (number) будет передаваться в тестовую функцию в качестве входного значения,
# а второй элемент (expected) — это ожидаемый результат, с которым мы будем сравнивать фактический
# результат выполнения функции
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (5, False),
    (0, True),   # при 0 проблем не будет, т.к. 0 можно делить на 2
    (56, True),
    (-3, False)
    ])
# assert вызывает функцию check, передавая ей число number
def test_check_with_param(number, expected):
    assert check(number) == expected
