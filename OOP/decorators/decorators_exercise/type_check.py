from functools import wraps


def type_check(type_info):
    def decorator(func_ref):

        @wraps(func_ref)
        def wrapper(*args):
            all_elements = []

            for el in args:
                if isinstance(el, type_info):
                    all_elements.append(el)

            if len(all_elements) == len(args):
                func_result = func_ref(*args)
                return func_result

            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Num ber'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
