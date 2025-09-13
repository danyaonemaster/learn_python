# test_lambda.py

from lambda_examples import *

def test_3_1_lambda_square():
    assert lambda_square(5) == 25

def test_3_2_filter_even():
    assert filter_even([1, 2, 3, 4]) == [2, 4]

def test_3_3_double_list():
    assert double_list([1, 2, 3]) == [2, 4, 6]

def test_3_4_sort_by_age():
    users = [{'name': 'Tom', 'age': 25}, {'name': 'Ann', 'age': 20}]
    result = sort_by_age(users)
    assert result[0]['name'] == 'Ann'

def test_3_5_make_multiplier():
    double = make_multiplier(2)
    assert double(4) == 8

def test_3_6_reduce_product():
    assert reduce_product([1, 2, 3, 4]) == 24
