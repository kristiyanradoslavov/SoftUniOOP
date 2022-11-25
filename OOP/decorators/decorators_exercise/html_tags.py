from functools import wraps


def tags(tag):
    def decorator(func_ref):
        @wraps(func_ref)
        def wrapper(*args):
            result = f"<{tag}>{func_ref(*args)}</{tag}>"
            return result
        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

