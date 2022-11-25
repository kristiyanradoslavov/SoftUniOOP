from functools import wraps


def cache(func):
    @wraps(func)
    def wrapper(num):
        chache_key = num

        if chache_key not in wrapper.log:
            wrapper.log[chache_key] = func(num)

        return wrapper.log[chache_key]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)
