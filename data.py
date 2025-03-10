from faker import Faker

faker = Faker()


class UserData:

    email = 'alyosha.popovich@yandex.ru'
    password = '7862535'
    name = 'Aleksey'

    wrong_data = [
        {'email':email,
         'password': faker.password(length=10)},
        {'email': faker.free_email,
         'password': '7862535'}
    ]


class UnfilledUserData:

    unfilled_data = [
        {'email': '',
         'password': faker.password(length=10),
         'name': faker.first_name},
        {'email': faker.free_email,
         'password': '',
         'name': faker.first_name},
        {'email': faker.free_email(),
         'password': faker.password(length=10),
         'name': ''}
    ]


class BurgersData:

    burger_reciept_1 = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa72']

    burger_reciept_2 = ['61c0c5a71d1f82001bdaaa6c', '61c0c5a71d1f82001bdaaa6e', '61c0c5a71d1f82001bdaaa74']

    incorrect_cash_of_ingredients = ['61c0c5a71d1f82001b123456', '61c0c5a71d1f82001b654321', '61c0c5a71d1f82001b112233']


class ResponseMessage:

    USER_ALREADY_EXIST = {'success': False,
                          'message': 'User already exists'}

    UNFILLED_DATA = {'success': False,
                     'message': 'Email, password and name are required fields'}

    EMPTY_ORDER = {'success': False,
                   'message': 'Ingredient ids must be provided'}

    INCORRECT_INGREDIENT = {"success": False,
                            "message": "One or more ids provided are incorrect"}

    AUTHORIZATION_REQUIRED = {'success': False,
                              'message': 'You should be authorised'}

    INVALID_DATA = {"success": False,
                    "message": "email or password are incorrect"}