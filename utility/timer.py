# decorators/time.measure.arguments.py
from time import sleep, time
from functools import wraps


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure_time(func, *args, **kwargs):
    """prints the time it takes to execute the target function"""
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took:', time() - t)


def measure_time_decorator(func):
    """returns the decorated function, which will print the time it takes to execute the target function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)

    return wrapper


