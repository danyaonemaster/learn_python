from task_04_07_figure import Triangle
import math

def test_triangle_class():
    a , b, c, = 10, 20, 30

    triangle = Triangle(a, b, c)

    s = (a + b + c) / 2
    d = math.sqrt(s * (s - a) * (s - b) * (s - c))

    assert triangle.area() == d
