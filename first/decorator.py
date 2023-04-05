import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции: {end_time - start_time}")
        return result

    return wrapper


@timer
def some_function():
    list = [i**5 for i in range(1, 10000000)]
    return sum(list)


print(some_function())
