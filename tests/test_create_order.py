from conftest import *
import allure


@allure.suite('Тестирование создания заказа')
class TestCreateOrder:

    @allure.title('Проверка создания заказа авторизированным пользователем')
    @pytest.mark.parametrize('burger_ingredients', [BurgersData.burger_reciept_1, BurgersData.burger_reciept_2])
    def test_create_order_by_authorized_user_success(self, create_user, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        headers = {'Authorization': create_user[1]['accessToken']}
        response = requests.post(Endpoints.CREATE_ORDER, headers=headers, data=payload)
        response_body = response.json()
        assert response.status_code == 200 and response_body['success'] is True

    @allure.title('Проверка создания заказа неавторизированным пользователем')
    @pytest.mark.parametrize('burger_ingredients', [BurgersData.burger_reciept_1, BurgersData.burger_reciept_2])
    def test_create_order_by_unauthorized_user_success(self, create_user, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Endpoints.CREATE_ORDER, data=payload)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка создания заказа без ингредиентов для авторизированного и неавторизированного пользователя')
    @pytest.mark.parametrize('authorized', [True, False])  # Параметризация по авторизации
    def test_create_order_without_ingredients_success(self, create_user, authorized):
        payload = {'ingredients': []}
        headers = {'Content-Type': 'application/json'}
        if authorized:
            headers = {'Authorization': create_user[1]['accessToken']}
        response = requests.post(Endpoints.CREATE_ORDER, headers=headers, json=payload)
        assert response.status_code == 400
        assert response.json() == {'success': False,
                                   'message': 'Ingredient ids must be provided'}

    @allure.title('Проверка создания заказа с невалидным хэшем ингредиента')
    def test_create_order_with_incorrect_cash_of_ingredients_success(self, create_user):
        payload = {'ingredients': [BurgersData.incorrect_cash_of_ingredients]}
        headers = {'Authorization': create_user[1]['accessToken']}
        response = requests.post(Endpoints.CREATE_ORDER, headers=headers, data=payload)
        assert response.status_code == 400 and response.json() == {"success": False,
                                                                   "message": "One or more ids provided are incorrect"}