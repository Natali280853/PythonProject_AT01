import pytest
from mainpt4 import count_vowels


def test_count_vowels_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("aeiouAEIOU") == 10


def test_count_vowels_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("") == 0


def test_count_vowels_mixed():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python is awesome") == 6
    assert count_vowels("PyThOn") == 2


if __name__ == "__main__":
    pytest.main()
