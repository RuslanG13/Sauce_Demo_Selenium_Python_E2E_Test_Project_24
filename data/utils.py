import random
from faker import Faker


def rand_index(list_range):
    return random.randint(0, list_range - 1)


def fake_first_name_data():
    faker = Faker()
    fake_first_name = faker.first_name()
    return fake_first_name


def fake_last_name_data():
    faker = Faker()
    fake_last_name = faker.last_name()
    return fake_last_name


def fake_post_code_data():
    faker = Faker()
    fake_post_code = faker.postcode()
    return fake_post_code
