from task_01_07_rectangle_test import Rectangle


def test_rectangle():
    rect = Rectangle.from_square(10)

    assert rect.width == 10
    assert rect.height == 10
