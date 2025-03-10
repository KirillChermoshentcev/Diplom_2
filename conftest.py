import pytest
import requests
from urls import Endpoints
from helpers import CreateNewUser
from data import *


@pytest.fixture
def create_user():
    user_data = CreateNewUser.generate_new_user_data()
    response = requests.post(f'{Endpoints.CREATE_USER}', json=user_data)
    response_body = response.json()

    yield user_data, response_body

    access_token = response_body.get('accessToken')
    requests.delete(f'{Endpoints.DELETE_USER}', headers={'Authorization': access_token})


@pytest.fixture(scope='function')
def create_order(create_user):
    payload = {'ingredients': [BurgersData.burger_reciept_1]}
    access_token = create_user[1]['accessToken']
    response = requests.post(f'{Endpoints.CREATE_ORDER}', data=payload, headers={'Authorization': access_token})
    order_data = response.json()

    yield order_data, access_token

    requests.delete(Endpoints.DELETE_USER, headers={'Authorization': access_token})
