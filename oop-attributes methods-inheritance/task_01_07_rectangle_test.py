from task_01_07_rectangle import Rectangle

def test_rectangle_class():
    rectangle = Rectangle(10, 10)

    assert rectangle.area() == rectangle.width * rectangle.height