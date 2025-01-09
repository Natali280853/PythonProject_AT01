import pytest
from mainmock1 import get_github_user


def test_get_github_user(mocker):
    mock_get = mocker.patch('mainmock1.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nina'
    }

    user_data = get_github_user('!!!')  # функция будет работать верно, независимо от того, какое значение передается в user_data
    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nina'
    }


def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('mainmock1.requests.get')
    mock_get.return_value.status_code = 500

    user_data = get_github_user('!!!')
    assert user_data is None
