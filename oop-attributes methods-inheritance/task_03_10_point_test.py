from task_03_10_point import Point


def test_point_class():
    point = Point.origin()

    assert point.y == 0
    assert point.x == 0
