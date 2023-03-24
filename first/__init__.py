import random


def create_list_of_random_numbers(count):
    return [random.randint(1, 1000) for i in range(count)]


print(create_list_of_random_numbers(8))
