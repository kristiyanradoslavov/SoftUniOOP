from functools import wraps


def logged(func_ref):

    @wraps(func_ref)
    def wrapper(*args):
        func_result = f"it returned {func_ref(*args)}"

        return f"you called {func_ref.__name__}({', '.join(map(str, args))})\n{func_result}"

    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))


