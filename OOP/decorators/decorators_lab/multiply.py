def multiply(times):

    def decorator(function):
        def wrapper(*args):
            func_result = function(*args)
            multiply_result = func_result * times

            return multiply_result

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
