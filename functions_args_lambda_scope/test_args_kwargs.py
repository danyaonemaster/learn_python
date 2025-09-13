# test_args_kwargs.py

from args_kwargs import *

def test_2_1_sum_all():
    assert sum_all(1, 2, 3) == 6

def test_2_2_print_args(capsys):
    print_args(1, "a", True)
    captured = capsys.readouterr()
    assert "1" in captured.out and "a" in captured.out and "True" in captured.out

def test_2_3_print_kwargs(capsys):
    print_kwargs(name="Alice", age=30)
    captured = capsys.readouterr()
    assert "name" in captured.out and "Alice" in captured.out and "age" in captured.out

def test_2_4_show_all(capsys):
    show_all(1, 2, a="A", b="B")
    captured = capsys.readouterr()
    assert "1" in captured.out and "A" in captured.out

def test_2_5_describe_person(capsys):
    describe_person(name="Bob", age=40)
    captured = capsys.readouterr()
    assert "Bob" in captured.out and "40" in captured.out

def test_2_6_sum_numbers():
    result = sum_numbers(1, 2, "a", b=3, c="x", d=4)
    assert result == 10
