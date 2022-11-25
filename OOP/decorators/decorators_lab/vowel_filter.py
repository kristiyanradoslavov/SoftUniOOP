from functools import wraps


def vowel_filter(func_ref):
    vowels = "aeiuoy"

    @wraps(func_ref)
    def wrapper():
        result = func_ref()
        vowels_result = [x for x in result if x in vowels]
        return vowels_result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
