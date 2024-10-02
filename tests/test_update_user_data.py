from conftest import *
from faker import Faker
import requests
import allure


faker = Faker()


@allure.suite('Тестирование возможности изменения данных пользователя')
class TestUpdateUserData:

    @allure.title('Проверка возможности изменения любого поля авторизованного пользователя')
    @pytest.mark.parametrize("param, new_value", [
        ('email', faker.free_email()),
        ('name', faker.first_name())
    ])
    def test_update_user_data_success(self, create_user, param, new_value):
        response = requests.patch(Endpoints.UPDATE_USER_DATA,
                                  headers={'Authorization': create_user[1]['accessToken'],
                                           'Content-Type': 'application/json'},
                                  json={param: new_value})
        response_body = response.json()
        assert response.status_code == 200
        assert response_body['user'][param] == new_value
        print(response.text)

    @allure.title('Проверка возможности изменения любого поля неавторизованного пользователя')
    @pytest.mark.parametrize("param, new_value", [
        ('email', faker.free_email()),
        ('name', faker.first_name())
    ])
    def test_update_unauthorized_user_data_success(self, create_user, param, new_value):
        response = requests.patch(Endpoints.UPDATE_USER_DATA,
                                  headers={'Content-Type': 'application/json'},
                                  json={param: new_value})
        response_body = response.json()
        assert response.status_code == 401
        assert response_body == {'success': False,
                                 'message': 'You should be authorised'}
        print(response.text)

