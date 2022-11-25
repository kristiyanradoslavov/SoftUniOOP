def even_numbers(function):

    def wrapper(*args):
        func_result = function(*args)

        result = [x for x in func_result if x % 2 == 0]
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
