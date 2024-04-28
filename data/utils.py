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


def increase_test_case_num(start, end):
    index = start
    for start in range(end + 1):
        start += 1
    return index


def get_length_list(entry_list):
    return len(entry_list)


def get_int_value_from_str(num_text):
    return int(num_text)
