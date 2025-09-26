from curses.textpad import rectangle
import math

from task_04_02_shape import *


def test_shape_class():
    c = Circle(100)

    assert c.area() == math.pi * 100 ** 2

    r = Rectangle(100, 100)

    assert  r.area() == 10000


