from functools import wraps
def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) <= 2:
            raise ValueError("Function must have less than 3 arguments")
        return func(*args, **kwargs)
    return wrapper
@prohibit_more_than_2_args
def sum_with_gen(*args):
    return sum(args)

print(sum_with_gen(3,2,3))