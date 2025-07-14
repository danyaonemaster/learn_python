# test_scope.py

import scope_examples
from scope_examples import *

def test_4_1_test_scope(capsys):
    test_scope()
    captured = capsys.readouterr()
    assert "10" in captured.out

def test_4_2_global_counter():
    scope_examples.counter = 0
    scope_examples.increment()
    scope_examples.increment()
    assert scope_examples.counter == 2

def test_4_3_outer_nonlocal():
    assert outer_nonlocal() == 20

def test_4_4_conflict_names(capsys):
    global_value, local_value = conflict_names()
    assert global_value == 5 and local_value == 10

def test_4_5_mutate_list():
    assert mutate_list() == [1, 2, 3, 4]

def test_4_6_lambda_scope():
    assert lambda_scope(3) == 8  # если x был 5 до вызова, и x стал 10 потом
