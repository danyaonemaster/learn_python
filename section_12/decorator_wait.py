from functools import wraps
from time import sleep
def wait(time):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('start')
            sleep(time)
            func(*args, **kwargs)
            print(f'There was a pause {time} seconds before execution {func.__name__}')
        return wrapper
    return inner_dec

@wait(3)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)

print_text_n_times('Goha', 3)