from conftest import *
from urls import Endpoints
from data import UserData, UnfilledUserData
from helpers import CreateNewUser
import allure

faker = Faker()


@allure.suite('Тестирование создания пользователя')
class TestCreateUser:

    @allure.title('Проверка успешной регистрации пользователя с валидными данными ')
    def test_create_new_user_success(self):
        payload = CreateNewUser.generate_new_user_data()
        response = requests.post(Endpoints.CREATE_USER, json=payload)
        response_body = response.json()
        assert response.status_code == 200 and response_body['user']['email'] == payload['email']
        access_token = response_body['accessToken']
        requests.delete(Endpoints.DELETE_USER, headers={'Authorization': access_token})

    @allure.title('Проверка регистрации пользователя с уже существующим email')
    def test_create_already_exist_user_success(self):
        payload = {
            'email': UserData.email,
            'password': faker.password(),
            'name': faker.first_name()
        }
        response = requests.post(Endpoints.CREATE_USER, json=payload)
        response_body = response.json()
        assert response.status_code == 403 and response_body == {'success': False,
                                                                 'message': 'User already exists'}

    @allure.title('Проверка регистрации пользователя при незаполнении одного из обязательных полей')
    @pytest.mark.parametrize('data', UnfilledUserData.unfilled_data)
    def test_create_user_without_required_data_success(self, data):
        response = requests.post(Endpoints.CREATE_USER, data=data)
        assert response.status_code == 403 and response.json() == {'success': False,
                                                                   'message': 'Email, password and name are required fields'}



