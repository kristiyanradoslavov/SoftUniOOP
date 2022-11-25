from functools import wraps
import time


def exec_time(func_ref):
    @wraps(func_ref)
    def wrapper(*args):
        start_time = time.time()
        func_ref(*args)
        end_time = time.time()
        time_res = end_time - start_time

        return time_res

    return wrapper


@exec_time
def loop(start, end):
    total = 0

    for x in range(start, end):
        total += x

    return total


print(loop(1, 10000000))
