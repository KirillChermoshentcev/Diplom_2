class Endpoints:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    LOGIN = f'{BASE_URL}/api/auth/login'

    CREATE_USER = f'{BASE_URL}/api/auth/register'

    DELETE_USER = f'{BASE_URL}/api/auth/user'

    UPDATE_USER_DATA = f'{BASE_URL}/api/auth/user'

    INGREDIENTS = f'{BASE_URL}/api/ingredients'

    CREATE_ORDER = f'{BASE_URL}/api/orders'

    GET_USER_ORDERS = f'{BASE_URL}/api/orders'