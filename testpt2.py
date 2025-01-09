import pytest
from mainpt2 import sort_list  # замените my_module на имя вашего модуля


def test_sort_list_ascending():
    assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]


def test_sort_list_descending():
    assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_sort_list_mixed():
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]


@pytest.mark.parametrize("numbers, expected", [
    ([7, 2, 5, 3], [2, 3, 5, 7]),
    ([10, -10, 0], [-10, 0, 10]),
    ([], []),
    ([1], [1])
    ])
def test_sort_list_parametrized(numbers, expected):
    assert sort_list(numbers) == expected
