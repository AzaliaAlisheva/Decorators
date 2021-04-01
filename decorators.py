import time
import functools


def timer(func):
    @functools.wraps(func)
    def decorator(*args):
        time1 = time.time()
        result = func(*args)
        time2 = time.time()
        print(time2 - time1)
        return result
    return decorator


@timer
def function():
    time.sleep(3)
    return None


print(function())