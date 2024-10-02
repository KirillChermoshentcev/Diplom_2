from conftest import *
import requests
from urls import Endpoints
import allure


@allure.suite('Тестирование получения заказов пользователя')
class TestGetUserOrders:

    @allure.title('Проверка получения заказов авторизированного пользователя')
    def test_get_orders_of_authorized_user_success(self, create_order):
        response = requests.get(Endpoints.GET_USER_ORDERS, headers={'Authorization': create_order[1]})
        response_body = response.json()
        assert response.status_code == 200 and response_body['success'] is True
        assert 'orders' in response_body
        user_orders = response_body['orders']
        print("Список заказов пользователя:", user_orders)

    @allure.title('Проверка получения заказов неавторизированного пользователя')
    def test_get_orders_of_unauthorized_user_success(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(Endpoints.GET_USER_ORDERS, headers=headers)
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': 'You should be authorised'}
