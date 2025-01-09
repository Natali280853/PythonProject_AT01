import pytest
from mainmock import get_weather  # замените my_module на имя вашего модуля

# Mocker — это фикстура, которая предоставляется модулем Pytest mock, который мы только что установили.
# Эта фикстура позволяет мокировать объекты и различные функции

# Используем patch, чтобы изменить поведение функции get, прописанной в main.py.
# Для этого создадим переменную mock_get и мокируем (меняем поведение) у функции request_get
def test_get_weather_success(mocker):
    mock_get = mocker.patch('mainmock.requests.get')

    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 282.55}
    }

    api_key = '272009fd696656bbaea88b8d974dd950'
    city = 'London'
    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 282.55}
    }


def test_get_weather_failure(mocker):
    mock_get = mocker.patch('mainmock.requests.get')

    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404

    api_key = '272009fd696656bbaea88b8d974dd950'
    city = 'London'
    weather_data = get_weather(api_key, city)

    assert weather_data is None
