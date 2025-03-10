import pytest

import data
from conftest import create_user
import requests
from urls import Endpoints
from data import *
import allure


@allure.suite('Тестирование логина пользователя')
class TestLoginUser:

    @allure.title('Проверка авторизации пользователя с валидными данными')
    def test_login_user_success(self, create_user):
        payload = create_user[0]
        response = requests.post(f'{Endpoints.LOGIN}', json=payload)
        response_body = response.json()
        assert response.status_code == 200 and response_body['user']['email'] == create_user[0]['email']

    @allure.title('Проверка авторизации пользователя с невалидными данными')
    @pytest.mark.parametrize('user_data', UserData.wrong_data)
    def test_login_with_incorrect_data_success(self, user_data):
        response = requests.post(f'{Endpoints.LOGIN}', data=user_data)
        assert response.status_code == 401 and response.json() == ResponseMessage.INVALID_DATA

