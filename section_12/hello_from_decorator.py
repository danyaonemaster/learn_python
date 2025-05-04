from curses import wrapper
from functools import wraps
def hello_from_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return str(result) + " Hello from decorator!"
    return wrapper()

@hello_from_decorator
def sum_with_gen():
    return sum(number for number in range(10000000))
print(sum_with_gen)