from functools import wraps


def even_parameters(func_ref):
    @wraps(func_ref)
    def wrapper(*args):
        even_nums = []
        for num in args:
            if isinstance(num, int) and num % 2 == 0:
                even_nums.append(num)

        if len(even_nums) == len(args):
            func_result = func_ref(*args)
            return func_result

        return "Please use only even numbers!"

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
