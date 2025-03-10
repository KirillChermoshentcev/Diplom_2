from faker import Faker

faker = Faker()
fakeRU = Faker(locale='ru_RU')


class CreateNewUser:

    @staticmethod
    def generate_new_user_data():
        name = faker.first_name()
        email = faker.free_email()
        password = faker.password(length=10, special_chars=False, digits=False, upper_case=False, lower_case=True)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

