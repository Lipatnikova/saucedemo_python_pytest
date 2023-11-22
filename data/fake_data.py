import random
from faker import Faker


class FakeData:
    @property
    def first_name(self):
        return Faker().first_name()

    @property
    def last_name(self):
        return Faker().last_name()

    @property
    def email(self):
        return Faker().email()

    @property
    def password(self):
        return Faker().password()

    @property
    def phone_number(self):
        return Faker().phone_number()

    @property
    def postcode(self):
        return Faker().postcode()

    def random_num(self, start, end):
        return random.randint(start, end)
