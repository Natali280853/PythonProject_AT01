# **Тесты**:
#    - `test_get_random_cat_image_success`: Проверяет, что функция возвращает правильный URL,
#    когда запрос успешен (статус-код 200).
#    - `test_get_random_cat_image_not_found`: Проверяет, что функция возвращает `None`, когда запрос
#    неуспешен (например, статус-код 404).
# import pytest
# from unittest.mock import patch
from mainmock_dz import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    # Создаем мока для ответа API
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    url = get_random_cat_image()
    assert url == 'https://example.com/cat.jpg'


def test_get_random_cat_image_not_found(mocker):
    # Создаем мока для ответа API с ошибкой 404
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 404

    url = get_random_cat_image()
    assert url is None
