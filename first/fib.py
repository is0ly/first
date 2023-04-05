def fibonacci(n):
    if n in (1, 2):
        return 1
    if n == 0:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
