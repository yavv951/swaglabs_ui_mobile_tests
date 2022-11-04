import os

import attr
from faker import Faker

fake = Faker()


@attr.s
class AuthData:
    login: str = attr.ib(default=os.getenv('LOGIN'))
    password: str = attr.ib(default=os.getenv('PASSWORD'))

    @staticmethod
    def fill_field():
        return AuthData(login=fake.name(), password=fake.name())
