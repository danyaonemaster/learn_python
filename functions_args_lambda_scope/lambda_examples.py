
from functools import reduce

def lambda_square(x):
    return (lambda y: y * y)(x)

def filter_even(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

def double_list(lst):
    return list(map(lambda x: x * 2, lst))

def sort_by_age(users):
    return sorted(users, key=lambda user: user['age'])

def make_multiplier(n):
    return lambda x: x * n

def reduce_product(lst):
    return reduce(lambda x, y: x * y, lst)
