# test_functions.py

from functions import *

def test_1_1_greet(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello world!"

def test_1_2_square():
    assert square(4) == 16

def test_1_3_add():
    assert add(3, 5) == 8

def test_1_4_repeat(capsys):
    repeat("Hello", 3)
    captured = capsys.readouterr()
    assert captured.out.count("Hello") == 3

def test_1_5_operations():
    result = operations(6, 2)
    assert result == (8, 4, 12)

def test_1_6_calculate_and_print(capsys):
    calculate_and_print(2, 3)
    captured = capsys.readouterr()
    assert "5" in captured.out
