import random
from faker import Faker


def rand_index(list_range):
    return random.randint(0, list_range - 1)


def fake_data():
    faker = Faker()

    fake_first_name = faker.first_name()
    fake_last_name = faker.last_name()
    fake_post_code = faker.postcode()

    return fake_first_name, fake_last_name, fake_post_code
