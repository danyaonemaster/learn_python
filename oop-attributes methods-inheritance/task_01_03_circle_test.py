from task_01_03_circle import Circle

def test_circle_class():
    circle = Circle(2)
    assert circle.area() == 2**2 * 3.14
